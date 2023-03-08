from flask import Flask, request, render_template
from views.products import product_app
from views.user import user_app
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import db

app = Flask(__name__)
app.config.update(
    ENV="dev",
    SECRET_KEY="czxczczxc",
    SQLALCHEMY_DATABASE_URI="sqlite:///project.db",
    SQLALCHEMY_ECHO=True,
)

db.init_app(app)
migrate = Migrate(app, db)
app.register_blueprint(product_app, url_prefix="/products")
app.register_blueprint(user_app, url_prefix="/user")


@app.cli.command("db-create-all")
def db_create_all():
    db.create_all()

@app.route("/")
def root_view():
    print(request.args.get('username'))
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)