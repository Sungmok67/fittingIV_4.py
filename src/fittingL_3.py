#from importing_1 import D07 ,D08_0526,D08_0528,D08_0712,D23_0528,D23_0531,D23_0603,D24_0528,D24_0528_1,D24_0531,D24_0603
#from input_file import file_name
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
from parsing_2 import L_list, IL_list 

#ref 4,5,6차 fitting
def polyfit(x,y,degree):
    results = {}
    coeffs = np.polyfit(x,y,degree)
    results['polynomial'] = coeffs.tolist()
    # r-squared
    p = np.poly1d(coeffs)
    yhat = p(x)
    ybar = np.sum(y) / len(y)  # 평균값
    ssreg = np.sum((yhat - ybar) ** 2)  # 실제값과 예측값차이
    sstot = np.sum((y - ybar) ** 2)  # 실제값과 평균값 차이
    results['determination'] = ssreg / sstot
    return results
#4차
f4 = polyfit(L_list,IL_list,4)['polynomial']
p4 = np.poly1d(f4)
rsqaured4 = polyfit(L_list,IL_list,4)['determination']
#5차
f5 = polyfit(L_list,IL_list,5)['polynomial']
p5 = np.poly1d(f5)
rsqaured5 = polyfit(L_list,IL_list,5)['determination']
#6차
f6 = polyfit(L_list,IL_list,6)['polynomial']
p6 = np.poly1d(f6)
rsqaured6 = polyfit(L_list,IL_list,6)['determination']

#print(rsqaured4,rsqaured5,rsqaured6)
print(rsqaured4)


# try 1