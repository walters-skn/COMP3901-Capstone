# from flask import Flask, request, jsonify


# auth = Flask(__name__)



# def connect_to_db():
#     cnx = mysql.connector.connect(**db_config)
#     cursor = cnx.cursor()
#     return cnx, cursor

# @auth.route('/login', methods=['POST'])
# def login():
#     email = request.json.get('email')
#     password = request.json.get('password')
#     cnx, cursor = connect_to_db()
#     cursor.execute("SELECT * FROM users WHERE email = %s AND password = %s", (email, password))
#     user = cursor.fetchone()
#     # check if is_admin is 0, if so, it is a patient
#     print(user)