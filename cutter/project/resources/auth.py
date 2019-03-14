from flask_restful import Resource
from flask import request
from sqlalchemy import exc, or_
from flask_jwt_extended import create_access_token

from project import db, bcrypt
from .user_model import User


class Register(Resource):

    def post(self):
        """
        POST /register
        """
        post_data = request.get_json()
        if not post_data:
            return {"message": "Invalid payload", "status": "fail"}, 400

        username = post_data.get('username')
        email = post_data.get('email')
        password = post_data.get('password')

        try:
            user = User.query.filter(
                or_(User.username == username, User.email == email)).first()
            # check if user exists
            if not user:
                new_user = User(
                    username=username,
                    email=email,
                    password=password
                )
                db.session.add(new_user)
                db.session.commit()
                return {"message": "user added."}, 201
            else:
                return {"message": "That user already exists."}, 400
        # hendle error
        except (exc.IntegrityError, ValueError):
            db.session.rollback()
            return {"message": "Invalid payload"}, 400


class Login(Resource):

    def post(self):
        post_data = request.get_json()
        if not post_data:
            return {"status": "fail", "message": "Invalid payload."}, 400

        username = post_data.get('username')
        password = post_data.get('password')

        try:
            # fetch the user data
            user = User.query.filter_by(username=username).first()
            if user and bcrypt.check_password_hash(user.password, password):
                auth_token = create_access_token(identity=user.id)
                if auth_token:
                    return {
                        "status": "success",
                        "message": "Successfully logged in",
                        "auth_token": auth_token
                    }, 200
            else:
                return {"message": "User does not exist."}, 404
        except Exception:
            return {"message": "Server error. Try again."}, 500
