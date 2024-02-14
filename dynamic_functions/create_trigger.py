def create_trigger(connection, table_name, trigger_name, trigger_time, trigger_event, function_name):
    """
    Create a trigger on a specified table.

    :param connection: psycopg2 connection object to the database.
    :param table_name: Name of the table to create the trigger on.
    :param trigger_name: Name of the trigger.
    :param trigger_time: Timing of the trigger (BEFORE, AFTER).
    :param trigger_event: Event that triggers the trigger (INSERT, UPDATE, DELETE).
    :param function_name: Name of the function to call when the trigger is fired.
    """
    sql = f"CREATE TRIGGER {trigger_name} {trigger_time} {trigger_event} ON {table_name} " \
          f"FOR EACH ROW EXECUTE FUNCTION {function_name}()"

    cursor = connection.cursor()
    try:
        cursor.execute(sql)
        connection.commit()
        logging.info("Trigger %s created on %s", trigger_name, table_name)
    except Exception as e:
        connection.rollback()
        logging.error("Failed to create trigger %s on %s: %s", trigger_name, table_name, e)
    finally:
        cursor.close()
