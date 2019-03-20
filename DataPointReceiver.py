import intrinio_sdk
from intrinio_sdk.rest import ApiException
from pprint import pprint
import urllib.request
import json
import EquityScreen

api_key = "OmQ1ZDM5ZGUwYTI4YThiZTI3Mzc1OWZjMjQwZmE0MTM1"

companies = ['ABCB', 'ABMD', 'ABR']

print("--")
company_str = ','.join(companies)

print(company_str)


def build_between(lower, upper, term):

    if lower > upper:
        lower, upper = upper, lower

    logic = term+"~gte~"+str(lower)+","+term+"~lte~"+str(upper)
    print(logic)
    return logic


def get_logic():

    defensive = ','.join(EquityScreen.defensive_basic)
    return defensive


def run_screen(request):

    contents = urllib.request.urlopen(request)

    decode = contents.read().decode('utf-8')
    json_obj = json.loads(decode)


    # returns a list of dictionaries
    return json_obj['data']


def make_screen_request():

    logic = get_logic()

    screen_request = "https://api.intrinio.com/securities/search?conditions="+logic+"&api_key="+api_key

    #print(screen_request)
    print("requesting screen ", screen_request)

    return run_screen(screen_request)

def make_data_request(company_list, tag_list):

    companies_str = ','.join(company_list)
    tags_str = ','.join(tag_list)

    request_str = "https://api.intrinio.com/data_point?identifier="+companies_str+"&item="+tags_str+"&api_key="+api_key

    print(request_str)
    # contents = urllib.request.urlopen(
    #     "https://api.intrinio.com/data_point?identifier=TSLA,NTNX&item=marketcap,ceo&api_key=OmQ1ZDM5ZGUwYTI4YThiZTI3Mzc1OWZjMjQwZmE0MTM1")

