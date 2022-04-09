import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
import seaborn as sns
from sklearn import preprocessing
from sklearn import linear_model

df = pd.read_csv('data/lab2_dataSet/bmi_data_lab3.csv')

g = sns.FacetGrid(df, col='BMI', col_order=[0,1,2,3,4])
g.map(plt.hist, 'Height (Inches)', bins = 10)
# plt.show()

height_weight_Data = df.loc[:, ['Height (Inches)','Weight (Pounds)']]
stdscaler = preprocessing.StandardScaler()
scaled_df = stdscaler.fit_transform(height_weight_Data)
scaled_df = pd.DataFrame(scaled_df, columns=['Height (Inches)', 'Weight (Pounds)'])

fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(6,5))

ax1.set_title('Before Scaling')
sns.kdeplot(df['Height (Inches)'], ax=ax1)
sns.kdeplot(df['Weight (Pounds)'], ax=ax1)

ax2.set_title('After Standard Scaler')
sns.kdeplot(scaled_df['Height (Inches)'], ax=ax2)
sns.kdeplot(scaled_df['Weight (Pounds)'], ax=ax2)
plt.show()
