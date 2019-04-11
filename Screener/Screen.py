from Screener.screen_Builder import screen_Builder
import pandas as pd
import Screener.test_screen_results as tr
import urllib.request
import json
import time


class Screen:

    def __init__(self):
        self.screen_metrics = []
        self.results = []
        self.top_result = None
        self.objective = ""
        self.Reasoning = []
        self.url = None
        self.industry = ""
        self.risk_tolerance = None
        self.results = ""
        self.executed = False
        self.analyzed = False
        self.json_obj = None

    def get_url(self, objective, profile, industry):

        self.objective = objective
        self.industry = industry
        screen_url = screen_Builder(industry, objective)
        self.url = screen_url.screen_url

    def run_screen(self):
        debug = True
        if debug:
            self.result = tr.test

        else:
            time.sleep(5)
            print('running screen', self.url)
            contents = urllib.request.urlopen(self.url)
            decode = contents.read().decode('utf-8')
            #self.json_obj = json.loads(decode)
            self.result = json.loads(decode)['data']
            #self.results = pd.DataFrame(json_obj['data'])
            #print(type(self.results))
            # result_frame = pd.DataFrame(test_screen_results.test2)

        self.executed = True

    def to_dict(self):

        d = {'Analyzed':self.analyzed,'Objective ': self.objective, 'Industry': self.industry, 'URL ': self.url}

        return d

    def __str__(self):

        return "SCREEN REPORT: \nOBJECTIVE:"+ self.objective+ "\nINDUSTRY:"+ self.industry+ "\nURL:"+self.url+"\nRESULTS:"+str(self.result)
