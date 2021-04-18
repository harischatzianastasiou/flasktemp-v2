from setuptools import find_packages
from setuptools import setup

setup(
        name='flasktemp',
        version='1.0.0',
        description='contains some sample hello world code using Flask',
        author='tchatzian',
        author_email='harischatzi1988@gmail.com',
        url='https://github.com/tchatzian/flasktemp',
        packages=['flasktemp'],
        include_package_data=True,
        zip_safe=False,
        install_requires=[
            'flask',
            'requests',
        ],
        scripts=['flasktemp/flasktemp.py']
)
