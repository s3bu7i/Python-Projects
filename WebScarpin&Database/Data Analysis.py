import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load dataset
dataset = pd.read_csv('data.csv')

# Perform statistical calculations
mean = np.mean(dataset['price'])
median = np.median(dataset['price'])
std_dev = np.std(dataset['price'])

# Generate visualizations
plt.figure(figsize=(8, 6))
plt.hist(dataset['price'], bins=10)
plt.xlabel('Price')
plt.ylabel('Count')
plt.title('Distribution of Prices')
plt.show()

print('Mean:', mean)
print('Median:', median)
print('Standard Deviation:', std_dev)
