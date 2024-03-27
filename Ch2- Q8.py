# Solving questions for the book "An Introduction to Statistical Learning" by Gareth James • Daniela Witten • Trevor Hastie • Robert Tibshirani
# Zahra Rahmati
# Chapter 2

# Chapter 2 Question 8: This exercise relates to the College data set, which can be found in
# the file College.csv on the book website. It contains a number of
# variables for 777 different universities and colleges in the US.

# (a) Use the pd.read_csv() function to read the data into Python. Call the loaded data college.
# Make sure that you have the directory set to the correct location for the data.
import numpy as np
import pandas as pd
import seaborn as sns
import warnings

warnings.filterwarnings('ignore')
import matplotlib.pyplot as plt

college = pd.read_csv('C:/Users/rahma/Desktop/Pycharm-HW/Data/College.csv')

# (b)Look at the data using the View() function. You should notice that the first column is just the name of each university. We don’t
# really want R to treat this as data. However, it may be handy to have these names for later. Try the following commands:

college2 = pd.read_csv('C:/Users/rahma/Desktop/Pycharm-HW/Data/College.csv', index_col=0)
college3 = college.rename({'Unnamed: 0': 'College'}, axis=1)
college3 = college3.set_index('College')
college = college3

# (c) Use the describe() method of to produce a numerical summary of the variables in the data set.
print(college.describe())

# (d) Use the pd.plotting.scatter_matrix() function to produce a scatterplot matrix of the first columns [Top10perc, Apps, Enroll].
# Recall that you can reference a list C of columns of a data frame A using A[C].
pd.plotting.scatter_matrix(college[["Top10perc", "Apps", "Enroll"]])
plt.show()
# plt.savefig('scatterplot_matrix.png')

# (e) Use the boxplot() method of college to produce side-by-side boxplots of Outstate versus Private.
college.boxplot(column='Outstate', by='Private', figsize=(8, 6))
plt.show()

# (f) Create a new qualitative variable, called Elite, by binning the
# Top10perc variable into two groups based on whether or not the
# proportion of students coming from the top 10% of their high
# school classes exceeds 50%

college['Elite'] = pd.cut(college['Top10perc'], [0, 50, 100], labels=['No', 'Yes'])
elite_counts = college['Elite'].value_counts()
print(elite_counts)
college.boxplot(column='Outstate', by='Elite', figsize=(8, 6))
plt.show()

# (g) Use the plot.hist() method of college to produce some histograms with differing numbers of bins for a few of the quantitative variables. The command plt.subplots(2, 2) may be useful: it will divide the plot window into four regions so that four
# plots can be made simultaneously. By changing the arguments
# you can divide the screen up in other combinations.

variables = ["Apps", "Accept", "Enroll", "Top10perc", "Top25perc", "F.Undergrad", "P.Undergrad",
             "Outstate","Room.Board"]
fig, axes = plt.subplots(3, 3, figsize=(10, 8))
axes = axes.flatten()
for i, variable in enumerate(variables):
    college[variable].plot.hist(ax=axes[i], bins=50)
    axes[i].set_title(f'Histogram of {variable}')
    axes[i].set_xlabel(variable)
    axes[i].set_ylabel('Frequency')
plt.tight_layout()
plt.show()
