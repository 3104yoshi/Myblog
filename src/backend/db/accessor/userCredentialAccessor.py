import psycopg2
import os
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from io import BytesIO

postgresuser = os.environ.get('POSTGRES_USER')
postgrespassword = os.environ.get('POSTGRES_PASSWORD')
postgreshost = os.environ.get('POSTGRES_HOST')
postgresdb = os.environ.get('POSTGRES_DB')
cryptokey = b'\xac\xb3\xb3\x92\xed?\xd6-E\xa4\x0f\xec\xedGY`'

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
                fetched_users = list(cursor.fetchall())[0]
                nonce = bytes(fetched_users[2])
                encryptedPassword = bytes(fetched_users[1])
                tag = bytes(fetched_users[3])
                print(nonce, encryptedPassword, tag)
                cipher = AES.new(cryptokey, AES.MODE_EAX, nonce=nonce)
                decryptedPassword = cipher.decrypt_and_verify(encryptedPassword, tag)
                print(decryptedPassword)
                print(userCredential.password)
                if decryptedPassword.decode('utf-8') != userCredential.password:
                    return False
                return True
    
    def addUser(userCredential):
        with getconnection() as connection:
            with connection.cursor() as cursor:
                pass_nonce = get_random_bytes(16)
                cipher = AES.new(cryptokey, AES.MODE_EAX, nonce=pass_nonce)
                encryptedPassword, pass_tag = cipher.encrypt_and_digest(userCredential.password.encode('utf-8'))
                cursor.execute('INSERT INTO users VALUES(%s, %s, %s, %s, %s)',(userCredential.userName, encryptedPassword, pass_nonce, pass_tag, userCredential.updateDate))
                # print(cipher.nonce)
                # print(pass_tag)
                # print(encryptedPassword)
                # print(userCredential.userName)
                # print(userCredential.updateDate)
                # cursor.execute('INSERT INTO Users VALUES(%s, %s, %s)', (userCredential.userName, userCredential.password, userCredential.updateDate))
            connection.commit()

    
    def checkUserIs(userCredential):
        with getconnection() as connection:
            with connection.cursor() as cursor:
                cursor.execute('SELECT * FROM Users WHERE UserName=%s ', (userCredential.userName, ))
                return cursor.fetchall()
            