def add_primary_key_constraint(connection, table_name, column_name):
    """
    Add a primary key constraint to an existing table.

    :param connection: psycopg2 connection object to the database.
    :param table_name: Name of the table to add the constraint to.
    :param column_name: Name of the column to set as the primary key.
    """
    sql = f"ALTER TABLE {table_name} ADD CONSTRAINT pk_{table_name} PRIMARY KEY ({column_name})"

    cursor = connection.cursor()
    try:
        cursor.execute(sql)
        connection.commit()
        logging.info("Primary key constraint added to %s", table_name)
    except Exception as e:
        connection.rollback()
        logging.error("Failed to add primary key constraint to %s: %s", table_name, e)
    finally:
        cursor.close()
