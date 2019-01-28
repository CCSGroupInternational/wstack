from optparse import OptionParser
from sys import stderr

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


    return parser.parse_args()
