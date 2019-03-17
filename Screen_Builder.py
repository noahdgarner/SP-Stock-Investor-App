class screen_builder():

    def __init__(self, industry_input, sector_input):
        self.finance_metrics = []
        self.finance_values = []
        self.other_metrics = []
        self.objective = None
        self.sector_medians = []
        self.industry = industry_input
        self.sector = sector_input


    def get_sector_medians(self):

        print("get sector medians")

    def get_finance_metrics(self):

        self.finance_metrics = []

        if(self.objective == "Defensive"):
            self.finance_metrics.append("trailing_dividend_yield")
            self.finance_metrics.append("five_yr_weekly_beta")

        elif(self.objective == "Risky"):
            self.finance_metrics.append("revenue_growth")
            self.finance_metrics.append("five_yr_weekly_beta")

    def value_builder(self):

        print("value builder")
        #TODO
        # In the future, this function will dynamically allocation numerical values
        # to the financial ratios and metrics chosen in get_finance_metrics()
        # for now, they are assigned statically in get_finance_metrics()

        if (self.objective == "Defensive"):
            self.finance_values.append(".3")
            self.finance_values.append("1")
        elif (self.objective == "Risky"):
            self.finance_values.append(".10")
            self.finance_values.append("1")


    def metric_value_builder(self):

        print("metric_value_builder")
