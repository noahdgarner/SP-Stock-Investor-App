import pandas as pd
from Screener import test_screen_results
from Screener.Screen import Screen
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


class Analyzer:

    def __init__(self, user_info):
        debug = True
        testing = True
        print("NEW ANALYZER INSTANCE: \n", user_info)
        self.profile_info = user_info['UserInfo']
        risky_screen = user_info['Risky']
        mod_screen = user_info['Moderate']
        def_screen = user_info['Defensive']
        self.screens = [risky_screen, mod_screen, def_screen]

        # Only runs screen that matches user's profile
        if not debug:
            for i in self.screens:
                if self.profile_info['risk_profile'] == i['Objective']:
                    self.screen_results = self.run_screen(i)

        else:
            print("Analyzer in Debug")
            self.screen_results = test_screen_results.defensive_test



    def run_screen(self, screen_info):
        url = screen_info['URL']
        contents = urllib.request.urlopen(url)
        decode = contents.read().decode('utf-8')
        json_obj = json.loads(decode)
        return json_obj

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
