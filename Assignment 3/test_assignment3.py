from Assignment3.assignment3 import *

"""
Psych 138 Winter 2017
Assignment 3 Test Code (Uses pytest module)
Travis Seymour, PhD
----------------------

If any of the function names below have red lines under them, that means
they are not yet defined in your code file. The red lines will automatically
go away as you define each function. You can still run this test, but
obviously tests for functions you have yet to create will fail as expected.
"""


def test_max_num():
    print('\nTesting max_num()\n')
    assert max_num((12, 60, 26, 39, 19, 29, 33)) == 60  # works with a tuple
    assert max_num([16, 51, 29, 52, 24, 98]) == 98  # works with a list
    assert max_num((75, 74)) == 75  # works with only 2 numbers
    assert max_num((42, 42, 42, 42)) == 42  # work when all numbers are the same
    assert max_num(('2', '4', '3')) == '4'  # works fine when values are number strings
    assert max_num(('2', '4', 3)) is None  # fails gracefully with mixed types
    assert max_num(785) is None  # fails gracefully when numlist is not a list


def test_get_randoms():
    print('\nTesting get_randoms()\n')
    rnd_list1 = get_randoms()
    print('rnd_list1: ', rnd_list1)
    assert all([(0 <= r <= 100) for r in rnd_list1])
    rnd_list2 = get_randoms(low=5, high=34, num_type='odd')
    print('rnd_list2: ', rnd_list2)
    assert all([((5 <= r <= 34) and (r % 2 > 0)) for r in rnd_list2])
    rnd_list3 = get_randoms(low=56, num_type='even')
    print('rnd_list3: ', rnd_list3)
    assert all([((56 <= r <= 100) and (not r % 2 > 0)) for r in rnd_list3])


def test_capital_count():
    print('\nTesting capital_count()\n')
    assert capital_count(declaration) == 36  # variable containing a string
    assert capital_count("Who's woods these are I think I know?") == 3  # normal string
    assert capital_count(45) is None  # Not an iterable
    assert capital_count(['a', 'B', 'C', 'd']) == 2  # list of strings
    assert capital_count(['a', 2, 3, 4]) is None  # some non strings


def test_word_distance():
    print('\nTesting word_distance()\n')
    assert word_distance(declaration, 'People', 'Rights') == -296
    assert word_distance(declaration, 'truths', 'self-evident') == 13
    assert word_distance(declaration, 'inhaler', 'Safety') is None


def test_long_words():
    print('\nTesting long_words\n')
    assert long_words(declaration, 0) == []
    assert long_words(declaration, 11) == ['unalienable', 'Governments', 'destructive', 'Governments',
                                           'established', 'accordingly', 'usurpations', 'usurpations']
    assert long_words("", 1) == []


def test_reverse_it():
    print('\nTesting long_words\n')
    the_office = ['Michael', 'Dwight', 'Jim', 'Pam', 'Oscar', 'Angela', 'Stanley']
    assert reverse_it(the_list=the_office, mode='list') == \
           ['Stanley', 'Angela', 'Oscar', 'Pam', 'Jim', 'Dwight', 'Michael']
    assert reverse_it(the_list=the_office, mode='word') == \
           ['leahciM', 'thgiwD', 'miJ', 'maP', 'racsO', 'alegnA', 'yelnatS']
    assert reverse_it(the_list=the_office, mode='firefly') is None
    assert reverse_it(the_list=1600) is None
