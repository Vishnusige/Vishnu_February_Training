# Assignment 3: Data Preprocessing Pipeline

## Mandatory Conclusion & Justification

* **Missing Value Handling:** The Mode (most frequent value) was used for categorical features like `country` and `rating` to preserve the natural distribution of the dataset without deleting valuable rows. Unknown text imputation was used for `director` to retain the records.
* **Categorical Encoding:** * *One-Hot Encoding* was best for `type` due to its low cardinality (only Movies/TV Shows). 
  * *Frequency Encoding* was highly effective for `country` to handle its massive cardinality without creating hundreds of sparse columns.
* **Feature Scaling:** *Z-score (Standardization)* was the most effective method because it centered our log-transformed duration data around a mean of zero, which is optimal for most downstream machine learning models.
* **Outliers and Skewness:** I detected outliers in `duration` using the IQR method and treated them using Capping (np.clip) to prevent extreme values from distorting the scales. Because the data was right-skewed, a *Log Transformation* (`np.log1p`) was applied prior to scaling to normalize the distribution.