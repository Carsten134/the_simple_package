#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click>=7.0', ]

test_requirements = ['pytest>=3', ]

setup(
    author="Carsten Stahl",
    author_email='carstenstahl122@gmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Just a practice package, that bundles all the basic knowledge of algorithms and data-structures.",
    entry_points={
        'console_scripts': [
            'the_simple_package=the_simple_package.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='the_simple_package',
    name='the_simple_package',
    packages=find_packages(include=['the_simple_package', 'the_simple_package.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/Carsten134/the_simple_package',
    version='0.1.0',
    zip_safe=False,
)
