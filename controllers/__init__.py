from flask import Blueprint

user_bp = Blueprint('user_bp', __name__)

from .user_controller import *