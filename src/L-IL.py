import numpy as np
import pandas as pd
import xml.etree.ElementTree as et
import matplotlib.pyplot as plt
from numpy import exp,sqrt,pi
import glob2 as gl
import warnings
warnings.simplefilter('ignore',np.RankWarning)
from parsing_2 import Voltage1,Current1,WavelengthSweep
from input_file import file_name
from parsing_2 import L1,IL1



for i in file_name:
    tree = et.parse(i)
    root = tree.getroot()

    for j in range(0,6):
        #L = j.findtext('L').split(',')
        #IL = j.findtext('IL').split(',')

        L1 = list(map(float,L[i].text.split(',')))
        IL1 = list(map(float,IL[i].text.split(',')))

        #plt.subplot(2, 2, 2)
        plt.plot(L1, IL1, 'o', label=str('DCBias=') + str(j.attrib['DCBias']), markersize=1)
        plt.title("Transmission spectra-as measured", fontsize=15)
        plt.ylabel('Measured transmission[dB]')
        plt.xlabel('Wavelength[nm]')
        plt.legend(loc="lower right")
    plt.show()
