# Smartcar API implementation

A RESTful API implementation turning information from GM API into clear format on Smartcar endpoints

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

### Prerequisites

Following are the prerequisites to run this program you need to install and how to intall them

```
python3 - The project was built using python 3.6.3, to see which version you have installed
$ python3 --version

Then you may visit the following guidance to install it in your system
For [Linux](http://docs.python-guide.org/en/latest/starting/install3/linux/)
For [MacOS](http://docs.python-guide.org/en/latest/starting/install3/osx/)
```
```
pip - A tool for python library quick installation 
Follow [this](https://stackoverflow.com/questions/6587507/how-to-install-pip-with-python-3) to check and install
```
```
virtualenv - A tool to create isolated python environments to help manage dependencies and versions
Follow [this](http://docs.python-guide.org/en/latest/dev/virtualenvs/) to check and install
```
### Installing

Here is the guide to get a development environment of this project running for you

Please using this github repo url: https://github.com/AmberWangjie/Smartcar-API.git(HTTPS) or git@github.com:AmberWangjie/Smartcar-API.git(SSH) and clone the project into your local directory, then in that directory, make and activate an virtualenv for this project, remember to install the requirements for this virtualenv, now you are all set to play with the program.

```
$ mkdir your-directory
$ git clone <url> your-directory
$ cd your-directory; makevirtualenv your-env
$ source your-directory/your-env/bin/activate
$ pip install -r requirements.txt
```
Under smartcar\, make sure you can see the following file hierarchy.
Note that this project was structured as a DRF project called <b>smartcar</b>, with all the features built in a DRF application inside this project called <b>vehicles</b>; the whole project was developed in a virtual env called <b>smart-api</b> and under the folder called smartcar. The requirement.txt is for holding the dependencies imported into this env.
```
── smartcar
    ├── db.sqlite3
    ├── manage.py
    ├── smartcar
    │   ├── __init__.py
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    └── vehicles
        ├── __init__.py
        ├── admin.py
        ├── apps.py
        ├── migrations
        │   ├── 0001_initial.py
        │   ├── __init__.py
        │   └── __pycache__
        │       ├── 0001_initial.cpython-36.pyc
        │       └── __init__.cpython-36.pyc
        ├── models.py
        ├── serializers.py
        ├── test
        │   ├── __init__.py
        │   ├── __pycache__
        │   │   ├── __init__.cpython-36.pyc
        │   │   ├── test_api.cpython-36.pyc
        │   │   └── test_views.cpython-36.pyc
        │   ├── test_api.py
        │   ├── test_api.py~
        │   ├── test_views.py
        │   └── test_views.py~
        ├── urls.py
        └── views.py
```
If so, to run the server
```
$ python3 manage.py runserver
```
Now you may monitor the HTTP requests information and their responses status in this window for each operation.
You may also visit the simple browsable UI of this API using your favorite browser.
```
http://127.0.0.0:8000/vehicles
```

## Running the tests

The tests for this project were written using Django's unittest framework. Here is how to run the automated tests for this system.
Under smartcar/ (same location to run the server), run the command below, optional is for getting more  information
```
$ python3 manage.py test -v(optional) 2(optional)
```
The results will be shown as "OK" if all of the test cases are passed, otherwise "Failed" with detail error information

### Testcases break down 

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Django Rest Framework](http://www.django-rest-framework.org/) 
* [Django](https://docs.djangoproject.com/en/2.0/intro/) 


## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Amber Wang** - *Initial work* - [AmberWangjie](https://github.com/AmberWangjie)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone who's code was used
* Inspiration
* etc

