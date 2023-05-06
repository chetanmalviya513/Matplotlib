# -*- coding: utf-8 -*-
"""
Created on Fri May  5 21:51:54 2023

@author: hp
"""


import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.ticker as mtick

data = pd.read_excel(r"C:\Users\hp\Desktop\Feedback_project\Question\Que_Visulize\Did you find the course.xlsx")

X = data['Did you find the course useful ? '].tolist()
Y = data['Percentage'].tolist()
#Z = data["Total"].tolist()

fig, ax = plt.subplots()
plt.bar(X,Y , label = "Yes" , color = "c" ,width = 0.8 )
plt.bar(X,Y,label = "No" , color = "c")
plt.bar(X,Y,label = "Some Extent",color = "c")

plt.ylabel('Percentage(%)',fontsize=13)
plt.title('Did you find the course useful ? ')
plt.legend()
yticks = mtick.PercentFormatter(xmax=1.0, decimals=0)
ax.yaxis.set_major_formatter(yticks)

#plt.xticks()

plt.show()