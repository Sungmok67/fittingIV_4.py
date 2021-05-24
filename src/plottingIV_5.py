import numpy as np
import pandas as pd
import xml.etree.ElementTree as et
import matplotlib.pyplot as plt
from numpy import exp,sqrt,pi


import glob2 as gl
import warnings
warnings.simplefilter('ignore',np.RankWarning)
from parsing_2 import Voltage1,Current1
from input_file import file_name

for i,j in Voltage1,Current1:
    plt.plot(i,j,'bo--', markersize=5)

    plt.title("IV-analysis", fontsize=15)
    plt.ylabel('Current[A]')
    plt.xlabel('Voltage[V]')

    plt.yscale('log')
    plt.show()


