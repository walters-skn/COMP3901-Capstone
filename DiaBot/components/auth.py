from flask import Blueprint, request, jsonify
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity

import mysql.connector
from db.connect import db_config

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/register', methods=['POST'])
def register():
    fname = request.json.get('fname')
    lname = request.json.get('lname')
    email = request.json.get('email')
    password = request.json.get('password')
    address1 = request.json.get('address1')
    address2 = request.json.get('address2')

    try:
        cnx = mysql.connector.connect(**db_config)
        cursor = cnx.cursor()
        # check if email already exists
        cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
        user = cursor.fetchone()
        if user:
            return jsonify({"error": "Email already exists"}), 400
        cursor.execute("INSERT INTO users (email, upassword) VALUES (%s, %s)", (email, password))
        cnx.commit()

        cursor.execute("SELECT user_id FROM users WHERE email = %s", (email,))
        user_id = cursor.fetchone()[0]
        if user_id:
            cursor.execute("""
                INSERT INTO patients (user_id, first_name, last_name, address1, address2) 
                VALUES (%s, %s, %s, %s, %s)""", (user_id, fname, lname, address1, address2))
            cnx.commit()

        return jsonify({"message": "Patient successfully registered"}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@auth_bp.route('/login', methods=['POST'])
def login():
    email = request.json.get('email')
    password = request.json.get('password')
    try:
        cnx = mysql.connector.connect(**db_config)
        cursor = cnx.cursor()
        cursor.execute("SELECT user_id, is_admin FROM users WHERE email = %s AND upassword = %s", (email, password))
        user = cursor.fetchone()
        if user:
            user_id, is_admin = user

            token_data = {
                'user_id': user_id,
                'is_admin': is_admin == 1
            }

            access_token = create_access_token(identity=token_data)
            return jsonify(access_token=access_token, is_admin=is_admin)
        else:
            return jsonify({"error": "Invalid username or password"}), 401
    except Exception as e:
        return jsonify({'error': str(e)}), 400


