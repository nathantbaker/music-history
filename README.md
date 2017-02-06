# Music History README

## Installation Instructions
1. If you don't have Python version 2.7, 3.2, 3.3, 3.4, or 3.5: install the latest version of [Python](https://www.python.org/downloads/)
1. If you don't have Django version 1.8, 1.9 or 1.10: install the latest version of [Django](https://www.djangoproject.com/download/).
1. Run `git clone git@github.com:nathantbaker/music-history.git` in a folder where you'd like to keep this project.
1. Run `cd music-history` to navigate into the created directory.
1. Run `python manage.py migrate`.
1. Run `python manage.py runserver` to start the Django server.
1. Run `python manage.py createsuperuser` if you aren't a superuser to see access all endpoints.
1. Navigate to [http://127.0.0.1:8000/](http://127.0.0.1:8000/) and log in  to view the API resources.
1. Resources can be added in the admin interface at ([http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin))

## How to Use The API
Follow the steps above to run this app locally. Since this is a RESTful API, you can go to the root URL ([http://127.0.0.1:8000/](http://127.0.0.1:8000/)) to see all resources available and which methods can be used on each resource.