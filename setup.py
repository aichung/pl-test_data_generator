
import sys
import os


# Make sure we are running python3.5+
if 10 * sys.version_info[0] + sys.version_info[1] < 35:
    sys.exit("Sorry, only Python 3.5+ is supported.")


from setuptools import setup


def readme():
    print("Current dir = %s" % os.getcwd())
    print(os.listdir())
    with open('README.rst') as f:
        return f.read()

setup(
      name             =   'test_data_generator',
      # for best practices make this version the same as the VERSION class variable
      # defined in your ChrisApp-derived Python class
      version          =   '0.1',
      description      =   'Outputs test data for classification module (CNI)',
      long_description =   readme(),
      author           =   'AWC',
      author_email     =   'aiwern.chung@childrens.harvard.edu',
      url              =   'http://wiki',
      packages         =   ['test_data_generator'],
      install_requires =   ['chrisapp', 'pudb'],
      test_suite       =   'nose.collector',
      tests_require    =   ['nose'],
      scripts          =   ['test_data_generator/test_data_generator.py'],
      license          =   'MIT',
      zip_safe         =   False
     )
