def rollback_transaction(connection):
    """
    Rollback the current transaction in case of errors.

    :param connection: psycopg2 connection object to the database.
    """
    connection.rollback()
    logging.info("Transaction rolled back")
