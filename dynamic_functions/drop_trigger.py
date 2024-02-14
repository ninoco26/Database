def drop_trigger(connection, trigger_name):
    """
    Drop an existing trigger from the database.

    :param connection: psycopg2 connection object to the database.
    :param trigger_name: Name of the trigger to drop.
    """
    sql = f"DROP TRIGGER IF EXISTS {trigger_name} ON {table_name}"

    cursor = connection.cursor()
    try:
        cursor.execute(sql)
        connection.commit()
        logging.info("Trigger %s dropped", trigger_name)
    except Exception as e:
        connection.rollback()
        logging.error("Failed to drop trigger %s: %s", trigger_name, e)
    finally:
        cursor.close()
