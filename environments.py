import os

class DevelopmentConfig:
    port = 5000
    debug = True
    log_path = "games_ratings.log"
    documentation_path = "/swagger-ui"

class ProductionConfig:
    port = 8000
    debug = False
    log_path = "games_ratings.log"
    documentation_path = None

configurations = {
    "dev":  DevelopmentConfig,
    "prod": ProductionConfig }

environment = os.environ.get("BG_CONFIG", "dev")
config = configurations[environment]
