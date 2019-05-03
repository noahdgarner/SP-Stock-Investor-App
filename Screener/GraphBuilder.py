import matplotlib.pyplot as plt
import os


def build_graph(profile, df):


    #TODO Make graph more nice
    ticker = profile.ticker

    plt.style.use('seaborn-darkgrid')

    ax = plt.gca()
    df.plot(kind='line', x='date', y='adj_close', ax=ax)

    path = os.path.abspath(os.path.join('frontend/static/images/graphs/graph.png'))

    print("Saving image in path", path)
    plt.savefig(path)

    return path