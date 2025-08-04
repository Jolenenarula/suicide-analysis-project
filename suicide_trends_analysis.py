# Step 1: Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Make plots look better
sns.set(style="whitegrid")
plt.rcParams["figure.figsize"] = (10, 6)

# Step 2: Load the dataset
df = pd.read_csv("who_suicide_statistics.csv")

# Step 3: Preview the data
print(df.head())
print("\nShape of dataset:", df.shape)
print("\nColumn names:", df.columns)

# Step 4: Check for missing values
print("\nMissing values:\n", df.isnull().sum())

# Step 5: Drop rows with missing suicide number OR population
df = df.dropna(subset=['suicides_no', 'population'])

# Step 6: Convert suicide numbers and population to integers
df['suicides_no'] = df['suicides_no'].astype(int)
df['population'] = df['population'].astype(int)

# Check the new shape
print("\nNew shape after cleaning:", df.shape)

# Step 7: Calculate suicide rate per 100k population
df['suicide_rate'] = (df['suicides_no'] / df['population']) * 100000

# Preview the data again
print(df.head())

# Step 8: Global suicide rate per year
global_trend = df.groupby('year')['suicide_rate'].mean().reset_index()

# Plot the trend
plt.figure(figsize=(12, 6))
sns.lineplot(data=global_trend, x='year', y='suicide_rate', marker='o', color='crimson')
plt.title('🌍 Global Average Suicide Rate Over Time (1985–2016)', fontsize=14)
plt.xlabel('Year')
plt.ylabel('Suicide Rate per 100k')
plt.grid(True)
plt.tight_layout()
plt.show()

# Step 9: Gender-based suicide rates per year
gender_trend = df.groupby(['year', 'sex'])['suicide_rate'].mean().reset_index()

# Plot gender trends
plt.figure(figsize=(12, 6))
sns.lineplot(data=gender_trend, x='year', y='suicide_rate', hue='sex', marker='o')
plt.title('🧑‍🤝‍🧑 Global Suicide Rate by Gender Over Time', fontsize=14)
plt.xlabel('Year')
plt.ylabel('Suicide Rate per 100k')
plt.legend(title='Gender')
plt.grid(True)
plt.tight_layout()
plt.show()

# Step 10: Top 10 countries by average suicide rate
country_avg = df.groupby('country')['suicide_rate'].mean().sort_values(ascending=False).head(10).reset_index()

# Plot
plt.figure(figsize=(12, 6))
sns.barplot(data=country_avg, x='suicide_rate', y='country', palette='Reds_r')
plt.title('🌎 Top 10 Countries by Average Suicide Rate (1985–2016)', fontsize=14)
plt.xlabel('Average Suicide Rate per 100k')
plt.ylabel('Country')
plt.tight_layout()
plt.show()

# Step 11: Average suicide rate by age group
age_avg = df.groupby('age')['suicide_rate'].mean().sort_values(ascending=False).reset_index()

# Plot
plt.figure(figsize=(10, 6))
sns.barplot(data=age_avg, x='suicide_rate', y='age', palette='Blues_d')
plt.title('📊 Average Global Suicide Rate by Age Group (1985–2016)', fontsize=14)
plt.xlabel('Average Suicide Rate per 100k')
plt.ylabel('Age Group')
plt.tight_layout()
plt.show()


