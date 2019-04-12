from Screener import Analyzer

import matplotlib.pyplot as plt
import numpy as np

import pandas as pd
from datetime import datetime

def build_graph(profile, df):

    ticker = profile.ticker
    print(ticker)
    print(df['date'])
    df.sort_values(by=['date'], ascending=False)
    print(df['date'])

    #
    # plt.style.use('seaborn-darkgrid')
    #
    # ax = plt.gca()
    # df.plot(kind='line', x='date', y='adj_close', ax=ax)
    #
    # plt.show()



    # plotly.tools.set_credentials_file(username='j_hill14', api_key='aUbpiyjDYEpXSFBuFKae')
    # graph_title = "1-Year Price Change for " + ticker
    #
    # data = [go.Scatter(x=df.date, y=df['adj_close'])]
    # py.iplot(data, filename=graph_title)

    # plotly.offline.plot({"data": [go.Scatter(x=df.date, y=df['adj_close'])],
    #                      "layout": go.Layout(title=graph_title)},
    #                     image='png', image_filename='graph_test')



#build_graph("test" , "test")