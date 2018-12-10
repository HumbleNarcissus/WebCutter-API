from flask_restful import Resource
from flask import jsonify, request
from sqlalchemy import exc, or_

from project import db
from .user_model import User


class Register(Resource):

    def post(self):
        """
        POST register/
        """
        post_data = request.get_json()
        if not post_data:
            return {'status': 'fail', 'message': 'Invalid payload'}, 400
        
        username = post_data.get('username')
        email = post_data.get('email')
        
        try:
            user = User.query.filter(
                or_(User.username == username, User.email == email)).first()
            #check if user exists
            if not user:
                new_user = User(
                    username=username,
                    email=email
                )
                db.session.add(new_user)
                db.session.commit()
                return {"message": "user added."}, 201
            else:
                return {"message": "user already exists."}, 400
        #hendle error
        except (exc.IntegrityError, ValueError) as e:
            db.session.rollback()
            return {}, 400





