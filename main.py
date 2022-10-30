import psycopg2
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from models import *


login = '' 
password = ''
title_db = ''
server = 'localhost:5432'
DSN = f'postgresql://{login}:{password}@{server}/{title_db}'
engine = sqlalchemy.create_engine(DSN)

#create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()

#publisher1 = Publisher(name = 'Arctic')
#book1 = Book(title = 'Arctic book', publisher= publisher1)
#shop1 = Shop(name = 'colosus')
#publisher2 = Publisher(name= 'electro')
#book2 = Book(title = 'electrobook', publisher = publisher2)
#book2_1 = Book(title = 'electrobook1', publisher = publisher2)
#stock1 = Stock(shop = shop1, book = book1, count = 4)
#shop2 = Shop(name = 'lightbooks')
#stock2 = Stock(shop = shop2, book = book2, count = 3)
#stock2_1 = Stock(shop = shop2, book = book2_1, count = 7)
#session.add_all([])
#session.commit()

def search_publisher():
    input_user1 = input('введите имя или id исполнителя: ')
    try:
        input_user = int(input_user1)
        print(session.query(Publisher).filter(Publisher.id == input_user).all())
    except:
        print(session.query(Publisher).filter(Publisher.name == input_user1).all())
        pass

#не стал изобретать велосипед и написал простой и понятный всем sql, копался в документации, чтобы выбрать конкретное поле в селект
#однако документация вообще непонятная, к слову, как у гугла, где чтобы получить токен, нужно пройти 9 кругов ада
def search_book():
    input_user1 = int(input('id исполнителя: '))
    with psycopg2.connect(database= title_db, user= login, password= password) as con:
        with con.cursor() as cur:
            cur.execute("""
                    SELECT DISTINCT shop.name FROM shop
                    JOIN stock ON stock.id_shop = shop.id
                    JOIN book ON book.id = stock.id_book
                    JOIN publisher ON publisher.id = book.id_publisher
                    WHERE publisher.id = %s; 
                            """, (input_user1, ))
            print(cur.fetchall())

#search_publisher()    
#search_book()

session.close()
