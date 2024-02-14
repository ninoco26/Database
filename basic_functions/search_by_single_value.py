def search_by_single_value(connection, table_name, column, value):
    try:
        with connection.cursor() as cursor:
            query = f"SELECT * FROM {table_name} WHERE {column} = %s;"
            cursor.execute(query, (value,))
            rows = cursor.fetchall()
            return rows
    except Exception as e:
        print(f"An error occurred: {e}")
        return []
