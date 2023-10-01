import psycopg2
import os
import bcrypt

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
            with connection.cursor() as cursor:
                cursor.execute('SELECT * FROM Users WHERE UserName=%s', (userCredential.userName,))
                if cursor.rowcount == 0:
                    return False
                fetched_users = list(cursor.fetchall())[0]
                password_hash = bytes(fetched_users[1])
                password_salt = bytes(fetched_users[2])
                if bcrypt.hashpw(userCredential.password.encode('utf-8'), password_salt) != password_hash:
                    return False
                return True
    
    def addUser(userCredential):
        with getconnection() as connection:
            with connection.cursor() as cursor:
                password_salt = bcrypt.gensalt(rounds=16)
                password_hash = bcrypt.hashpw(userCredential.password.encode('utf-8'), password_salt)
                cursor.execute('INSERT INTO users VALUES(%s, %s, %s, %s)',(userCredential.userName, password_hash, password_salt, userCredential.updateDate))
            connection.commit()

    
    def checkUserIs(userCredential):
        with getconnection() as connection:
            with connection.cursor() as cursor:
                cursor.execute('SELECT * FROM Users WHERE UserName=%s ', (userCredential.userName, ))
                return cursor.fetchall()
            