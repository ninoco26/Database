def add_foreign_key_constraint(connection, table_name, column_name, foreign_table, foreign_column):
    """
    Add a foreign key constraint to an existing table.

    :param connection: psycopg2 connection object to the database.
    :param table_name: Name of the table to add the constraint to.
    :param column_name: Name of the column to set as the foreign key.
    :param foreign_table: Name of the referenced table.
    :param foreign_column: Name of the referenced column.
    """
    sql = f"ALTER TABLE {table_name} ADD CONSTRAINT fk_{table_name}_{column_name} FOREIGN KEY ({column_name}) " \
          f"REFERENCES {foreign_table}({foreign_column})"

    cursor = connection.cursor()
    try:
        cursor.execute(sql)
        connection.commit()
        logging.info("Foreign key constraint added to %s", table_name)
    except Exception as e:
        connection.rollback()
        logging.error("Failed to add foreign key constraint to %s: %s", table_name, e)
    finally:
        cursor.close()
