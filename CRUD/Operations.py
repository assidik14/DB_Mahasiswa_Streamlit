'''Import Module'''
import mysql.connector
import pandas as pd
import string
import random

DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = "notpassword"
DB = "db_mahasiswa"
DB_TABLE = "mahasiswa"

def conn():
    '''DB Connections'''
    mydb = mysql.connector.connect(
        host = DB_HOST,
        user = DB_USER,
        password = DB_PASSWORD,
        database = DB
    )

    return mydb

def random_id():
    '''ID Mahasiswa'''
    str_data = string.digits + string.ascii_uppercase
    lenght = 6
    random_data = "".join(random.choices(str_data, k=lenght))
    
    return random_data

def createData(nama, lahir, fakultas, jurusan):
    '''Create Data'''

    db_conn  = conn()
    mycursor = db_conn.cursor()
    id_random = random_id()

    query = f"INSERT INTO {DB_TABLE} (ID, NAMA, LAHIR, FAKULTAS, JURUSAN) VALUES (%s, %s, %s, %s, %s)"
    values = (id_random, nama, lahir, fakultas, jurusan)
    mycursor.execute(query, values)

    db_conn.commit()
    

def readData():
    '''Read Data from Database'''

    db_conn = conn()
    query = f"SELECT * FROM {DB_TABLE}"
    data = pd.read_sql_query(query, db_conn)

    return data

def rowData():
    '''Row Data'''
    db_conn = conn()
    cursor = db_conn.cursor()
    query = f"SELECT * FROM {DB_TABLE}"
    cursor.execute(query)
    result = cursor.fetchall()

    return result


def searchData(by_id):
    '''Search Data by ID'''
    db_conn = conn()
    cursor = db_conn.cursor()
    query = f"SELECT * FROM {DB_TABLE} WHERE ID = '{by_id}'"
    cursor.execute(query)
    result = cursor.fetchall()

    for data in result:
        nama = data[1]
        lahir = data[2]
        fakultas = data[3]
        jurusan = data[4]

    return nama, lahir, fakultas, jurusan

def updateData(id, nama, lahir, fakultas, jurusan):
    '''Update Data'''

    mydb = conn()
    mycursor = mydb.cursor()
    query = f"UPDATE {DB_TABLE} SET NAMA = '{nama}', LAHIR = '{lahir}', FAKULTAS = '{fakultas}', JURUSAN = '{jurusan}' WHERE ID = '{id}'"
    mycursor.execute(query)
    mydb.commit()

def displayData(by_id):
    '''Display data by ID'''

    db_conn = conn()
    query = f"SELECT * FROM {DB_TABLE} WHERE ID = '{by_id}'"
    data = pd.read_sql_query(query, db_conn)

    return data

def deleteData(by_id):
    '''Delete data'''
    db_conn = conn()
    cursor = db_conn.cursor()
    query = f"DELETE FROM {DB_TABLE} WHERE ID = '{by_id}'"
    cursor.execute(query)
    db_conn.commit()