from flask import Blueprint

# Create a blueprint
main = Blueprint('main', __name__)

from . import views
from .. import models