from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
import mysql.connector

db_config = {
    "user": "root",
    "password": "mysql-25",
    "host": "localhost",
    "database": "diabot"
}

def connect_to_db():
    cnx = mysql.connector.connect(**db_config)
    cursor = cnx.cursor()
    return cnx, cursor