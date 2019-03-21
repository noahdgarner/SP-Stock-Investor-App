output = [{'data':[
           {'number_value': '1639964160.0',
           'tag': 'marketcap',
           'text_value': None},


          {'number_value': '0.266667',
           'tag': 'revenuegrowth',
           'text_value': None}
        ],
'security':{'code': None,
              'company_id': 'com_yd9dog',
              'composite_figi': None,
              'composite_ticker': 'ABCB:US',
              'currency': None,
              'figi': 'BBG000CDYGZ6',
              'id': 'sec_NXnVXV',
              'name': 'Ameris Bancorp',
              'share_class_figi': None,
              'ticker': 'ABCB'}}]

# print(output)
#
# print(output[0]['security']['ticker'])

items = ['debttoequity', 'beta', 'pricetoearnings']

term = ""

for i in items:
    term += i+"~gte~-999999,"

term = term.rstrip(',')
term = term+"&"

print(term)