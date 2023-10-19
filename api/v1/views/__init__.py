"""Blueprint for API"""
from flask import Blueprint
app_views = Blueprint('app.views', __name__, url_prefix='/api/v1')

from api.v1.views.articles import *
from api.v1.views.auth import *
from api.v1.views.autosave import *