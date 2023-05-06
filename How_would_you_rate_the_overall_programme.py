# -*- coding: utf-8 -*-
"""
Created on Sat May  6 14:37:58 2023

@author: hp
"""

import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.ticker as mtick

data = pd.read_excel(r"C:\Users\hp\Desktop\Feedback_project\Question\Que_Visulize\How_would_you_rate_the_overall_programme.py.xlsx")

X = data['How would you rate the overall programme  '].tolist()
Y = data['Percentage'].tolist()
#Z = data["Total"].tolist()

fig, ax = plt.subplots()
plt.bar(X,Y , label = "Yes" , color = "g" ,width = 0.8 )
plt.bar(X,Y,label = "No" , color = "g")
plt.bar(X,Y,label = "Some Extent",color = "g")

plt.ylabel('Percentage(%)',fontsize=13)
plt.title('How would you rate the overall programme  ')
plt.legend()
yticks = mtick.PercentFormatter(xmax=1.0, decimals=0)
ax.yaxis.set_major_formatter(yticks)

plt.xticks()

plt.show()