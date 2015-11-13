import sys

def main(argv):
    print(argv[0])
    print(argv[1])
    print(argv[2])
    print(len(sys.argv))

if __name__ == '__main__':
    main(sys.argv[1:])
