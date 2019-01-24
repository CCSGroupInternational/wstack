from .cli.options import parse
from .cli.input import process

def main():
    (options, args) = parse()
    process(args)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        sys.exit(2)