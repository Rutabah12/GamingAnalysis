#!/usr/bin/env python
# coding: utf-8

# ### Heroes Of Pymoli Data Analysis
# * Of the 1163 active players, the vast majority are male (84%). There also exists, a smaller, but notable proportion of female players (14%).
# 
# * Our peak age demographic falls between 20-24 (44.8%) with secondary groups falling between 15-19 (18.60%) and 25-29 (13.4%).  
# -----

# ### Note
# * Instructions have been included for each segment. You do not have to follow them exactly, but they are included to help you think through the steps.

# In[1]:


# Dependencies and Setup
import pandas as pd

# File to Load (Remember to Change These)
file_to_load = "Resources/purchase_data.csv"

# Read Purchasing File and store into Pandas data frame
purchase_data_df = pd.read_csv(file_to_load)

purchase_data_df.head()


# ## Player Count

# * Display the total number of players
# 

# In[2]:


count_of_player =len(purchase_data_df["SN"].unique())
count_of_player_disp=pd.DataFrame({"Player Count" : [count_of_player]})

count_of_player_disp


# ## Purchasing Analysis (Total)

# * Run basic calculations to obtain number of unique items, average price, etc.
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame
# 

# In[8]:


items_count= len(purchase_data_df["Item ID"].unique())
avg_price= round(purchase_data_df["Price"].mean(),2)
number_of_purchases = len(purchase_data_df["Item Name"])
revenue= purchase_data_df["Price"].sum()

summary_df = pd.DataFrame ({"Number of Items" : [items_count],
                          "Average Price" : [avg_price], 
                          "Number of Purchases" : [number_of_purchases],
                           "Total Revenue" : [revenue]
                           })
summary_df


# ## Gender Demographics

# * Percentage and Count of Male Players
# 
# 
# * Percentage and Count of Female Players
# 
# 
# * Percentage and Count of Other / Non-Disclosed
# 
# 
# 

# In[56]:


grouped_df=purchase_data_df.groupby(["Gender"])
unique_df = grouped_df.nunique()

total_gender=unique_df["SN"].sum()

count= unique_df["SN"].unique()
percentage= unique_df["SN"]/total_gender*100

final_gender = pd.DataFrame({"Percentage of Players" : percentage,
                            "Count": count})
final_gender


# 
# ## Purchasing Analysis (Gender)

# * Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. by gender
# 
# 
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame

# In[64]:


purchase_count=unique_df["Gender"].value_counts()

average_price = grouped_df["Price"].mean()

purchase_price=grouped_df["Price"].sum()

average_per_person=purchase_price/count

gender_analysis=pd.DataFrame({"Avgerage Purchase Price" : average_price,
                             "Total Purchase Price" : purchase_price,
                             "Purchase total per person": average_per_person})

gender_analysis


# ## Age Demographics

# * Establish bins for ages
# 
# 
# * Categorize the existing players using the age bins. Hint: use pd.cut()
# 
# 
# * Calculate the numbers and percentages by age group
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: round the percentage column to two decimal points
# 
# 
# * Display Age Demographics Table
# 

# In[71]:


bins = [0,10,15,20,25,30,35,40,200]
binLab = ['Under 10', '10 - 14', '15 - 19', '20 - 24', '25 - 29', '30 - 34', '35 - 39', 'Over 40']

binner_df = purchase_data_df.copy()
binner_df["Age Groups"] = pd.cut(binner_df["Age"], bins, labels=binLab)
group_bin = binner_df.groupby(["Age Groups"])

binnerCount = group_bin["SN"].count()
countTotal = purchase_data_df["SN"].count()
percentage = (binnerCount / countTotal) * 100
percentage

Age_Perc = pd.DataFrame({"Total Count": binnerCount,
                         "Percentage of Players": percentage})


# ## Purchasing Analysis (Age)

# * Bin the purchase_data data frame by age
# 
# 
# * Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. in the table below
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame

# In[7]:





# ## Top Spenders

# * Run basic calculations to obtain the results in the table below
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Sort the total purchase value column in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the summary data frame
# 
# 

# In[8]:





# ## Most Popular Items

# * Retrieve the Item ID, Item Name, and Item Price columns
# 
# 
# * Group by Item ID and Item Name. Perform calculations to obtain purchase count, item price, and total purchase value
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Sort the purchase count column in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the summary data frame
# 
# 

# In[9]:





# ## Most Profitable Items

# * Sort the above table by total purchase value in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the data frame
# 
# 

# In[10]:




