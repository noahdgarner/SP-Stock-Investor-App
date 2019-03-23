from __future__ import print_function
import time
import intrinio_sdk
from intrinio_sdk.rest import ApiException
from pprint import pprint
import urllib.request
import json
import UrlBuilder as dpr
import test_screen_results
import pandas as pd
import test_screen_results


companies = ['ABCB', 'ABMD', 'AAPL']

company = 'AAPL'
tag = 'revenuegrowth', 'marketcap', 'trailing_dividend_yield'
# tag = 'revenuegrowth' #this does

# for i in range(0, len(test_screen_results.test)):
#     print(test_screen_results.test[i])


dpr.make_screen_request()


#l = dpr.make_screen_request()

#frame = pd.DataFrame(l)

# frame = pd.DataFrame(test_screen_results.test2)
#
# print(frame)

#dpr.make_screen_request(dpr.build_between(.5, 1.1, "beta"))
# dpr.make_data_request(companies, tag)
# DataPointReceiver.make_data_request(companies, tag)
#dpr.make_screen_request()

# contents = urllib.request.urlopen("https://api.intrinio.com/data_point?identifier=TSLA,NTNX&item=marketcap,ceo&api_key=OmQ1ZDM5ZGUwYTI4YThiZTI3Mzc1OWZjMjQwZmE0MTM1")
# # pprint(type(contents))
# # pprint(type(pprint(contents.read().decode('utf-8'))))
# # pprint(contents.read().decode('utf-8'))
#
# decode = contents.read().decode('utf-8')
# json_obj = json.loads(decode)
# print(json_obj)
# print(json_obj['result_count'])
# print(json_obj['data'][0]['value'])

# pprint(dir(contents))
# print(contents.read().decode('utf-8'))
# test = literal_eval(contents.read().decode('utf-8'))
# print(type(test))
# print(test['value'])
# try:
#     api_response = company_api.get_company_data_point_text(company, tag)
#     pprint(api_response)
# except ApiException as e:
#     print("Exception when calling CompanyApi->get_company_data_point_text: %s\n" % e)