#!/usr/bin/env python

from setuptools import setup, find_packages
setup(
    name = "suursuo",
    version = "0.0.1",
    packages=find_packages(),
    include_package_data=True,
    author = "Juho Rutila",
    author_email = "juho.rutila@iki.fi",
    description = "suursuo.fi web app",
    url = "http://suursuo.fi",
    install_requires=[
        'Django==1.5',
        'django-stables==dev',
        'django-reversion',
        'psycopg2',
        'django-cms',
        'django-social-auth',
        'django-apptemplates',
        'django-menus',
    ],
    dependency_links = [
      "https://api.github.com/repos/jrutila/django-stables/tarball/multitenant?access_token=30e539ba9491700b201ccbeda82b8cb722c4064c#egg=django-stables-dev",
    ]

)
