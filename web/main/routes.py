
from flask import g, get_flashed_messages, stream_template, Blueprint, flash, request, jsonify
from flask_login import current_user, login_required
from sqlalchemy import func
import traceback
from datetime import datetime, date, timedelta

from web.models import (
    User, 
)

from web import db, csrf

from web.utils.db_session_management import db_session_management
from web.utils.decorators import role_required

main = Blueprint('main', __name__)

@main.route("/")
@login_required
# @role_required('*')
# @db_session_management
def index():
    user = User.query.filter(User.username==current_user.username).first_or_404()
    return stream_template('index.html')

@main.route("/users")
@role_required('admin')
def users():
    return stream_template('users/users.html')

@main.route("/maintainance")
def maintainance():
    return stream_template('maintainance.html')