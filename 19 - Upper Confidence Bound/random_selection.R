# Random Selection

# Importing the dataset
dataset = read.csv('Ads_CTR_Optimisation.csv')

# Implementing Random Selection
N = 10000
d = 10
ads_selected = integer(0)
total_reward = 0
for (n in 1:N) {
  ad = sample(1:10, 1)
  ads_selected = append(ads_selected, ad)
  #reward goes up by one if the dataset contains a 1 for that ad, otherwise it goes up by zero
  #as the cell will contain either a 1 or 0  
  reward = dataset[n, ad]
  total_reward = total_reward + reward
}

# Visualising the results
# plot shows roughly uniform distribution as algorithm not preferring any one version
hist(ads_selected,
     col = 'blue',
     main = 'Histogram of ads selections',
     xlab = 'Ads',
     ylab = 'Number of times each ad was selected')