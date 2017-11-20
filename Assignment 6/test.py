import os
import re
import collections
from horizontalrule import hr
from pprint import pprint
import sometext

"""
Psych 138 Spring 2017
Assignment 6
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
    pattern = r'[A-Za-z0-9]{8,}'

    # use findall to get all matches of your pattern
    found = re.findall(pattern=pattern, string=text)

    if found:
        return found
    else:
        return []

        # whether or not there are other steps here, depends on exactly how you choose to write your pattern.

        # return your word list (or an empty list if you pattern matches no words in text)


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
    pattern = r'\(\w.\w., \w+ \&* \w+ \d{4}\)|\(\w+, \w+ \d{4}\)|\( *\w+,* *\w+,* *\w+,* *\w+,* *\w+,* *\&+,* *\w+, \d{4}\)'
    found = re.findall(pattern=pattern, string=text)
    if found:
        return found
    else:
        return []


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
    # *** SETUP TASK
    # --------------
    records = []
    Debrief_Record = collections.namedtuple("Debrief_Record", "id sex debrief")
    files_list = [file for file in os.listdir(data_folder) if file.endswith(".TXT")]
    for files in files_list:

        with open(os.path.join("data", files), "r") as infile:
            lines = infile.readlines()
            no_newlines = re.sub(pattern=r"\n", repl="", string="".join(lines))
            no_end_deb = re.sub(pattern=r"END DEBRIEF.*", repl="", string=no_newlines)
            deb_pattern = r"1\)\s*\w+.*"
            match_debrief = re.findall(deb_pattern, no_end_deb)

            no_num = re.sub(pattern=r"\d\)", repl="", string="".join(match_debrief))
            deb = re.sub(pattern=r"\s{2,}", repl=" ", string=no_num)
            deb = re.split(pattern="\n", string=deb)
            id_sex = r"(\d\d\d\d) ([fe]*male)"
            match_id_sex = re.findall(id_sex, "".join(lines))

            for ID, sex in match_id_sex:
                for words in deb:
                    full_debrief = Debrief_Record(ID, sex, words)
                    records.append(full_debrief)

    return records


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
    # we helped you plan out the previous function, for this one, you're on your own.

    pos_neg_words = []
    SENTIMENT_ANALYSIS = collections.namedtuple("SENTIMENT_ANALYSIS", "file positive negative ratio")
    file_list = [file for file in os.listdir(data_folder) if file.endswith(".txt")]
    for file in file_list:
        with open(os.path.join("scripts", file), "r") as infile:
            lines = infile.readlines()
            remove_newlines = re.sub(pattern=r"\n+", repl="", string="".join(lines))
            pos_patt = r" *({})"
            pos_seq = ""

            for words in pos_words:
                pos_seq += words + "|"
            pos_seq = pos_seq[:-1]
            pos_patt = pos_patt.format(pos_seq)
            match_pos = re.findall(pos_patt, remove_newlines, re.IGNORECASE)
            neg_patt = r" *({})"
            neg_seq = ""

            for words in neg_words:
                neg_seq += words + "|"
            neg_seq = neg_seq[:-1]
            neg_patt = neg_patt.format(neg_seq)
            match_neg = re.findall(neg_patt, remove_newlines, re.IGNORECASE)

            pos_count = collections.Counter(match_pos)
            neg_count = collections.Counter(match_neg)
            positive = sum(pos_count.vales())
            negative = sum(neg_count.vales())
            ratio = positive / negative
            sentiment = SENTIMENT_ANALYSIS(file, positive, negative, ratio)
            pos_neg_words.append(sentiment)

    return pos_neg_words


if __name__ == '__main__':
    print(how_pedantic())
    pprint(citations())
    pprint(debrief_records())
    pprint(sentiment_analysis())
