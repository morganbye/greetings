# Greetings

A demo project of a REST API with "Hello World" functionality

[![Build Status](https://travis-ci.org/morganbye/greetings.svg?branch=dev)](https://travis-ci.org/morganbye/greetings)

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing 
purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

- Python3.5+

### Installing

Create a new virtual env

```
$ mkdir venv-greetings
$ python3 -m venv venv-greetings/
$ source venv-greetings/bin/activate
```

Checkout the latest release from Github

```
$ git clone https://github.com/morganbye/greetings.git
```

With the virtual env, install the repo with editable permissions

```
$ cd greetings
$ pip install -e ".[testing]"
```

The application can how be launched using the in-built Pyramid `pserve` command 

```
$ pserve greetings.ini
Starting server in PID 9703.
Serving on http://0.0.0.0:6543
```

Once the application is running, visit http://127.0.0.1:6543 in your browser and make sure you get:

```
{'Hello': 'World'}
```

You should also get the same results calling the URL via Curl on the command line:

```
$ curl -i http://localhost:6543/
```

Yielding,

```
HTTP/1.1 200 OK
Content-Length: 18
Content-Type: application/json
Date: Tue, 10 Jul 2018 17:00:42 GMT
Server: waitress
X-Content-Type-Options: nosniff

{"Hello": "World"}
```

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Example usage

### Hello World!

A generic "Hello World!" example can be achived using no endpoints
 
```
$ curl http://localhost:6543/
"Hello World!"

```

### User specific examples

Trying to access the `users` endpoint with no authorize returns a 401 error.

```
$ curl http://localhost:6543/users
{"status": 401, "message": "Unauthorized"}
```

Instead create a new user session

```
$ curl --request POST http://localhost:6543/users -d 'dave'
{"token": "dave-12aae04cbf6d94320f1ff5fd5efa1173296a7097"}
```

Now call the users list with the token

```
$ curl http://localhost:6543/users -H "X-Messaging-Token:dave-12aae04cbf6d94320f1ff5fd5efa1173296a7097"
{"users": ["dave"]}
```

We can then remove the user with

Now call the users list with the token

```
$ curl --request DELETE http://localhost:6543/users -H "X-Messaging-Token:dave-12aae04cbf6d94320f1ff5fd5efa1173296a7097"
{"Goodbye": "dave"}
```

## Deployment

Move to production environment

```
$ cd /production/greetings
```

Create a new directory, and link production

```
$ unlink production
$ mkdir v0.1
$ ln -s v0.1 production
```

Setup git

```
$ git init
$ git clone https://github.com/morganbye/greetings.git
```

Create a Python virtual environment.

```
$ python3 -m venv env
```

Upgrade packaging tools.

```
$ env/bin/pip install --upgrade pip setuptools
```
Install the project in editable mode with its testing requirements.

```
$ env/bin/pip install -e ".[testing]"
```

Ensure the tests pass

```
$ env/bin/pytest
```

Run your project.

```
env/bin/pserve greetings.ini &
```

## Built With

* [Pyramid](https://trypyramid.com/) - The web framework used
* [Cornice](https://cornice.readthedocs.io/en/latest/) - REST web service management
* [Cookiecutter](https://cookiecutter.readthedocs.io/en/latest/) - Project templating

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Morgan Bye** - *Initial work* - [GitHub](https://github.com/morganbye), [Personal](http://morganbye.com)

See also the list of [contributors](https://github.com/morganbye/greetings/graphs/contributors) who participated in this project.

## License

This project is licensed under the GNU GENERAL PUBLIC LICENSE (v3) - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Karen Eddy [LinkdedIn](https://www.linkedin.com/in/karen-eddy-45975aab/)

