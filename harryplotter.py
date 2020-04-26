import matplotlib.pyplot as plt
from os import listdir
from os.path import isfile, join
import matplotlib
import matplotlib.style as style
import random
import sys
import numpy as np

def draw_plot(curve, data, graph_data):
    print("plot")
    x = list(data.get('x'))
    y = list(data.get('y'))
    label = data.get('label', str(curve))
    marker = data.get('marker')
    linewidth = data.get('linewidth', 1)
    err = data.get('yerr')
    err_diff = [[], []]
    if err != None:
        for xkey, diff_err in err.items():
            err_diff[0].append(abs(diff_err[0] - y[x.index(int(xkey))]))
            err_diff[1].append(abs(diff_err[1] - y[x.index(int(xkey))]))
    if err != None:
        plt.errorbar(x,y,yerr=err_diff, label=label, linewidth=linewidth)
    else:
        plt.plot(x,y, label=label,marker=marker,linewidth=linewidth)

    plt.title(graph_data.get("title", ""))
    leg = plt.legend(loc="best", ncol = 1, fancybox = True)
    leg.get_frame().set_alpha(0.5)
    plt.ylabel(graph_data.get("ylabel", ""))
    plt.xlabel(graph_data.get("xlabel", ""))
    plt.yscale(graph_data.get("xscale", "linear"))
    plt.xscale(graph_data.get("yscale", "linear"))

def draw_hist(curve, data, graph_data, start):
    print("hist")
    xtick = list(data.get('x'))
    y = list(data.get('y'))
    pos = np.arange(start, start + len(y))
    #label = data.get('label', str(curve))
    barlist = plt.bar(pos,y)
    for bar in barlist:
        bar.set_color((random.random(), random.random(), random.random()))
    plt.title(graph_data.get("title", ""))
    #leg = plt.legend(loc="best", ncol = 1, fancybox = True)
    #leg.get_frame().set_alpha(0.5)
    plt.ylabel(graph_data.get("ylabel", ""))
    plt.xlabel(graph_data.get("xlabel", ""))
    plt.yscale(graph_data.get("xscale", "linear"))
    plt.xscale(graph_data.get("yscale", "linear"))
    #plt.xticks(pos, xtick)
    return len(y) + 2

def horizontal_line(height, label):
    x = [10, 1000]
    y = [height,height]
    plt.plot(x,y, '--',label=label, linewidth=2)
    plt.legend(loc="best", ncol = 1, fancybox = True)




def show_plot(curves_data, graph_data):
    style.use('fivethirtyeight')
    start = 0
    nb_curve = 0
    all_ticks = []
    pos = []
    curr = 0
    for curve, data in curves_data.items():
        if data.get("type") != "hist":
            draw_plot(curve, data, graph_data)
        else:
            start += draw_hist(curve, data, graph_data, start)
            nb_curve += len(data['x'])
            for x in list(data['x']):
                all_ticks.append(x)
                pos.append(curr)
                curr += 1


            curr += 2

    if data.get("type") == "hist":
        # print(all_tickes)
        plt.xticks(pos, all_ticks, fontsize=8)
    plt.gcf().axes[0].yaxis.get_major_formatter().set_scientific(False)
    plt.show()
