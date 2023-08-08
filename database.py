import mysql.connector

def database():
    # Connect to MySQL database
    db = mysql.connector.connect(
        host='host_name',
        user='user_name',
        password='passowrd',
        database='db_name'
    )
    return db