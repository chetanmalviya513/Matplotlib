# -*- coding: utf-8 -*-
"""
Created on Sat May  6 14:15:47 2023

@author: hp
"""

import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.ticker as mtick

data = pd.read_excel(r"C:\Users\hp\Desktop\Feedback_project\Question\Que_Visulize\Did_you_acquire_sufficient_knowledge_regarding_your_role_and_responsibilities_in_higher_education.xlsx")

X = data['Did you acquire sufficient knowledge regarding your role and responsibilities in higher education?'].tolist()
Y = data['Percentage'].tolist()
#Z = data["Total"].tolist()

fig, ax = plt.subplots()
plt.bar(X,Y , label = "Yes" , color = "m" ,width = 0.8 )
plt.bar(X,Y,label = "No" , color = "m")
plt.bar(X,Y,label = "Some Extent",color = "m")

plt.ylabel('Percentage(%)',fontsize=13)
plt.title('Did you acquire sufficient knowledge regarding your role and responsibilities in higher education?')
plt.legend()
yticks = mtick.PercentFormatter(xmax=1.0, decimals=0)
ax.yaxis.set_major_formatter(yticks)

plt.xticks()

plt.show()