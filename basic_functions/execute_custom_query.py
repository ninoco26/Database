def execute_custom_query(connection, query, args=None):
    """
    Execute a custom SQL query.

    :param connection: psycopg2 connection object to the database.
    :param query: SQL query string to execute.
    :param args: Optional arguments to pass to the execute method.
    :return: The result of the query execution.
    """
    cursor = connection.cursor()
    try:
        cursor.execute(query, args or ())
        if query.strip().upper().startswith("SELECT"):
            results = cursor.fetchall()
            logging.info("Custom query executed successfully")
            return results
        else:
            connection.commit()
            logging.info("Custom non-select query executed and committed successfully")
    except Exception as e:
        connection.rollback()
        logging.error("Failed to execute custom query: %s", e)
    finally:
        cursor.close()
