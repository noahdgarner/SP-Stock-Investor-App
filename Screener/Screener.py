from __future__ import print_function
import time
import intrinio_sdk
from intrinio_sdk.rest import ApiException
from pprint import pprint
import EquityScreen

api_key = 'OmRhNGVlMTlhZGQ5ZWVmOTdiZTAwOWY3NjNjZGI1OTNi'

company_api = intrinio_sdk.CompanyApi()
security_api = intrinio_sdk.SecurityApi()

logic = EquityScreen.risky
order_column = 'order_column_example'
order_direction = 'asc'
primary_only = False
page_size = 100


#TODO Fix for US exchanges only

output = security_api.screen_securities(logic=logic)


company_screen_results = []

for i in range(0, 10):
    company_screen_results.append(output[i].security.ticker)

print(company_screen_results)

#pprint(security_api.screen_securities(logic=logic))