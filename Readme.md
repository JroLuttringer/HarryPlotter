# Title
HarryPlotter is a simple plotting wizard that acts as a wrapper to python's matplotlib.

It processes log files written in the following format: 

X	Y 	Z	T
VALUE1 VALUE2 VALUE3 VALUE4 

and allows to plot them easily. 


# Install
## Dependencies
HarryPlotter used numpy, scipy and matplotlib with python3. Thus, you will need to install the following packages using pip before using HarryPlotter.
## Commands
 	
~~~~
apt update
apt install python3-pip
pip3 install scipy
pip3 install numpy 
pip3 install matplotlib
git clone https://github.com/JroLuttringer/HarryPlotter.git
~~~~
 	

# Examples
An example is available in the example directory. I will explain the example here. In this setup, I have several files contains the results to various experiments that I want to compare. The first thing to do is to convert all the lines within this files into a list

~~~~
from logprocessor import *
from collections import defaultdict
from harryplotter import *

l, fields_per_file = files2list(["diablo_k5_powertwo", "diablo_k10_powertwo"])
~~~~

Here, l contains the lines, and fields_per_file contains the name of each fields (described in the 
header of the files). Each field can have a different number of columns and different fields name. The arguments of the functions are the files I want to process. 



Here, I want for each file the mean time depending on the number of nodes. 

~~~~
 means = means_per_indexes(l, fields_per_file, ["FILE", "NB_NODE"], "TIME")
~~~~

This functions takes as arguments the lines as returned by files2list, the indexes that I'm interesting in, and the value I want to extract.

This will return, indexed on the file and number of nodes, the mean time taken (e.g; mean[diablo_k10_powertwo][22] = 10 means that in the experiments diablo_k10_powertwo, it tooks 10 seconds in average when the number of nodes was 22. 

If one does not want to mean, but rather the sum of every experiment, this can be done via 
~~~~
 sums = sums_per_indexes(l, fields_per_file, ["FILE", "NB_NODE"], "TIME")
~~~~

Here, I also want the error bars, as I have done several experiments for each parameters. This can be done through
~~~~
 error = mustaches_per_indexes(l, fields_per_file, ["FILE", "NB_NODE"], "TIME")
~~~~


Now that the logs have been processed, I can plot them. HarryPlotter uses a dictionnary to gather the parameters of the graph. Here, I want to plot two things: the experiment for k=5, and the one for k = 10. 

~~~
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
~~~


This is described as such. I create a dictionnary, with an entry for each curve (k=5 and k=10). The x values are the key of the dictionnary computed by mean_per_indexes, and the y valeus the associated values. I personnalize the marker and the label. In another dictionnary, I put the graph title, xlabel and y label.

I draw an horizontal line at y=10 with a specific label as a reference, and draw the plot.









