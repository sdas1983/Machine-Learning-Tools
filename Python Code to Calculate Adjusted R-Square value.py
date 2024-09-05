# Python Code to Calculate Adjusted R-Square value

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Load the Boston dataset from the original source
data_url = "http://lib.stat.cmu.edu/datasets/boston"
raw_df = pd.read_csv(data_url, sep="\s+", skiprows=22, header=None)

# Organize the data into feature matrix (X) and target variable (y)
data = np.hstack([raw_df.values[::2, :], raw_df.values[1::2, :2]])  # Features
target = raw_df.values[1::2, 2]  # Target (house prices)

# Convert to DataFrame for easier handling
df = pd.DataFrame(data, columns=[f"Feature_{i}" for i in range(data.shape[1])])
df['Target'] = target

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(df.drop('Target', axis=1), df['Target'], test_size=0.2, random_state=42)

# Train a linear regression model
lr = LinearRegression()
lr.fit(X_train, y_train)

# Function to calculate adjusted R-squared
def adj_r2(lr, x, y):
    r2 = lr.score(x, y)
    n = x.shape[0]  # number of observations
    p = x.shape[1]  # number of predictors
    adjusted_r2 = 1 - (1 - r2) * (n - 1) / (n - p - 1)
    return r2, adjusted_r2

# Calculate and print adjusted R-squared
value = adj_r2(lr, X_test, y_test)
print(f"R-squared: {value[0]:.4f}")
print(f"Adjusted R-squared: {value[1]:.4f}")

