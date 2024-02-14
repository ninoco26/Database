def batch_insert_data(connection, table_name, data_list):
    """
    Insert multiple records into a table in a single operation.

    :param connection: psycopg2 connection object to the database.
    :param table_name: Name of the table to insert data into.
    :param data_list: List of dictionaries, where each dictionary represents a row to insert.
    """
    if not data_list:
        logging.warning("No data provided for batch insertion.")
        return

    columns = ', '.join(data_list[0].keys())
    placeholders = ', '.join(['%s'] * len(data_list[0]))
    sql = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"

    values_list = [tuple(item.values()) for item in data_list]

    cursor = connection.cursor()
    try:
        cursor.executemany(sql, values_list)
        connection.commit()
        logging.info("Batch data inserted successfully into %s", table_name)
    except Exception as e:
        connection.rollback()
        logging.error("An error occurred during batch data insertion: %s", e)
    finally:
        cursor.close()
