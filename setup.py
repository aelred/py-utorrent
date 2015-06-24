import os

from setuptools import setup

README = '''uTorrent WEB UI API Client Library in Python'''

setup(name='py-utorrent',
      version='0.2',
      description='',
      long_description=README,
      classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Topic :: Internet :: Bitorrent",
        ],
      author='Filia Tao',
      author_email='Filia.Tao@gmail.com',
      url='',
      keywords='utorrent',
      packages=['utorrent'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
            'simplejson',
            ],
      tests_require=[
            'simplejson',
            ],
      )

