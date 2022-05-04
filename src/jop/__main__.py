import sys
from Encoder import Encoder


def main(args):
    # encode as array
    if "-a" in args:

        # remove the flag
        args.remove("-a")
        #
        print(Encoder.to_array(args[1:]))

    # encode as json
    else:
        print(Encoder.to_json(args[1:]))


if __name__ == "__main__":
    args = sys.argv
    if "--help" in args:
        print("you requested help!")
    main(args)
