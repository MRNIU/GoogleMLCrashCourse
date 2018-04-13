import pandas as pd
import numpy as np


print(pd.__version__)


pd.Series(['San Francisco', 'San Jose', 'Sacramento'])

city_names = pd.Series(['San Francisco', 'San Jose', 'Sacramento'])
population = pd.Series([852469, 1015785, 485199])

pd.DataFrame({ 'City name': city_names, 'Population': population })

california_housing_dataframe = pd.read_csv("california_housing_train.csv", sep=",")
california_housing_dataframe.describe()

california_housing_dataframe.head()

california_housing_dataframe.hist('housing_median_age')

cities = pd.DataFrame({ 'City name': city_names, 'Population': population })
print(type(cities['City name']))
cities['City name']

print(type(cities['City name'][1]))
cities['City name'][1]

print(type(cities[0:2]))
cities[0:2]

population / 1000.

np.log(population)

population.apply(lambda val: val > 1000000)

cities['Area square miles'] = pd.Series([46.87, 176.53, 97.92])
cities['Population density'] = cities['Population'] / cities['Area square miles']
print(cities)

# 练习一
cities['Is wide and has saint name'] = (cities['Area square miles'] > 50) & cities['City name'].apply(lambda name: name.startswith('San'))
print(cities)
##

print(city_names.index)

print(cities.index)

cities.reindex([2, 0, 1])

cities.reindex(np.random.permutation(cities.index))

# 练习二
cities.reindex([0, 4, 5, 2])
##




