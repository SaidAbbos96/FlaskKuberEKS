#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#
from flask import Flask, request, jsonify, abort
# from jose import jwt
#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#
APP = Flask(__name__)


@APP.route('/', methods=['GET'])
def hello_world():
    return 'Hello, World from Flask!\n'

@APP.route('/auth', methods=['POST'])
def auth():
    return 'Hello, World from Flask!\n'


@APP.route('/contents', methods=['GET'])
def content():
    return 'Hello, World from Flask!\n'


if __name__ == '__main__':
    APP.run(host='127.0.0.1', port=8080, debug=True)
