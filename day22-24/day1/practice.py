from functools import wraps
import time

def mydecorator(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)
        return result
    return wrapper

@mydecorator
def my_function(args):
    pass

def get_prrofile(name, active=True, *sports, **awards):
    print('Positional arguments (required): ', name)
    print('Keyword arguments (not required, default values): ', active)
    print('Arbitrary argument list (sports): ', sports)
    print('Arbitrary keyword argument dictionary (awards): ', awards)

get_prrofile('julian')

get_prrofile('julian', False)

get_prrofile('julian', False, 'basketball', 'soccer',
             pythonista='special honor of the community', topcoder='2017 code camp')

def show_args(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        print('hi from decorator - args:')
        print(args)
        result = function(*args, **kwargs)
        print('hi again from decorator - kwargs:')
        print(kwargs)
        return result
    return wrapper

@show_args
def get_profile(name, active=True, *sports, **awards):
    print('\n\thi from the get_profile function\n')

get_prrofile('bob', True, 'basketball', 'soccer',
             pythonista='special honor of the community', topcoder='2017 code camp')

