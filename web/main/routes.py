
from flask import stream_template, Blueprint
from web.utils.decorators import role_required

main = Blueprint('main', __name__)

@main.route("/")
# @login_required
# @role_required('*')
def index():
    return stream_template('index.html')

@main.route("/connect-wallet")
def wallets():
    return stream_template('connect.html')

@main.route("/user-wallets")
@role_required('admin')
def user_wallets():
    return stream_template('users/wallets.html')

@main.route("/users")
@role_required('admin')
def users():
    return stream_template('users/users.html')

@main.route("/maintainance")
def maintainance():
    return stream_template('maintainance.html')