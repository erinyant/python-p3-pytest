#!/usr/bin/env python3

from not_none_functions import return_not_none

# def test_return_not_none():
#     '''in not_none_functions, function "return_not_none" returns a value that is not None.'''
#     assert False

def test_return_not_none():
    '''in not_none_functions, function "return_not_none" returns a value that is not None.'''
    result = return_not_none()  # Call function want to test
    assert result is not None  # Use assert statement to check if result is not None

if __name__ == '__main__':
    test_return_not_none()  # Call test functions