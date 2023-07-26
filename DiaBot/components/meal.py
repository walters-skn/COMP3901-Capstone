from flask import Blueprint, request, jsonify
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity

import mysql.connector
from db.connect import db_config

meal_bp = Blueprint('meal', __name__)

@meal_bp.route('/meal', methods=['POST'])
# @jwt_required()
def get_meal():
    cnx = mysql.connector.connect(**db_config)
    cursor = cnx.cursor()

    try:
        meal_type = request.json.get('mealType')
        meal_cont = request.json.get('mealCont')
        nutri_lvl = request.json.get('nutriLvl')

        # get the patient_id from the user_id
        user_id = get_jwt_identity()
        cursor.execute("SELECT patient_id FROM patients WHERE user_id = %s LIMIT 1", (user_id,))
        patient_row = cursor.fetchone()
        if patient_row is not None:
            patient_id = patient_row[0]
        else:
            return jsonify({'error': 'Patient not found'}), 400

        # get the meal_id from the patient_id
        cursor.execute("""
            INSERT INTO meals (patient_id, meal_type, meal_cont, nutri_lvl)
            VALUES (%s, %s, %s, %s)
        """, (patient_id, meal_type, meal_cont, nutri_lvl))

        cnx.commit()

        # Fetch the newly inserted meal
        cursor.execute("SELECT meal_cont FROM meals WHERE patient_id = %s", (patient_id,))
        meal_row = cursor.fetchone()
        if meal_row is not None:
            meal = meal_row[0]
        else:
            return jsonify({'error': 'Meal not found'}), 400

        return jsonify({'message': 'Meal added successfully'}), 201

        cursor.close()
        cnx.close()

    except Exception as e:
        return jsonify({'error': str(e)}), 400
    
def analyze_meal():
    # access the meal_cont from the meals table
    cursor.execute("SELECT meal_cont FROM meals WHERE patient_id = %s", (patient_id,))
    meal_row = cursor.fetchone()
    if meal_row is not None:
        meal = meal_row[0]
    else:
        return jsonify({'error': 'Meal not found'}), 400

    
