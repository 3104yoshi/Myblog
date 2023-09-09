import psycopg2
import os

postgresuser = os.environ.get('POSTGRES_USER')
postgrespassword = os.environ.get('POSTGRES_PASSWORD')
postgreshost = os.environ.get('POSTGRES_HOST')
postgresdb = os.environ.get('POSTGRES_DB')

def getconnection():
    return psycopg2.connect(host=postgreshost,
                        dbname=postgresdb,
                        user=postgresuser,
                        password=postgrespassword)

class userCredentialAccessor:
    def getUser(userCredential):
        with getconnection() as connection:
            cursor = connection.cursor()
            cursor.execute('SELECT * FROM Users WHERE UserName=%s and PassWord=%s ', (userCredential.userName, userCredential.password))
            return cursor.fetchall()
    
    def addUser(userCredential):
        with getconnection() as connection:
            cursor = connection.cursor()
            cursor.execute('INSERT INTO Users VALUES(%s, %s, %s)', (userCredential.userName, userCredential.password, userCredential.updateDate))
    
    def checkUserIs(userCredential):
        with getconnection() as connection:
            cursor = connection.cursor()
            cursor.execute('SELECT * FROM Users WHERE UserName=%s ', (userCredential.userName, ))
            return cursor.fetchall()
        
