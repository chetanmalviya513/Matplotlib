# -*- coding: utf-8 -*-
"""
Created on Sat May  6 15:09:45 2023

@author: hp
"""


import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel(r"C:\Users\hp\Desktop\Feedback_project\Other\Resource_person_graph.xlsx")

Name = data['Name of resource person'].tolist()
#Rating  = data['Rating '].tolist()
Score  = data['Score '].tolist()

Name_11 = Name
Score_11 = Score


plt.bar(Name_11,Score_11,width=0.4,color="m",label="Rating")

plt.xlabel("Name of resource person & Rating")
plt.ylabel("Score",fontsize=18)
plt.title("Resource person Rating")
plt.legend()
plt.xticks(rotation=90)
#fig=plt.figure(figsize=(5,5))
plt.ylim(100, 900)
plt.xlim(14)
plt.show()
