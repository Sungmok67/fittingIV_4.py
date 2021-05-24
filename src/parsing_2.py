from importing_1 import D_LMZC
from input_file import file_name
import numpy as np
import pandas as pd
import xml.etree.ElementTree as et
import matplotlib.pyplot as plt
from numpy import exp,sqrt,pi
import glob2 as gl
import warnings
warnings.simplefilter('ignore',np.RankWarning)
from input_file import file_name
#반영은 1번밖에 안됨

Voltage1=[]
Current1=[]
for i in file_name:
    tree=et.parse(file_name)
    root = tree.getroot()

    ModulatorSite =tree.findall('ElectroOpticalMeasurements/ModulatorSite')
    Modulator =tree.findall('ElectroOpticalMeasurements/ModulatorSite/Modulator')
    PortCombo =tree.findall('ElectroOpticalMeasurements/ModulatorSite/Modulator/PortCombo')
    TestSiteInfo_=root.find("TestSiteInfo")
    WavelengthSweep = tree.findall('ElectroOpticalMeasurements/ModulatorSite/Modulator/PortCombo/WavelengthSweep')

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


    #ref
    L_6 = L[6].text.split(',')
    IL_6 = IL[6].text.split(',')
    L_list = list(map(float,L_6))
    IL_list =list(map(float,IL_6))

    #print(L_6)
    Voltage1.append(Voltage)
    Current1.append(Current)



