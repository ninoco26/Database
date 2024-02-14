import psycopg2
from psycopg2 import OperationalError, DatabaseError, InterfaceError
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename='database_logs.log',
                    filemode='a')
console = logging.StreamHandler()
console.setLevel(logging.ERROR)
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)

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
        logging.info("Connection to PostgreSQL DB successful")
    except InterfaceError as ie:
        logging.error(f"Interface error occurred: {ie}")
    except OperationalError as oe:
        logging.error(f"Operational error occurred: {oe}")
        logging.error(f"Additional info: {oe.pgcode}, {oe.pgerror}")
    except DatabaseError as de:
        logging.error(f"Database error occurred: {de}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
    return connection
