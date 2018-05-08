import sys
from functools import wraps
import os
import datetime

file_name = 'report.txt'


def main():
    @report_decortor(return_boolean=False)
    def printer():
        for i in range(0,10):
            print(i)
    printer()

    @report_decortor(return_boolean=True)
    def get_text(txt):
        return txt

    txt = get_text('A very nice output')


def report_decortor(return_boolean=True):
    def write_report(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if os.path.exists(file_name):
                f_mode = 'a'
            else:
                f_mode = 'w'
            f = open(file_name, f_mode)
            today_date = str(datetime.datetime.now())
            f.write('\nDate: {}'.format(today_date))
            if return_boolean is True:
                f.write('func {} has a return result:\n{}\n'.format(func.__name__, str(func(*args, **kwargs))))
            else:
                f.write('func {} does not has a return result:'.format(func.__name__))
                sys.stdout=f
                func(*args, **kwargs)
                
                #sys.stdout = sys.__stdout__ (could print result in console)
                #func(*args, **kwargs)
                print()
            f.close()

        return wrapper

    return write_report


if __name__ == '__main__':
    main()