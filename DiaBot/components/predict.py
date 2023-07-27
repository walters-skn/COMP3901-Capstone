from flask import Blueprint, request, jsonify
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity

import mysql.connector
from db.connect import db_config

predict_bp = Blueprint('predict', __name__)

@predict_bp.route('/symptoms', methods=['GET'])
@jwt_required()
def get_symptoms():
    cnx = mysql.connector.connect(**db_config)
    cursor = cnx.cursor()
    symptoms = []

    try:
        patient_id = get_jwt_identity()
        cursor.execute("SELECT user_id FROM users WHERE user_id = %s LIMIT 1", (patient_id, ))

        user = cursor.fetchone()
        if user is not None:
            cursor.execute("""
                SELECT 
                    symptom_id, gender, weight, height, age, 
                    waist_circumference, is_physically_active, 
                    fruit_veggie_intake, has_high_bp_medication, 
                    has_hyperglycemia_history, has_family_history 
                FROM symptoms WHERE patient_id = %s""", (patient_id, ))

            for symptom_id, gender, weight, height, age, waist_circumference, is_physically_active, fruit_veggie_intake, has_high_bp_medication, has_hyperglycemia_history, has_family_history in cursor:
                symptom = {}
                symptom['symptom_id']                = symptom_id
                symptom['gender']                    = gender
                symptom['weight']                    = weight
                symptom['height']                    = height
                symptom['age']                       = age
                symptom['waist_circumference']       = waist_circumference
                symptom['is_physically_active']      = is_physically_active
                symptom['fruit_veggie_intake']       = fruit_veggie_intake
                symptom['has_high_bp_medication']    = has_high_bp_medication
                symptom['has_hyperglycemia_history'] = has_hyperglycemia_history
                symptom['has_family_history']        = has_family_history
                symptoms.append(symptom)

            return jsonify({'symptoms': symptoms}), 200
        else:
            return jsonify({'error': 'Patient not found'}), 400

    except Exception as e:
        return jsonify({'error': str(e)}), 400


@predict_bp.route('/questions', methods=['GET'])
@jwt_required()
def send_questions_to_client():
    cnx = mysql.connector.connect(**db_config)
    cursor = cnx.cursor()
    question_data = []
    
    try:
        cursor.execute("SELECT * FROM diabetes_questions WHERE is_answered = 0")
    
        for db_id, question, is_answered in cursor:
            question_obj = {}
            question_obj['db_id'] = db_id
            question_obj['question'] = question
            question_obj['is_answered'] = is_answered
            question_data.append(question_obj)
    
        return jsonify({'questions': question_data}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400
    
    cnx.commit()
    cnx.close()
    cursor.close()


@predict_bp.route('/answers', methods=['POST'])
@jwt_required()
def receive_symptoms_from_client():
    cnx = mysql.connector.connect(**db_config)
    cursor = cnx.cursor()

    try:
        answers = request.json.get('responses')
        print("Response from client: ", answers)

        # for answer in answers:
        gender = answers[0]
        weight = float(answers[1])
        height = float(answers[2])
        age = int(answers[3])
        waist_circumference = float(answers[4])
        
        is_physically_active = answers[5]
        if is_physically_active.lower() == 'yes':
            is_physically_active = True
        else:
            is_physically_active = False

        fruit_veggie_intake = int(answers[6])

        has_high_bp_medication = answers[7]
        if has_high_bp_medication.lower() == 'yes':
            has_high_bp_medication = True
        else:
            has_high_bp_medication = False

        has_hyperglycemia_history = answers[8]
        if has_hyperglycemia_history.lower() == 'yes':
            has_hyperglycemia_history = True
        else:
            has_hyperglycemia_history = False

        has_family_history = answers[9]
        if has_family_history.lower() == 'yes':
            has_family_history = True
        else:
            has_family_history = False

        patient_id = get_jwt_identity()
        cursor.execute("SELECT user_id FROM users WHERE user_id = %s LIMIT 1", (patient_id, ))

        user = cursor.fetchone()
        if user is not None:

            cursor.execute(""" 
                INSERT INTO symptoms 
                    (patient_id, gender, weight, height, age, waist_circumference, is_physically_active, fruit_veggie_intake, has_high_bp_medication, has_hyperglycemia_history, has_family_history)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (
                patient_id, gender, weight, height, age, waist_circumference, 
                is_physically_active, fruit_veggie_intake, has_high_bp_medication, 
                has_hyperglycemia_history, has_family_history
            ))
            cnx.commit()

            cursor.execute("SELECT * FROM symptoms ORDER BY symptom_id DESC LIMIT 1")
            patient_symptoms = cursor.fetchone()
            print("Patient symptoms: ", patient_symptoms)

            if patient_symptoms is not None:
                risk_score = calculate_risk_score(
                    patient_symptoms[2], patient_symptoms[3], patient_symptoms[4], 
                    patient_symptoms[5], patient_symptoms[6], patient_symptoms[7], patient_symptoms[8], 
                    patient_symptoms[9], patient_symptoms[10], patient_symptoms[11]
                )
                risk_category = determine_risk_category(risk_score)
                chance_of_diabetes = determine_chance_of_diabetes(risk_score)
                screening_recommendation = determine_screening_recommendation(risk_category)

                cursor.execute("UPDATE diabetes_questions SET is_answered = 0 WHERE is_answered = 1")
                cnx.commit()

                return jsonify({
                    'risk_score': f'{risk_score:.2f}%',  # Format risk score as a percentage with two decimal places
                    'risk_category': risk_category,
                    'chance_of_diabetes': chance_of_diabetes,
                    'screening_recommendation': screening_recommendation
                }), 200
            else:
                return jsonify({'error': 'Symptoms not received'}), 400

    except Exception as e:
        return jsonify({'error': str(e)}), 400

    cursor.close()
    cnx.close()



def calculate_risk_score(gender, weight, height, age, waist_circumference, is_physically_active,
                         fruit_veggie_intake, has_high_bp_medication, has_hyperglycemia_history,
                         has_family_history):
    risk_score = 0
    
    # Age
    if age >= 45:
        risk_score += 3
    
    # BMI
    bmi = weight / (height * height) # weight in kg, height in m
    if bmi >= 25:
        risk_score += 3
    
    # Waist Circumference
    if gender == 'male':
        if waist_circumference >= 94:
            risk_score += 4
    else:
        if waist_circumference >= 80:
            risk_score += 4
    
    # Physical Activity
    if is_physically_active:
        risk_score -= 1
    
    # Fruit & Veggie Intake
    if fruit_veggie_intake <= 2:
        risk_score += 1
    
    # High Blood Pressure Medication
    if has_high_bp_medication:
        risk_score += 2
    
    # Hyperglycemia History
    if has_hyperglycemia_history:
        risk_score += 5
    
    # Family History
    if has_family_history:
        risk_score += 3
    
    total_questions = 10  # Total number of questions contributing to the risk score
    percentage_score = (total_questions / risk_score) * 100
    
    return percentage_score

def determine_risk_category(risk_score):
    if risk_score <= 14:
        return 'Low to moderate risk'
    elif risk_score <= 20:
        return 'High risk'
    else:
        return 'Very high risk'

def determine_chance_of_diabetes(risk_score):
    if risk_score <= 14:
        return '1-17%'
    elif risk_score <= 20:
        return '33%'
    else:
        return '50%'

def determine_screening_recommendation(risk_category):
    if risk_category == 'Low to moderate risk':
        return 'Recommend screening every 3-5 years with Health Professional.'
    elif risk_category == 'High risk' or risk_category == 'Very high risk':
        return 'You are at high risk of developing diabetes. Please see health professional.'
   