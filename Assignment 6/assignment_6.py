import os
import re
import collections
from horizontalrule import hr
from pprint import pprint
import sometext

"""
Psych 138 Spring 2017
Assignment 6
Ha Song Tran
htran15
"""

"""
THE FOLLOWING ARE PROHIBITED FOR THIS ASSIGNMENT:
- str.split(), str.search(), str.strip(), str.lower(), str.upper() or the string module 
  [this is all to force you to fully explore the re module]
"""

"""
WHAT TO DO
- Count the number of words in text that have 8 or more characters in them.
- You are to use regular expressions to identify and collect these words.
- Do not include symbols, numbers , and newlines in the words you consider. 
- There are some words with trailing numbers, e.g., 'Stimulus1' or 'Task2', 
  you should match these words if they are long enough.
WHAT TO RETURN
- Return a list of all the words that have lengths over 8, or an empty list if there are none.
- Make sure the words you're returning don't have leading or trailing spaces.
- E.g.,:
['Attention', 'Performance', 'Although', 'explores', 'contexts', 'participants',....]
"""


@hr
def how_pedantic(text=sometext.webblurb):
    # create a pattern that matches all words in text that are 8 or more characters long.
    empty_list = []
    entry = ''.join(text)
    # use findall to get all matches of your pattern
    # whether or not there are other steps here, depends on exactly how you choose to write your pattern.
    pattern = r'\w{8,}\d*'
    eight_letters = re.findall(pattern, entry)
    if not pattern:
        return empty_list
    # return your word list (or an empty list if you pattern matches no words in text)
    else:
        return eight_letters


"""
WHAT TO DO
- Use regex to find all of the citations in text.
- Citations include a sequence of authors and dates surrounded by parentheses.
  For example (Posner, 1975) or (Seymour & Fraynt, 2008).
  Look in the text yourself to see how they vary!
  Remember that open and close parens are used to specify groups in regular expressions. So if you
  actually want to match parens characters in text, you need to escape these characters in your regex pattern
TO RETURN
- Return a list of all the words that have lengths over 8, or an empty list if there are none.
- Make sure the words you're returning don't have leading or trailing spaces.
E.g.,
['(viz, Pashler 1994)', '(Schumacher, Seymour, Glass, Kieras, & Meyer, 2001)',.....]
"""


@hr
def citations(text=sometext.webblurb):
    # we helped you plan out the previous function, for this one, you're on your own.
    empty_list = []
    entry = ''.join(text)
    pattern = r"[(].+\d{4}[)]"
    find_citations = re.findall(pattern, entry)
    if not pattern:
        return empty_list
    else:
        return find_citations


"""
WHAT TO DO
- In the data folder there are several data files from one of my experiments using a virtual environment from 1995!
- For each file, you are to extract 
  a) The participant's ID and SEX, both of which can be found in text towards the top of the file 
     that looks sort of like this:
     "SUBJECT = 1212 female"
  b) The participant's debriefing responses, that can be found towards the end of the file between the phrases
     "START DEBRIEF" and "END DEBRIEF".
- Debriefing responses have numbers in front of them. We want to remove those and combine all of one person's responses
  into a single paragraph without any newline breaks.
WHAT TO RETURN
- a named tuple with the following fields 'id', 'sex' and 'debrief'
E.G., imagine you have this information in a file:

SUB0001.TXT
-----------
SUBJECT = 0001 female
...
START DEBRIEF
1) Yes I felt like I was in a hurry.
2)  I thought the program was fun.
3)  No I have never played a game like this.
END DEBRIEF

Your output should be a list of named tuples that each look something like this:
[(DEBRIEF_RECORD(id='1212', sex='female', debrief="Yes I felt like I was in a hurry. I thought the program was fun. No I have never played a game like this.")]
"""


@hr
def debrief_records(data_folder='data'):
    hold_records = []
    DEBRIEF_RECORDS = collections.namedtuple('DEBRIEF_RECORDS', 'id sex debrief')
    file_list = [file for file in os.listdir(data_folder) if file.endswith('.TXT')]
    for files in file_list:
        with open(os.path.join(data_folder, files), 'r') as infile:
            all_text = infile.readlines()
            no_new_lines = re.sub(pattern=r'\n', repl='', string=''.join(all_text))
            no_start_end = re.sub(pattern=r'END DEBRIEF.*', repl='', string=no_new_lines)
            debrief_pattern = r'1[)]\s*\w+.*'
            match_debrief = re.findall(debrief_pattern, no_start_end)

            no_numbers = re.sub(pattern = r'\d[)]', repl='', string=''.join(match_debrief))
            debrief = re.sub(pattern=r'\s{2,}', repl=' ', string=no_numbers)
            debrief = re.split(pattern='\n', string=debrief)
            pattern_id_sex = r'(\d{4}) (female|male)'
            match_id_sex = re.findall(pattern_id_sex, ''.join(all_text))
            for id, sex in match_id_sex:
                for words in debrief:
                    debrief_all = DEBRIEF_RECORDS(id, sex, words)
                    hold_records.append(debrief_all)

    return hold_records




"""
WHAT TO DO
- In the scripts folder there are 3 movie script files.
- For each file, you are to use regular expressions to 
-    obtain a list of the words it contains that are in sometext.pleasant
-    obtain a list of the words it contains that are in sometext.unpleasant
-    create a namedtuple called SENTIMENT_ANALYSIS that has the fields 'file', 'positive', 'negative', and 'ratio'
-       file will be the name of the file you're processing at the moment
-       positive will be the NUMBER of positive words you found in the script
-       negative will be the NUMBER of negative words you found in the script
-       ratio will be positive/negative
-    add this namedtuple to an output list.
WHAT TO RETURN
- A list of the namedtuples described above, e.g.:
[SENTIMENT_ANALYSIS(file='a_new_hope.txt', positive=260, negative=180, ratio=1.4444444444444444),
 SENTIMENT_ANALYSIS(file='double_indemnity.txt', positive=392, negative=115, ratio=3.408695652173913),
 SENTIMENT_ANALYSIS(file='youve_got_mail.txt', positive=227, negative=82, ratio=2.768292682926829)]
HINT
- You are going to have to first programatically BUILD a regex expression using the words you are looking for.
- Luckily, a regex string is just a kind of string and you should already know how to piece those together.
- Just make sure you don't forget the `r` in front of the string, e.g.: r'expression here'
- You're going to want to ignore case in your match!
NOTE
- This code may take several seconds to run...it's checking a lot of words!
"""


@hr
def sentiment_analysis(data_folder='scripts', pos_words=sometext.pleasant, neg_words=sometext.unplesant):
    pos_neg_words = []
    SENTIMENT_ANALYSIS =  collections.namedtuple("SENTIMENT_ANALYSIS", "file positive negative ratio")
    file_list = [file for file in os.listdir(data_folder) if file.endswith(".txt")]
    for file in file_list:
        with open(os.path.join("scripts", file), "r") as infile:
            all_text = infile.readlines()
            no_new_lines = re.sub(pattern=r'\n', repl='', string="".join(all_text))
            positive_pattern = r' *({})'
            postive_seq = ''
            for words in pos_words:
                postive_seq += words + '|'
            postive_seq = postive_seq[:-1]
            positive_pattern = positive_pattern.format(postive_seq)
            match_pos = re.search(positive_pattern, no_new_lines, re.IGNORECASE())

            neg_pattern = r' *({})'
            neg_seq = ''
            for words in neg_words:
                neg_seq += words + '|'
            neg_seq = neg_seq[:-1]
            neg_pattern = neg_pattern.format(neg_seq)
            match_neg = re.search(neg_pattern, no_new_lines, re.IGNORECASE())

            pos_count = collections.Counter(match_pos)
            neg_count = collections.Counter(match_neg)
            pos = sum(pos_count.values())
            neg = sum(neg_count.values())
            ratio = pos/neg
            output = SENTIMENT_ANALYSIS(file, pos, neg, ratio)
            pos_neg_words.append(output)

    return pos_neg_words



if __name__ == '__main__':
    print(how_pedantic())
    pprint(citations())
    pprint(debrief_records())
    pprint(sentiment_analysis())
