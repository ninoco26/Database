def delete_data(connection, table_name, conditions):
    """
    Delete data from a table based on conditions.

    :param connection: psycopg2 connection object to the database.
    :param table_name: Name of the table to delete data from.
    :param conditions: Dictionary of conditions to identify the records to delete.
    """
    condition_str = ' AND '.join([f"{k} = %s" for k in conditions.keys()])
    sql = f"DELETE FROM {table_name} WHERE {condition_str}"
    values = tuple(conditions.values())

    cursor = connection.cursor()
    try:
        cursor.execute(sql, values)
        connection.commit()
        logging.info("Data deleted successfully from %s", table_name)
    except Exception as e:
        connection.rollback()
        logging.error("An error occurred during data deletion: %s", e)
    finally:
        cursor.close()
