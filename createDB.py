#pip install mysql-connector-python
#pip install pandas
#pip install selenium

import mysql.connector
from mysql.connector import Error
import pandas as pd

#establish a connection to the MySQL Community Server
def create_server_connection(host_name, user_name, user_password):
    
    #close any existing connections so that the server doesn't become confused with multiple open connections
    connection = None
    
    try:
        connection = mysql.connector.connect(
            host = host_name,
            user = user_name,
            passwd = user_password
        )
        print("MySQL database connection successful")
        
    except Error as err:
        print(f"Error: '{err}'")
        
    #if the connection is successful the function returns a connection object
    return connection
  
#set password here
pw = "****************"
connection = create_server_connection("localhost", "root", pw)

def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
        
    except Error as err:
        print(f"Error: '{err}'")
        
create_database_query = "CREATE DATABASE speeches"
create_database(connection, create_database_query)
