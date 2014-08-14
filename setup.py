from setuptools import setup
import os

setup(name='Mezzanine', version='1.0',
      description='Mezzanine on Openshift - py3',
      author='Cody Chiu', author_email='codyit@gmail.com',
      url='http://blog-codyit.rhcloud.com',
      install_requires= [
          'Mezzanine==3.1.9',
      ],
     )
