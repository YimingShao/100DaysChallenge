from logbook import Logger, StreamHandler
import sys

def main():
    StreamHandler(sys.stdout).push_application()
    log = Logger('Logbook')
    log.info('Hello, World')


if __name__ == '__main__':
    main()