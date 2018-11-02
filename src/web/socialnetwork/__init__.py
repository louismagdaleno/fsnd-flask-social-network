import config  # noqa:E401
from flask import Flask
from flask_login import LoginManager
import os


app = Flask(__name__)

# Environment Configuration
app.config.from_object('config.settings.' + os.environ['ENV'])

# User Session Management
login_manager = LoginManager(app)
login_manager.init_app(app)
login_manager.login_view = 'users.login'

# Database
from .models import db, user, post # noqa:E401
from .models.user import User # noqa:E401
from .models.post import Post # noqa:E401

db.create_all()
db.session.commit()


# Blueprints
from socialnetwork.routes.userauth import userauth # noqa:E401
from socialnetwork.routes.post import post # noqa:E401
from socialnetwork.routes.main import main # noqa:E401
from socialnetwork.routes.errorhandlers import errorhandlers # noqa:E401
from socialnetwork.routes.account import users # noqa:E401

app.register_blueprint(userauth)
app.register_blueprint(post)
app.register_blueprint(main)
app.register_blueprint(errorhandlers)
app.register_blueprint(users)

"""
# Fake Data
# Populate Database Users
homer = User()
homer.name = 'Homer Simpson'
homer.username = 'Homer Simpson'
homer.email = 'homer@simpson.com'
db.session.add(homer)
db.session.commit()

marge = User()
marge.name = 'Marge Simpson'
marge.username = 'Marge Simpson'
marge.email = 'marge@simpson.com'
db.session.add(marge)
db.session.commit()

lisa = User()
lisa.name = 'Lisa Simpson'
lisa.username = 'Lisa Simpson'
lisa.email = 'lisa@simpson.com'
db.session.add(lisa)
db.session.commit()

bart = User()
bart.name = 'Bart Simpson'
bart.username = 'Bart Simpson'
bart.email = 'bart@simpson.com'
db.session.add(bart)
db.session.commit()

# Populate Database posts
post1 = Post()
post1.title = 'Sports'
post1.text = "Son, when you participate in sporting events, it's not whether you win or lose: it's how drunk you get."
post1.user_id = 2
post1.author = 'Homer Simpson'
db.session.add(post1)
db.session.commit()

post2 = Post()
post2.title = 'Fail'
post2.text = "Me fail English? That's unpossible. Facts are meaningless. You could use facts to prove anything that's even remotely true! Homer no function beer well without. You don't win friends with salad. This is the greatest case of false advertising I've seen since I sued the movie The Never Ending Story."
post2.user_id = 3
post2.author = 'Lisa Simpson'
db.session.add(post1)
db.session.commit()

post3 = Post()
post3.title = 'Eww'
post3.text = "Mrs. Krabappel and Principal Skinner were in the closet making babies and I saw one of the babies and then the baby looked at me"
post3.user_id = 4
post3.author = 'Bart Simpson'
db.session.add(post1)
db.session.commit()

post4 = Post()
post4.title = 'Sigh'
post4.text = "We started out like Romeo and Juliet, but it ended up in tragedy. "
post4.user_id = 2
post4.author = 'Marge Simpson'
db.session.add(post1)
db.session.commit()
"""

