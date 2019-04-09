import pandas as pd
import test_screen_results
import urllib.request
import json
import numpy as np


class ReportGenerator:

    def __init__(self, profile):
        self.profile = profile

        print("Creating new report on", self.profile.ticker, "based on...")
        for i in profile.reasons:
            print(i.measure, i.value, i.impact)

    # def sentence_builder(self):
    #     s


class Reasons:

    def __init__(self, measure, value, impact):
        self.measure = measure
        self.value = value
        self.impact = impact


class Profile:

    def __init__(self, ticker, reasons):
        self.ticker = ticker
        self.reasons = reasons

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
    ticker = company_selection['ticker']
    del company_selection['ticker']

    list_reasons = []

    # TODO differentiate between positive, negative, neutral
    for key, value in company_selection.items():
        reason = Reasons(key, value, "positive")
        list_reasons.append(reason)

    company_profile = Profile(ticker, list_reasons)

    report = ReportGenerator(company_profile)

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