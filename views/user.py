from flask_restx import Resource, Namespace
from flask import request
from dao.model.user import UserSchema
from implemented import user_service

user_ns = Namespace('users')


@user_ns.route('/')
class UserView(Resource):
    def post(self):
        data = request.json

        return UserSchema().dump(user_service.create(data)), 201
