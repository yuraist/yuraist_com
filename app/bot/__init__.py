from flask import Blueprint

# Create a blueprint
bot = Blueprint('bot', __name__)

from . import views
