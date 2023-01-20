from flask import request
from flask_restful import Resource
from http import HTTPStatus
from models.user import User

class UserListRecource(Resource):

    def post(self):
        data = request.get_json()

        username = data.get('username')
        password = data.get('passoword')

        if User.get_by_username(username= username):
            return {'messege': 'username already in use'}, HTTPStatus.BAD_REQUEST

        user = User(
            username=username,
            password=password
        )

        user.save()

        return user.data, HTTPStatus.CREATED