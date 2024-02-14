import psycopg2
from psycopg2 import OperationalError, DatabaseError, InterfaceError
import pandas as pd

def create_connection(db_name, db_user, db_password, db_host, db_port, ssl_mode, connect_timeout):
    connection = None
    try:
        connection = psycopg2.connect(
            dbname=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port,
            sslmode=ssl_mode,
            connect_timeout=connect_timeout
        )
        print("Connection to PostgreSQL DB successful")
    except InterfaceError as ie:
        print(f"Interface error occurred: {ie}")
    except OperationalError as oe:
        print(f"Operational error occurred: {oe}")
        print("Additional info:", oe.pgcode, oe.pgerror)
    except DatabaseError as de:
        print(f"Database error occurred: {de}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    return connection
# Adjusted function to create a table with exact column names from the DataFrame
def create_dynamic_table_from_csv(connection, csv_file_path):
    df = pd.read_csv(csv_file_path, nrows=0)  # Only read the headers

    create_table_sql = 'CREATE TABLE IF NOT EXISTS transactions (id SERIAL PRIMARY KEY, '

    for column in df.columns:
        column_name = column.replace('%', 'percent').replace(' ', '_')  # Simplify naming
        create_table_sql += f'"{column_name}" TEXT, '

    create_table_sql = create_table_sql.rstrip(', ')  # Remove trailing comma
    create_table_sql += ');'

    cursor = connection.cursor()
    try:
        cursor.execute(create_table_sql)
        connection.commit()
        print("Table created successfully based on CSV structure")
    except Exception as e:
        print(f"An error occurred during table creation: {e}")
    finally:
        cursor.close()



def insert_csv_data_with_columns(connection, csv_file_path):
    df = pd.read_csv(csv_file_path)
    df = df.replace({pd.NA: None})

    # Prepare column names for the SQL query
    db_columns = ['"' + col.replace('%', 'percent').replace(' ', '_') + '"' for col in df.columns]  # Match table creation
    placeholders = ', '.join(['%s'] * len(db_columns))

    insert_query = f"INSERT INTO transactions ({', '.join(db_columns)}) VALUES ({placeholders});"

    data_tuples = [tuple(x) for x in df.to_numpy()]

    cursor = connection.cursor()
    try:
        for data_tuple in data_tuples:
            cursor.execute(insert_query, data_tuple)
        connection.commit()
        print("Data inserted successfully")
    except Exception as e:
        connection.rollback()  # Rollback in case of error
        print(f"An error occurred during data insertion: {e}")
    finally:
        cursor.close()


### USAGE EXAMPLE 
## Database connection info
#db_name = ""
#db_user = ""
#db_password = ""
#db_host = ""
#db_port = ""
#ssl_mode = "prefer"
#connect_timeout = 10
#
## Create the connection
#connection = create_connection(db_name, db_user, db_password, db_host, db_port, ssl_mode, connect_timeout)
#csv_file_path = r""
#
#if connection is not None:
#    create_dynamic_table_from_csv(connection, csv_file_path)
#    insert_csv_data_with_columns(connection, csv_file_path)
#    connection.close()
