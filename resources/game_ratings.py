from flask_restx import Namespace, Resource
from flask import Flask, jsonify, request
from http import HTTPStatus

games = {} #games stored in memory

api = Namespace('game_ratings',
                 description='game_ratings related operations') 

@api.route('<id>')
class Game(Resource):
    def get(self, id):
        ''' Gest a game by id '''
        if id in games:
            return games[id], HTTPStatus.ok
        else:
            abort(HTTPStatus.NOT_FOUND, 'game {0} not found.' .format(id))

    def delete(self, id):
        ''' removes a game from list'''
        if id in games:
            del games[id]
            return '', HTTPStatus.NO_CONTENT
        else:
            abort(HTTPStatus.NOT_FOUND, 'game {0} not found.' .format(id))
    def put(self, id):
        ''' Updates a game'''
        game = request.json
        # need be more specific with json datastructure
        if id in games:
            games[id] = game
            return game, HTTPStatus.OK
        else:
            abort(HTTPStatus.NOT_FOUND, 'game {0} not found.' .format(id))

@api.route('')
class GameLists(Resource):
    def get(self):
        ''' List alle Games '''
        games_list = list(games.values())
        return games, HTTPStatus.OK

    def post(self):
        '''Adds a game to games'''
        new_game_json = request.json
        print(new_game_json)
        id_from_json = new_game_json['id']
        games[id_from_json] = new_game_json
        return new_game_json, HTTPStatus.CREATED
