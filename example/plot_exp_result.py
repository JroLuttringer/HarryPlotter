import matplotlib.pyplot as plt
from os import listdir
from os.path import isfile, join
import matplotlib
import matplotlib.style as style
import random
import sys
sys.path.insert(1, '../')

from logprocessor import *
from collections import defaultdict
from harryplotter import *



def main():
    l, fields_per_file = files2list(["diablo_k5_powertwo", "diablo_k10_powertwo"])

    means = means_per_indexes(l, fields_per_file, ["FILE", "NB_NODE"], "TIME")
    error = mustaches_per_indexes(l, fields_per_file, ["FILE", "NB_NODE"], "TIME")

    p = defaultdict(dict)
    p['k = 5']['x'] = [float(i) for i in means['diablo_k5_powertwo'].keys()]
    p['k = 5']['y'] = [float(i) for i in means['diablo_k5_powertwo'].values()]
    p['k = 5']['marker'] = "x"
    p["k = 5"]['label'] = "DIABLO (k = 5)"

    p['k = 10']['x'] = [float(i) for i in means['diablo_k10_powertwo'].keys()]
    p['k = 10']['y'] = [float(i) for i in means['diablo_k10_powertwo'].values()]
    p['k = 10']['marker'] = "o"
    p["k = 10"]['label'] = "DIABLO (k = 10)"

    g = defaultdict(dict)
    g["xlabel"] = "# of Nodes"
    g["ylabel"] = "Time (s)"
    g["title"] = "Time taken depending on the number of nodes / topologies\n"

    horizontal_line(10, "Sprint07 worst case")
    show_plot(p,g)






if __name__ == "__main__":
    main()
