import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'README.md')) as f:
    README = f.read()


setup(name='greetings',
      version=0.1,
      description='Greetings',
      long_description=README,
      classifiers=[
          "Programming Language :: Python",
          "Framework :: Pylons",
          "Topic :: Internet :: WWW/HTTP",
          "Topic :: Internet :: WWW/HTTP :: WSGI :: Application"
      ],
      keywords="web services",
      author='Morgan Bye',
      author_email='morgan@morganbye.com',
      url='http://morganbye.com',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=['pyramid',
                        'cornice',
                        'waitress'],
      entry_points="""\
      [paste.app_factory]
      main=greetings:main
      """,
      paster_plugins=['pyramid'])
