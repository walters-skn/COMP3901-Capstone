from components.connect import db_config
from flask import Blueprint, request, jsonify
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
import bcrypt
import mysql.connector

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    fname = request.json.get('fname')
    lname = request.json.get('lname')
    email = request.json.get('email')
    
    salt     = bcrypt.gensalt()
    password = request.json.get('password')
    password_hash = bcrypt.hashpw(password.encode('utf-8'), salt)
    
    address1 = request.json.get('address1')
    address2 = request.json.get('address2')
    phone    = request.json.get('phone')

    try:
        cnx = mysql.connector.connect(**db_config)
        cursor = cnx.cursor()
        # check if email already exists
        cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
        user = cursor.fetchone()
        if user is not None:
            return jsonify({"error": "Email already exists"}), 400
        cursor.execute("INSERT INTO users (email, upassword) VALUES (%s, %s)", (email, password_hash))
        cnx.commit()

        cursor.execute("SELECT user_id FROM users WHERE email = %s", (email,))
        user_id = cursor.fetchone()[0]
        if user_id is not None:
            cursor.execute("""
                INSERT INTO patients (user_id, first_name, last_name, address1, address2) 
                VALUES (%s, %s, %s, %s, %s)""", (user_id, fname, lname, address1, address2))
            cnx.commit()

        cursor.execute("SELECT patient_id FROM patients WHERE user_id = %s", (user_id,))
        patient_id = cursor.fetchone()[0]
        if patient_id is not None:
            cursor.execute("""
                INSERT INTO contacts (patient_id, phone) 
                VALUES (%s, %s)""", (patient_id, phone))
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
        cursor.execute("SELECT email, upassword, is_admin FROM users WHERE email = %s LIMIT 1", (email, ))
        user = cursor.fetchone()
        if user is not None:
            is_admin = user[2]
            if is_admin == 1:
                access_token = create_access_token(identity=user[0])
                return jsonify({'access_token': access_token, 'is_admin': 1}), 200
            
            elif is_admin == 0 and bcrypt.checkpw(password.encode('utf-8'), user[1].encode('utf-8')):
                access_token = create_access_token(identity=user[0])
                return jsonify({'access_token': access_token}), 200
            else:
                return jsonify({'error': 'Invalid credentials'}), 400
        else:
            return jsonify({'error': 'User not found'}), 400
   
    except Exception as e:
        return jsonify({'error': str(e)}), 400


