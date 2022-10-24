import sqlalchemy
from sqlalchemy.orm import sessionmaker
from models import *


login = '' #не стал мудрить с чтением из ini файла
password = ''
title_db = ''
server = 'localhost:5432'
DSN = f'postgresql://{login}:{password}@{server}/{title_db}'
engine = sqlalchemy.create_engine(DSN)

#create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()

input_user1 = input('введите имя или id исполнителя: ')
try:
    input_user = int(input_user1)
    a = print(session.query(Publisher).filter(Publisher.id == input_user).all())
except:
    print(session.query(Publisher).filter(Publisher.name == input_user1).all())
    pass




session.close()
