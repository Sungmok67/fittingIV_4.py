import numpy as np
import pandas as pd
import xml.etree.ElementTree as et
import matplotlib.pyplot as plt
from numpy import exp,sqrt,pi
import lmfit
from lmfit import Model
import glob2 as gl
import warnings
warnings.simplefilter('ignore',np.RankWarning)
from parsing_2 import TestSiteInfo,Modulator,PortCombo,ModulatorSite,DesignParameter,Voltage,Current,L_list,IL_list
from fittingL_3 import p6
import fittingL_3
from fittingIV_4 import poly1dIV_list,best_f,results



def a(results):
        error_result={}
        if results>1:
                error_result['error'] = 'Ref.spec.Error'
                error_result['Flag'] =1
                return error_result
        else:
                error_result['error'] = 'No error'
                error_result['Flag'] = 0
                return error_result

data = {'Lot' : [TestSiteInfo['Batch']],
        'Wafer': [TestSiteInfo['Wafer']],
        'Mask': [TestSiteInfo['Maskset']],
        'TestSite':[TestSiteInfo['TestSite']],
        'Name':[Modulator[0].attrib['Name']],
        'Date':[PortCombo[0].attrib['DateStamp']],
        'Script ID':['process LMZ'],
        'Script Version':['0.1'],
        'Script Owner':['B2'],
        'Operator':[ModulatorSite[0].attrib['Operator']],
        'Row':[TestSiteInfo['DieRow']],
        'Column':[TestSiteInfo['DieColumn']],
        'ErrorFlag':[a(results)['Flag']],
        'Error description':[a(results)['error']],
        'Analysis Wavelength':[DesignParameter[1].text],
        'Rsq of Ref.spectrum (6th)':[fittingL_3.polyfit(L_list,IL_list ,6)['determination']],
        'Max trnasmission Ref.spec.(dB)':[max(p6(L_list))],
        'Rsq of IV':[results],
        'I at -1V':[poly1dIV_list[4]],
        'I at 1V':[best_f[12]]}


pd.set_option('display.max_rows',None)
pd.set_option('display.max_columns',None)

df = pd.DataFrame(data)
df.to_csv('./result_all.csv')