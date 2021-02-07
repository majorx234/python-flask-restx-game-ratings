from flask_restx import Namespace, Resource
from flask import Flask, jsonify, request
from http import HTTPStatus
from resources.user_account_db_interface import UserAccountDBInterface

userdb = UserAccountDBInterface() 

api = Namespace('user_accounts',
                description="user accounts related operations")

@api.route('')
class UserAccounts(Resource):
    def post(self):
        '''Erstelle einen UserAccount'''
        new_user_json = request.json

        username = new_user_json["username"]
        password = new_user_json["password"]
        
        if (userdb.loginQuery( username, password )):
            return new_user_json, HTTPStatus.OK
        else:
            # HTTPStatus meldung verbessern
            return new_user_json, HTTPStatus.FORBIDDEN
           
    def get(self):
        '''Gebe alle erstellten User zurück'''
        return users, HTTPStatus.OK


