def execute_stored_procedure(connection, procedure_name, args=None):
    """
    Execute a stored procedure in the database.

    :param connection: psycopg2 connection object to the database.
    :param procedure_name: Name of the stored procedure to execute.
    :param args: Optional arguments to pass to the stored procedure.
    """
    cursor = connection.cursor()
    try:
        cursor.callproc(procedure_name, args or ())
        connection.commit()
        logging.info("Stored procedure %s executed successfully", procedure_name)
    except Exception as e:
        connection.rollback()
        logging.error("Failed to execute stored procedure %s: %s", procedure_name, e)
    finally:
        cursor.close()
