from flask_restx import Namespace, Resource
from flask import Flask, jsonify, request
from http import HTTPStatus

users = []
api = Namespace('user_accounts',
                description="user accounts related operations")

@api.route('')
class UserAccounts(Resource):
    def post(self):
        '''Erstelle einen UserAccount'''
        new_user_json = request.json
        print(new_user_json)      
        id = len(users)
        print("my id: " + str(id))
        users.append(new_user_json)
        return new_user_json, HTTPStatus.CREATED

    def get(self):
        '''Gebe alle erstellten User zurück'''
        return users, HTTPStatus.OK
    
