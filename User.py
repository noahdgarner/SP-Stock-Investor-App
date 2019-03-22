from UserRisk import UserRisk
import Screen_Builder

class User:

    def __init__(self):
        # self.risk = UserRisk.riskScore
        self.risk_profile = None
        self.age = None
        self.income = None
        self.financialGoals = None
        self.incomeNeeds = None
        self.industry_preference = None # []
        self.screens = {"Risky": None, "Moderate": None, "Defensive": None}

    # User.User("Defensive", "low", "high", "REITs")

    def setup_profile(self, risk_profile, investing_knowledge, interests):

        self.risk_score = risk_profile
        self.investing_knowledge = investing_knowledge
        self.interests = interests


    def build_screens(self):

        if(self.screens["Defensive"] == None):
            Screen_Builder.build_screen()
            print("building Defensive screen in User.build_screen()")
