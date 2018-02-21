from flask import Blueprint

# Create a blueprint
main = Blueprint('main', __name__)

from . import views
from .. import models


@main.app_context_processor
def inject_permissions():
    return dict(Permission=models.Permission)
