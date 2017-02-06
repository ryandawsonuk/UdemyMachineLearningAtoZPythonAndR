# Random Selection

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Ads_CTR_Optimisation.csv')

# Implementing Random Selection
import random
N = 10000
d = 10
ads_selected = []
total_reward = 0
for n in range(0, N):
    ad = random.randrange(d)
    ads_selected.append(ad)
	#reward goes up by one if the dataset contains a 1 for that ad, otherwise it goes up by zero
	#as the cell will contain either a 1 or 0
    reward = dataset.values[n, ad]
    total_reward = total_reward + reward

# Visualising the results - Histogram
# plot shows roughly uniform distribution as algorithm not preferring any one version
plt.hist(ads_selected)
plt.title('Histogram of ads selections')
plt.xlabel('Ads')
plt.ylabel('Number of times each ad was selected')
plt.show()