from flask import Flask
from dotenv import dotenv_values
import os

config = dotenv_values('.env')


def create_app():
    app = Flask(__name__)  # name of the file
    #     access env variables
    secret_key = config.get('SECRET_KEY')
    app.config['SECRET_KEY'] = secret_key

    return app

