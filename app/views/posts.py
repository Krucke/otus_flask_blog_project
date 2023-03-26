from flask import Blueprint, render_template, request, url_for, redirect, flash
from http import HTTPStatus
post_app = Blueprint("post_app", __name__)
from models import db
from models.model import Post
from flask_login import login_required


@post_app.get("/")
@login_required
def product_list():
    posts = Post.query.all()
    return render_template('posts/index.html', posts=posts)


@post_app.get("/<int:post_id>")
@login_required
def post_detail(post_id):
    post = Post.query.filter_by(id=post_id).first_or_404()
    return render_template('posts/post.html', post=post)