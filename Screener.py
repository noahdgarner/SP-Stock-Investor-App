from __future__ import print_function
import time
import intrinio_sdk
from intrinio_sdk.rest import ApiException
from pprint import pprint
import EquityScreen


intrinio_sdk.ApiClient().configuration.api_key['api_key'] = 'OmRhNGVlMTlhZGQ5ZWVmOTdiZTAwOWY3NjNjZGI1OTNi'

company_api = intrinio_sdk.CompanyApi()
security_api = intrinio_sdk.SecurityApi()

logic = EquityScreen.risky
order_column = 'order_column_example'
order_direction = 'asc'
primary_only = False
page_size = 100

pprint(security_api.screen_securities(logic=logic))
