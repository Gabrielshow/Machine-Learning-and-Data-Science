#pandas
import pandas as pd
import matplotlib.pyplot as plt

#a series is a 1-dimensional array while a Dataframe is a multi-dimensional array

#creating dataframes
data = {'ages': [14, 18, 24, 42],
        'height': [174, 180, 175, 184]}

df = pd.DataFrame(data)


#each key is column while the value is an array representing the data for the column
print(df)

#DataFrame automatically creates a numeric index for each row but we can specify
# a custom index, when creating the DataFrame
df2 = pd.DataFrame(data, index=['James', 'Bob', 'Amy', 'Dave'])
print(df2)

#now we can access a row sing its index and the loc[] function
# print(df2.loc('Bob'))

#indexing and slicing
#we can select a single column by specifying its name in square brackets
print(df['ages'])

# to select multiple columns
print(df[["ages", "height"]])

# slicing

# pandas use the iloc function to select data based on its numeric index
print(df.iloc[2])  #third row

print(df.iloc[:3])  #first three rows

print(df.iloc[1:3])  #rows 2 and 3

#conditions
print(df2[(df2['ages']>18) & (df2['height'] > 180)])

#reading csv files
# df = pd.read_csv("covid.csv")
# we can get first rows of the data using the head() function of the Data Frame:
# print(df.head())
# info() function gets essential information about tyour dataset, such as number of rows, columns, datatypes etc
# df.info()
# pandas has added an auto generated index to get our own index column in by using the set_index() function
# print(df.set_index("data", inplace = True))
# specifies that the change will be applied to our dataframe, without the need to assign it to a new dataframe variable.

#Dropping a column
# df.drop('state', axis=1, inplace = True)
# axis=1 specifies we want to drop a column, 0 specifies we want to drop a row
# creating columns
# df['month'] = pd.to_dateTime(df['ages'], format=%d.%m%y").df.month_name()
# df['area'] = df['width'] * df['height']

#summary statistics
print(df.describe())
print(df['height'].describe())

#grouping
print(df['height'].value_counts())
# value_counts() returns the frequency of the values

#group by
print(df.groupby('ages')['height'].sum())

# df.plot(kind= "bar") #barplot
# df.plot(kind='bar', stacked= True) #stacked barplot
# df.plot(kind='barh') #horizontal bar plot
# df.plot(kind='box') #box plot
# df.plot(kind='hist', bins=2) #default number of bins is 7
# df.plot(kind='area', stacked=False) #area plot
# df.plot(kind='scatter',x='ages',y='height')
# df.plot(kind='pie', subplots=True) #pie plot
df.plot(kind='line', legend=True)
plt.xlabel('Ages')
plt.ylabel('Height')
plt.savefig('plotformatting.png')
plt.show()

