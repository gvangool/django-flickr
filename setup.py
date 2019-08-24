import os
from setuptools import setup, find_packages
from flickr import VERSION, DEV_STATUS

setup(
    name='django-flickr',
    version='.'.join(map(str, VERSION)),
    description='Mirror your Flickr into Django.',
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.rst')).read(),
    keywords='django flickr photo photography photoblog',
    author='Jakub Zalewski',
    author_email='zalew7@gmail.com',
    url='https://bitbucket.org/zalew/django-flickr',
    license='BSD license',
    packages=find_packages(exclude=["example",]),
    zip_safe=False,
    package_data = {
        'flickr': [],
    },
    classifiers=[
        'Development Status :: %s' % DEV_STATUS,
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
	'Programming Language :: Python :: 3',
	'Programming Language :: Python :: 3.5',
	'Programming Language :: Python :: 3.6',
	'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3 :: Only',
        'Framework :: Django',
    ],
    python_requires='>=3.5',
    install_requires=[
        'django >= 1.11',
        'munch >= 2.0',
        'django-taggit >= 0.13',
        'oauth2',
    ],
)
