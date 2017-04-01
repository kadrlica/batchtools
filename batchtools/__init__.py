#!/usr/bin/env python
"""
Package for working with distributed computing frameworks
"""
__author__ = "Alex Drlica-Wagner"
__email__ = "kadrlica@fnal.gov"

if __name__ == "__main__":
    import argparse
    description = __doc__
    parser = argparse.ArgumentParser(description=description)
    args = parser.parse_args()

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions
