# Upper Confidence Bound

# Importing the dataset
dataset = read.csv('Ads_CTR_Optimisation.csv')

# Implementing UCB
# number of user visits to run through, N
N = 10000
# number of different adverts, d
d = 10
# record of which ad selected in which round
ads_selected = integer(0)
# initialise number_of_selections as vector of size d containing only 0s
# records number of times each advert gets selected
numbers_of_selections = integer(d)
# sum_of_rewards records number of times each advert was correctly selected
sums_of_rewards = integer(d)
#total_reward is record of how many correct selections overall
total_reward = 0

#for each round we need to compute average of each ad up to the round
#and also confidence interval of each ad so that we can use max UCB to make selection

#for each round
for (n in 1:N) {
  #initialise a variable to represent which ad is selected
  ad = 0
  #and another to record the highest UCB we're able to find (which will be the UCB of the ad to select)
  max_upper_bound = 0
  
  #for each ad
  for (i in 1:d) {
  	#compute average reward for the ad up to now
	#also compute confidence interval and add to average reward to get UCB
	#but if the ad has never been selected then give it an artificially high UCB
	#this ensures each ad gets selected at least once
    if (numbers_of_selections[i] > 0) {
      average_reward = sums_of_rewards[i] / numbers_of_selections[i]
      delta_i = sqrt(3/2 * log(n) / numbers_of_selections[i])
      upper_bound = average_reward + delta_i
    } else {
      upper_bound = 1e400
    }
	#pick the ad with the highest UCB
    if (upper_bound > max_upper_bound) {
      max_upper_bound = upper_bound
      ad = i
    }
  }
  #record that we've selected this ad in this round and update its selection count
  ads_selected = append(ads_selected, ad)
  numbers_of_selections[ad] = numbers_of_selections[ad] + 1
  
  #the chosen ad's reward count and total reward go up if the dataset has a 1, otherwise we're adding 0
  reward = dataset[n, ad]
  sums_of_rewards[ad] = sums_of_rewards[ad] + reward
  total_reward = total_reward + reward
}

# Visualising the results
# this will show which ad is most successful
hist(ads_selected,
     col = 'blue',
     main = 'Histogram of ads selections',
     xlab = 'Ads',
     ylab = 'Number of times each ad was selected')