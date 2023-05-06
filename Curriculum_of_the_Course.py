# -*- coding: utf-8 -*-
"""
Created on Sat May  6 14:34:16 2023

@author: hp
"""

import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.ticker as mtick

data = pd.read_excel(r"C:\Users\hp\Desktop\Feedback_project\Question\Que_Visulize\Curriculum_of_the_Course.xlsx")

X = data['Curriculum of the Course '].tolist()
Y = data['Percentage'].tolist()
#Z = data["Total"].tolist()

fig, ax = plt.subplots()
plt.bar(X,Y , label = "Yes" , color = "y" ,width = 0.8 )
plt.bar(X,Y,label = "No" , color = "y")
plt.bar(X,Y,label = "Some Extent",color = "y")

plt.ylabel('Percentage(%)',fontsize=13)
plt.title('Curriculum of the Course ')
plt.legend()
yticks = mtick.PercentFormatter(xmax=1.0, decimals=0)
ax.yaxis.set_major_formatter(yticks)

plt.xticks()

plt.show()