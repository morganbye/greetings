import os
import binascii

from pyramid.httpexceptions import HTTPUnauthorized
from cornice import Service

"""Globals
"""
# _USERS = {}

"""Validation functions
"""
def _create_token():
    """Create a user token

    Returns:
        binascii hash
    """
    return binascii.b2a_hex(os.urandom(20)).decode('utf-8')


def valid_token(request, **kargs):
    """Validate the token

    Args:
        request (cls): API call
        **kargs:

    Returns:
        request (cls): update API class (user field)
    """

    header = 'X-Messaging-Token'
    htoken = request.headers.get(header)

    if htoken is None:
        raise HTTPUnauthorized()

    try:
        user, token = htoken.split('-', 1)
    except ValueError:
        raise HTTPUnauthorized()

    valid = user in _USERS and _USERS[user] == token

    if not valid:
        raise HTTPUnauthorized()

    request.validated['user'] = user


def unique(request, **kargs):
    """Check to see if user already in user list

    Args:
        request (cls): API call
        **kargs:

    Returns:

    """
    name = request.text

    if name in _USERS:
        request.errors.add('url', 'name', 'This user exists!')
    else:
        user = {'name': name, 'token': _create_token()}
        request.validated['user'] = user


"""ENDPOINT: hello
"""
hello = Service(name='Hello World', path='/', description="A demo REST API")


@hello.get()
def get_hello(request):
    """Generic GET, always returns "Hello World!"

    Args:
        request (cls): API call

    Returns:
        str: "Hello World!"
    """
    return "Hello World!"


@hello.post()
def post_hello(request):
    """POST that returns Hello World with input

    Args:
        request (cls): API call

    Returns:
        str: "Hello {name} World!"
    """
    import pdb; pdb.set_trace()
    return 'Hello {name} World!'.format(name=str(request))


"""ENDPOINT: users
"""
users = Service(name='users', path='/users', description="User registration")


@users.get(validators=valid_token)
def get_users(request):
    """Return a list of current users

    Args:
        request (cls): API call

    Returns:
        list: list of current users
    """
    return {'users': list(_USERS)}


@users.post(validators=unique)
def create_user(request):
    """Creates a new user session

    Args:
        request (cls): API call

    Returns:
        dict:
            {
              'message': 'Hello {user} world!'
              'token': access token
            }
    """
    """Adds a new user."""
    user = request.validated['user']

    # Update global dictionary
    _USERS[user['name']] = user['token']

    # Format return
    return_dict = {'message': 'Hello {user} World!'.format(user=user.get('name')),
                   'token': user.get('token')}

    return return_dict


@users.delete(validators=valid_token)
def delete_user(request):
    """Remove a user from the current session

    Args:
        request (cls): API call

    Returns:
        dict:
            {
              'Goodbye': '{user}'
            }
    """
    """Removes the user."""
    name = request.validated['user']
    del _USERS[name]
    return {'Goodbye': name}

