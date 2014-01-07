#!/usr/bin/env python

from setuptools import setup, find_packages

import os

def fullsplit(path, result=None):
    """
    Split a pathname into components (the opposite of os.path.join) in a
    platform-neutral way.
    """
    if result is None:
        result = []
    head, tail = os.path.split(path)
    if head == '':
        return [tail] + result
    if head == path:
        return result
    return fullsplit(head, [tail] + result)

packages, data_files = [], []
root_dir = os.path.dirname(__file__)
if root_dir != '':
    os.chdir(root_dir)
myapp_dir = 'suursuo'

for dirpath, dirnames, filenames in os.walk(myapp_dir):
    # Ignore dirnames that start with '.'
    for i, dirname in enumerate(dirnames):
        if dirname.startswith('.'): del dirnames[i]
    if '__init__.py' in filenames:
        packages.append('.'.join(fullsplit(dirpath)))
    elif filenames:
        for f in filenames:
            data_files.append(os.path.join(dirpath.split('/', 1)[1], f))

setup(
    name = "suursuo",
    version = "dev",
    packages=['suursuo'],
    package_data={ 'suursuo': data_files },
    author = "Juho Rutila",
    author_email = "juho.rutila@iki.fi",
    description = "suursuo.fi web app",
    url = "http://suursuo.fi",
    install_requires=[
        'Django==1.5',
        'django-reversion',
        'psycopg2',
        'django-cms',
        'django-social-auth',
        'django-apptemplates',
        'django-blog-zinnia',
        'django-filer',
        'PIL',
        'cmsplugin-zinnia',
        'cmsplugin-filer',
        'django-taggit',
    ],
    zip_safe=False,

)
