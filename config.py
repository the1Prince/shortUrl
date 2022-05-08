import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    # ...
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'mongodb+pymongo://localhost:27017/users'

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SERCRET_KEY = '5f4feabe-e605-4deb-944a-6940de13b5b5'