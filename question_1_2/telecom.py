import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")

df = pd.read_csv("telecom.csv")

print(df.head())
print(df.info())

print(df.isnull().sum())
print(df.describe())

if 'Churn' in df.columns:
    plt.figure()
    df['Churn'].value_counts().plot(kind='bar')
    plt.title("Churn Distribution")
    plt.xlabel("Churn")
    plt.ylabel("Count")
    plt.show()

categorical_cols = df.select_dtypes(include=['object']).columns
numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns

if 'Churn' in df.columns:
    for col in categorical_cols:
        if col != 'Churn':
            plt.figure()
            sns.countplot(data=df, x=col, hue='Churn')
            plt.xticks(rotation=45)
            plt.title(f"Churn by {col}")
            plt.show()

if len(numeric_cols) > 0:
    df[numeric_cols].hist(figsize=(12, 8))
    plt.show()

if len(numeric_cols) > 1:
    plt.figure(figsize=(10, 6))
    sns.heatmap(df[numeric_cols].corr(), annot=True, cmap="coolwarm")
    plt.title("Correlation Heatmap")
    plt.show()

if 'Churn' in df.columns:
    for col in numeric_cols:
        plt.figure()
        sns.boxplot(x=df['Churn'], y=df[col])
        plt.title(f"{col} vs Churn")
        plt.show()
