from flask import Blueprint, render_template, jsonify
from socialnetwork.models.post import Post
from flask_login import current_user, login_required


main = Blueprint('main', __name__)


@main.route('/')
@main.route("/home")
def index():
    """Returns all posts"""
    posts = Post.query.all()  # noqa:501
    return render_template('main.html',
                           title='Home',
                           posts=posts,
                           current_user=current_user)


@main.route('/api/v1/posts/json')
@login_required
def get_catalog():
    """Returns of all posts"""
    posts = Post.query.all()  # noqa:501
    return jsonify(post=[i.serialize for i in posts])
