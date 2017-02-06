# Thompson Sampling Reinforcement Learning

This applies Thompson Sampling to the same example problem as was used for the Upper Confidence Bound example explained previously. Here we apply Thompson Sampling and will see whether it can give a better total reward than UCB.

The implementation is similar to the previous example since the problems are the same and both algorithms require us to make selections in rounds. Elements explained previously are not explained again.

The Thompson Sampling algorithm is:

![Image of ThompsonSampling](ThompsonSampling.gif)

Beta is a [https://en.wikipedia.org/wiki/Beta_distribution](beta distribution) defined by the two parameters. The beta distribution models the highest probability of success. 