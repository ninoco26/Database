def commit_transaction(connection):
    """
    Commit the current transaction to the database.

    :param connection: psycopg2 connection object to the database.
    """
    connection.commit()
    logging.info("Transaction committed")
