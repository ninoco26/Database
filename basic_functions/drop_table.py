def drop_table(connection, table_name):
    """
    Drop a table from the database.

    :param connection: psycopg2 connection object to the database.
    :param table_name: Name of the table to be dropped.
    """
    cursor = connection.cursor()
    try:
        cursor.execute(f"DROP TABLE IF EXISTS {table_name}")
        connection.commit()
        logging.info("%s table dropped successfully", table_name)
    except Exception as e:
        connection.rollback()
        logging.error("Failed to drop table %s: %s", table_name, e)
    finally:
        cursor.close()
