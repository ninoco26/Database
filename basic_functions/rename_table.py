def rename_table(connection, old_name, new_name):
    """
    Rename an existing table in the database.

    :param connection: psycopg2 connection object to the database.
    :param old_name: Name of the table to be renamed.
    :param new_name: New name for the table.
    """
    sql = f"ALTER TABLE {old_name} RENAME TO {new_name}"

    cursor = connection.cursor()
    try:
        cursor.execute(sql)
        connection.commit()
        logging.info("Table %s renamed to %s", old_name, new_name)
    except Exception as e:
        connection.rollback()
        logging.error("Failed to rename table %s: %s", old_name, e)
    finally:
        cursor.close()
