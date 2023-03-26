from flask import Flask, request, render_template
from views.posts import post_app
from views.auth import auth_app
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import db
from models.model import Post
from flask_login import LoginManager, login_required, current_user


app = Flask(__name__)
app.config.update(
    ENV="dev",
    SECRET_KEY="czxczcz24879650678gsdfhjigsd893q7453xc",
    SQLALCHEMY_DATABASE_URI="sqlite:///project.db",
    SQLALCHEMY_ECHO=False,
)

db.init_app(app)
migrate = Migrate(app, db)
app.register_blueprint(post_app, url_prefix="/posts")
app.register_blueprint(auth_app)


def localize_callback(*args, **kwargs):
    if 'Please log in to access this page.' in args:
        return 'Авторизуйтесь для просмотра данной страницы.'
    return ''


login_manager = LoginManager()
login_manager.login_view = 'auth_app.login'
login_manager.init_app(app)
login_manager.localize_callback = localize_callback

from models.model import User

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# @app.cli.command("db-create-all")
# def db_create_all():
#     db.create_all()

@app.route("/")
@login_required
def root_view():
    posts = Post.query.all()[:3]
    return render_template("index.html", posts=posts)


@app.route("/contacts")
@login_required
def contacts_view():
    return render_template('contacts.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=False)