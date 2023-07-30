from components.connect import db_config
from dotenv import load_dotenv
from flask import Blueprint, request, jsonify
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
from werkzeug.utils import secure_filename
import base64
import mysql.connector
import os
import requests


meal_bp = Blueprint('meal', __name__)

@meal_bp.route('/history', methods=['GET'])
@jwt_required()
def get_meal_history():
    cnx = mysql.connector.connect(**db_config)
    cursor = cnx.cursor()

    try:
        # get the patient_id from the user_id
        email = get_jwt_identity()
        cursor.execute("SELECT * FROM users WHERE email = %s LIMIT 1", (email,))
        user_row = cursor.fetchone()
        if user_row is not None:
            user_id = user_row[0]

            cursor.execute("SELECT patient_id FROM patients WHERE user_id = %s LIMIT 1", (user_id,))
            patient_row = cursor.fetchone()
            if patient_row is not None:
                patient_id = patient_row[0]

                cursor.execute("SELECT * FROM meals WHERE patient_id = %s", (patient_id,))
                meals = []
                for meal_id, meal_type, meal_cont, meal_pic in cursor:
                    meal = {}
                    meal['meal_id'] = meal_id
                    meal['meal_type'] = meal_type
                    meal['meal_cont'] = meal_cont
                    meal['meal_pic'] = meal_pic
                    meals.append(meal)

                return jsonify({'meals': meals}), 200

            else:
                return jsonify({'error': 'Patient not found'}), 400

        else:
            return jsonify({'error': 'User not found'}), 400

    except Exception as e:
        return jsonify({'error': str(e)}), 400

    cursor.close()
    cnx.close()


@meal_bp.route('/meal', methods=['GET', 'POST'])
@jwt_required()
def get_meal():
    cnx = mysql.connector.connect(**db_config)
    cursor = cnx.cursor()

    try:
        if request.method == 'GET':
            cursor.execute("SELECT risk_category, risk_meals FROM recommendations")
            categories = []
            for risk_category, risk_meal in cursor:
                category = {}
                category['risk_category'] = risk_category
                category['risk_meal'] = risk_meal
                categories.append(category)

            return jsonify({'categories': categories}), 200

        elif request.method == 'POST':

            meal_type = request.json.get('mealType')
            meal_cont = request.json.get('mealCont')
            # nutri_lvl = request.json.get('nutriLvl')
            meal_pic = request.files['selectedFile']
            upload_folder = os.path.join(os.path.dirname(__file__), '..', 'uploads')
            filename = secure_filename(meal_pic.filename)
            image_path = os.path.join(upload_folder, meal_pic.filename)
            meal_pic.save(image_path)

            # get the patient_id from the user_id
            email = get_jwt_identity()
            cursor.execute("SELECT * FROM users WHERE email = %s LIMIT 1", (email,))
            user_row = cursor.fetchone()
            if user_row is not None:
                user_id = user_row[0]

                cursor.execute("SELECT * FROM patients WHERE user_id = %s LIMIT 1", (user_id,))
                patient_row = cursor.fetchone()
                if patient_row is not None:
                    patient_id = patient_row[0]

                    # insert into meals table
                    cursor.execute("""
                        INSERT INTO meals (patient_id, meal_type, meal_cont, meal_pic)
                        VALUES (%s, %s, %s, %s)
                    """, (patient_id, meal_type, meal_cont, image_path))
                    cnx.commit()

                    return jsonify({'message': 'Meal added successfully!'}), 201

                else:
                    return jsonify({'error': 'Patient not found'}), 400

            else:
                return jsonify({'error': 'User not found'}), 400


    except Exception as e:
        return jsonify({'error': str(e)}), 400
    
    cursor.close()
    cnx.close()
    
def analyze_meal(image_path):
    # Load environment variables from the .env.local file in the parent directory
    env_file_path = os.path.join(os.path.dirname(__file__), '..', '.env.local')
    load_dotenv(env_file_path)

    api_user_token = os.getenv('LOGMEAL_API_TOKEN')
    api_user_id = os.getenv('LOGMEAL_API_USER_ID')


    # access the meal_cont from the meals table
    print(image_path)
    # return requests.post(
    #     "https://api.logmeal.es/v2/analyze",
    #     headers={


    
