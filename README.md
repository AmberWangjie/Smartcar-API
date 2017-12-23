# Smartcar API implementation

A RESTful API implementation turning information from GM API into clear format on Smartcar endpoints

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

### Prerequisites

Following are the prerequisites to run this program you need to install and how to intall them

<b>python3</b> - The project was built using python 3.6.3, to see which version you have installed
```
$ python3 --version
```
Then you may visit the following guidance to install it in your system
For [Linux](http://docs.python-guide.org/en/latest/starting/install3/linux/)
For [MacOS](http://docs.python-guide.org/en/latest/starting/install3/osx/)

<b>pip</b> - A tool for python library quick installation 
Follow [this](https://stackoverflow.com/questions/6587507/how-to-install-pip-with-python-3) to check and install

<b>virtualenv</b> - A tool to create isolated python environments to help manage dependencies and versions
Follow [this](http://docs.python-guide.org/en/latest/dev/virtualenvs/) to check and install

### Installing

Here is the guide to get a development environment of this project running for you

Please using this github repo url by clicking the button at the upper-right corner of this page and clone the project into your local directory, then in that directory, make and activate an virtualenv for this project, remember to install the requirements for this virtualenv, now you are all set to play with the program.

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
└── smartcar
    ├── db.sqlite3
    ├── manage.py
    ├── smartcar
    │   ├── __init__.py
    │   ├── __pycache__
    │   │   ├── __init__.cpython-36.pyc
    │   │   ├── settings.cpython-36.pyc
    │   │   ├── urls.cpython-36.pyc
    │   │   └── wsgi.cpython-36.pyc
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    └── vehicles
        ├── __init__.py
        ├── __pycache__
        │   ├── __init__.cpython-36.pyc
        │   ├── admin.cpython-36.pyc
        │   ├── models.cpython-36.pyc
        │   ├── serializers.cpython-36.pyc
        │   ├── urls.cpython-36.pyc
        │   └── views.cpython-36.pyc
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
        │   │   ├── test_serializer.cpython-36.pyc
        │   │   └── test_views.cpython-36.pyc
        │   ├── test_api.py
        │   ├── test_serializer.py
        │   └── test_views.py
        ├── urls.py
        └── views.py
```
If you see so, it is time to run the server under smartcar/smartcar
```
$ python3 manage.py runserver
```
Now you may monitor the HTTP requests information and their responses status in this window for each operation.
You may also visit the simple browsable UI of this API using your favorite browser.
```
http://127.0.0.0:8000/vehicles
```
Please reference the The Smartcar API Spec for how to visit each endpoint RESTfully

## Running the tests

The tests for this project were written using Django's unittest framework. Here is how to run the automated tests for this system.
Under smartcar/ (same location to run the server), run the command below, optional is for getting more  information
```
$ python3 manage.py test -v(optional) 2(optional)
```
The results will be shown as "OK" if all of the test cases are passed, otherwise "FAIL|ERROR" with detail information

### Testcases break down 

The tests written for this application were based on both features of different endpoints and functional modules of DRF framework.

Due to the limit of time, the test cases offered here are not be able to cover all of the function points and use cases. For example, in test_view.py and test_serializer.py, only tests for vehicle info and security info offered for now, other tests could be written following the same structures and idea.

* <b>views tests</b> - Testing the flows from objects creation to object retrieving through GET and POST requests to Smart API endpoints
* <b>api tests</b> - Testing the complete flow for every Smart API endpoint from sending requests to GM API endpoints, getting information from responses, parsing and construcing data for requesting Smart API and validating the responses finally
* <b>serializer tests</b> - Testing the flow from objects creation based on models to serializing them to valid data type


### Modules break down

* <b>models</b> - Models are designed to store the objects with some structures into database. In this project, different resources have their own model but related through some attributes.
* <b>serializers</b> - Serializers are used to serializing the instances into representations such as json format in our case. In this project, they are highly uniform with the models.
* <b>views</b> - Views are how data interacting with the web APIs using requests and responses. In this project, views were created based on funcionality of the endpoints and the request methods.
* <b>urls</b> - Urls are url patterns matching resources to API endpoints. In this project, urls were formed along with the resource name and query parameter using regex.


## Built With

* [Django Rest Framework](http://www.django-rest-framework.org/) 
* [Django](https://docs.djangoproject.com/en/2.0/intro/) 


## Versioning

This is so far the only version available from this author. Later development and iteration is recommended to use version management tools for versioning.

## Authors

* **Amber Wang** - *Initial work* - [AmberWangjie](https://github.com/AmberWangjie)

## License

Not applicable yet.

## Acknowledgments

* This project was technically supported by Smartcar Inc, really appreciate the help from their team! 


