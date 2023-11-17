from LLN import roll_dies_multi
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

# question: what is the distribution of the sample mean?
# answer: central limit theorem

df_result = roll_dies_multi(N=1000, K=50, T=1)
# calculate the sample mean per trial per experiment; size is 1 x N
sample_means = pd.DataFrame(df_result.mean(axis=1))
# plot histogram to see distribution
# plot a vertical line at the mean in the same plot

#sample_means.hist()
#plt.axvline(sample_means.mean().values, color='red')
#plt.show()


# generate lognormal distribution
N = 1000
K = 50
df_result_lognormal = np.random.lognormal(mean=0, sigma=0.5, size=N * K)
df_result_lognormal = pd.DataFrame(df_result_lognormal)
# first plot it
df_result_lognormal.hist(bins=100)
plt.show()

# calculate the sample mean per trial per experiment; size is 1 x N
# reshape the dataframe into N x K
df_result_lognormal = df_result_lognormal.values.reshape(N, K)
sample_means_lognormal = pd.DataFrame(df_result_lognormal.mean(axis=1))
# plot histogram to see distribution of sample mean
# plot a vertical line at the mean in the same plot
sample_means_lognormal.hist(bins=100)
plt.axvline(sample_means_lognormal.mean().values, color='red')
plt.show()
