#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#import pandas(for dataframe purposes) and matplotlib (for visualization purposes)
import pandas as pd
import matplotlib.pyplot as plt


# In[ ]:


#convert the csv file to a DataFrame
office_df = pd.read_csv("the_office_series.csv", parse_dates=['Date'])


# In[ ]:


#Create two empty lists
color = []
sizes = []


# In[ ]:


#loops to iterate through the DataFrame, and add values to the empty lists.
for ind, row in office_df.iterrows():
    if row['Ratings'] < 0.25:
        color.append('red')
    elif row['Ratings'] < 0.50:
        color.append('orange')
    elif row['Ratings'] < 0.75:
        color.append('lightgreen')
    else:
        color.append('darkgreen')

# Iterate through the DataFrame, and assign a size based on whether it has guests        
for ind, row in office_df.iterrows():
    if row['has_guests'] == False:
        sizes.append(25)
    else:
        sizes.append(250)


# In[ ]:


#create new columns for the list created above
office_df['colors'] = color
office_df['sizes'] = sizes


# In[ ]:


#split data into guest and non_guest DataFrames
non_guest_df = office_df[office_df['has_guests'] == False]
guest_df = office_df[office_df['has_guests'] == True]


# In[ ]:


#choose the size and style of your graph
plt.rcParams['figure.figsize'] = [11, 7]
plt.style.use('fivethirtyeight')
fig = plt.figure()


# In[ ]:


# create two scatter plots for guests and non_guests DataFrame
plt.scatter(x=non_guest_df.episode_number, y=non_guest_df.viewership_mil, 
                 c=non_guest_df['colors'], s=25)


plt.scatter(x=guest_df.episode_number, y=guest_df.viewership_mil,
                 c=guest_df['colors'], marker='*', s=250)


# In[ ]:


# Create a title
plt.title("Popularity, Quality, and Guest Appearances on the Office", fontsize=28)

# Create an x-axis label
plt.xlabel("Episode Number", fontsize=18)

# Create a y-axis label
plt.ylabel("Viewership (Millions)", fontsize=18)


# In[ ]:


# Show the plot
plt.show()


# In[ ]:


# Get the most popular guest star
print(office_df[office_df['viewership_mil'] > 20]['guest_stars'])

