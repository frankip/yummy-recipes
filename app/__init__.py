'''
Initialize the app
'''

from flask import Flask

# Initialize the app
app = Flask(__name__, instance_relative_config=True)

# load views
from app import views

# load config files
app.config.from_object('config')

