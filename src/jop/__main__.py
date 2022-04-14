import sys

def main():
    print("this is from __main__.py")

if __name__ == '__main__':
    args = sys.argv
    if '--help' in args:
        print('you requested help!')
    main()