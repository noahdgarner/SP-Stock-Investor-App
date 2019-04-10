class UserRisk:
    def __init__(self):
        self.riskScore = None
        self.acceptableLosses = None

    def calc_acceptableLosses(self):
        lower_bound_1 = 0
        upper_bound_1 = 0
