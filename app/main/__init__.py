from unittest.main import main
from flask import Blueprint
main = Blueprint('main',__name__)
from ..main import views, errors