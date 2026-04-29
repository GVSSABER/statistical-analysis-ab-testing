import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind
df = pd.read_csv("ab_data.csv")
df.head()
df.info()
df.isnull().sum()
print(df.head())
print(df.shape)
print(df['group'].value_counts())
print(df['converted'].value_counts())
conversion_rate = df.groupby('group')['converted'].mean()
print(conversion_rate)
conversion_rate.plot(kind='bar')
plt.title("Conversion Rate by Group")
plt.ylabel("Conversion Rate")
plt.show()
control = df[df['group'] == 'control']['converted']
treatment = df[df['group'] == 'treatment']['converted']
from scipy.stats import ttest_ind
t_stat, p_value = ttest_ind(control, treatment)
print("p-value:", p_value)
if p_value < 0.05:
    print("Reject Null Hypothesis (Significant)")
else:
    print("Fail to Reject Null Hypothesis")