import psycopg2
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import re

# Создаем табличку
try:
    # Подключение к существующей базе данных
    connection = psycopg2.connect(user = "postgres",
                                  # пароль, который указали при установке PostgreSQL
                                  password = "170608kolyaL)",
                                  host = "127.0.0.1",
                                  port = "5432"
                                )
    
    connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    
    # Курсор для выполнения операций с базой данных
    cursor = connection.cursor()
    sql_create_database = 'create database mtj_dtb_finally'
    #cursor.execute(sql_create_database)

    # Выполнение команды: это создает новую таблицу
    create_table = """CREATE TABLE users(
                          user_id BIGINT PRIMARY KEY    NOT NULL,
                          refferals           BIGINT    NOT NULL,
                          refferer_id         BIGINT    NOT NULL,
                          refferer_per        BIGINT    NOT NULL); """
    cursor.execute(create_table)
    connection.commit()
    print("Таблица успешно создана в PostgreSQL")
    
except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL", error)

    


# Функции таблицы

# Функция добавления юзера
def add_user(user_id, refferer_id):
  cur = connection.cursor() 
  return cur.execute('INSERT INTO users(user_id, refferals, refferer_id, refferer_per) VALUES(%s, %s, %s, %s)', (user_id, 0, refferer_id, 0))
  database.commit()  

# Засчитывание реферала
def refs_increase(ref_id):
   cur = connection.cursor() 
   cur.execute("""SELECT refferals FROM users WHERE user_id = %s""", (ref_id, ))
   refs1 = cur.fetchall()
   for row in refs1:
     refs = row[0]
   refs = refs + 1
   cur.execute("""UPDATE users SET refferals = %s WHERE user_id = %s""", (str(refs), ref_id))
   connection.commit()

def ref_id_count(user_id):
  cur = connection.cursor()
  cur.execute("""SELECT refferer_id FROM users WHERE user_id = %s""", (user_id, )) #считываем айди реферера
  ref_id1 = cur.fetchall()
  for row in ref_id1:
    ref_id = row[0]
  return ref_id

# Функция отображеня рефералов
def count_refs(user_id):
  cur = connection.cursor()
  cur.execute("""SELECT refferals FROM users WHERE user_id = %s""" , (user_id, ))
  refs1 = cur.fetchall()    
  for row in refs1:
    refs = row[0]
  return refs

# функция, выводящая таблицу
def check_table(status):
  cur = connection.cursor()
  if status['status'] == 'creator':
    cur.execute('SELECT * FROM users')
    table = cur.fetchall()
    return table
  else:
    return 'Данная функция доступна только создателю.'
  
# Изменение переменной реферала
def ref_per_increase(user_id):
  cur = connection.cursor()
  cur.execute("SELECT refferer_per FROM users WHERE user_id = %s", (user_id, ))
  ref_per1 = cur.fetchall()
  for row in ref_per1:
    ref_per = row[0]
  ref_per =+ 1
  cur.execute('UPDATE users SET refferer_per = %s WHERE user_id = %s', (str(ref_per), user_id))
  connection.commit()
  
# Проверка переменной реферала
def check_ref_per(user_id):
  cur = connection.cursor()
  cur.execute('SELECT refferer_per FROM users WHERE user_id = %s', (user_id, ))
  ref_per1 = cur.fetchall()
  for row in ref_per1:
    ref_per = row[0]
  return ref_per
  connection.commit()


    
    
    
  
