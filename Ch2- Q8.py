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

df = pd.read_csv('C:/Users/rahma/Desktop/Pycharm-HW/Data/College.csv')

# (b)Look at the data using the View() function. You should notice that the first column is just the name of each university. We don’t
# really want R to treat this as data. However, it may be handy to have these names for later. Try the following commands:

df_college = df.set_index(['Unnamed: 0'], append=True, verify_integrity=True)
df_college.rename_axis([None, 'College'], inplace=True)
print(df_college.head())

# (c) i. Use the summary function to produce a numerical summary of the variables in the data set.
print(df_college.describe())

# (c) ii. Use the pairs() function to produce a scatterplot matrix of the first ten columns or variables of the data. Recall that
# you can reference the first ten columns of a matrix A using A[,1:10].
sns.pairplot(df_college.iloc[:, 1:11]);
plt.show()
# (c) iii. Use the plot() function to produce side-by-side boxplots of Outstate versus Private.
sns.boxplot(x=df_college['Private'], y=df_college['Outstate']);
plt.show()


# (c) iv. Create a new qualitative variable, called Elite, by binning the Top10perc variable. We are going to divide universities
# into two groups based on whether or not the proportion # of students coming from the top 10 % of their high school classes exceeds 50 %
# Use the summary() function to see how many elite universities there are. Now use the plot() function to produce side-by-side boxplots of Outstate versus Elite.

df_college['Elite'] = df_college['Top10perc'] > 50
print(df_college['Elite'].sum())
sns.boxplot(x=df_college['Elite'], y=df_college['Outstate']);
plt.show()

# v. Use the hist() function to produce some histograms with differing numbers of bins for a few of the quantitative variables.
# You may find the command par(mfrow = c(2, 2)) useful: it will divide the print window into four regions so that four plots can be made simultaneously.
# Modifying the arguments to this function will divide the screen in other ways.

# to standardize or scale X -> Xi = Xi - mean(Xi) / stn dev(Xi)
def scale(df):
    return (df-df.mean())/(df.std())
var_count = 12
df_stand = scale(df_college.iloc[:, 1:var_count+1])

# The melt function is used to reshape the DataFrame. It essentially "melts" or unpivots the DataFrame from a wide format to a long format.
df_melted = df_stand.melt(var_name='cols', value_name='vals')

# Plot grid of plots
grid = sns.FacetGrid(df_melted, col='cols', col_wrap=4)
grid.map(sns.distplot, 'vals')
grid.set(xlim=(-4, 4));
plt.show()

