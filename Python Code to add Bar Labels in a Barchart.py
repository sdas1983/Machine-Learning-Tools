# Python Code to add Bar Labels in a Barchart
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Create a dummy DataFrame for a clustered bar chart
df = pd.DataFrame({
    'Team': ['Team A', 'Team A', 'Team A', 'Team B', 'Team B', 'Team B', 'Team C', 'Team C', 'Team C'],
    'Outcome': ['Win', 'Loss', 'Draw', 'Win', 'Loss', 'Draw', 'Win', 'Loss', 'Draw'],
    'Count': [5, 3, 2, 6, 4, 1, 7, 5, 3]
})

# Create a clustered bar chart using seaborn
plt.figure(figsize=(10, 7))  # Set the figure size
ax = sns.barplot(data=df, x='Team', y='Count', hue='Outcome', palette='Set2')

# Add bar labels to each bar in the chart
for bars in ax.containers:
    ax.bar_label(bars)

# Set the title of the chart
plt.title('Clustered Bar Chart of Outcomes by Team')

# Display the chart
plt.show()
