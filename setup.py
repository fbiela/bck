import os

from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
        name = 'bck',
        version = '0.5',
        author = 'Frederico Sales',
        author_email = 'fredericosales@globo.com',
        license = 'GPL3',
        description = ['backup with 7z + python and click.'],
        url = 'https://github.com/fbiela/bck',
        long_description = read('README.md'),
        platform = ['any'],
        py_modules = ['bck'],
        install_requires = [
            'click',
            'psycopg2',
            'sqlalchemy',
            'reportlab',
        ],
        entry_points = '''
            [console_scripts]
            bck=bck:cli
        ''',
)
