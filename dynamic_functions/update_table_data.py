def update_table_data(connection, table_name, set_values, conditions):
    """
    Update data in a table based on conditions.

    :param connection: psycopg2 connection object to the database.
    :param table_name: Name of the table where data will be updated.
    :param set_values: Dictionary of columns and their new values.
    :param conditions: Dictionary of conditions to identify the records to update.
    """
    set_str = ', '.join([f"{key} = %s" for key in set_values.keys()])
    condition_str = ' AND '.join([f"{key} = %s" for key in conditions.keys()])
    sql = f"UPDATE {table_name} SET {set_str} WHERE {condition_str}"
    values = list(set_values.values()) + list(conditions.values())

    cursor = connection.cursor()
    try:
        cursor.execute(sql, values)
        connection.commit()
        logging.info("Data updated successfully in %s", table_name)
    except Exception as e:
        connection.rollback()
        logging.error("Failed to update data in %s: %s", table_name, e)
    finally:
        cursor.close()
