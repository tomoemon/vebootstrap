# -*- coding: utf-8 -*-
import os
from os import path
import sys
from . import context


if __name__ == '__main__':
    # python -m vebootstrap.init
    from argparse import ArgumentParser
    parser = ArgumentParser(prog="python -m vebootstrap.{}".format(path.splitext(path.basename(__file__))[0]))
    parser.add_argument("-n", "--no-bootstrap", action="store_true", default=False)
    args = parser.parse_args()

    c = context.Context(sys.executable, "sample.py")
    c.setup()

    bootstrap_file = "bootstrap.py"
    if not args.no_bootstrap and not os.access(bootstrap_file, os.F_OK):
        with open(bootstrap_file, "wb") as fp:
            fp.write("""
# -*- coding: utf-8 -*-
import vebootstrap

if __name__ == '__main__':
    pass
""".lstrip())
