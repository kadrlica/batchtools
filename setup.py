import os,sys
from setuptools import setup
import versioneer

URL = 'https://github.com/kadrlica/batchtools'

setup(
    name='batchtools',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    url=URL,
    author='Alex Drlica-Wagner',
    author_email='kadrlica@fnal.gov',
    scripts = ['bin/csub','bin/cjobs','bin/ckill','bin/cfail'],
    install_requires=[],
    packages=['batchtools'],
    description="Tools for batch job submission and management.",
    long_description=URL,
    platforms='any',
    keywords='python tools',
    classifiers = [
        'Programming Language :: Python',
        'Development Status :: 2 - Pre-Alpha',
        'Natural Language :: English',
        'Intended Audience :: Science/Research',
    ]
)
