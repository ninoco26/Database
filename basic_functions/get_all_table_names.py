def get_all_table_names(connection):
    """
    Retrieve all table names in the database.

    :param connection: psycopg2 connection object to the database.
    :return: List of table names.
    """
    sql = "SELECT table_name FROM information_schema.tables WHERE table_schema='public'"
    cursor = connection.cursor()
    try:
        cursor.execute(sql)
        tables = [table[0] for table in cursor.fetchall()]
        logging.info("Retrieved all table names.")
        return tables
    except Exception as e:
        logging.error("An error occurred while retrieving table names: %s", e)
        return []
    finally:
        cursor.close()
