import os
import shutil
import random
import string
import collections

"""
Psych 138
Assignment 4
Winter 2017
Ha Song Tran
"""

# WARNING, DO NOT ALTER THIS TEXT OR THE TESTS BASED ON IT MIGHT FAIL UNNECESSARILY!
crawler = \
    "It is a period of civil war. Rebel spaceships, striking from a hidden base, have won their\
     first victory against the evil Galactic Empire. During the battle, Rebel spies managed\
     to steal secret plans to the Empire's ultimate weapon, the DEATH STAR, an armored space station\
     with enough power to destroy an entire planet. Pursued by the Empire's sinister agents,\
     Princess Leia races home aboard her starship, custodian of the stolen plans that can save\
     her people and restore freedom to the galaxy"

"""
********* RULES & POINT DEDEUCTIONS **********
1. [- 8 POINTS] 
The only thing that should be above __name__ == '__main__' should be imports, function definitions, and global
variable definitions (like the given crawler variable). All other code you write (e.g., temporary tests and prints)
should be placed BELOW __name__ == '__main__', we will not run or look at that code.
2. [- 8 points] 
As in the homework assignments, Python concepts and techniques that we have not yet covered in lecture or that 
have yet to be covered in the assigned book chapters are not to be used in your code. This include list comprehensions.
3. [- 8 points] 
Do not change the structure of this file, i.e., IMPORTS-->FUNCTION DEFS-->NAME==MAIN-->OPTIONAL LOCAL FUNCTION CALLS
4. [- 8 points]
Do not delete function stubs or question text, even if you are not going to answer a question. Also, do
   not comment out a function, even if it doesn't work.

NOTE: You only need to submit assignment4.py with your functions in it, do not submit the test file or any other file.
"""

"""
SUGGESTIONS
1. Consult the book, lecture slides, and previous code you've worked on in class. We are not expecting you to
   take this test from memory.
2. The best strategy is to search for and do first the easiest ones. Then come back to the more challenging ones.
   If you choose one and get stuck, consider coming back to it.
3. Run the tests! If a function fails, you can see exactly which call caused it to fail. When we grade your code,
   we only focus on how the tests run. We do not run your code file directly. 
   For example, if pytest fails and gives you a message like this:
    def test_capital_count():
            print('\nTesting capital_count()\n')
            assert capital_count(declaration) == 36  # variable containing a string
            assert capital_count("Who's woods these are I think I know?") == 3  # normal string
    >       assert capital_count(45) is None  # Not an iterable
    E       assert False is None
    E        +  where False = capital_count(45)

    you see that it passed the first assert (capital_count(declaration) == 36)
    it also passed the second assert (capital_count("Who's woods these are I think I know?") == 3
    but the greater than sign (>) is pointing at the 3rd assert: capital_count(45) is None
    This function is supposed to return None when its parameter is given a non string argument, 
    but it is returning False instead. So go to the code where capital_count() is defined and
    work on passing that test. To see what exception was thrown (i.e., the one you need to handle),
    look below the failed assert in test, you should see the exception output.
"""

"""***************************************************************************************************************"""
"""***************************************************************************************************************"""

"""
Write a function called modify(word_list, modifier, the_text)
    - word_list can either be a comma separated string OR a list of strings. 
      Since you'll need to manually check word_list, you should just complain (and return None) 
      if you get something that is neither a list or a string. Thus, deal with the wrong type of 
      word_list without exceptions.
    - Return a version of the_text (don't update the_text directly!) that has *modifier* in front of
      each word in the word_list.
    - e.g., modify(['Earth', 'day'], 'beautiful', 'Hello Earth, enjoy your day') would return
            "Hello beautiful Earth, enjoy your beautiful day"
    - Handle any errors that may arise from either *modifier* or *the_text* being non-strings
"""

def modify(word_list, modifier, the_text):
    if (type(modifier) != str or type(the_text)) != str:
        print('Error: modifiers and/or the_text must be strings!')
        return None
    if type(word_list) == list:
        word = word_list
    elif type(word_list) == str:
        word = word_list.split(',')
    else:
        print("Error: word_list must be a comma separated list or a list")
        return None

    aword = ''  # creates an empty string
    new_text = the_text.split()  # split the text into individual words
    for i in new_text:
        translation = str.maketrans('', '', string.punctuation)  # remove punctuation
        new = i.translate(translation)
        for j in word:
            if j == new:
                aword = aword + modifier + ' '
        aword = aword + i + ' '
    return aword

"""
Write a function called random_files()
    - Create 9 files INSIDE that folder called 'random1.txt' 'random2.txt', ... 'random9.txt' [STARTS AT 1, NOT 0]
    - Inside each file, write 10 random words taken from the crawler variable (see top of this file).
      Each word needs to be separated by a space and all 10 words are written on one line.
    - NOTE: you MUST achieve this using str.join(). So create your list of random words from crawler,
            then join them together, then write them to an appropriately named file. 
    - No Returns
    - No Exception Handling
    - Your code should result in 9 files being written to the disk in the specified folder
    - Hint: You could just generate a random number and then use that to index a list of words
            from crawler. However, it may be much eaiser if you use random.sample() 
            Either way is fine with us.
"""


# NOTE: Do not alter this function
def setup_folder(folder):
    # NOTE: letting all exceptions be raised if there is a problem
    # try to remove the folder content if folder already exists
    if os.path.isdir(folder):
        shutil.rmtree(folder)
    # try to create create new version of folder
    os.makedirs(folder, exist_ok=True)
    # return true or false depending on whether folder is there and readable
    return os.path.isdir(folder)


def random_files():
    directory = "randfiles"
    setup_folder(directory)  # set up a folder called directory
    randwords = crawler.split()  # split all the words in crawler
    for files in range(9):  # go through 9 files
        file_name = 'random' + str(files + 1) + '.txt'  # creates 1 file
        placement = os.path.join(directory, file_name)  # place the file into the directory
        open_file = open(placement, 'w')  #write inside the file
        rand_word_list = random.sample(randwords, 10)  # choose 10 rand words from crawler
        line = ' '  # create an empty string inside the text file
        update_line = line.join(rand_word_list)  # put all 10 words into 1 line
        open_file.write(update_line)  # return the line


"""
def all_content()
    - If you didn't succeed with the previous problem (which would produce the folder of files for this one),
      that's ok. Just download and use randfile.zip provided with the prompt.
    - Read in the content from each file in randfiles.
    - Remove ALL punctuation from the content.
    - **Return** (not print) a punctuation free paragraph of the content from all files in randfiles.
      The output is a single Python string.
      The content of each file should be on a new line. 
      E.g. the output might look like this:

        restore races spaceships managed Rebel starship people sinister the war
        her Leia a races space to Rebel secret her planet
        first by can It armored hidden agents won have plans
        plans custodian to hidden aboard period their armored Empires entire
        from of home plans is by evil Princess that During
        stolen secret is It plans the first of hidden an
        to spies Empire aboard a won destroy starship home evil
        have agents steal to plans a spaceships managed evil period
        the galaxy is by to aboard Empires their races the

    - NOTE: str.split(), str.join(), and str.replace() will be helpful here.
            os.listdir() will also be needed, but beware that it only gives you a list of names, not paths.
    - NOTE: don't want to type out all the possible punctuation yourself? just import the string module
            and refer to string.punctuation
"""

def all_content():
    out = ''
    # for loop to go through all 9 files
    for files in range(9):
        file_name = 'randfiles/random' + str(files + 1) + '.txt'
        open_file = open(file_name, 'r')  # open file name as read
        read_file = open_file.read()  # read inside the file
        # remove punctuation
        punctuation = ".,'/?!"
        output = ""
        for character in read_file:
            if not character in punctuation:
                output = output + character
        out = out + output + '\n'  # update the new output to have no punctuation then add a new line
        open_file.close()  #close the file
    return out  # return the output from each file
"""
Write a function called lil_stats(values)
    - input should be a list of numbers
    - return a tuple containing the following information (in order)
      average of values in list  
      minimum value in the list
      maximum value in the list
      dispersion of values in list (max - min)
      number of values in the list
    - NOTE: in the problem, you **CAN** use built in functions such as sum, min, and max, 
      but not ones that would require the math or statistics modules (or any module)
    - e.g., if the call was
        lil_stats([8, 6, 7, 5, 3, 0, 9])
      the output should be:
        (5.428571428571429, 0, 9, 9, 7)
    - you must handle exceptions. See the test to get a sense of what exceptions you need to handle.
      NOTE: on exception, just return None. Do not print any helpful messages.
"""


def lil_stats(values):
    try:
        if type(values) == list:
            avg = sum(values) / len(values)
            min_values = min(values)
            max_values = max(values)
            dispersion = max_values - min_values
            num_values = len(values)
            all_values = (avg, min_values, max_values, dispersion, num_values)
            return all_values
        else:
            return None
    except(TypeError, ZeroDivisionError):
        return None


"""
Write a function called lil_stats_nt(values)
    - this function should be identical to lil_stats() except that it outputs a named tuple such that
      it can be used like this:
      result = lil_stats([8, 6, 7, 5, 3, 0, 9])
      print(result.average)   # prints 5.428571428571429
      print(result.minimum)    # prints 0
      print(result.maximum)    # prints 9
      print(result.dispersion) # prints 9
      print(result.N)          # prints 7
"""


def lil_stats_nt(values):
    try:
        if type(values) == list:
            average = sum(values) / len(values)
            minimum = min(values)
            maximum = max(values)
            dispersion = maximum - minimum
            N = len(values)
            tuples_output = collections.namedtuple('result', 'average, minimum, maximum, dispersion, N')
            return tuples_output(average, minimum, maximum, dispersion, N)
        else:
            return None
    except(TypeError, ZeroDivisionError):
        return None


"""
Write a function called bad_key(dictionary)
    - uses dict methods to return True if one of the dictionary's keys is the word 'bad' or 'BAD'
      otherwise return False
    - no erorr handling
"""


def bad_key(dictionary):
    if 'bad'.lower() in dictionary.keys():  # return true if a key in the dictionary is bad
        return True
    elif 'bad'.upper() in dictionary.keys():  # return true if a key in the dictionary is BAD
        return True
    else:  # if bad or BAD is not a key in dictionary, return False
        return False


"""
Write a function called bad_value(dictionary)
    - uses dict methods to return True if one of the dictionary's values is the word 'bad' or 'BAD'
      otherwise return False
    - no error handling
"""


def bad_value(dictionary):
    if 'bad'.lower() in dictionary.values():  # return true if a key in the dictionary is bad
        return True
    elif 'bad'.upper() in dictionary.values():  # return true if a key in the dictionary is BAD
        return True
    else:  # if bad or BAD is not a key in dictionary, return False
        return False


"""
Write a function called word_count(astring)
    - accepts a string that presumably has a space delimited set of words in it.
    - returns a new normal dict (no DefaultDict) containing the counts of each word in astring.
    - you cannot use collections.Counter(), which, by the way, does the same thing!
    - Unlike collections.counter(), you should first remove any punctuation from astring
    - E.g., word_count('how much wood would a wood chuck chuck, if a wood chuck could chuck wood?')
      would produced something like this (could be in diff order though!)
      {'chuck': 4, 'wood': 4, 'a': 2, 'how': 1, 'would': 1, 'much': 1, 'could': 1, 'if': 1}
    - handle any exception(s) caused by providing bad input: message + None
"""


def word_count(astring):
    try:
        translation = str.maketrans('', '', string.punctuation)
        new = astring.translate(translation)
        if type(new) == list:  # error if astring is not a string
            print('Error: astring must be a string!')
            return None
        else:  # if astring is a string
            counter = {}  # creates an empty dictionary
            new_list = new.split(' ')  # split the list of string
            for word in new_list:
                if word in counter.keys(): # if the word is in the key of the dictionary
                    counter[word] += 1
                else:
                    counter[word] = 1
            return counter
    except AttributeError:
            print('AttributeError! Input must be a string! ')
            return None

if __name__ == '__main__':

    print(modify(word_list=['Earth', 'day'], modifier='beautiful', the_text='Hello Earth, enjoy your day'))
    print(modify(word_list='Earth,day', modifier='beautiful', the_text='Hello Earth, enjoy your day'))
    print(modify(word_list=39493, modifier='beautiful', the_text='Hello Earth, enjoy your day'))
    print(modify(word_list='Earth,day', modifier=34323, the_text='Hello Earth, enjoy your day'))
    print(modify(word_list='Earth,day', modifier='beautiful', the_text=32343))

    random_files()

    print(all_content())

    print(lil_stats([8, 6, 7, 5, 3, 0, 9]))
    print(lil_stats([100, 23, 74, 99, 819, 23, 44, 14, 639]))
    print(lil_stats([]))
    print(lil_stats('8,6,7,5,3,0,9'))

    print(lil_stats_nt(values=[8, 6, 7, 5, 3, 0, 9]))

    print(bad_key(dictionary={'one': 1, 'two': 2, 'three': 'tres', 'four': 'shi'}))
    print(bad_key(dictionary={'one': '1', 'two': 2, 'three': 'tres', 'bad': 'shi'}))
    print(bad_key(dictionary={'one': '1', 'two': 2, 'BAD': 'tres', 'four': 'shi'}))
    print(bad_key(dictionary={'one': 'bad', 'two': 2, 'three': 'tres', 'four': 'shi'}))

    print(bad_value(dictionary={'one': 1, 'two': 2, 'three': 'tres', 'four': 'shi'}))
    print(bad_value(dictionary={'one': 'bad', 'two': 2, 'three': 'tres', 'bad': 'shi'}))

    s = 'how much wood, would a wood chuck chuck, if a wood chuck could chuck wood?'
    my_counter = word_count(s)
    print(my_counter)
