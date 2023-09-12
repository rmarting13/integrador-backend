import mysql.connector as conn
from config import Config


class DatabaseConnection:
    """
        An abstract class that allows a single connection to a MySql database
    """
    _CONNECTION = None

    @classmethod
    def get_connection(cls):
        """
        Allows to get an existing or new connection to the database
        :return: A MySQLConnection instance
        """
        if cls._CONNECTION is None:
            # cls._CONNECTION = conn.connect(
            #     user=Config.DATABASE_USERNAME,
            #     password=Config.DATABASE_PASSWORD,
            #     host=Config.DATABASE_HOST,
            #     port=Config.DATABASE_PORT,
            #     database=Config.DATABASE_NAME
            # )
            cls._CONNECTION = conn.connect(
                user='root',
                password='admin',
                host='localhost',
                port='3306',
                database='chatify'
            )
        return cls._CONNECTION

    @classmethod
    def execute_query(cls, query: str, params: iter =None):
        """
        Allows a specific sql query execution
        :param query: A sql query string
        :param params: (optional) An iterable that contains the query params
        :return: A MySQLCursor instance
        """
        cursor = cls.get_connection().cursor()
        cursor.execute(query, params)
        cls.get_connection().commit()
        return cursor

    @classmethod
    def fetch_one(cls, query, params=None):
        """
        Gets one row from database (if exists) available in a query result set
        :param query: A sql query string
        :param params: (optional) A tuple that contains the query params
        :return: Next row of the query result set or None if set is empty
        """
        cursor = cls.get_connection().cursor()
        cursor.execute(query, params)
        return cursor.fetchone()

    @classmethod
    def fetch_all(cls, query, params=None):
        """
        Gets all rows from database (if exists) available in a query result set
        :param query: A sql query string
        :param params: (optional) A tuple that contains the query params
        :return: Next row of the query result set
        """
        cursor = cls.get_connection().cursor()
        cursor.execute(query, params)
        return cursor.fetchall()

    @classmethod
    def close_connection(cls):
        """
        Add connection back to pool and the session state
        will be cleared by re-authenticating the user.
        :return: None
        """
        if cls._CONNECTION is not None:
            cls._CONNECTION.close()
            cls._CONNECTION = None


if __name__ == '__main__':
    query = "SELECT film_id, title, description FROM film LIMIT 5;"
    result1 = DatabaseConnection.fetch_all(query=query)
    result2 = DatabaseConnection.fetch_one(query=query)
    # print(*result, sep=''.center(50, '-')+'\n')
    #print(*result1, sep='\n')
    print(*result2, sep='\n')