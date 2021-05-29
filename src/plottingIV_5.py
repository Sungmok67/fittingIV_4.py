import numpy as np
import pandas as pd
import xml.etree.ElementTree as et
import matplotlib.pyplot as plt
from numpy import exp,sqrt,pi
import glob2 as gl
import warnings
warnings.simplefilter('ignore',np.RankWarning)
from parsing_2 import Voltage1,Current1,L1,IL1,L2,IL2,L3,IL3,L4,IL4,L5,IL5,L6,IL6,ref_L1,ref_IL1,WavelengthSweep,s
from input_file import file_name
from fittingL_3 import p4_list,p5_list,p6_list,rsquared4_list,rsquared5_list,rsquared6_list,p1_list_fit,p2_list_fit,p3_list_fit,p4_list_fit,p5_list_fit,p6_list_fit
#print(Current1)
#print(Current1[1],Current1[2],sep='\n')
#print(len(Voltage1))
for i in range(0,len(Voltage1)):
    plt.figure(figsize=(16,10))
    plt.subplot(2, 3, 4)
    plt.plot(Voltage1[i],Current1[i],'bo', markersize=5)

    plt.title("IV-analysis", fontsize=15)
    plt.ylabel('Current[A]')
    plt.xlabel('Voltage[V]')

    plt.yscale('log')


#-----------------------------------------------------------------------4번 i-v law data

    '''for j in WavelengthSweep:
        L = j.findtext('L').split(',')
        IL = j.findtext('IL').split(',')
        L1 = list(map(float, L))
        IL1 = list(map(float, IL))
        print(len(L1))
        plt.subplot(2, 2, 2)
        plt.plot(L1, IL1, 'o', label=str('DCBias=') + str(j.attrib['DCBias']), markersize=1)
    plt.title("Transmission spectra-as measured", fontsize=15)
    plt.ylabel('Measured transmission[dB]')
    plt.xlabel('Wavelength[nm]')
    plt.legend(loc="lower right")
    plt.show()'''
    plt.subplot(2,3,1)
    plt.plot(L1[i],IL1[i],'r',label = 'DCBias =' + str(s[0]))
    plt.plot(L2[i],IL2[i], 'b', label='DCBias =' + str(s[1]))
    plt.plot(L3[i],IL3[i], 'y', label='DCBias =' + str(s[2]))
    plt.plot(L4[i], IL4[i], 'g', label='DCBias =' + str(s[3]))
    plt.plot(L5[i], IL5[i], 'c', label='DCBias =' + str(s[4]))
    plt.plot(L6[i], IL6[i], 'm', label='DCBias =' + str(s[5]))
    plt.plot(ref_L1[i],ref_IL1[i], 'k', label= str(s[6]))
    plt.title("Transmission spectra-as measured", fontsize=15)
    plt.ylabel('Measured transmission[dB]')
    plt.xlabel('Wavelength[nm]')
    plt.legend(loc="best")


#-----------------------1번 6개짜리 l-il그래프
    plt.subplot(2,3,2)
    plt.scatter(ref_L1[i],ref_IL1[i],facecolor = 'none', edgecolor ='r', s = 10, alpha = 0.1, linewidth = 1, label=str('ref'))

    plt.plot(ref_L1[i],p4_list[i],'c',label = '4th' + "  R^2 =" +str(rsquared4_list[i]))
    plt.plot(ref_L1[i],p5_list[i],'m',label = '5th' + "  R^2 =" +str(rsquared5_list[i]))
    plt.plot(ref_L1[i],p6_list[i],'y',label = '6th' + "  R^2 =" +str(rsquared6_list[i]))
    plt.title("Transmission spectra-as processed", fontsize=15)
    plt.ylabel('Measured transmission[dB]')
    plt.xlabel('Wavelength[nm]')
    plt.legend(loc="best")

#------------------------------------4,5,6차 refrent 그래프 2번
    plt.subplot(2,3,3)
    sub_ref=[(x - y) for x, y in zip(ref_IL1[i], p6_list[i])]
    plt.plot(ref_L1[i],sub_ref , 'k', label=str(s[6]))
    sub1 = [(y - x) for x, y in zip(p1_list_fit[i], IL1[i])]
    sub2 = [(y - x) for x, y in zip(p2_list_fit[i], IL1[i])]
    sub3 = [(y - x) for x, y in zip(p3_list_fit[i], IL1[i])]
    sub4 = [(y - x) for x, y in zip(p4_list_fit[i], IL1[i])]
    sub5 = [(y - x) for x, y in zip(p5_list_fit[i], IL1[i])]
    sub6 = [(y - x) for x, y in zip(p6_list_fit[i], IL1[i])]

    plt.plot(L1[i],sub1, 'r', label='DCBias =' + str(s[0]))
    plt.plot(L2[i], sub2, 'b', label='DCBias =' + str(s[1]))
    plt.plot(L3[i], sub3, 'y', label='DCBias =' + str(s[2]))
    plt.plot(L4[i], sub4, 'g', label='DCBias =' + str(s[3]))
    plt.plot(L5[i], sub5, 'c', label='DCBias =' + str(s[4]))
    plt.plot(L6[i], sub6, 'm', label='DCBias =' + str(s[5]))

    plt.title("Transmission spectra-as filtered", fontsize=15)
    plt.ylabel('Measured transmission[dB]')
    plt.xlabel('Wavelength[nm]')
    plt.legend(loc="best")





    #plt.show()


#-----------------------------------------------------------------------------

    plt.savefig('./result_final/{}.png'.format(file_name[i][109:]))
    plt.clf()


