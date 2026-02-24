import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")

df = pd.read_csv("emp.csv")

print(df.head())
print(df.info())

print(df.isnull().sum())
print(df.describe())

plt.figure()
df['Attrition'].value_counts().plot(kind='bar')
plt.title("Attrition Count")
plt.xlabel("Attrition")
plt.ylabel("Number of Employees")
plt.show()

plt.figure()
sns.countplot(data=df, x='Department', hue='Attrition')
plt.title("Attrition by Department")
plt.xticks(rotation=45)
plt.show()

attrition_rate = (
    df.groupby('Department')['Attrition']
      .value_counts(normalize=True)
      .rename('rate')
      .reset_index()
)

attrition_yes = attrition_rate[attrition_rate['Attrition'] == 'Yes']

plt.figure()
sns.barplot(data=attrition_yes, x='Department', y='rate')
plt.title("Attrition Rate by Department")
plt.xticks(rotation=45)
plt.ylabel("Attrition Rate")
plt.show()

numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns

df[numeric_cols].hist(figsize=(12, 8))
plt.show()

plt.figure(figsize=(10, 6))
sns.heatmap(df[numeric_cols].corr(), annot=True, cmap="coolwarm")
plt.title("Feature Correlation")
plt.show()
