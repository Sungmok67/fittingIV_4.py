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
from parsing_2 import x_cut,y_cut,Voltage,Current
import fittingL_3

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

polyIV=polyfit(x_cut,y_cut,12)['polynomial']
poly1dIV=np.poly1d(polyIV)

def foo(x, amp, b):
    return abs(amp * (exp(b * x) - 1)) + poly1dIV(x)


my_model = Model(foo)
result = my_model.fit(Current, x=Voltage, amp=0.1, b=0.1)

best_f  = result.best_fit.tolist()
poly1dIV_list =list(poly1dIV(x_cut))

yhat=best_f
ybar = np.sum(Current)/len(Current)         #평균값
ssreg=np.sum((yhat-ybar)**2)   #실제값과 예측값차이
sstot = np.sum((Current-ybar)**2)     #실제값과 평균값 차이
results=ssreg/sstot

print(results)
