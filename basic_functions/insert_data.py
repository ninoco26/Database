def insert_data(connection, table_name, data_dict):
    """
    Insert data into a table.

    :param connection: psycopg2 connection object to the database.
    :param table_name: Name of the table to insert data into.
    :param data_dict: Dictionary of column names and their values to insert.
    """
    columns = ', '.join(data_dict.keys())
    placeholders = ', '.join(['%s'] * len(data_dict))
    sql = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
    values = tuple(data_dict.values())

    cursor = connection.cursor()
    try:
        cursor.execute(sql, values)
        connection.commit()
        logging.info("Data inserted successfully into %s", table_name)
    except Exception as e:
        connection.rollback()
        logging.error("An error occurred during data insertion: %s", e)
    finally:
        cursor.close()
