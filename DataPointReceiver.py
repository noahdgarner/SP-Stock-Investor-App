import intrinio_sdk
from intrinio_sdk.rest import ApiException
from pprint import pprint
import urllib.request
import json

api_key = "OmQ1ZDM5ZGUwYTI4YThiZTI3Mzc1OWZjMjQwZmE0MTM1"

companies = ['ABCB', 'ABMD', 'ABR']

print("--")
company_str = ','.join(companies)

print(company_str)

def make_request(company_list, tag_list):

    companies_str = ','.join(company_list)
    tags_str = ','.join(tag_list)

    request_str = "https://api.intrinio.com/data_point?identifier="+companies_str+"&item="+tags_str+"&api_key="+api_key

    print(request_str)
    # contents = urllib.request.urlopen(
    #     "https://api.intrinio.com/data_point?identifier=TSLA,NTNX&item=marketcap,ceo&api_key=OmQ1ZDM5ZGUwYTI4YThiZTI3Mzc1OWZjMjQwZmE0MTM1")

