import os
basedir = os.path.abspath(os.path.dirname(__file__))

# Windows = Documents\codingtemple-july2020\week5\day1\
# Mac & Linux = Documents/codingtemple-july2020/week5/day1/

class Config():
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you will never guess...'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir,'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
