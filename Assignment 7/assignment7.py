# todo: PUT ALL OF YOUR IMPORTS HERE
from horizontalrule import hr
import os
import pandas
import requests
from bs4 import BeautifulSoup
from pprint import pprint
import urllib
import random
import collections

"""
Trina Tran
1432495
Assignment 7
"""


"""
PLEASE READ ALL PROBLEM PROMPTS CAREFULLY!

IF YOU HAVE QUESTIONS ABOUT WHAT A PROBLEM IS ASKING, PLEASE ASK UP!

AS IN PREVIOUS ASSIGNMENTS, DO NOT ALTER THE STRUCTURE OF THIS FILE OR DELETE PROBLEMS.
"""

"""
@@@@@@@@@
Problem 1
@@@@@@@@@
GOAL:
    - Write a function that
    - Grabs the html code from this webpage: http://psychology.ucsc.edu/about/people/grad-directory.php
    - Creates a folder called `gradpics`
    - Collects a list of all of the links to the grad student pictures you see on the page.
    - Note that they don't look like full URLS (they start like this: //wcms-prod...) so you'll have to add 'https:'
      to the front of each one.
    - DOWNLOAD all of the images to the `gradpics` folder using urllib.
    - RETURN the list of links (with 'https:' attached to the front of each).
    - Keep this logic in mind:
    -    First, find an example of the content you want to isolate (in this case, `.jpg` files)
    -    Now, notice what kind of tags they are in (it's not the same `a` tag from our class example) and
         use find_all to grab them in a list.
    -    Now, notice what kind of attribute holds the actual image link (it's not the same `href` attribute from
         our class example). Go through your list of tags and grab the links. 
    -    Don't know what I'm talking about? That's ok, just do one step at a time and see how it goes. First get the
         key tags using soup.find_all(). Then use tag.get() to pull out all of the picture links. I posted a 
         step by step version of the example we went over in class. If you are uncertain about how to do
         any of this, study the example for downloading .wav files. This exercise is nearly identical.
    - No error handling is required
"""


@hr
def grad_pics():
    url = 'http://psychology.ucsc.edu/about/people/grad-directory.php'
    web_object = requests.get(url)
    text = web_object.text
    text = text.encode('utf-8')
    soup = BeautifulSoup(text, 'html.parser')
    links = [tag.get('src') for tag in soup.find_all('img') if '.jpg' in tag.get('src')]
    links = ['http:' + link for link in links]
    pprint(links)

    os.makedirs(os.path.join('gradpics'), exist_ok=True)
    for url in random.sample(links, 30):
        outpath = os.path.join('gradpics', os.path.basename(url))
        urllib.request.urlretrieve(url, outpath)
    print(os.listdir('gradpics'))



"""
@@@@@@@@@
Problem 2
@@@@@@@@@
SETUP:
    - Write a function that
    - accepts two string keywords (keyword1 and keyword2)
    - initialize 2 lists that will each hold a bunch of namedtuples, one for each keyword. E.g., records1 and records2.
    - go ahead and define your namedtuple (details below)
    - FOR EACH KEYWORD, gets the text from this url:
      http://api.nsf.gov/services/v1/awards.xml?keyword=XXXXXXX
      except replace `XXXXXXX` with a lowercase version of the keyword, e.g.:
      http://api.nsf.gov/services/v1/awards.xml?keyword=sociology
    - Once you have the page text, use BeautifulSoup to get a list of awards.
      (The Twitter example from the Lec 16 slides can help)
    - For every award, make a namedtuple with the following properties:
      'keyword', 'funds', 'name', 'title',  
      and assign to them the values you get from the award in these fields:
      the current keyword, <fundsObligatedAmt>, <piFirstName> + ' ' + <piLastName>, <title>
      for example:
      Something like AWARD(keyword='xxxxxx', funds=xxxxxx, name='xxxxxx', title='xxxxxxx')
    - Add this namedtuple to one of the lists you initialized earlier (e.g., records1).
    - Now repeat this process for the other keyword and add those namedtuples to the other list (e.g., records2)
GOAL:
    - Now you need to use these lists of namedtuples to RETURN a dictionary with the following keys:
    - 'lowest_payout_amount'     <-- this is the dollar amount of the smallest awarded funds (FROM ANY KEYWORD)
    - 'highest_payout_amount'    <-- this is the dollar amount of the largest awarded funds (FROM ANY KEYWORD)
    - 'busiest_keyword'          <-- this is the keyword that has the most awards
    - 'richest_keyword'          <-- this is the keyword whose summed funds is the highest of the two keywords

    - No error handling is required
HINT:
    - Don't for get that BeautifulSoup searches (whether finda_all, get(), or find()) need lowercase search terms,
      even if it is actually uppercase or mixed case on the webpage source. Also remember that what these return may
      LOOK like a string, but require you use their contents property to actually get a string. Study the lecture slides
      carefully (or your notes from lecture) before starting this problem.
    - When calculating the various stats for the return dict, don't forget useful 
      list functions like max() min() len() and sum()
"""


@hr
def nsf_compare(keyword1, keyword2):

    def records(keyword):
        url = 'http://api.nsf.gov/services/v1/awards.xml?keyword={}'.format(keyword1, keyword2)
        r = requests.get(url)
        data = r.text
        data = data.encode('utf-8')
        soup = BeautifulSoup(data, "html.parser")

        records = []
        awards = [award for award in soup.find_all('award')]
        page_awards = [item for item in soup.find_all('award')]  # this is a list of the chunks(items) between <award>x2
        for item in page_awards:
            funds = item.find(name='fundsobligatedamt').contents[0]  # for item in page_awards]
            name = item.find(name='pifirstname').contents[0]
            last = item.find(name='pilastname').contents[0]
            title = item.find(name='title').contents[0]
            Psych_Award = collections.namedtuple('Psych_Award', 'keyword funds name title')
            records.append(Psych_Award(keyword=keyword1 or keyword2, funds=funds, name=name + ' ' + last, title=title))

        return records


    records1 = records(keyword1)
    records2 = records(keyword2)

    dict = {}

    min1 = min(int(item.funds) for item in records1)
    min2 = min(int(item.funds) for item in records2)
    max1 = max(int(item.funds) for item in records1)
    max2 = max(int(item.funds) for item in records2)
    highest = max(max1, max2)

    if len(records1) >= len(records2):
        busiest = keyword1
    else:
        busiest = keyword2

    sum1 = sum(int(item.funds) for item in records1)
    sum2 = sum(int(item.funds) for item in records2)

    if sum1 > sum2:
        richest = keyword1
    else:
        richest = keyword2

    dict['lowest_payout_amount'] = min(min1, min2)
    dict['highest_payout_amount'] = highest
    dict['busiest_keyword'] = busiest
    dict['richest_keyword'] = richest
    print("lowest_payout_amount: " + str(dict['lowest_payout_amount']))
    print("highest_payout_amount: " + str(dict['highest_payout_amount']))
    print("busiest_keyword: " + str(dict['busiest_keyword']))
    print("richest_keyword: " + str(dict['richest_keyword']))
    return dict



"""
@@@@@@@@@
Problem 3
@@@@@@@@@
SETUP:
    - Notice that you have a file called fake_task_data_combined.csv
    - Consider double clicking it in the Finder/Explorer, Excel will open it. It's nicely formatted here!
    - Now double click it from within PyCharm. You can see that it is just Comma Separated Text!
GOAL:
    - Write a function that accepts the following parameters: data_file (path to a data file to use in our analysis),
      and correct_only (if True, will only analyze data from correct trials) [default to True].
    
    - Use Pandas to load in the data file.
    - If correct_only is True, filter out any rows where `accuracy` is not 'Correct'
    - Drop the ratings column
    - PRINT the following:
    -   Descriptive Statistics for rt
    -   Descriptive Statistics for rt by color
    -   Descriptive Statistics for rt by color and shape
    -   Descriptive Statistics for rt
    -   Descriptive Statistics for rt by color
    -   Descriptive Statistics for rt by color and shape
    - Between each of these, print a message saying what it is (you can use one of the descriptions above)
    - ALTER the dataframe so that all rts are converted from milliseconds to seconds.
    - ALTER the dataframe so that all variable names are capitalized
    - Save only subject 100's data to a file called subject_100.csv
    - Save only subject 101's data to a file called subject_101.csv
"""

@hr
def analysis(data_file, correct_only=True):
    data = pandas.read_csv(data_file)
    data.to_csv('fake_task_data_combined.csv', index=False)

    data = data.query('accuracy != "Incorrect"')
    data = (data.drop(['rating'], axis=1))
    data3 = data.copy()
    data3['rt'] = [rt * 1000 for rt in data['rt']]
    print('___ Descriptive Statistics for RT___')
    print(data3['rt'].describe())

    colors = ["Blue","Red","Yellow","Green"]
    shapes = ["Circle", "Square"]

    print("\n___ Descriptive Statistics for RT by Color___")
    for color in colors:
        list = data3.query('color == "' + color + '"')
        print(list['rt'].describe())

    print("\n___ Descriptive Statistics for RT by Color and Shape___")
    for color in colors:
        for shape in shapes:
            list = data3.query('color == "' + color + '"').query('shape == "' + shape + '"')
            print(list['rt'].describe())


    data_100 = data3.query('subjectid == 100').copy()
    data_100.to_csv('subject_100.csv', index=False)

    data_101 = data3.query('subjectid == 101').copy()
    data_101.to_csv('subject_101.csv', index=False)





if __name__ == '__main__':

    try:
        grad_pics()
        grad_pic_list = os.listdir('gradpics')
        expected_pics = ['aditta.jpg', 'anguye38.jpg', 'aoveroye.jpg', 'aslarson.jpg', 'barander.jpg', 'cestarr.jpg',
                    'chelbrow.jpg', 'daryan.jpg', 'eacevesa.jpg', 'edlbrown.jpg', 'eetoolis.jpg', 'ehentsch.jpg',
                    'eljgoldm.jpg', 'gsolis2.jpg', 'ibvalle.jpg', 'jdarcey.jpg', 'jeaday.jpg', 'mrsingh.jpg',
                    'nnamiran.jpg', 'peakraus.jpg', 'psamermi.jpg', 'rlgross.jpg', 'rsteets.jpg', 'sadhughe.jpg',
                    'sharsey.jpg', 'slgreen.jpg', 'tlockett.jpg', 'twaltzer.jpg', 'vhollis.jpg', 'ychen159.jpg']
        print('Files Downloaded:')
        print(grad_pic_list)
        print('Expected:')
        print(expected_pics)
        print('Verdict:')
        print('They Match!!' if sorted(grad_pic_list) == sorted(expected_pics) else 'They DON\'T MATCH')
    except Exception as e:
        print(e)

    try:
        res1 = nsf_compare(keyword1='psychology', keyword2='sociology')
        expect1 = {'lowest_payout_amount': 0, 'richest_keyword': 'sociology',
                   'highest_payout_amount': 16447611, 'busiest_keyword': 'sociology'}
        print('Output')
        print(res1)
        print('Expected:')
        print(expect1)
        print('Verdict:')
        print('They Match!!' if set(res1.values()) == set(expect1.values()) else 'They DON\'T MATCH')
    except Exception as e:
        print(e)

    try:
        res2 = nsf_compare(keyword1='monkey', keyword2='bird')
        expect2 = {'richest_keyword': 'monkey', 'highest_payout_amount': 756181,
                   'lowest_payout_amount': 10080, 'busiest_keyword': 'bird'}
        print('Output')
        print(res2)
        print('Expected:')
        print(expect2)
        print('Verdict:')
        print('They Match!!' if set(res2.values()) == set(expect2.values()) else 'They DON\'T MATCH')
    except Exception as e:
        print(e)

    try:
        analysis('fake_task_data_combined.csv', True)

        # EXPECTED: A bunch of stuff in this format (this is just a bit of it):
                    #         subjectid          rt
                    # count   75.000000   75.000000
                    # mean   100.533333  582.453333
                    # std      0.502247  128.098916
                    # min    100.000000  301.000000
                    # 25%    100.000000  478.000000
                    # 50%    101.000000  571.000000
                    # 75%    101.000000  665.500000
                    # max    101.000000  870.000000
    except Exception as e:
        print(e)