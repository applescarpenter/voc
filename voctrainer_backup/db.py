import psycopg2
import psycopg2.extras

"""
This class handles the connection to the database
As well as the insertion and retrieving of data. 
The connection will be handled by a context manager therefore it shouldn't be possible to run out of database sessions
Returns:
    dictionary with the requested (SQL) data
"""
class DatabaseConnection:
    def __init__(self, host, database, user, pw, port) -> None:
        self.host = host
        self.database = database
        self.user = user
        self.pw = pw
        self.port = port
        self.cnxn = None

    def __connect(self):
        self.cnxn = psycopg2.connect(
            host = self.host,
            database=self.database,
            user = self.user,
            password = self.pw,
            port = self.port
        )
        return self.cnxn


    def get_data(self, qry, data):
        self.cnxn = self.__connect()
        
        with self.cnxn:
            with self.cnxn.cursor(cursor_factory = psycopg2.extras.RealDictCursor) as cur:
                cur.execute(qry, data)
                data = cur.fetchall()
                return data

    def insert_data(self, qry, data):
        self.cnxn = self.__connect()

        with self.cnxn:
            with self.cnxn.cursor() as cur:
                cur.execute(qry, data)
                


# import needed modules for database connection
from dotenv import load_dotenv
from os import getenv

load_dotenv()

# instantiate database connection
def db_connection():
    try:
        db = DatabaseConnection(getenv("SERVER"), getenv("DATABASE"), getenv("USER"), getenv("PW"), getenv("PORT"))   
    except (Exception, psycopg2.Error) as e:
        return e
    return db
        
