import mypackage, sys, os, os.path

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


me = 'Firstname Lastname'
memail = 'Firstname@example.com'
url = 'http://pypi.python.org/pypi/mypackage'

setup (
    name='mypackage',
    version=mypackage.VERSION,
    zip_safe=True,
    description='An empty package to be used as a template for creating a new package for pypi.',
    long_description=open('README.txt','r').read(),
    author=me,
    author_email=memail,
    maintainer=me,
    maintainer_email=memail,
    url=url,
    license='BSD',
    keywords=['template','mypackage', 'empty', 'package', 'example'],
    packages=['mypackage'],
    download_url=url,
    platforms=['Independant'],
    classifiers = [
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        ],
    test_suite='nose.collector',
    tests_require=['nose'],
    )
