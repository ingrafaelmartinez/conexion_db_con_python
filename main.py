
import pymysql as MySQLdb
from pymysql.cursors import Cursor


HOST = "localhost"
PORT = 3306
USER = "root"
PASSWORD = ""
DATABASE = "conexion_python"
CHARSET = "utf8mb4"


USER_TABLE = """ CREATE TABLE users(
    id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(50) NOT NULL
    )"""

DROP_USER = " DROP TABLE IF EXISTS users "
SHOW_TABLES = "SHOW TABLES"

INSERT_USER = " INSERT INTO users(username, password) VALUES( '{username}', '{password}' ) "
SELECT_USER = " SELECT * FROM users WHERE id = {id} "
UPDATE_USER = " UPDATE users SET username='{username}', password='{password}' WHERE id={id} "
DELETE_USER = " DELETE FROM users WHERE id = {id} "


if __name__ == '__main__':
    try:
        connection = MySQLdb.connect(host=HOST , user=USER, passwd=PASSWORD, db=DATABASE)

        cursor = connection.cursor()

        cursor.execute(DROP_USER)
        cursor.execute(USER_TABLE)

        username = input("Ingrese el username: ")
        password = input("Ingrese el password: ")

        query = INSERT_USER.format(username=username, password=password)
        print(query)
        try:
            cursor.execute(query)
            connection.commit()  # Permite persistir los datos almacenados por el usuario
        except:
            connection.rollback()  # Revierte los cambios en caso que se presente un error al ejecutar la inserción


        username_update = input("Ingrese en nuevo username: ")
        password_update = input("Ingrese en nuevo password: ")
        id_update = input("Ingrese en id del usuario a actualizar: ")
        query_update = UPDATE_USER.format(username=username_update, password=password_update, id=id_update)
        try:
            cursor.execute(query_update)
            connection.commit()
        except:
            connection.rollback()

        query_select = SELECT_USER.format(id=1)
        print(query_select)
        cursor.execute(query_select)
        users = cursor.fetchall()

        for user in users:
            print(user)

        query_delete = DELETE_USER.format(id=1)
        print(query_delete)
        try:
            cursor.execute(query_delete)
            connection.commit()
        except:
            connection.rollback()


        # cursor.execute(SHOW_TABLES)
        # tables = cursor.fetchall()

        # for table in tables:
        #     print(table)

        connection.close()

    except MySQLdb.Error as error:
        print(error)

