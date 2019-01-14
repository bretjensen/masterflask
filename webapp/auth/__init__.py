from flask_login import LoginManager, AnonymousUserMixin
from flask_bcrypt import Bcrypt

bycrypt = Bcrypt()

login_manager = LoginManager()
login_manager.login_view = "auth.login" 
login_manager.session_protection = "strong"
login_manager.login_message = "Please login to access this page"
login_manager.login_message_category = "info"


class BlogAnonymous(AnonymousUserMixin):
    def __init__(self):
        self.username = 'Guest'

@login_manager.user_loader
def load_user(userid):
    bcrypt.init_app(app)
    from models import User
    return User.query.get(userid)

def create_module(app, **kwargs):
    login_manager.init_app(app)

    from .controllers import auth_blueprint
    app.register_blueprint(auth_blueprint)