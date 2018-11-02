[![license](https://img.shields.io/badge/license-MIT-blue.svg)](https://choosealicense.com/)

<a href="https://www.udacity.com/">
  <img src="https://s3-us-west-1.amazonaws.com/udacity-content/rebrand/svg/logo.min.svg" width="300" alt="Udacity logo svg">
</a> 

# Social Network

## Technologies Used

* `Docker` 
* `Python`
* `Flask` 
* `SQLAlchemy`
* `Google oAuth 2.0`
* `Flask-Dance`
* `pip-env`
* `git`

## Screens

# Landing Page
![landing_page](https://user-images.githubusercontent.com/33568112/47936631-83f57980-de9b-11e8-9c63-89fbaeaf5cf1.PNG)
# OAuth
![oauth](https://user-images.githubusercontent.com/33568112/47936639-8952c400-de9b-11e8-852e-6120ce6aca1f.PNG)
# Sign In
![sign_in](https://user-images.githubusercontent.com/33568112/47936641-8952c400-de9b-11e8-8741-1979a55981b5.PNG)
# Sign Up
![sign_up](https://user-images.githubusercontent.com/33568112/47936642-8952c400-de9b-11e8-82b0-b7609da856c2.PNG)
# Update Profile
![update_profile](https://user-images.githubusercontent.com/33568112/47936643-8952c400-de9b-11e8-8429-643b27601928.PNG)
# API
![api](https://user-images.githubusercontent.com/33568112/47936644-8952c400-de9b-11e8-8115-a28277a62571.PNG)
# Create Post
![create_post](https://user-images.githubusercontent.com/33568112/47936645-89eb5a80-de9b-11e8-8c90-aef669d9bb95.PNG)
# Logged In - View Posts
![logged_in](https://user-images.githubusercontent.com/33568112/47936647-89eb5a80-de9b-11e8-9a06-14dbc84dbdf9.PNG)

## Key Ideas

* `Clean, Readable Code and Design.` 
* `Simplicity over Complexity.`
* `Automation.` 
* `UI/UX matter.` 
* `Build to scale.` 

## Design and Architecture

This application is organized around a MVC pattern. 

```bash
.
├── config
└── app
    ├── models      # Model
    ├── routes      # Controller
    ├── templates   # View
    ├── forms
    └── static
```
Modules and features are isolated and decoupled for single responsibility and seperation of concerns. 

Organized into Package modules to promote code readability, re-use and collaboration.

```bash
.
├── Dockerfile                # Dockerfile is optimized for pip-install Container caching.
├── config                      
│   └── settings.py           # Considered YAML, environment classes inherit from Default class.
├── docker-compose.yml
├── app
│   ├── egu-nyc-dev-001.db    # Required db objects are seeded with Faker.
│   ├── forms
│   │   └── item.py           # Create/Update re-leverage/share unified form.
│   ├── models
│   │   ├── category.py       # Hybrid property/expression to dynamically calc child relationships.
│   │   ├── item.py
│   │   └── user.py
│   ├── routes
│   │   ├── category.py
│   │   ├── errorhandlers.py
│   │   ├── item.py
│   │   ├── main.py           # Leveraged marshmallow for serialization. Single endpoint with nested children.
│   │   └── userauth.py       # Flashes a signal/instance of blueprint and token via Flask-Dance.
│   ├── services
│   ├── static
│   │   ├── img
│   │   │   └── google.png
│   │   └── styles
│   │       └── main.css
│   └── templates             # Limited and avoided logic in templates. Responsive bootstrap with modal window.
│       ├── errors
│       │   ├── 403.html      # Custom error handlers
│       │   ├── 404.html
│       │   └── 500.html
│       ├── item.html
│       ├── layout.html
│       └── main.html
├── manage.py
└── requirements.txt
```


## API

```bash
{URI}/api/v1/posts/json
```

## Installation

### Requirements

Docker (https://www.docker.com/get-started)

### Deploy

```bash
# Clone this repository using git
cd src/web
docker-compose up --build
# Navigate to http://localhost:8000/
```

### Destroy

```bash
docker-compose down -v
```


[(Back to top)](#top)
