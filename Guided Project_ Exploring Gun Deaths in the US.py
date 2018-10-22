
# coding: utf-8

# In[1]:


import csv
import datetime

# Reading the dataset in as a list using the csv module
f = open("guns.csv", "r")
read = csv.reader(f)
data = list(read)

# Headers and Data distinguishing
headers = data[:1]
data = data[1:len(data)]

# Function for statistics calculation
def counts(lst):
    dic_counts = {}
    for elm in lst:
        if elm in dic_counts:
            dic_counts[elm] += 1
        if elm not in dic_counts:
            dic_counts[elm] = 1
    return dic_counts


# In[2]:


#Death quantity per year calculation
years = [row[1] for row in data]
year_counts = counts(years)
year_counts


# In[3]:


# Death quantity per month and year
dates = [datetime.datetime(year=int(row[1]),month=int(row[2]),day=1) 
         for row in data]
date_counts = counts(dates)
date_counts

# Maximum and minimum values calculation per year+month
maxim = None
max_date = None
minim = None
min_date = None
for key in date_counts:
    if maxim is None or date_counts[key] > maxim:
        maxim = date_counts[key]
        max_date = key
    if minim is None or date_counts[key] < minim:
        minim = date_counts[key]
        min_date = key
print(maxim, max_date)
print(minim, min_date)


# In[4]:


# Death per sex calculation
sex = [row[5] for row in data]
sex_counts = counts(sex)
sex_counts


# In[5]:


# Death per race calculation
race = [row[7] for row in data]
race_counts = counts(race)
race_counts
race_counts


# # Conclusions:
# ## Death per year calculations
# Deaths quantity equals 33600 in average
# 
# ## Death per month and year calculations:
# Maximum deaths equal 3079 on 2013-07-01
# Minimum deaths equal 2357 on 2012-02-01
# 
# ## Sex statistics calculations:
# Men are involved in gun deaths more frequent than women
# 
# ## Race statistics calculations:
# Native americans kill people less rarely than others, the highest value is found in white people race.

# In[6]:


d = open("census.csv","r")
census_read = csv.reader(d)
census = list(census_read)
census = census[1:2]
census


# ## Deaths quantity per 100000 of each race

# In[7]:


mapping = {}
mapping["Asian/Pacific Islander"] = 674625 + 15159516
mapping["Black"] = 40250635
mapping["Native American/Native Alaskan"] = 3739506
mapping["Hispanic"] = 44618105
mapping["White"] = 197318956
race_per_hundred = {}
for key in race_counts:
    race_per_hundred[key] = (race_counts[key]/mapping[key]) * 100000
race_per_hundred


# ## Filtering by Homicide Intent

# In[8]:


intents = [item[3] for item in data]
races = [item[7] for item in data]
homicide_race_counts = {}
for i, race in enumerate(races):
    if intents[i] == "Homicide":
        if race not in homicide_race_counts:
            homicide_race_counts[race] = 1
        if race in homicide_race_counts:
            homicide_race_counts[race] += 1
homicide_race_per_hundred = {}
for key in homicide_race_counts:
    homicide_race_per_hundred[key] = (homicide_race_counts[key]/mapping[key])* 100000
homicide_race_per_hundred 

