def begin_transaction(connection):
    """
    Begin a new transaction in the database.

    :param connection: psycopg2 connection object to the database.
    """
    connection.autocommit = False
    logging.info("Transaction started")
