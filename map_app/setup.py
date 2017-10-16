from setuptools import setup

setup(name='map_app',
      version='0.79',
      include_package_data=True,
      description='A test map application',
      packages=[
          'map_app',
          'map_app.views',
          'map_app.models',
          'map_app.forms',
          ],
      install_requires=[
          'flask',
          'flask-wtf',
          'sqlalchemy',
          'googlemaps',
          'facebook-sdk',
          'geocoder',
          ],
      zip_safe=False)
