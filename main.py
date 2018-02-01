import sys
import Management

def main(args):
    kws = ["Tom", "Finn", "Becky"] # List of keywords to be found
    Management.manager(args[1], kws)

if __name__ == '__main__':
    main(sys.argv)
