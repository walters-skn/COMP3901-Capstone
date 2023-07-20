from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
from flask import Flask, Blueprint, request, jsonify
from flask_cors import CORS

from components import create_app
from db.connect import db_config

app = create_app()
app.config.from_object(__name__)
app.config["JWT_SECRET_KEY"] = "comp3901-secret-key"
jwt = JWTManager(app)

CORS(app, resources={r'/*': {'origins': '*'}})




if __name__ == "__main__":
    app.run(debug=True)

