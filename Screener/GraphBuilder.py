from Screener import Analyzer

import matplotlib.pyplot as plt
import numpy as np

import pandas as pd
from datetime import datetime

def build_graph(profile, df):


    #TODO Make graph more nice
    ticker = profile.ticker

    plt.style.use('seaborn-darkgrid')

    ax = plt.gca()
    df.plot(kind='line', x='date', y='adj_close', ax=ax)



    path = 'images/graph.png'

    plt.savefig(path)

    return path