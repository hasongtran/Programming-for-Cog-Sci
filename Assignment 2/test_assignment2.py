from assignment2_trinatran import *  # Change this to match the actual name of your code file!!

"""
Psych 138 Winter 2017
Assignment 2 Test Code (Uses pytest module)
Travis Seymour, PhD
----------------------

If the import statement above has a red line under it, then your code file
must not be called assignment2.py 
It's not supposed to be called that, instead it should be something like
assignment2_travisseymour.py
Whatever it is called, change the import statement above to match it!

If any of the function names below have red lines under them, that means
they are not yet defined in your code file. The red lines will automatically
go away as you define each function. You can still run this test, but
obviously tests for functions you have yet to create will fail as expected.
"""


def test_right_age():
    assert right_age(age=9) is False
    assert right_age(age=18) is True
    assert right_age(age=21) is True
    assert right_age(age=50) is True
    assert right_age(age=89) is False
    assert right_age(age=102) is True
    assert right_age(age="102") is False


def test_dinner_buddy():
    assert dinner_buddy(cost=19.95, rate=.15, people=2) == 11.47125
    assert dinner_buddy(cost=174.95, rate=.20, people=4) == 52.485
    assert dinner_buddy(cost=25.63, rate=".18", people=3) is None
    assert dinner_buddy(cost=68.23, rate=.15, people=0) is None


def test_max_num():
    assert max_num(a=23, b=13, c=44) == 44
    assert max_num(a="23", b=43) is None
    assert max_num(a=87, b=3, c=33) == 87
    assert max_num(a=52, b=52) == 52
    assert max_num(a=23, b=87, c=max_num(44, 98, 33)) == 98


def test_handedness():
    pass


def test_get_random():
    r = get_random()
    assert type(r) is int and (0 <= r < 99)
    r = get_random(low=5, high=34, num_type='odd')
    assert (5 <= r <= 34) and r % 2
    r = get_random(low=56, num_type='even')
    assert (56 <= r <= 100) and (not r % 2)


def test_zjnd():
    assert zjnd(1, 3) == 4.666666666666666
    assert zjnd(123, 187) == 528168.3333333331
    assert zjnd('123', 84) is None
    assert zjnd(12.23, 87.87) is None