def create_index(connection, table_name, column_name, index_name=None):
    """
    Create an index on a specified column of a table.

    :param connection: psycopg2 connection object to the database.
    :param table_name: Name of the table to create the index on.
    :param column_name: Name of the column to index.
    :param index_name: Optional name for the index.
    """
    index_name = index_name or f"idx_{table_name}_{column_name}"
    sql = f"CREATE INDEX {index_name} ON {table_name} ({column_name})"

    cursor = connection.cursor()
    try:
        cursor.execute(sql)
        connection.commit()
        logging.info("Index %s created on %s", index_name, table_name)
    except Exception as e:
        connection.rollback()
        logging.error("Failed to create index %s on %s: %s", index_name, table_name, e)
    finally:
        cursor.close()
