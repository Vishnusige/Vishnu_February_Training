import pandas as pd
import numpy as np

# 1. Load the dataset
df = pd.read_csv('netflix_titles.csv')
print("Original Data Shape:", df.shape)

# REQUIREMENT: Identifying and dropping irrelevant or redundant features
# 'show_id' is just an arbitrary ID, 'description' is raw text unusable for standard scaling
df = df.drop(columns=['show_id', 'description'])

# REQUIREMENT: Handling missing values
df['director'] = df['director'].fillna('Unknown Director')
df['cast'] = df['cast'].fillna('Unknown Cast')
df['country'] = df['country'].fillna(df['country'].mode()[0])
df['rating'] = df['rating'].fillna(df['rating'].mode()[0])
df = df.dropna(subset=['date_added', 'duration'])

# REQUIREMENT: Removing duplicate records
df = df.drop_duplicates()

# REQUIREMENT: Fixing incorrect data types
# Convert 'duration' (e.g., "90 min") into a pure float number
df['duration_num'] = df['duration'].str.extract('(\d+)').astype(float)
df['duration_num'] = df['duration_num'].fillna(df['duration_num'].median())

print("Missing values after cleaning:\n", df.isnull().sum())
df.to_csv('cleaned_netflix_data.csv', index=False)
print("Saved perfectly as 'cleaned_netflix_data.csv'")