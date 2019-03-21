import pandas as pd
import test_screen_results
import numpy as np


#TODO analyze financials and valuation

frame = pd.DataFrame(test_screen_results.test2)

# gets the median company returned from screen
row = int(len(frame.index) / 2)

item = 'debttoequity'

the_dict = frame.iloc[row].to_dict()
print(the_dict)
print(the_dict[item])

def analyze_financials():

    print("analyzing financials")

    # some testing values
    frame = pd.DataFrame(test_screen_results.test2)

    #gets the median company returned from screen
    row = int(len(frame.index) / 2)

    item = 'debttoequity'

    the_dict = frame.iloc[row].to_dict()

    print(the_dict[item])


