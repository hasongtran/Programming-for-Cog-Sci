from pprint import pprint
import os
import calculator  # Todo: uncomment this after you write your calculator.py module!
import collections

"""
Ha Song Tran
Assignment 5 
"""

"""
Python string methods:
https://docs.python.org/3.5/library/stdtypes.html#str.capitalize

For each of these, you will have to carefully scrutinize the script to see how things are formatted.
Where is the text you need? Is there stuff you need to clean up? Are there extra spaces, or newline
characters that will throw off your search. If so, remove them!
We have not yet covered regular expressions, they are not allowed here.
"""

"""
Best role in You've Got Mail
----
Create a function called ygm_best_role that reads in the file 'youve_got_mail.txt'. 
It's in the scripts folder. Make sure that your open command will work on mac or pc by using os.path.join()!!!
Determine the number of different times each character gets to speak.
Make sure you only count the all caps names (we don't care if someone is mentioned elsewhere,
we only want to know how many different times does each character gets to speak. 
The names are offset in a consistent way..can you figure out how to identify them?
E.g., in this snippet:

    INT. KATHLEEN KELLY'S APARTMENT - DAY

                KATHLEEN (O.C.)
        I'll see you tonight.

                FRANK
        Sushi.

                KATHLEEN (O.C.)
        Great.  Bye.

KATHLEEN has 2 sections, and FRANK has 1.

Your function should return a Counter object with all the character names as keys and the counts as the values. 
Make sure you don't count something like 'KATHLEEN' and 'KATHLEEN (O.C.)' as 2 different characters.
*** Manually LOOK through the files and consider which junk, like " (O.C.)" you might need to remove from 
character names before counting.**
To identify these names, you may need to consider how many spaces precedes them on each line, as
well as whether or not they are all caps.

You don't need any error checking here. Just return the Counter object (you'll need the collections module for that)
To see what it should look like, check out the provided tests.

The output of this function should look like this (partial):
Counter({'KATHLEEN': 336,
         'JOE': 301,
         'FRANK': 84,
         'CHRISTINA': 68,
         'PATRICIA': 50,
         'KEVIN': 41,
          ...
         'ROSE': 1,
         'MAUREEN': 1,
         'PERSON IN LINE': 1,
         'PERSON BEHIND HER IN LINE': 1,
         'WILLIAM SPUNGEON': 1,
         'MAN': 1})
"""


def ygm_best_role():
    # open the file and read in the text
    count = collections.Counter()
    list = []
    with open(os.path.join('scripts', 'youve_got_mail.txt'), 'r') as infile:
        all_text = infile.read()
        split_lines = all_text.splitlines()
        # loop over a list of the things you want to remove and remove them
        for line in split_lines:
            line = line.replace('(cont\'d)', '')
            line = line.replace('(V.O.)', '')
            line = line.replace('(V.O. cont\'d)', '')
            line = line.replace('(V.O., cont\'d)', '')
            line = line.replace('(V.O.,cont\'d)', '')
            line = line.replace('(O.C.)', '')
            line = line.replace('ON TELEVISION', '')
            line = line.replace('OVER', '')
            line = line.replace('(V.O, CONTINUES)', '')
            line = line.replace('TOGETHER', '')
            if 'FADE OUT' in line:
                continue
            if '2nd Final White revised' in line:
                continue
            if 'February 2, 1998' in line:
                continue
            # loop over and save the lines that seem to have character names in them
            if line.startswith('                '):
                line = line.strip()
                list.append(line)
                count[line] += 1
        return count
"""
Line counts in A New Hope
----
Write a function called sw_number_lines that reads in 'a_new_hope.txt' from the scripts folder.
Make sure that your open command will work on mac or pc by using os.path.join()!!!
Save a version of the input file except that it has line number on the left side.
For example, this text in a_new_hope.txt:
           A long time ago, in a galaxy far, far, away...

           A vast sea of stars serves as the backdrop for the main title. 
           War drums echo through the heavens as a rollup slowly crawls 
           into infinity.
would be changed to:
0019                A long time ago, in a galaxy far, far, away...
0021                A vast sea of stars serves as the backdrop for the main title. 
0022                War drums echo through the heavens as a rollup slowly crawls 
0023                into infinity.
Make sure that all line numbers are 4 numbers wide.
For the output file name, use 'a_new_hope_lines.txt' and it should be saved in the same scripts folder as the original.
This is a void function!
"""


def sw_number_lines():
    # read in the lines (keep the line endings...we'll need them later)
    with open(os.path.join('scripts', "a_new_hope.txt"), "r") as infile:
        all_text = infile.readlines()
    #  open output file (USE A CONTEXT MANAGER!)
    with open(os.path.join('scripts', 'a_new_hope_lines.txt'), 'w') as outfile:
        write_lines = 1
        #  loop over the lines and write them to the output file along with the line number.
        for line in all_text:
            outfile.write(str(write_lines).zfill(4) + " " + line)
            write_lines += 1
    outfile.close()


"""
(note: This is VERY similar to the faculty directory exercise we've been doing.)
Write a module in another file called calculator.py  
Inside, create the following:
1. A global variable called history (a list)
3. These operator functions:
    add(a, b)
    sub(a, b)
    div(a, b)
    mul(a, b)
    Each of these functions takes two operands, a and b as strings and returns either the appropriate result as a string
    (e.g., add('4', '4') returns '8' or if there is some exception (e.g., type error, or value error), 
    returns the string 'ERROR'...if there is a division by zero error, return 'UNDEFINED'
    NOTE: convert a and b to floats before using them in mathematical operations)
4. At the bottom, under the __name__ == '__main__' area, add little tests to make sure each of the functions in your
   calculator module actually works.

Write a function HERE IN THIS FILE, BELOW, called my_calc (don't forget to import your calculator module)
1. In a while loop, ask the user for input. If they enter a blank line with nothing on it, then break out of the loop.
2. Input should be a command (add, sub, mul, or div) followed by two operands, all separated by spaces,
   for example:
   > add 5 6
   > div 15 / 3
   or if they enter the word 'help', they should be told the possible commands, and be reminded to separate them 
   by spaces. This help message should also tell them that just pressing ENTER/RETURN will quit the program.
3. If you get a line with just 'help', just print the help message.
4. If you get an empty line (including if they accidentally enter a space or a tab), then quit
5. If you get a line that has 3 space delimited parts, the first part is one of the valid commands, and the last
   2 parts are numeric (i.e., strings that contain numbers), then call the appropriate function from the calculator
   module and print the result like this:
   If this input is:
   > div 15 3
   Then the output should look like this:
   15 / 3 = 5
   This input:
   > div 15 0
   Will output:
   15 / 0 = UNDEFINED
6. After printing the result, append this same string to the global history variable inside calculator.
7. If you get the word 'history', don't just print or pprint calculator.history. 
   Instead, loop through history and print each result string on its own line, like this:
   '15 / 3 = 5'
   '15 / 0 = UNDEFINIED'
8. If you get the phrase 'clear history', clear out the contents from calculator.history, 
   and then print 'history cleared.'
9. Otherwise, print this: 'UNKNOWN COMMAND, type "help" for more information.' BUT DO NOT ADD THIS RESULT TO THE HISTORY!

Here is an example run:

Calculator Program. Enter your mathematical expression below.
Enter "help" for help and hit ENTER/RETURN to quit
=============================================================
> 5 + 3
UNKNOWN COMMAND, type "help" for more information.
> add 5 3
5 + 3 = 8.0
> mul 25 4
25 + 4 = 100.0
> sub 100 50
100 + 50 = 50.0
> div 100 4
100 + 4 = 25.0
> exp 4 2
UNKNOWN COMMAND, type "help" for more information.
> history
5 + 3 = 8.0
25 + 4 = 100.0
100 + 50 = 50.0
100 + 4 = 25.0
> clear history
history cleared
> history
> 
"""


def my_calc():
    # show intro text
    print('Calculator Program. Enter your mathematical expression below. '
          '\nEnter "help" for help and hit ENTER/RETURN to quit')
    # start while loop
    while True:
        cmd = input('> ')
        if cmd == "":
            break
        elif 'help' in cmd:
            print('DIRECTORY COMMANDS:')
            print('To add two numbers, enter: add' )
            print('To subtract two numbers, enter: sub')
            print('To multiply two numbers, enter: mul')
            print('To divide two numbers, enter: div')
            print('To view calculator history, enter: history')
            print('To clear calculator history, enter: clear history')
            print('To quit, press enter')
            print('Must type these command like so: command, space, number, space, number. i.e: div 10 2')
        elif cmd == ('add'):
            cmd = cmd.split(" ")
            output = calculator.add(cmd[1], cmd[2])
            print(output)
        elif cmd == 'sub':
            cmd = cmd.split(" ")
            output = calculator.sub(cmd[1], cmd[2])
            print(output)
        elif cmd =='mul':
            cmd = cmd.split(" ")
            output = calculator.mul(cmd[1], cmd[2])
            print(output)
        elif cmd == 'div':
            cmd = cmd.split(" ")
            output = calculator.div(cmd[1], cmd[2])
            print(output)
        elif cmd == 'clear history':
            calculator.clear_history()
            print("history cleared.")
        elif cmd == 'history':
            output = calculator.calc_history()
            print('Here is your calculator history:')
            print(output)
        else:
            print('Invalid command, please try again')


if __name__ == '__main__':

    # just show the top 5 best roles
    counter = ygm_best_role()
    pprint(counter)
    pprint({role: count for role, count in counter.items() if count > 50})

    # just show the top 10 lines from a_new_hope_lines.txt
    sw_number_lines()
    try:
        print('\n')
        with open(os.path.join('scripts', 'a_new_hope_lines.txt'), 'r') as infile:
            pprint(infile.read().splitlines(False)[:10])
    except:
        # broad clause ok here while testing...just in case sw_number_lines() isn't written yet
        print('couldn\'t find "a_new_hope_lines.txt" in the "scripts" folder')

    # try out my calculator code
    calculator.add('4', '6')
    calculator.div('6', '3')
    calculator.mul('4', '5')
    calculator.sub('10', '4')
    my_calc()
