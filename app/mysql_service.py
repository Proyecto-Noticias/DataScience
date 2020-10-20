import pymysql.cursors

# Connect to the database

HOST='127.0.0.1'
DB_USER='root'
PASSWORD='8h260Mc92PuF8tN8'
DB='easynews'
CHARSET='utf8'
CURSORCLASS=pymysql.cursors.DictCursor


def _connect_to_db(
        host=HOST, port=3306,
        db_user=DB_USER, password=PASSWORD,
        db=DB, charset=CHARSET,
        cursorclass=CURSORCLASS):
 
    try:
        con = pymysql.connect(host=host, user=db_user, password=password, db=db, charset=charset, cursorclass=cursorclass)
        return con
    except Exception as e:
        print('Error: ', e)

def get_articles_joined():
    result = {}
    connection = _connect_to_db()

    try:
        with connection.cursor() as cursor:
            row_count = 0
            e = 'none'
            # Read a single record
            sql = f"""SELECT title, subtitle, article_date, image_url, c.name AS category, body, article_url, j.name AS journal, scraping_date, sentiment_classification FROM articles JOIN categories AS c ON articles.category_id=c.id JOIN journals AS j ON articles.journal_id=j.id"""
            cursor.execute(sql)
            result = cursor.fetchall()

    except Exception as ex:        
        #print(ex.args[1]) 
        e = ex.args[0]
    finally:
        connection.close()
        return  result