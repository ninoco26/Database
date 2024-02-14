def create_table(connection, create_table_sql):
    """
    Create a new table in the database.

    :param connection: psycopg2 connection object to the database.
    :param create_table_sql: Complete SQL statement to create a table.
    """
    cursor = connection.cursor()
    try:
        cursor.execute(create_table_sql)
        connection.commit()
        logging.info("Table created successfully")
    except Exception as e:
        connection.rollback()
        logging.error("Failed to create table: %s", e)
    finally:
        cursor.close()
