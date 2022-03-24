import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib as plt
from sklearn.preprocessing import LabelEncoder

train_url = "http://s3.amazonaws.com/assets.datacamp.com/course/Kaggle/train.csv"
test_url = "http://s3.amazonaws.com/assets.datacamp.com/course/Kaggle/test.csv"
train = pd.read_csv(train_url)
test = pd.read_csv(test_url)

print("***** Train_Set *****")
print(train.head())
print("\n")
print("***** Train_Set *****")
print(test.head())

print("***** Train_Set *****")
print(train.describe())
print("\n")
print("***** Test_Set *****")
print(test.describe())

print(train.columns.values)

train.isna().head()
test.isna().head()

# isna.sum() : na값, 즉 missing values의 수를 반환해줌.
print("*****In the train set*****")
print(train.isna().sum())
print("\n")
print("*****In the test set*****")
print(test.isna().sum())

# Fill missing values with mean column values in the train set
# missing value를 평균값으로 치환해줌.
train.fillna(train.mean(), inplace=True)
# Fill missing values with mean column values in the test set
test.fillna(test.mean(), inplace=True)

# after fillna with mean value
# 여기서 Cabin과 Embarked가 0이 아닌 이유는 numerical value가 아니기 때문, 즉 평균값을 얻을 수 없기 때문.
print("*****In the train set*****")
print(train.isna().sum())
print("\n")
print("*****In the test set*****")
print(test.isna().sum())

train[['Pclass', 'Survived']].groupby(['Pclass'], as_index=False).mean().sort_values(by='Survived', ascending=False)

train[["Sex", "Survived"]].groupby(['Sex'], as_index=False).mean().sort_values(by='Survived', ascending=False)

train[["SibSp", "Survived"]].groupby(['SibSp'], as_index=False).mean().sort_values(by='Survived', ascending=False)

# matplotlib만 import할 것이 아니라
g = sns.FacetGrid(train, col='Survived')
g.map(plt.hist, 'Age', bins=20)

grid = sns.FacetGrid(train, col='Survived', row='Pclass', height=2.2, aspect=1.6)
grid.map(plt.hist, 'Age', alpha=.5, bins=20)
grid.add_legend()

train.info()

# 데이터 분석에 영향을 미치지 않는 값들 drop
train = train.drop(['Name','Ticket','Cabin','Embarked'], axis=1)
test = test.drop(['Name','Ticket','Cabin','Embarked'], axis=1)

# 딥러닝에서는 수치가 아닌 값을 다루기 어렵기 때문에 LabelEncoder를 통해 수치로 바꾸어준다.
labelEncoder = LabelEncoder()
labelEncoder.fit(train['Sex'])
labelEncoder.fit(test['Sex'])
train['Sex'] = labelEncoder.transform(train['Sex'])
test['Sex'] = labelEncoder.transform(test['Sex'])

# 바꾼 후 info를 보면 성 항목의 타입이 변경된 것을 확인할 수 있다.
train.info()
test.info()