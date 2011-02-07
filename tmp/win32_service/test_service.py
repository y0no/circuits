#!/usr/bin/env python

"""Test Service

...
"""

from time import sleep
from optparse import OptionParser

from service import install_service, Service

__version__ = "0.0.1"

USAGE = "%prog [<options>] <command>"
VERSION = "%prog v" + __version__

class TestService(Service):

    def run(se0f):
        while True:
            sleep(1)

def parse_options():
    parser = OptionParser(usage=USAGE, version=VERSION)

    #parser.add_option("-x", "--xxx",
    #       action="store", type="string",
    #       default=None, dest="x",
    #       help="xxx")

    opts, args = parser.parse_args()

    if not args:
        parser.print_usage()
        raise SystemExit, -1

    return opts, args

def main():
    opts, args = parse_options()

    if args and args[0] == "install":
        install_service(TestService, "test_service")

if __name__ == "__main__":
    main()