from flask_restx import Namespace, Resource
from flask import Flask, jsonify, request
from http import HTTPStatus

users = {}

api = Namespace('user_accounts',
                description="user accounts related operations')
