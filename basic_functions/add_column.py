def add_column(connection, table_name, column_name, data_type):
    """
    Add a new column to an existing table.

    :param connection: psycopg2 connection object to the database.
    :param table_name: Name of the table to add the column to.
    :param column_name: Name of the new column.
    :param data_type: Data type of the new column.
    """
    sql = f"ALTER TABLE {table_name} ADD COLUMN {column_name} {data_type}"

    cursor = connection.cursor()
    try:
        cursor.execute(sql)
        connection.commit()
        logging.info("Column %s added to table %s", column_name, table_name)
    except Exception as e:
        connection.rollback()
        logging.error("Failed to add column %s to table %s: %s", column_name, table_name, e)
    finally:
        cursor.close()
