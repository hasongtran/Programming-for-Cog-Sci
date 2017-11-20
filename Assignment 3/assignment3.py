
"""
Ha Song Tran
Psych 138
Assignment 3
Winter 2017
"""
#
# A small chunk of the Declaration of Independence, Used in some of the problems below.
# WARNING, DO NOT ALTER THIS TEXT OR THE TESTS BASED ON IT MIGHT FAIL UNNECESSARILY!
declaration = """We hold these truths to be self-evident, that all men are created equal, \
that they are endowed by their Creator with certain unalienable Rights, that among these are Life, \
Liberty and the pursuit of Happiness. That to secure these rights, Governments are instituted among Men, \
deriving their just powers from the consent of the governed, That whenever any Form of Government \
becomes destructive of these ends, it is the Right of the People to alter or to abolish it, and to \
institute new Government, laying its foundation on such principles and organizing its powers in such form, \
as to them shall seem most likely to effect their Safety and Happiness. Prudence, indeed, will dictate that \
Governments long established should not be changed for light and transient causes; and accordingly all \
experience hath shewn, that mankind are more disposed to suffer, while evils are sufferable, than to right \
themselves by abolishing the forms to which they are accustomed. But when a long train of abuses and usurpations, \
pursuing invariably the same Object evinces a design to reduce them under absolute Despotism, it is their right, \
it is their duty, to throw off such Government, and to provide new Guards for their future security. Such has been \
the patient sufferance of these Colonies; and such is now the necessity which constrains them to alter their former \
Systems of Government. The history of the present King of Great Britain is a history of repeated injuries and \
usurpations, all having in direct object the establishment of an absolute Tyranny over these States. To prove this, \
let Facts be submitted to a candid world.
"""

"""
Write a function max_num(numlist) that accepts either a list or tuple. 
max_num() should return the maximum value in the list.
Note: Python has a built-in function called max(), you are not to use this function. 
Also, because it exists, don't use the variable name max inside your function.
Use try/except to return None AND print a helpful message if numlist is neither a list or tuple,
or if it contains non-numeric data. Note: ['1', '2', '3'] is OK, but mixed types are not (e.g., [1, '2', '3'])
"""

def max_num(numlist):
    """
        This function failed because I had if __name__ == "__main__". It also failed because instead of trying to get 
        the for loop to go over the length of the numlist, I made it so that it went over the whole list by splicing the 
        first item of the list so it could go over the rest
    """
    if __name__ == "__main__":  # delete this
        try:
            maximum = numlist[0]
            for i in numlist[1:]:  # should have set the for loop to go over the range of length in numlist and check if
            # numlist[i] > maximum
                if maximum < i:  # if maximum is less than the maximum of the list
                    maximum = i   # set the maximum to the max number in the list
            return maximum  # return the new max number
        except TypeError:  # if the numbers in the list is not a list or tuple,
            print('Error: All numbers in list must be either a list or a tuple!')  # prints error message
            return None  # return nothing


"""
Write a function called get_randoms() with 4 parameters low, high, count, and num_type that 
generates and returns a list of random number whose length is equal to the count parameter.
low = lowest number for random number generator, defaults to 0
high = highest number for random number generator, defaults to 100
count = number of random numbers to return (in a list), defaults to 10
num_type = one of the following strings "any", "odd", or "even"
Obviously, if the num_type is any, just generate 'count' random numbers in the specified (or default) range,
put them in a list and return it.
Otherwise, you may need to keep generating numbers until you get 'count' odd or 'count' even numbers, 
depending on the value of num_type, and then return them in a list.
properly handle any TypeError by printing a message about low and high needing to be numeric, then return None
if high is not greater than low, or num_type is not a string, print the appropriate error and return None
"""

import random  # should be at top

def get_randoms(low=0, high=100, count=10, num_type="any"):
    """
       This function failed because I had if __name__ == "__main__".
    """
    if __name__ == "__main__":  # delete this
        try:  # try below
            a_list = [0] * count  # set the list to an empty list returns the number of random numbers in a list
            generator = 0   # set random number generator  to 0
            if high < low:  # checks if the low number is greater than nigh
                print("Low must be less than high!")  # prints error message
                return None  # returns nothing
            if type(num_type) is not str:  #  checks if the num_type a string
                print("Your input must be a string!")  # prints error message
                return None  # returns nothing
            # for i in the range of the count in list
            for i in range(count):
                # while the count is at zero, continue to increment rand numbers up to count value
                while generator == 0:  # while the random number generator is at 0
                    ran_nums = random.randint(low, high)  # generate random numbers between low and high
                    if num_type == "any":  # checks if the num_type is any
                        a_list[i] = ran_nums  # set the list of random umber into a_list
                        generator = 1
                    elif num_type == "odd":  # if input of num_type is odd
                        if ran_nums % 2 != 0:  # checks to see if the random number if the remainder of divide by 2 is 0
                            a_list[i] = ran_nums  # set the list of random umber into a_list
                            generator = 1
                    else:
                        if ran_nums % 2 == 0:  # if the random number is divisible by 2
                            a_list[i] = ran_nums  # set the list of random umber into a_list
                            generator = 1
                generator = 0  # set the number generator back into 0
            return a_list  # return the list of random number
        except TypeError:  # low and high are not in numbers
            print("Error: Low and High has to be numeric!")  # prints an error code
            return None  # return nothing


"""
Write a function called capital_count_w(text) that accepts a string or a list and returns the number capital letters it 
contains. For example, capital_count_w(declaration) should return 36. See test function for other asserts.
"""

def capital_count(text):
    """
    This function failed because I had if __name__ == "__main__". It also failed because I failed to ask the function to 
    accept either a list or a string and instead, I started the code with starting the count at zero when I should've created
    an argument that accepts the list or the string.
    """
    if __name__ == "__main__":  # delete this
        count = 0  # starts the count of the capital letters at 0
        for i in text:  # loop over the text, ends when the text ends
            if i.isupper():  # If the text that the function ran over is in uppercase. Should have the if statement accept a list or a string
                count += 1  # Increment the capital count when the the function finds a capital letter.
        return count  # return the number of capital letters in the text

"""
Write a function called word_distance(the_text, word1, word2)

All parameters should be strings. Just try to proceed with the assumption that they are strings and handle any resulting
type exceptions. If one is raised, return None after printing a nice message about how the parameters all needed to be 
strings. If either word1 or word2 do not exists within the_text, then return None after printing a nice message about 
**which** string is not actually present in the_text. E.g., "Error: word1 does not exist in the_text". Otherwise, 
return the distance in characters between the first letter of word1 and the first letter of word2 in the_text. 
You cannot use looping of any kind in the function

Notes: Assume that word2 comes later in the_text than word1. If strings are supplied in the reverse order, that's ok, 
the distance will just be negative. If there are more than one copy of either word1 or word2 in the_text, 
then this function will only apply to the first instance of each.
"""


def word_distance(the_text, word1, word2):
    try:
        place1 = the_text.find(word1)
        place2 = the_text.find(word2)
        sum = place2 - place1
        if place1 == -1:
            print("Error: word1 does not exist within the_text")
            return None
        elif place2 == -1:
            print("Error: word2 does not exist within the_text")
            return None
        else:
            return sum
    except TypeError:
        print("Error: All parameters must be strings!")
        return None


"""
Create a function called long_words(text, long=5) that returns a list containing any word in text that has exactly 
'long' characters in it. For example long_words("projects go together with ease", 5) == ['projects', 'together']. 
Warning: Before processing 'text', remove any commas, colons, semi-colons, or periods. 
Note: Unlike the other problems here, for this one you don't have to handle any exceptions!!
"""

def long_words(text, long=5):
    """
    This function failed because I had if __name__ == "__main__".
    """
    if __name__ == '__main__': #should take this out!!
        """
        The 4 lines below replaces punctuation with nothing to remove them from the word length
        """
        no_punctuation = text.replace(',', '')
        no_punctuation = no_punctuation.replace(':', '')
        no_punctuation = no_punctuation.replace(';', '')
        no_punctuation = no_punctuation.replace('.', '')
        word_length = [] # Accepts a list of words
        n = no_punctuation.split(' ') #Split the list of words into each word for the for loop to go over
        for i in n: #for loop to go over the list of text
            if len(i) == long: #if statement to check if the length of the word is equal to the length of long
                word_length.append(i) #If it is, add the word to the list of word_length
        return word_length #Prints out the list of words that are the length of "long"





"""
Create a function called reverse_it(the_list, mode='word'). Use try/except to warn users and return None if the_list.
Also check that mode is in ('word', 'list'). If mode is 'word' then return the list in the original order, but with
each word reversed. If mode is 'list', then just return the original list in reversed order.
"""

def reverse_it(the_list, mode = 'word'):
    """
       This function failed because I had if __name__ == "__main__".
    """
    if __name__ == "__main__":
        try:  # try function below
            if mode == 'word':  # checks if mode == "word"
                reversed_words = " "  # creates an empty string
                a_list = []  # accepts a list
                for words in the_list:  # for loop to iterate over words in the_list
                    for i in range(len(words)):  # nested for loop: for the range in the length of the words in the_list
                        reversed_words =  reversed_words + words[len(words) - i - 1]  # set the empty string of the
                        # reversed_words to the original order, reversing each words. Used length to reverse each letters
                        # of the word
                    a_list.append(reversed_words)  # add each reversed words to the list
                    reversed_words = ''  # reset the words to its original empty list
            elif mode == 'list':  # checks if mode is called to list
                a_list = the_list.reverse()  # return the reverse each word of the list
            else:  # if the user does not call either word or list
                print("Mode must contain either 'word' or 'list'!")  # prints error
                return None  # return nothing
            return a_list
        except TypeError:  # if the user enters anything that's not a string
            print('Error: the_list must be in strings!')  # prints error
            return None



if __name__ == '__main__':
    # Todo: Do all of your quick checking and testing down here.

    print(max_num((12, 60, 26, 39, 19, 29, 33)))

    print(get_randoms())

    print(capital_count(declaration))

    print(word_distance(declaration, 'truths', 'self-evident'))

    print(long_words(declaration, 11))

    print(reverse_it(['Michael', 'Dwight', 'Jim', 'Pam', 'Oscar', 'Angela', 'Stanley']))
