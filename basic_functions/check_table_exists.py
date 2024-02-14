def check_table_exists(connection, table_name):
    """
    Check if a table exists in the database.

    :param connection: psycopg2 connection object to the database.
    :param table_name: Name of the table to check.
    :return: True if the table exists, False otherwise.
    """
    sql = "SELECT EXISTS(SELECT * FROM information_schema.tables WHERE table_name=%s)"
    cursor = connection.cursor()
    try:
        cursor.execute(sql, (table_name,))
        exists = cursor.fetchone()[0]
        logging.info("Checked if table %s exists.", table_name)
        return exists
    except Exception as e:
        logging.error("An error occurred while checking if table %s exists: %s", table_name, e)
        return False
    finally:
        cursor.close()
