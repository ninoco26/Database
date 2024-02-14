def drop_index(connection, index_name):
    """
    Drop an existing index from the database.

    :param connection: psycopg2 connection object to the database.
    :param index_name: Name of the index to drop.
    """
    sql = f"DROP INDEX IF EXISTS {index_name}"

    cursor = connection.cursor()
    try:
        cursor.execute(sql)
        connection.commit()
        logging.info("Index %s dropped", index_name)
    except Exception as e:
        connection.rollback()
        logging.error("Failed to drop index %s: %s", index_name, e)
    finally:
        cursor.close()
