#!/usr/bin/python3

import sys
from npm2deb.scripts import main

try:
    sys.exit(main(sys.argv))
except KeyboardInterrupt:
    print("")
    pass
