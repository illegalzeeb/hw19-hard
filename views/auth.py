from flask_restx import Resource, Namespace
from flask import request
from implemented import user_service
from service.auth import generate_token, check_token

auth_ns = Namespace('auth')


@auth_ns.route('/')
class AuthView(Resource):
    def post(self):
        data = request.json
        username = data.get("username")
        password = data.get("password")
        role = data.get('role')
        if not username or password:
            return "", 400
        return generate_token(username=username,
                       password=password,
                       role=role,
                       is_refresh=False), 201

    def put(self):
        data = request.json
        if not data.get("refresh_token"):
            return "", 400
        return check_token(data.get("refresh_token")), 200


