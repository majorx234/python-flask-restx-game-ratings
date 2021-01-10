# python-flask-restx-game-ratings
* example to do REST with python, additional want use SQL Databases and JWT

# folder structure 
* `
├── environments.py
├── main.py
├── models
│   ├── __init__.py
│   └── game_rating.py
├── resources
│   ├── __init__.py
│   └── game_ratings.py
└── tests
    └── test_game_ratings_api.py
`
# environments.py 
* for switching between Develop and Productive envronment
```python
import os

class DevelopmentConfig:
    port = 5000
    debug = True
    log_path = "games_ratings.log"
    documentation_path = "/swagger-ui"
    ...

class ProductionConfig:
    port = 8000
    debug = False
    log_path = "games_ratings.log"
    documentation_path = None
    ...

configurations = {
    "dev":  DevelopmentConfig,
    "prod": ProductionConfig }

environment = os.environ.get("BG_CONFIG", "dev")
config = configurations[environment]
```
# main.py 
* 1st step: 
```python
from flask import Flask
from flask_restx import Api
from environments import config
import logging

app = Flask("games ratings")
api = Api(app,
          version='0.1',
          title='game ratings',
          description='a web service to manage your game ratings',
#          doc=config.documentation_path
          doc='/swagger-ui'
          )
if __name__ == '__main__':
    logging.basicConfig(filename=config.log_path, level=logging.DEBUG)
    logging.info("start game ratings service")

#    app.run(debug=config.debug, port=config.port)
    app.run(debug=True, port=5000)
```
* run with ~~python main.py~~
  * or better `export BG_CONFIG="dev"; python main.py`
* afterwards open in browser: http://127.0.0.1:5000/swagger-ui
* now with use of ~~resources~~ with a namespace:
```python
from flask import Flask
from flask_restx import Api
from environments import config
import logging
from resources.game_ratings import api as game_ratings_api_namespace


app = Flask("User games ratings")
api = Api(app,
          version='0.1',
          title='user game ratings',
          description='a web service to manage your game ratings',
#          doc=config.documentation_path
          doc='/swagger-ui'
          )
api.add_namespace(game_ratings_api_namespace)

if __name__ == '__main__':
    logging.basicConfig(filename=config.log_path, level=logging.DEBUG)
    logging.info("start user game ratings service")

    app.run(debug=config.debug, port=config.port)
```
# resources 
## game_ratings.py 
```python
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
        games[new_game_json['id']] = new_game_json
        return new_game_json, HTTPStatus.CREATED
```
* testing a resource with:
  * ~~POST~~: `curl -H "Content-Type: application/json" --request POST -d '{"id":"2","name":"Mario","designer":"ElizabethHargrave","playing_time":"60Min"}' "http://localhost:5000/game_ratings"`
  * ~~GET~~: `curl --request GET "http://localhost:5000/game_ratings"`


