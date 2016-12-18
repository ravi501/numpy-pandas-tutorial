import pandas as pd


'''
Pandas series

A series is a 1-D array like object.
'''

obj = pd.Series([4, 7, -5, 3])
print(obj)
print(obj.values)
print(obj.index)

# It is often desirable to create a series with an index identifying each data point
print('Pandas series with indexes')
obj1 = pd.Series([4, 7, 5, -2], index=['d', 'b', 'a', 'c'])
print(obj1)
print(obj1.index)
print(obj1['a'])
print(obj1[['c', 'a', 'd']])

#Operations on pandas series
print('Operations on pandas series')
print(obj1[obj1 > 0])
print(obj1*2)
print('b' in obj1)
print('f' in obj1)


# Pandas series with indexes
print('Pandas series with indexes')
sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
obj3 = pd.Series(sdata)
print(obj3)

# When only passing a dictionary, the index in the resulting series will have the dictionaries keys in sorted order
states = ['California', 'Ohio', 'Oregon', 'Texas']
obj4 = pd.Series(sdata, index=states)
print(obj4)

# isNull and notNull functions in pandas series
print('isNull and notNull functions in pandas series')
print(pd.isnull(obj4))
print(pd.notnull(obj4))
print(obj4.isnull())

# Addition operations
print('Addition operations')
print(obj3 + obj4)

# Both the series object and its index have a name attribute which integrates with other key areas of pandas
# functionality
print('Name functionality in pandas')
obj4.name = 'population'
obj4.index.name = 'states'
print(obj4)

# A series can be altered in place by assignment
print('A series can be altered in place by assignment')
obj.index = ['Bob', 'Steve', 'Jeff', 'Ryan']
print(obj)
