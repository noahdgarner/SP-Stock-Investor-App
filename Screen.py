class Screen():

    def __init__(self):
        self.screen_metrics = []
        self.results = []
        self.top_result = None
        self.objective = None
        self.Reasoning = []

        self.industry = None
        self.risk_tolerance = None


    def get_metrics(self):

        return self.screen_metrics