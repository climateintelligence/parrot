#!/usr/bin/env python

"""The setup script."""

import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()
CHANGES = open(os.path.join(here, 'CHANGES.rst')).read()
REQUIRES_PYTHON = ">=3.6.0"

about = {}
with open(os.path.join(here, 'parrot', '__version__.py'), 'r') as f:
    exec(f.read(), about)

requirements = [line.strip() for line in open('requirements.txt')]

dev_reqs = [line.strip() for line in open('requirements_dev.txt')]


classifiers = [
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Intended Audience :: Science/Research',
    'Operating System :: MacOS :: MacOS X',
    'Operating System :: POSIX',
    'Programming Language :: Python',
    'Natural Language :: English',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
    'Programming Language :: Python :: 3.11',
    'Programming Language :: Python :: 3.12',
    'Topic :: Scientific/Engineering :: Atmospheric Science',
    'License :: OSI Approved :: Apache Software License',
]

setup(
    name='parrot',
    version=about['__version__'],
    description="A little intelligent bird that likes to talk much.",
    long_description=README + '\n\n' + CHANGES,
    long_description_content_type="text/x-rst",
    author=about['__author__'],
    author_email=about['__email__'],
    url='https://github.com/climateintelligence/parrot',
    python_requires=REQUIRES_PYTHON,
    classifiers=classifiers,
    license="Apache Software License 2.0",
    zip_safe=False,
    keywords='wps pywps birdhouse parrot',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requirements,
    extras_require={
        "dev": dev_reqs,  # pip install ".[dev]"
    },
    entry_points={
        'console_scripts': [
            'parrot=parrot.cli:cli',
        ]
    }
)
