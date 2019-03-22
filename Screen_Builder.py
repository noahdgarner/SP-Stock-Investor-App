import pandas as pd
import xlrd


defensive_basic = [
    "marketcap",
    "trailing_dividend_yield",
    "debttoequity"
]

risky_basic = [
    "revenuegrowth"
]


class screen_builder():

    def __init__(self, industry_input, sector_input, objective):
        self.finance_metrics = []
        self.finance_values = []
        self.other_metrics = []
        self.objective = objective
        self.sector_medians = []
        self.industry = industry_input
        self.sector = sector_input
        self.excel_sheet = pd.read_excel("Financial Values.xlsx", sheet_name="Sheet1")

    def build_screen(self):

        self.get_finance_metrics()
        self.get_other_metrics()
        self.value_builder()

    def get_finance_metrics(self):

        self.finance_metrics = []

        if(self.objective == "Defensive"):
            self.finance_metrics = defensive_basic

        elif(self.objective == "Risky"):
            self.finance_metrics = risky_basic

    def get_other_metrics(self):

        # will build list of qualitative screen criteria

        print("get_other_metrics in Screen_Builder.py ")

    def get_sector_medians(self):

        # will pull sector median for self.financial_metrics. Possibly might not be used.

        print("get_sector_medians in Screen_Builder.py")

    def value_builder(self):

        print("value builder")
        #TODO
        # In the future, this function will dynamically allocation numerical values
        # to the financial ratios and metrics chosen in get_finance_metrics()
        # for now, they are assigned statically in get_finance_metrics()

        print(self.excel_sheet)

        if (self.objective == "Defensive"):

            self.finance_values.append(".3")
            self.finance_values.append("1")

        elif (self.objective == "Risky"):

            self.finance_values.append(".10")
            self.finance_values.append("1")



    def metric_value_builder(self):

        print("metric_value_builder")