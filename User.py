from UserRisk import UserRisk
from Screen import Screen
import pandas as pd

class User:

    def __init__(self):
        # self.risk = UserRisk.riskScore
        self.risk_profile = None
        self.risk_score = None
        self.investing_knowledge = None
        self.age = None
        self.income = None
        self.financialGoals = None
        self.incomeNeeds = None
        self.industry_preference = None # []
        self.screens = {"Risky": None, "Moderate": None, "Defensive": None}

    # User.User("Defensive", "low", "high", "REITs")

    def setup_profile(self, risk_profile, investing_knowledge, interests):

        self.risk_profile = risk_profile
        self.investing_knowledge = investing_knowledge
        self.industry_preference = interests


    def generate_screen_url(self):

        for key, value in self.screens.items():
            if value == None:
                new_screen = Screen()
                new_screen.get_url(key, self.risk_profile, self.industry_preference)
                self.screens[key] = new_screen

    def run_all_empty_screen(self):
        print("run all empty screen")
        for key, screen in self.screens.items():
            if screen.executed == False:
                print(screen)
                screen.run_screen()

    def get_all_screen_results(self):
        for key, screen in self.screens.items():
            print(screen)
            print(screen.json_obj)
