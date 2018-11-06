[![license](https://img.shields.io/badge/license-MIT-blue.svg)](https://choosealicense.com/)

<a href="https://www.udacity.com/">
  <img src="https://s3-us-west-1.amazonaws.com/udacity-content/rebrand/svg/logo.min.svg" width="300" alt="Udacity logo svg">
</a> 

# Social Network

## Technologies Used

* `Python`
* `Flask` 
* `SQLAlchemy`
* `Google oAuth 2.0`
* `Flask-Dance`
* `pip-env`
* `git`

## Screens

# Landing Page
![landing_page](https://user-images.githubusercontent.com/33568112/48032280-dd63df80-e10b-11e8-8560-7313f89ae62a.PNG)
# OAuth
![oauth](https://user-images.githubusercontent.com/33568112/47936639-8952c400-de9b-11e8-852e-6120ce6aca1f.PNG)
# Sign In
![sign_in](https://user-images.githubusercontent.com/33568112/48032305-fcfb0800-e10b-11e8-9298-ebc6f74ed4e0.PNG)
# Sign Up
![sign_up](https://user-images.githubusercontent.com/33568112/48032368-3d5a8600-e10c-11e8-8a6c-6b7ce4dc9220.PNG)
# Update Profile
![update_profile](https://user-images.githubusercontent.com/33568112/48032413-60853580-e10c-11e8-91c6-c80291babc02.PNG)
# API
![api](https://user-images.githubusercontent.com/33568112/47936644-8952c400-de9b-11e8-8115-a28277a62571.PNG)
# Create Post
![create_post](https://user-images.githubusercontent.com/33568112/48032508-bd80eb80-e10c-11e8-98b8-24b7bd243020.PNG)
# Logged In - View Posts
![logged_in](https://user-images.githubusercontent.com/33568112/48032542-dee1d780-e10c-11e8-9f72-98b42105fcf6.PNG)

## Key Ideas

* `MVC Design Pattern.` 
* `Separation of concerns.`
* `Scalable application design.` 
* `OAuth.` 
* `Flask, SQLAlchemy, and extensions.` 

## Design and Architecture

This application is organized around a MVC pattern. 

```bash
.
├── config
└── socialnetwork
    ├── utils
    ├── models      # Model
    ├── routes      # Controller
    ├── templates   # View
    ├── forms
    └── static
```


```bash
.
├── config                      
│   └── settings.py           
├── socialnetwork
│   ├── socialnetwprk.db    # db object
│   ├── forms
│   │   └── post.py           # create posts
|   |   └── user.py           # registration, login, update user
│   ├── models
│   │   ├── post.py           
│   │   └── user.py
│   ├── routes
│   │   ├── account.py
│   │   ├── errorhandlers.py
│   │   ├── post.py
│   │   ├── main.py           
│   │   └── userauth.py       # Flashes a signal/instance of blueprint and token via Flask-Dance.
│   ├── services
│   ├── static
│   │   ├── img
│   │   │   └── google.png
|   |   ├── profile_pics
│   │   │   └── default_profile.png      
│   │   └── styles
│   │       └── main.css
│   └── templates             #  Responsive bootstrap 
│       ├── errors
│       │   ├── 403.html      # Error handlers
│       │   ├── 404.html
│       │   └── 500.html
│       ├── account.html
│       ├── layout.html
│       ├── login.html
│       ├── main.html
│       ├── post.html
│       └── register.html
├── manage.py
└── requirements.txt
└── .env
```


## API

```bash
{URI}/api/v1/posts/json
```

## Installation

### Requirements
* Python 3.5+
* <a href="https://github.com/buildthatapp/fsnd-flask-social-network/blob/master/src/web/requirements.txt">requirements.txt</a>

### How to run the project

```bash
Download this project to your computer
cd src/web
virtualenv ENV
source env/scripts/activate
pip install -r requirements.txt
export FLASK_APP=manage.py
flask run
# Navigate to http://127.0.0.1:5000/
```


[(Back to top)](#top)
