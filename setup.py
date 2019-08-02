from setuptools import setup
import py2app

APP = ['alien_invasion']
DATA_FILES = ['images/open-location.bmp', 'images/filled-location.bmp']

setup(
    app=APP,
    data_files=DATA_FILES,
    setup_requires=['py2app']
)