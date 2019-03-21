from UserRisk import UserRisk


class User:

    def __init__(self):
        self.risk = UserRisk.riskScore
        self.age = None
        self.income = None
        self.financialGoals = None
        self.incomeNeeds = None
