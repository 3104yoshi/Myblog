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

class articlesAccessor:
    def getAllArticles():
        with getconnection() as connection:
            cursor = connection.cursor()
            cursor.execute('SELECT * FROM Articles')
            return cursor.fetchall()
        
    def addArticle(article):
        with getconnection() as connection:
            cursor = connection.cursor()
            cursor.execute('INSERT INTO Articles (title, content, updateDate) VALUES (%s, %s, %s)', (article.title, article.content, article.updateDate))