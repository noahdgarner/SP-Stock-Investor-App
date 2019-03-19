from __future__ import print_function
import time
import intrinio_sdk
from intrinio_sdk.rest import ApiException
from pprint import pprint
import urllib.request
import json
import DataPointReceiver


companies = ['ABCB', 'ABMD', 'ABR']

company = 'NTNX'
tag = 'revenuegrowth', 'marketcap'
# tag = 'revenuegrowth' #this does


DataPointReceiver.make_request(companies, tag)

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