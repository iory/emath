from setuptools import setup, find_packages
from pip.req import parse_requirements
import sys, os, pip

version = '0.0.2'

requirements = [
    str(requirement.req)
    for requirement in parse_requirements('requirements.txt', session = pip.download.PipSession())
]

setup(name='nmmath',
      version=version,
      description="Python Library for Number Theory",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='iory',
      author_email='ab.ioryz@gmail.com',
      url='',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=requirements,
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
