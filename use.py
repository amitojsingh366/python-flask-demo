# from flask import *

import mysql.connector
from mysql.connector import Error


class connect:
    def start(self):
        try:
            connection = mysql.connector.connect(
                host="localhost", database="tanishk", user="root", password="Test123321"
            )
            if connection.is_connected():
                db_Info = connection.get_server_info()
                print("Connected to MySQL Server version ", db_Info)
                connectioncursor = connection.cursor()
            else:
                connection = "fail"
        except Error as e:
            print("Error while connecting to MySQL", e)
            connection = "fail"

        return connection


class read:
    def readtable(self):
        conn = connect.start("")

        if conn != "fail":
            conncursor = conn.cursor()
            a = "SELECT * FROM user;"
            conncursor.execute(a)
            exist = conncursor.fetchall()
            if exist:
                print(exist)
                return exist
