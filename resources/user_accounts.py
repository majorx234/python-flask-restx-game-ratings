from flask_restx import Namespace, Resource
from flask import Flask, jsonify, request
from http import HTTPStatus

users = []
myuser = {'username':'TestUser', 'password': 'dd377093c6a6e841a49695cf11b440fb'}
users.append(myuser)

api = Namespace('user_accounts',
                description="user accounts related operations")

@api.route('')
class UserAccounts(Resource):
    def post(self):
        '''Erstelle einen UserAccount'''
        new_user_json = request.json
        print(new_user_json)      
        #id = len(users)
        #print("my id: " + str(id))
        #users.append(new_user_json)
        #return new_user_json, HTTPStatus.CREATED
        username = new_user_json["username"]
        password = new_user_json["password"]
        print("username: {}".format(username))
        print("password: {}".format(password))
        if ( self.logTheUserIn(users,new_user_json)):
            print("ok")
            return new_user_json, HTTPStatus.OK
        else:
            print("computer says no!")
            return new_user_json, HTTPStatus.FORBIDDEN
           
    def get(self):
        '''Gebe alle erstellten User zurück'''
        return users, HTTPStatus.OK

    def logTheUserIn(self, users, newuser):
       #Vergleich mit Passworthash einbauen
        for user in users:
            if  (user["username"] == newuser["username"]) :
                return True
        print("der user is nicht drin")    
        return False  # hier hatter die ganze schleife

