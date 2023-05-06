# -*- coding: utf-8 -*-
"""
Created on Sat May  6 14:23:55 2023

@author: hp
"""

import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.ticker as mtick

data = pd.read_excel(r"C:\Users\hp\Desktop\Feedback_project\Question\Que_Visulize\Do_you_have_the_confidence_in_developing_research_proposal_and_writing_research_articles.xlsx")

X = data['Do you have the confidence in developing research proposal and writing research articles?  '].tolist()
Y = data['Percentage'].tolist()
#Z = data["Total"].tolist()

fig, ax = plt.subplots()
plt.bar(X,Y , label = "Yes" , color = "m" ,width = 0.8 )
plt.bar(X,Y,label = "No" , color = "m")
plt.bar(X,Y,label = "Some Extent",color = "m")

plt.ylabel('Percentage(%)',fontsize=13)
plt.title('Do you have the confidence in developing research proposal and writing research articles?  ')
plt.legend()
yticks = mtick.PercentFormatter(xmax=1.0, decimals=0)
ax.yaxis.set_major_formatter(yticks)

plt.xticks()

plt.show()