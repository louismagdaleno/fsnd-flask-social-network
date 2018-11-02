from flask import (render_template, url_for, request,
                   redirect, Blueprint, abort, flash)
from flask_login import current_user, login_required
from socialnetwork import db
from socialnetwork.models.post import Post
from socialnetwork.forms.post import PostForm
from sqlalchemy import func

post = Blueprint('post', __name__)


@post.route("/post/create", methods=['GET', 'POST'])
@login_required
def create_post():
    """CREATE Post"""
    form = PostForm()
    if form.validate_on_submit():
        new_Post = Post(title=form.title.data,
                        text=form.text.data,
                        user_id=current_user.id)
        db.session.add(new_Post)
        db.session.commit()
        flash('Your Post has been successfully posted!', 'success')
        return redirect(url_for('main.index'))
    return render_template('Post.html', form=form)


@post.route("/post/<int:post_id>/update", methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    """
    UPDATE Post
    :param post_id: Post_id (int) for Post
    """
    post = Post.query.get_or_404(post_id)
    if post.user_id != current_user.id:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.text = form.text.data
        post.time_updated = func.now()
        db.session.commit()
        flash('Your Post has been successfully updated!', 'success')
        return redirect(url_for('post.update_post', post_id=post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.text.data = post.text
    return render_template('post.html', title='Update', form=form)


@post.route("/post/<int:post_id>/delete", methods=['POST'])
@login_required
def delete_post(post_id):
    """
    DELETE Post
    :param post_id: Post_id (int) for Post
    """
    post = Post.query.get_or_404(post_id)
    if post.user_id != current_user.id:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Your Post has been successfully deleted!', 'success')
    return redirect(url_for('main.index'))
