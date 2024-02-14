def query_data(connection, table_name, conditions=None, columns='*'):
    """
    Query data from a table with optional conditions.

    :param connection: psycopg2 connection object to the database.
    :param table_name: Name of the table to query data from.
    :param conditions: Optional dictionary of conditions for filtering (column: value).
    :param columns: Columns to retrieve, defaults to all (*).
    """
    condition_str = ' AND '.join([f"{k} = %s" for k in conditions.keys()]) if conditions else ''
    sql = f"SELECT {columns} FROM {table_name}" + (f" WHERE {condition_str}" if conditions else '')

    cursor = connection.cursor()
    try:
        cursor.execute(sql, tuple(conditions.values()) if conditions else ())
        results = cursor.fetchall()
        logging.info("Data queried successfully from %s", table_name)
        return results
    except Exception as e:
        logging.error("An error occurred during data query: %s", e)
    finally:
        cursor.close()
