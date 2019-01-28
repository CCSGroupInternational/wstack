from .cli.options import parse
from .cli.input import process
import sys

def main():
    sys.path.append('.')
    (options, args) = parse()
    process(args)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        exit(2)