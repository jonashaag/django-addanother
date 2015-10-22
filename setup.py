# encoding: utf-8

from setuptools import setup


setup(
    name='django_addanother',
    version='0.1.2',
    author='Jonas Haag',
    author_email='jonas@lophus.org',
    packages=['django_addanother'],
    zip_safe=False,
    include_package_data=True,
    url='https://github.com/jonashaag/django-addanother',
    description='"Add another" buttons outside the Django admin',
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: ISC License (ISCL)",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
    ],
    install_requires=['django'],
)

