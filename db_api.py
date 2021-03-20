import mysql.connector

class Database:
    __hostname = 'localhost'
    __username = 'root'
    __password = 'aCorn9811!'
    __database = None
    __connection = None
    __cursor = None

    def __init__(self, **kwargs):
        if 'host' in kwargs:
            self.__host = kwargs['host']
        if 'user' in kwargs:
            self.__user = kwargs['user']
        if 'password' in kwargs:
            self.__password = kwargs['password']
        if 'database' in kwargs:
            self.__database = kwargs['database']
        self.connection_db()

    def connection_db(self):
        try:
            #if the database name is specified, login to that databse
            if self.__database != None: 
                try:
                    self.__connection =  mysql.connector.connect(
                        host=self.__hostname,
                        user=self.__username,
                        password=self.__password,
                        database=self.__database
                    )
                    self.__cursor = self.__connection.cursor()
                except Exception as err:
                    self.__connection = mysql.connector.connect(
                    host=self.__hostname,
                    user=self.__username,
                    password=self.__password
                    )
                    self.__cursor = self.__connection.cursor()
                    self.create_db()
                    self.select_db()
            #otherwise just connect to mysql
            else: 
                self.__connection = mysql.connector.connect(
                    host=self.__hostname,
                    user=self.__username,
                    password=self.__password,
                )
                self.__cursor = self.__connection.cursor()
        except mysql.connector.Error as err:
            print('some problem with db: {}'.format(err))

    # creates a db with the specified name
    def create_db(self):
        try:
            self.__cursor.execute("CREATE DATABASE {}".format(self.__database))
            self.__connection.commit()
        except mysql.connector.Error as err:
            print('some problem with db: {}'.format(err))
            self.__connection.rollback()
        
    # selects a db with the specified name
    def select_db(self):
        try:
            self.__cursor.execute("Use {}".format(self.__database))
            self.__connection.commit()
        except mysql.connector.Error as err:
            print('some problem with db: {}'.format(err))
            self.__connection.rollback()

    def close_connection(self):
        try:
            self.__connection.close()
        except mysql.connector.Error as err:
            print('Some problem closing db connection: {}'.format(err))