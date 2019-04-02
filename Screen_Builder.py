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


class UrlBuilder():

    def __init__(self):
        self.api_key = "OmQ1ZDM5ZGUwYTI4YThiZTI3Mzc1OWZjMjQwZmE0MTM1"

    #TODO Indexing not working
    def build_between(lower, between_metrics):
        print("build between")
        print(type(between_metrics))
        print(between_metrics)
        logic = ""
        for i in between_metrics.index:
            logic = logic+between_metrics["Intrinio Tag"].loc[i] +"~gte~" + str(between_metrics["lower bound"].loc[i]) + "," + between_metrics["Intrinio Tag"].loc[i] + "~lte~" + str(between_metrics["upper bound"].loc[i]) + ','

        logic = logic.rstrip(',')

        print(logic)
        return logic

    def build_view_logic(items):

        term = ","

        for i in items:
            term += i + "~gte~-999999,"

        term = term.rstrip(',')

        return term

    #TODO Pass metrics for view only and for rankings

    def build_url(self, screen_metrics):

        standard = screen_metrics['Operation'] != "between"
        between = screen_metrics['Operation'] == "between"

        self.build_between(screen_metrics[between])


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
        self.get_sector_medians()
        self.value_builder()
        test = UrlBuilder()
        test.build_url(self.finance_metrics)
        #UrlBuilder.build_url(self.finance_metrics)

    def get_finance_metrics(self):

        self.finance_metrics = []
        basic = self.excel_sheet['Objective'] == "Standard"
        unique = self.excel_sheet['Objective'] == self.objective

        final_critera = basic | unique
        self.finance_metrics = self.excel_sheet[final_critera]

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


        # 3/22/2019 May not use this as originally intended

        if (self.objective == "Defensive"):

            self.finance_values.append(".3")
            self.finance_values.append("1")

        elif (self.objective == "Risky"):

            self.finance_values.append(".10")
            self.finance_values.append("1")

    def metric_value_builder(self):

        print("metric_value_builder")