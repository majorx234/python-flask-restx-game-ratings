from flask import Flask
from flask_restx import Api
from environments import config
import logging
from resources.game_ratings import api as game_ratings_api_namespace
from resources.user_accounts import api as user_accounts_api_namespace 

app = Flask("User games ratings")
# wir erstellen eine REST-Api mittels restx und flanschen die an die app
# app is von Flask , api is von restx
api = Api(app,
          version='0.1',
          title='user game ratings',
          description='a web service to manage your game ratings',
#          doc=config.documentation_path
          doc='/swagger-ui'
          )

#zugänglich machen
api.add_namespace(game_ratings_api_namespace)
api.add_namespace(user_accounts_api_namespace)

if __name__ == '__main__':
    logging.basicConfig(filename=config.log_path, level=logging.DEBUG)
    logging.info("start user game ratings service")

    app.run(debug=config.debug, port=config.port, host= '0.0.0.0')
            
