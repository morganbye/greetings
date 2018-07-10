""" Cornice services.
"""
from cornice import Service


hello = Service(name='Greetings API', path='/', description="A demo REST API")


@hello.get()
def get_info(request):
    """Returns Hello in JSON."""
    return {'Hello': 'World'}

