import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
from sklearn.impute import KNNImputer

warnings.filterwarnings(
    "ignore"
)


data = pd.read_csv(r'C:\Users\i7tuf\Downloads\archive (2)\Life Expectancy Data.csv')

print(data.head())
print(data.tail())

# sanity check of the data
print(data.shape)
print(data.info())


# finding missing values
print(data.isnull().sum()/data.shape[0]*100)

# finding duplicates
print(data.duplicated().sum())

# identifying the garbage values
# garbage value is always in the form of garbage 

for i in data.select_dtypes(include=object).columns:
    print(data[i].value_counts())
    print("***"*10)

# exploratory data analysis of the data
print(data.describe(include=object))


# histogram to understand the distribution
for i in data.select_dtypes(include="number").columns:
    sns.histplot(data=data, x=i)
    plt.show()

# to get the realtionship of life expectandancy

for i in ['Year', 'Adult Mortality', 'infant deaths',
       'Alcohol', 'percentage expenditure', 'Hepatitis B', 'Measles ', ' BMI ',
       'under-five deaths ', 'Polio', 'Total expenditure', 'Diphtheria ',
       ' HIV/AIDS', 'GDP', 'Population', ' thinness  1-19 years',
       ' thinness 5-9 years', 'Income composition of resources', 'Schooling']:
    sns.scatterplot(data=data, x=i, y='Life expectancy')
    plt.show()

print(data.select_dtypes(include="number").columns)


# Handling missing values:
# Use mean or median for continuous data.
# Use mode for categorical data.
# Consider using KNN Imputer as an alternative approach.

# first we will select numerical columns
print(data.isnull().sum())


for i in ["Polio", "Income composition of resources"]:
    data[i].fillna(data[i].median(), inplace=True)


print(data.isnull().sum())


impute = KNNImputer()
for i in data.select_dtypes(include="number").columns:
    data[i]=impute.fit_transform(data[[i]])

print(data.isnull().sum())

# dropping the duplicates from data
data.drop_duplicates()

# Encoding of the data
# labeling the endoing and one hot encoding
# 'Country' and 'Status' columns are converted to dummy variables
dummy = pd.get_dummies(data=data, columns=['Country', 'Status'], drop_first=True)

print(dummy)

# Save the processed dataset to a new CSV file
dummy.to_csv('Output.csv', index=False)