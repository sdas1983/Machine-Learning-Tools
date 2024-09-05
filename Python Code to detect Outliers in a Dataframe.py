# Python Code to detect Outliers in a Dataframe
import numpy as np
import pandas as pd

# Example DataFrame
data = {
    'col1': [10, 12, 14, 15, 16, 17, 100],  # Outlier at 100
    'col2': [20, 21, 22, 23, 24, 25, -50]   # Outlier at -50
}

df = pd.DataFrame(data)

# Define the columns to detect outliers
cols = ['col1', 'col2']

# Detect and Replace Outliers Function
def detect_outliers(data, cols, method):
    for x in cols:
        q75, q25 = np.percentile(data[x], [75, 25])
        intr_qr = q75 - q25
        max_val = q75 + (1.5 * intr_qr)
        min_val = q25 - (1.5 * intr_qr)

        # Determine replacement value based on the method
        if method == 'mean':
            replacement_value = data[x].mean()
        elif method == 'median':
            replacement_value = data[x].median()
        elif method == 'nan':
            replacement_value = np.nan
        else:
            raise ValueError("Method must be 'mean', 'median', or 'nan'")

        # Replace outliers with the determined value
        data.loc[data[x] < min_val, x] = replacement_value
        data.loc[data[x] > max_val, x] = replacement_value

# Apply the function to detect and replace outliers (choose method: 'mean', 'median', or 'nan')
detect_outliers(df, cols, method='mean')  # or 'median' or 'nan'

print(df)
