from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required


from socialnetwork import db
from socialnetwork.models.user import User
from socialnetwork.models.post import Post
from socialnetwork.forms.user import RegistrationForm, LoginForm, UpdateUserForm
from socialnetwork.utils.picture_handler import add_profile_pic


users = Blueprint('users', __name__)


@users.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.html'))


@users.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        user = User(email=form.email.data,
                    name=form.name.data,
                    username=form.username.data,
                    password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Thanks for registration')
        return redirect(url_for('users.login'))
    return render_template('register.html', form=form)


@users.route('/login', methods=['GET', 'POST'])
def login():

    form = LoginForm()
    if form.validate_on_submit():

        user = User.query.filter_by(email=form.email.data).first()

        if user.check_password(form.password.data) and user is not None:

            login_user(user)
            flash('Log in Success!')

            return redirect(url_for('users.account'))

    return render_template('login.html', form=form)


@users.route('/account', methods=['GET', 'POST'])
@login_required
def account():

    form = UpdateUserForm()
    if form.validate_on_submit():

        if form.picture.data:
            username = current_user.username
            pic = add_profile_pic(form.picture.data, username)
            current_user.profile_image = pic

        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('User Account Updated!')
        return redirect(url_for('users.account'))

    elif request.method == "GET":
        form.username.data = current_user.username
        form.email.data = current_user.email

    profile_image = \
        url_for('static',
                filename='profile_pics/' + current_user.profile_image)
    return render_template('account.html',
                           profile_image=profile_image, form=form)


@users.route('/<username>')
def user_posts(username):
    page = request.args.get('/page', 1, type=int)
    user = User.query.filter_by(username=username).first_or_404()
    posts = Post.query.filter_by(author=user).\
        order_by(Post.date.desc()).pageinate(page=page, per_page=5)
    return render_template('user_posts.html', posts=posts, user=user)
