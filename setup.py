
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'nanogenmo',
    'author': 'Ross Binden',
    'url': 'https://github.com/alyphen/nanogenmo',
    'download_url': 'https://github.com/alyphen/nanogenmo/releases',
    'author_email': 'ross.binden@gmail.com',
    'version': '0.1',
    'install_requires': [],
    'packages': ['nanogenmo'],
    'scripts': [],
    'name': 'nanogenmo'
}

setup(**config)
