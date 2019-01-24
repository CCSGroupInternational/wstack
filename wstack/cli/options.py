from optparse import OptionParser
from sys import stderr

usage = "usage: %prog [options]  run file.json"

def parse():
    parser = OptionParser(usage=usage)
    parser.add_option(
        "-f", "--file", dest="filename",
        help="write report to FILE", metavar="FILE"
    )

    options, args = parser.parse_args()
    if len(args) < 1:
        print(usage, file=stderr)
        exit(1)

    return parser.parse_args()
