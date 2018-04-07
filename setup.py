from setuptools import setup

setup(
   name='mrtg-compose',
   version='1.0',
   description='Command-line tool to compose MRTG configuration file',
   author='Web Cerebrium',
   author_email='webcerebrium@gmail.com',
   packages=['mrtg-compose'],  #same as name
   install_requires=[], #external packages as dependencies
   scripts=[
    'mrtg-compose.py'
   ]
)