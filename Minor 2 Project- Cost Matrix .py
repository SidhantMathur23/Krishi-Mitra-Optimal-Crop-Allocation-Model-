#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 

# importing data
data = pd.read_csv(r"C:\Users\Sidhant Mathur\Downloads\Agri (1).csv")

# accept user input for crops and states
crop_names = []
state_names = []
for i in range(0,4):
    crop_name= str(input("Enter Crop Name: "))
    crop_names.append(crop_name)
for i in range(0,4):
    state_name = str(input("Enter State Name: "))
    state_names.append(state_name)

# Calculate cost matrix 
cost_matrix = []
for crop_name in crop_names:
    all_states = list(pd.DataFrame(data[data["Crop"]==crop_name]["State"])["State"].unique())
    state_profit = []
    for state in state_names: 
        if state in all_states:
            profit = data[(data["Crop"]==crop_name) & (data["State"]==state) ]["Profit"].item()
            state_profit.append(profit)
        else:
            state_profit.append(0)
    cost_matrix.append(state_profit)
cost_matrix


# In[ ]:




