'''킹재혁'''

import sys
sys.path.append('./src/')
import numpy as np
import pandas as pd
import xml.etree.ElementTree as et
import matplotlib.pyplot as plt
from numpy import exp,sqrt,pi
import glob2 as gl
import warnings
warnings.simplefilter('ignore',np.RankWarning)
from input import file_name
#반영은 1번밖에 안됨

Voltage1=[]
Current1=[]


L1=[]
IL1=[]
L2=[]
IL2=[]
L3=[]
IL3=[]
L4=[]
IL4=[]
L5=[]
IL5=[]
L6=[]
IL6=[]
ref_L1=[]
ref_IL1=[]
for i in file_name:
    tree=et.parse(i)
    root = tree.getroot()

    ModulatorSite =tree.findall('ElectroOpticalMeasurements/ModulatorSite')
    Modulator =tree.findall('ElectroOpticalMeasurements/ModulatorSite/Modulator')
    PortCombo =tree.findall('ElectroOpticalMeasurements/ModulatorSite/Modulator/PortCombo')
    TestSiteInfo_=root.find("TestSiteInfo")
    WavelengthSweep = tree.findall('ElectroOpticalMeasurements/ModulatorSite/Modulator/PortCombo/WavelengthSweep')
    DCBias = tree.findall('ElectroOpticalMeasurements/ModulatorSite/Modulator/PortCombo/WavelengthSweep')
    s = []

    for i in range(0, len(DCBias) - 1):
        s.append(float(DCBias[i].attrib['DCBias']))
    s.append('reference')

    L = tree.findall('ElectroOpticalMeasurements/ModulatorSite/Modulator/PortCombo/WavelengthSweep/L')
    IL = tree.findall('ElectroOpticalMeasurements/ModulatorSite/Modulator/PortCombo/WavelengthSweep/IL')

    Voltage = tree.find('ElectroOpticalMeasurements/ModulatorSite/Modulator/PortCombo/IVMeasurement/Voltage')
    Current = tree.find('ElectroOpticalMeasurements/ModulatorSite/Modulator/PortCombo/IVMeasurement/Current')


    Voltage= Voltage.text.split(',')
    Current = Current.text.split(',')

    Voltage = list(map(float,Voltage))
    Current_float = map(float,Current)
    Current=list(map(abs,Current_float))

    x_cut = Voltage[:10]
    y_cut= Current[:10]

    #print(x_cut)
    TestSiteInfo =TestSiteInfo_.attrib
    DesignParameter =tree.findall('ElectroOpticalMeasurements/ModulatorSite/Modulator/DeviceInfo/DesignParameters/DesignParameter')

    WavelengthSweep = root.iter('WavelengthSweep')
    #ref
    L_6 = L[6].text.split(',')
    IL_6 = IL[6].text.split(',')
    L_list = list(map(float,L_6))
    IL_list =list(map(float,IL_6))
    ref_L1.append(L_list)
    ref_IL1.append(IL_list)
    #print(L_6)
    Voltage1.append(Voltage)
    Current1.append(Current)
    #print(L[0].text.split(','))
#--------------------------------------------------------------------------------------------
    L_1 = L[0].text.split(',')
    IL_1 = IL[0].text.split(',')
    L_list1 = list(map(float, L_1))
    IL_list1 = list(map(float, IL_1))
    L1.append(L_list1)
    IL1.append(IL_list1)

    L_2 = L[1].text.split(',')
    IL_2 = IL[1].text.split(',')
    L_list2 = list(map(float, L_2))
    IL_list2 = list(map(float, IL_2))
    L2.append(L_list2)
    IL2.append(IL_list2)

    L_3 = L[2].text.split(',')
    IL_3 = IL[2].text.split(',')
    L_list3 = list(map(float, L_3))
    IL_list3 = list(map(float, IL_3))
    L3.append(L_list3)
    IL3.append(IL_list3)

    L_4 = L[3].text.split(',')
    IL_4 = IL[3].text.split(',')
    L_list4 = list(map(float, L_4))
    IL_list4 = list(map(float, IL_4))
    L4.append(L_list4)
    IL4.append(IL_list4)

    L_5 = L[4].text.split(',')
    IL_5 = IL[4].text.split(',')
    L_list5 = list(map(float, L_5))
    IL_list5 = list(map(float, IL_5))
    L5.append(L_list5)
    IL5.append(IL_list5)

    L_6= L[5].text.split(',')
    IL_6 = IL[5].text.split(',')
    L_list6 = list(map(float, L_6))
    IL_list6 = list(map(float, IL_6))
    L6.append(L_list6)
    IL6.append(IL_list6)
#print(file_name[1][101:120])

#print(ref_L1[0])




