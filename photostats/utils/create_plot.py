"""Create a plot and save to disk."""

import matplotlib.pyplot as plt  # type: ignore


def create_plot(group_names: list, group_data: list, x_label: str = "", y_label: str = "", title: str = ""):
    plt.style.use('fivethirtyeight')
    plt.rcParams.update({'figure.autolayout': True})
    fig, ax = plt.subplots()
    ax.bar(group_names, group_data)
    x_labels = ax.get_xticklabels()
    plt.setp(x_labels, rotation=45, horizontalalignment='right')
    ax.set(xlabel=x_label, ylabel=y_label, title=title)
    plt.show()
