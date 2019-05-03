import matplotlib.pyplot as plt
import os
import string, random


def build_graph(profile, df):

    #TODO Make graph more nice
    ticker = profile.ticker

    plt.style.use('seaborn-darkgrid')

    ax = plt.gca()
    df.plot(kind='line', x='date', y='adj_close', ax=ax)

    code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))

    stat_path = 'frontend/static/images/graphs/' + code +'.png'

    save_path = os.path.abspath(os.path.join(stat_path))

    print("Saving image in path", save_path)
    plt.savefig(save_path)

    return stat_path