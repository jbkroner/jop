import sys
from Encoder import Encoder

def main(args):
    print(Encoder.to_json(args[1:]))


if __name__ == '__main__':
    args = sys.argv
    if '--help' in args:
        print('you requested help!')
    main(args)