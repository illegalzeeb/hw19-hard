from flask_restx import Resource, Namespace
from flask import request
from dao.model.user import UserSchema
from implemented import user_service

user_ns = Namespace('users')


@user_ns.doc(params={"username": "Username",
                     "password": "Password",
                     "role": "Role"})
@user_ns.route('/')
class UsersView(Resource):
    def post(self):
        data = dict(request.args)

        return UserSchema().dump(user_service.create(data)), 201
