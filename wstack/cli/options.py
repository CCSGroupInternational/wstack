from optparse import OptionParser
from sys import stderr
verboseprint = lambda *a, **k: None

usage = "usage: %prog [options] file.json"


def parse():
    global verboseprint
    parser = OptionParser(usage=usage)
    parser.add_option("-q", "--quiet",
                  action="store_false", dest="verbose", default=True,
                  help="don't print status messages to stdout")

    options, args = parser.parse_args()
    if len(args) < 1:
        print(usage, file=stderr)
        exit(1)

    print(options.verbose)
    verboseprint = print if options.verbose else lambda *a, **k: None

    return parser.parse_args()
