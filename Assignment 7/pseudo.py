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
    # *** PART 1 - GET BIG LIST OF AWARDS AS NAMED TUPLES
    records1 = get_records(keyword1)
    records2 = get_records(keyword2)
    # pprint(records1)
    # pprint(records2)

    stats_dict = {}

    min1 = min(int(item.funds) for item in records1)
    min2 = min(int(item.funds) for item in records2)

    max1 = max(int(item.funds) for item in records1)
    max2 = max(int(item.funds) for item in records2)
    highest = max(max1, max2)

    # print(str(len(records1))+" --- " +str(len(records2)))
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

    stats_dict['lowest_payout_amount'] = min(min1, min2)
    stats_dict['highest_payout_amount'] = highest
    stats_dict['busiest_keyword'] = busiest
    stats_dict['richest_keyword'] = richest
    print("lowest: "+str(stats_dict['lowest_payout_amount']))
    print("richest: "+str(stats_dict['richest_keyword']))
    print("highest: "+str(stats_dict['highest_payout_amount']))
    print("busiest: "+str(stats_dict['busiest_keyword']))
    return stats_dict

def get_records(keyword):
    records = []
    psych_info = 'http://api.nsf.gov/services/v1/awards.xml?keyword={}'.format(keyword)  # or keyword2?
    page = requests.get(psych_info)
    page_text = page.text
    page_text = page_text.encode('utf-8')
    soup = BeautifulSoup(page_text, 'html.parser')
    page_awards = [item for item in soup.find_all('award')]  # this is a list of the chunks(items) between <award>x2
    for item in page_awards:
        pfunds = item.find(name='fundsobligatedamt').contents[0]  # for item in page_awards]
        pname = item.find(name='pifirstname').contents[0]
        plast = item.find(name='pilastname').contents[0]
        ptitle = item.find(name='title').contents[0]
        Psych_Award = collections.namedtuple('Psych_Award', 'keyword funds name title')
        records.append(Psych_Award(keyword=keyword, funds=pfunds, name=pname + ' ' + plast, title=ptitle))
    #pprint(records)
    return records


if __name__ == '__main__':

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
