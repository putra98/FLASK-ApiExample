from flask import Flask, render_template, request, jsonify,redirect, url_for,session, Response
from flask_session import Session
from flask_restful import Resource, Api
from werkzeug.utils import secure_filename 
from flask_mysqldb import MySQL
from itsdangerous import URLSafeTimedSerializer, SignatureExpired
import os
import datetime
import json
import hashlib

app   = Flask(__name__)
mysql = MySQL(app)
api   = Api(app)
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'api_db'
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)



def message(message, status):
    tasks = [
                {
                    'message': message,
                    'status' : status
                }
            ]
    return  jsonify(tasks)

#dengan database
class Products(Resource):
    def get(self):
        cur = mysql.connection.cursor()
        sql = "SELECT * FROM `tbl_produk` WHERE 1"
        cur.execute(sql)
        data = cur.fetchall()

        return message(data, 'get')

    def post(self):
        cur = mysql.connection.cursor()
        sql = "SELECT * FROM `tbl_produk` WHERE id=2"
        cur.execute(sql)
        data = cur.fetchall()

        return message(data, 'post')

    def delete(self):
        cur = mysql.connection.cursor()
        sql = "DELETE FROM `tbl_produk` WHERE 0"
        cur.execute(sql)
        data = cur.fetchall()

        return message(data, 'delete')

    def put(self):
        return message(request.form['nama'], 'put')

#sederhana
class Pendapatan(Resource):
    def get(self):
        return message(request.form['nama'], 'get')

    def post(self):
        return message(request.form['nama'], 'post')

    def delete(self):
        return message(request.form['nama'], 'delete')

    def put(self):
        return message(request.form['nama'], 'put')

api.add_resource(Products, '/products')
api.add_resource(Pendapatan, '/pendapatan')

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True,)