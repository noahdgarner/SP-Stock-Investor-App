from screen_Builder import screen_Builder
import pandas as pd
import test_screen_results
import urllib.request
import json
import time

class Screen:

    def __init__(self):
        self.screen_metrics = []
        self.results = []
        self.top_result = None
        self.objective = None
        self.Reasoning = []
        self.url = None
        self.industry = None
        self.risk_tolerance = None
        self.results = None
        self.executed = False
        self.json_obj = None

    def get_url(self, objective, profile, industry):

        screen_url = screen_Builder(industry, objective)
        self.url = screen_url.screen_url

    def run_screen(self):
        time.sleep(5)
        print('running screen', self.url)
        contents = urllib.request.urlopen(self.url)
        decode = contents.read().decode('utf-8')
        self.json_obj = json.loads(decode)
        #self.results = pd.DataFrame(json_obj['data'])
        #print(type(self.results))
        # result_frame = pd.DataFrame(test_screen_results.test2)

