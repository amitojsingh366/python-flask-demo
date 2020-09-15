# from flask import *

import mysql.connector
from mysql.connector import Error
import random


class connect:
    def start(self):
        try:
            connection = mysql.connector.connect(
                host="localhost", database="demo", user="root", password="test", auth_plugin='mysql_native_password')
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


class action:
    def readtable(self):
        conn = connect.start("")

        if conn != "fail":
            conncursor = conn.cursor()
            a = "SELECT * FROM users;"
            conncursor.execute(a)
            exist = conncursor.fetchall()
            if exist:
                return exist

    def write(self, uname, pwd):
        conn = connect.start("")
        if conn != "fail":
            conncursor = conn.cursor()
            ii = 1
            jj = random.randint(5, 8)
            uid = ""
            while ii <= jj:
                uid = uid + str(random.randint(0, 9))
                ii += 1
            chk = action.chechUid('', uid)
            if chk:
                a = f"""INSERT INTO `users` (`username`,`password`,`uid`) VALUES ('{uname}','{pwd}','{uid}');"""
                try:
                    conncursor.execute(a)
                    conn.commit()
                except Error as ide:
                    print("Error while Saving To MySql", ide)
            else:
                action.write('', uname, pwd)

    def chechUid(self, cuid):
        conn = connect.start("")
        if not conn == "fail":
            conncursor = conn.cursor()
            a = f"""SELECT * FROM `users` WHERE `uid` = '{cuid}';"""
            conncursor.execute(a)
            exist = conncursor.fetchone()
            if exist:
                return False
            else:
                return True
