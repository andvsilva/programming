import matplotlib.pyplot as plt
import matplotlib as matplot
import seaborn as sns
import pandas as pd
import numpy as np

def plot_hist(data):
    fig, (ax1, ax2) = plt.subplots(nrows=2, sharex=True)
    medianprops = dict(linestyle='-', linewidth=2, color='yellow')
    sns.boxplot(x=data, color='lightcoral', saturation=1, medianprops=medianprops,
            flierprops={'markerfacecolor': 'mediumseagreen'}, whis=1.5, ax=ax1)

    mean = data.mean()
    std = data.std()
    q1, median, q3 = np.percentile(data, [25, 50, 75])
    iqr = q3 - q1

    ticks = [mean + std * i for i in range(-4, 5)]
    ticklabels = [f'${i}\\sigma$' for i in range(-4, 5)]
    ax1.set_xticks(ticks)
    ax1.set_xticklabels(ticklabels)
    ax1.set_yticks([])
    ax1.tick_params(labelbottom=True)
    ax1.set_ylim(-1, 1.5)
    ax1.errorbar([q1, q3], [1, 1], yerr=[0, 0.2], color='black', lw=1)
    ax1.text(q1, 0.6, 'Q1', ha='center', va='center', color='black')
    ax1.text(q3, 0.6, 'Q3', ha='center', va='center', color='black')
    ax1.text(median, -0.6, 'median', ha='center', va='center', color='black')
    ax1.text(median, 1.2, 'IQR', ha='center', va='center', color='black')
    ax1.text(q1 - 1.5*iqr, 0.4, 'Q1 - 1.5*IQR', ha='center', va='center', color='black')
    ax1.text(q3 + 1.5*iqr, 0.4, 'Q3 + 1.5*IQR', ha='center', va='center', color='black')
    # ax1.vlines([q1 - 1.5*iqr, q1, q3, q3 + 1.5*iqr], 0, -2, color='darkgrey', ls=':', clip_on=False, zorder=0)

    sns.kdeplot(data, ax=ax2)
    kdeline = ax2.lines[0]
    xs = kdeline.get_xdata()
    ys = kdeline.get_ydata()

    ylims = ax2.get_ylim()
    ax2.fill_between(xs, 0, ys, color='mediumseagreen')
    ax2.fill_between(xs, 0, ys, where=(xs >= q1 - 1.5*iqr) & (xs <= q3 + 1.5*iqr), color='skyblue')
    ax2.fill_between(xs, 0, ys, where=(xs >= q1) & (xs <= q3), color='lightcoral')
    # ax2.vlines([q1 - 1.5*iqr, q1, q3, q3 + 1.5*iqr], 0, 100, color='darkgrey', ls=':', zorder=0)
    ax2.set_ylim(0, ylims[1])
    plt.show()