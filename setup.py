#!/usr/bin/env python

from setuptools import setup, find_packages
setup(
    name = "suursuo",
    version = "dev",
    packages=['suursuo'],
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
        'django-blog-zinnia==0.12.3.1',
        'PIL',
        'cmsplugin-zinnia',
    ],
    zip_safe=False,
    dependency_links = [
      "https://api.github.com/repos/jrutila/django-stables/tarball/multitenant?access_token=30e539ba9491700b201ccbeda82b8cb722c4064c#egg=django-stables-dev",
      "https://api.github.com/repos/jrutila/django-blog-zinnia/tarball/master#egg=django-blog-zinnia-0.12.3.1",
    ]

)
