import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, OrdinalEncoder, MinMaxScaler, MaxAbsScaler, StandardScaler, normalize

# Load the cleaned data
df = pd.read_csv('cleaned_netflix_data.csv')

# ==========================================
# REQUIREMENT: Detecting and treating outliers
# ==========================================
print("Treating Outliers...")
Q1 = df['duration_num'].quantile(0.25)
Q3 = df['duration_num'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
# Cap the outliers at the boundaries
df['duration_capped'] = np.clip(df['duration_num'], lower_bound, upper_bound)

# ==========================================
# REQUIREMENT: Transform skewed features
# ==========================================
print("Applying Log Transformation for Skewness...")
# Log transformation normalizes the right-skewed duration data
df['duration_log'] = np.log1p(df['duration_capped'])

# ==========================================
# REQUIREMENT: Categorical Variable Handling (All 5)
# ==========================================
print("Applying Categorical Encodings...")
# 1. One-Hot Encoding
df = pd.get_dummies(df, columns=['type'], drop_first=True)
# 2. Label Encoding
df['rating_label'] = LabelEncoder().fit_transform(df['rating'].astype(str))
# 3. Ordinal Encoding 
df['rating_ordinal'] = OrdinalEncoder().fit_transform(df[['rating']].astype(str))
# 4. Frequency Encoding 
freq_encoding = df['country'].value_counts() / len(df)
df['country_freq'] = df['country'].map(freq_encoding)
# 5. Target Encoding (Using release_year as numerical target)
df['rating_target_enc'] = df['rating'].map(df.groupby('rating')['release_year'].mean())

# ==========================================
# REQUIREMENT: Feature Scaling (All 4)
# ==========================================
print("Applying Feature Scaling...")
# Applying scaling to our treated, normalized numeric column
df['duration_minmax'] = MinMaxScaler().fit_transform(df[['duration_log']])
df['duration_maxabs'] = MaxAbsScaler().fit_transform(df[['duration_log']])
df['duration_zscore'] = StandardScaler().fit_transform(df[['duration_log']])
df['duration_vector'] = normalize(df[['duration_log']], norm='l2', axis=0)

df.to_csv('final_preprocessed_data.csv', index=False)
print("Complete! Final dataset generated.")