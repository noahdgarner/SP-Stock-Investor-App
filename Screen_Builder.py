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
        self.api_key = "OmQ1ZDM5ZGUwYTI4YThiZTI3Mzc1OWZjMjQwZmE0MTM1"

    def build_between(lower, between_metrics):
        logic = ""
        for i in between_metrics.index:
            logic = logic+between_metrics["Intrinio Tag"].loc[i] +"~gte~" + \
                    str(between_metrics["lower bound"].loc[i]) + "," + between_metrics["Intrinio Tag"].loc[i] + \
                    "~lte~" + str(between_metrics["upper bound"].loc[i]) + ','

        logic = logic.rstrip(',')
        return logic

    def build_items_logic(self, metrics):
        logic = ""
        for i in metrics.index:
            logic = logic + metrics["Intrinio Tag"].loc[i] + metrics["Operation"].loc[i] + \
                    str(float(metrics["value"].loc[i])) + ","

        logic = logic.rstrip(',')

        return logic

    def build_view_logic(self, metrics):

        logic = ""
        for i in metrics.index:
            logic = logic + metrics["Intrinio Tag"].loc[i] + "~gt~-9999999,"

        logic = logic.rstrip(',')

        return logic

    def build_order_logic(self, metrics):
        # There is potential here to choose one item that makes the most sense. For now we just pass
        # in one metric which returns logic for it.

        logic = ""
        for i in metrics.index:
            logic = logic+"&order_column=" + metrics["Intrinio Tag"].loc[i] + "&order_direction=" \
                    + metrics["Operation"].loc[i]

        return logic

    #TODO Pass metrics for view only and for rankings

    def build_url(self, screen_metrics):

        base = "https://api.intrinio.com/securities/search?conditions="
        api_key = self.api_key
        api = "&api_key=" + api_key
        us_only = "&us_only=Yes"
        page_size = "&page_size=200"

        # Index of appropriate variables from data frame

        standard_view = (screen_metrics['Operation'] != "between") & (screen_metrics['Type'] == 'View')
        standard_search = (screen_metrics['Operation'] != "between") & (screen_metrics['Type'] == 'Search')
        order = screen_metrics['Type'] == "Order"
        between = (screen_metrics['Operation'] == "between") & (screen_metrics['Type'] == 'Search')

        # Gets text from each function for each part of the request URL. Input is the appropriately
        # sliced portion of the Dataframe

        between_logic = self.build_between(screen_metrics[between])
        standard_logic = self.build_items_logic(screen_metrics[standard_search])
        order_logic = self.build_order_logic(screen_metrics[order])
        view_logic = self.build_view_logic(screen_metrics[standard_view])

        if between_logic == "":
            screen_logic = standard_logic
        else:
            screen_logic = standard_logic + "," + between_logic

        if view_logic != "":
            screen_logic = screen_logic + "," + view_logic

        if order_logic != "":
            screen_logic = screen_logic + order_logic

        screen_request = base + screen_logic  + us_only + page_size + api
        return screen_request

    def build_screen(self):

        self.get_finance_metrics()
        self.get_other_metrics()
        self.get_sector_medians()
        self.value_builder()
        print(self.build_url(self.finance_metrics))
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

    def run_screen(self):
        print("run_screen")
        # contents = urllib.request.urlopen(self.screen_url)