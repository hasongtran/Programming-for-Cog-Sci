
# Travis Seymour 2017
# -------------------
# This function is a little advanced (creates something called a decorator).
# Please just ignore this for now. We shall discuss this on the last day of the class.
# I've already put it to use below.
# It just makes sure that each of these functions prints 2 newlines and a series of dashes after being run
# Because the output of some of the functions this week can be long...
#    this helps remember which function produced which output.

# NOTE: This function uses various techniques that are not allowed yet in your own code.
#       Namely: decorators, generic parameters, and use of dunder properties

MAX_RULE = 80

def hr(func):
    def inner(*args, **kwargs):
        line = '-' * MAX_RULE
        param_list = ', '.join([str(arg) for arg in args])
        print('\n{}'.format(line))
        print('{}({})'.format(func.__name__, param_list).center(MAX_RULE))
        print('{}\n'.format(line))
        return func(*args, **kwargs)
    return inner


@hr
def test_function(a, b):
    for i in range(a):
        for j in range(b):
            print(i, j)


if __name__ == '__main__':

    test_function(3, 5)
