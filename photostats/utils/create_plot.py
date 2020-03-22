"""Create a plot and save to disk."""

import matplotlib.pyplot as plt  # type: ignore


def create_plot(group_names: list, group_data: list):
    plt.style.use('fivethirtyeight')
    fig, ax = plt.subplots()
    ax.bar(group_names, group_data)
    xlabels = ax.get_xticklabels()
    plt.setp(xlabels, rotation=45, horizontalalignment='right')
    plt.show()
