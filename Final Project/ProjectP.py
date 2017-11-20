import os
import re
from _csv import reader
from pprint import pprint
from collections import namedtuple
import arrow
import requests
import seaborn
from matplotlib import pyplot
from bs4 import BeautifulSoup
import collections
import string
import csv
import pandas as pd
from scipy.stats import stats

# todo: PLEASE READ THE INSTRUCTIONS CAREFULLY
# todo: Take it instruction at at time, test as you go!
# todo: Don't understand the instructions, please ask!
# todo: ----------------------------------------------
# todo: WARNING: THIS IS NOT A GROUP PROJECT. MAKE SURE THE WORK YOU SUBMIT IS YOUR OWN.


"""
*********
RESOURCES
*********
- You'll be given a folder full of text files, each containing a poem.
- You'll be given a list indicating 10 of these files you are to process.
  Ignore the others!, but DO NOT delete the other data files from the folder.
- You'll also find a poem_info.csv file that contains poem size information you'll need

***************
Your files are:
***************
i-will-sing-you-one-o.txt
place-for-a-third.txt
the-runaway.txt
wild-grapes.txt
a-winter-eden.txt
sitting-by-a-bush-in-broad-sunlight.txt
new-hampshire.txt
pea-brush.txt
the-most-of-it.txt
the-times-table.txt

************************
PART I: GETTING THE DATA
************************
-For each of your poems, calculate the following (I suggest using regular expressions, but that's up to you):
    # BASIC INFO
    - sentences (number of sentences) there's one per line in the text file, so just count the lines.
    - for the next two calculations, I suggest you first
        - get rid of all punctuation except periods.
        - replace newlines with a single space
        - replace any consecutive spaces > 1 with a single space
    - words (number of words)
    - syllables (number of syllables - summed over all words)

    # CALCULATE SOME READABILITY MEASURES.
    (see: https://www.webpagefx.com/tools/read-able/check.php for the formulas for the fkgl, cli, and ari)
    - fkgl (Flesch kincaid grade-level)
    - cli (Coleman Liau Index)
    - ari (Automated readability index)

- This would all be super easy, EXCEPT for the syllables measure, which requires # of syllables in each word.
- Write a function that takes a single word and RETURNS it's # of syllables.
- That function should use requests to grab text from this URL: http://www.dictionary.com/browse/xxxx
  (where xxxx is replaced with the word you're analyzing)
- using the resulting text, search for a 'span' tag that has an attribute called 'data-syllable'
  and then get the data-syllable attribute.
-For, example, with the word 'invisible', you'll get a list like this:
   ['in·vis·i·ble',
   'in·vis·i·ble',
   'in·vis·i·bil·i·ty, ',
   'in·vis·i·ble·ness, ',
   'in·vis·i·bly, ',
   'qua·si-in·vis·i·ble, ',
   'qua·si-in·vis·i·bly, ',
   'inˌvisiˈbility, ',
   'inˈvisibleness, ',
   'inˈvisibly, ']
- Don't automatically just take the first one! Instead, search through this list and for each item,
  see if the the word you're searching for is the same as the current item, if all punctuation was stripped out.
  (including this character (note, you need to COPY/PASTE IT INTO YOUR CODE"): '·'
- If so, then that's your word.
- Now that you have your word, split it up by this character: (it's not a period, copy/paste it: '·').
- The resulting list's length is the syllable count, return it.
- Now you should be able to loop through all the words in your poem and sum the number of syllables you find in each.
- Once you have all of your information (words, sentences, syllables, fkgl, cli, and ari),
  create a CSV file called 'poem_data.csv', that looks sort of like this containing the analysis of all of your poems:

    poemid,poemsize,fkgl,cli,ari
    id1,small,7.2,8.3,2.4       <- these data are just fake examples
    ...
    id10,large,9.9,2.4,6.6       <- these data are just fake examples

**************************
PART II: Analyze the Data
**************************
- Now that you have your poem_data.csv file, you can load it in with pandas.

#### TABLE (print it):
Table 1: mean of fkgl, cli, and ari by poemsize and poemsize

#### STATS (print them nicely formatted, e.g., t(14)=-2.3, p=.02):
t-test cli for poemsize small vs. cli for poemsize medium
t-test cli for poemsize medium vs. cli for poemsize large
t-test cli for poemsize small vs. cli for poemsize large

#### GRAPHS (show them):
Bar Graph: x-axis is poemsize, y-axis = ari
Bar Graph: x-axis is poemsize, y-axis = ari
"""
def syllable_count(word):
    url = 'http://www.dictionary.com/browse/{}'.format(word)
    page = requests.get(url)
    page_text = page.text
    page_text = page_text.encode('utf-8')
    soup = BeautifulSoup(page_text, 'html.parser')
    page_words = [item for item in soup.find_all('span')]  # a list of items where each item is the text between one
    # 'span' tag and the next; DON'T NEED THIS LINE?
    # pprint(page_words)
    syl_data = [tag.get('data-syllable') for tag in page_words if tag.get('data-syllable') is not None]
    sylls = 0
    # print(syl_data)
    for messy_word in syl_data:
        norm_word = messy_word.replace('·', '')
        # pprint(norm_word)

        if norm_word == word.lower():  # WE END UP WITH TWO INSTANCES OF THE WORD, IS THIS GOING TO THROUGH OFF DATA??
            norm_word = messy_word  # what this word was before the strip
            length = norm_word.split('·')
            syl_count = len(length)
            sylls = syl_count
            break

    return sylls

def poetry_analysis():

    poems_needed = ['i-will-sing-you-one-o.txt', 'place-for-a-third.txt', 'the-runaway.txt', 'wild-grapes.txt',
                    'a-winter-eden.txt', 'sitting-by-a-bush-in-broad-sunlight.txt',
                    'new-hampshire.txt', 'pea-brush.txt', 'the-most-of-it.txt', 'the-times-table.txt']

    calculate_cli = []
    calculate_ari = []
    calculate_fkgl = []

    for file in poems_needed:
        with open(os.path.join("allpoems", file), "r") as infile:
            all_text = infile.readlines()
            entry = ''.join(all_text)
            split_words = entry.split()
            no_punc = re.sub(r"[^\w\d\s\.]*", "", entry)
            no_lines_punc = no_punc.replace('\n', ' ')
            ###########################################
            # CALCULATE NUMBER OF LINES
            ###########################################
            def count_lines():
                line_count = 0
                for line in entry:
                    if line == '\n':
                        line_count += 1
                return line_count

            ###########################################
            # CALCULATE NUMBER OF WORDS
            ###########################################
            def count_words():
                count = len(split_words)
                return (count)


            ###########################################
            # CALCULATE NUMBER OF CHARACTERS
            ###########################################
            def count_char():
                return len(no_lines_punc)

            ##########################################
            # CALCULATE NUMBER OF SYLLABLES IN POEMS
            #########################################
            no_newline = no_punc.replace("\n", " ")
            no_extra = re.sub(pattern=r"\s{2,}", repl=" ", string=no_newline)
            the_words = no_extra.split(' ')  # a list of every word in the poem, for every poem
            word_count = len(the_words)
            syllables = 0

            for word in the_words:
                syllables += syllable_count(word)



            ##########################################
            # CALCULATE NUMBER OF FKGL, CLI, ARI
            ##########################################

            FKGL = float(0.39 * (count_words()/count_lines()) + 11.8 * (syllables/count_words()) - 15.59)
            calculate_fkgl.append(FKGL)
            CLI = (5.89 * (count_char()/count_words())) - (0.3 * (count_lines()/count_words())) - 15.8
            calculate_cli.append(CLI)
            ARI = (4.71 * ((count_char()/count_words())) + 0.5 * ((count_words()/count_lines())) - 21.43)
            calculate_ari.append(ARI)

    # ##########################################
    # # CREATING A CSV FILE
    # ##########################################

    df = pd.read_csv('poem_info.csv')
    df.to_csv('poem_data.csv', header=True, index=False)
    poem_data = pd.read_csv('poem_data.csv')
    poem_data = df.loc[[2, 7, 12, 13, 14, 17, 27, 29, 30, 32]]
    poem_data.rename(columns={'poemname': 'poemid'}, inplace=True)
    poem_data['fkgl'] = [float(item) for item in calculate_fkgl]
    poem_data['cli'] = [float(item) for item in calculate_cli]
    poem_data['ari'] = [float(item) for item in calculate_ari]
    poem_data.to_csv('poem_data.csv', header=True, index=False)
    # pprint(poem_data)

    def zprint(*args, **kwargs):
        print(*args, **kwargs, end='\n\n')

    # ##########################################
    # SHOW MEAN
    # ##########################################
    zprint('___MEANS___:\n', poem_data.groupby('poemsize').mean())

    # ##########################################
    # SHOW STATS
    # ##########################################
    small_medium = stats.ttest_ind(poem_data.query('poemsize=="small"')['cli'], poem_data.query('poemsize=="medium"')['cli'], equal_var=False)
    medium_large = stats.ttest_ind(poem_data.query('poemsize=="medium"')['cli'], poem_data.query('poemsize=="large"')['cli'], equal_var=False)
    small_large = stats.ttest_ind(poem_data.query('poemsize=="small"')['cli'], poem_data.query('poemsize=="large"')['cli'], equal_var=False)
    N = len(poem_data.index) - 1
    print('t({})={:0.2f}, p={:0.2f}'.format(N, small_medium.statistic, small_medium.pvalue))
    print('t({})={:0.2f}, p={:0.2f}'.format(N, medium_large.statistic, medium_large.pvalue))
    print('t({})={:0.2f}, p={:0.2f}'.format(N, small_large.statistic, small_large.pvalue))
    fig = seaborn.factorplot(x='poemsize', y='ari', data=poem_data, kind='bar', size = 5)
    pyplot.show(fig)


if __name__ == '__main__':
    poetry_analysis()

