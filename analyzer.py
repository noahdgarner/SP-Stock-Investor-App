import pandas as pd
import test_screen_results
import urllib.request
import json
import numpy as np


class Reasons:

    def __init__(self, measure, value, impact):
        self.measure = measure
        self.value = value
        self.impact = impact


def analyze_financials():

    print("analyzing financials")

    # some testing values
    frame = pd.DataFrame(test_screen_results.test2)

    #gets the median company returned from screen
    row = int(len(frame.index) / 2)

    item = 'debttoequity'

    the_dict = frame.iloc[row].to_dict()

    print(the_dict[item])

def defensive_analyzer(items):

    # TODO
    # sort by each criteria, get median company from each and build scoring system of those 3-10 companies

    items.sort_values(by=['debttoequity'], ascending=True)
    row = int(len(items.index) / 2)

    company_selection = items.iloc[row].to_dict()
    print(company_selection)

    list_reasons = []
    for key, value in company_selection.items():
        reason = Reasons(key, value, "positive")
        list_reasons.append(reason)

def risky_analyzer(items):

    print("risk analyzer")

def exeucute_url(url):
    print("REAL URL: " + url + "  Getting dict fro test_screen_results")

    # contents = urllib.request.urlopen(url)
    # decode = contents.read().decode('utf-8')
    # json_obj = json.loads(decode)
    # result_frame = pd.DataFrame(json_obj['data'])

    result_frame = pd.DataFrame(test_screen_results.test2)

    defensive_analyzer(result_frame)