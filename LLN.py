# roll a die 50 times, record the average
# repeat 1000 times, plot the distribution of averages

import numpy as np
import pandas as pd

# support plotting in pycharm
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')

def roll_dies(N: int, K: int):
    # use numpy to generate a matrix which is N x K
    # N rows: N experiments
    # K columns: K rolls
    # each element is a random integer between 1 and 6
    # return the matrix
    return pd.DataFrame(np.random.randint(1, 7, (N, K)))

def roll_dies_multi(N: int, K: int, T: int) -> np.ndarray:
    # use numpy to generate a matrix which is N x K x T
    # N rows: N experiments
    # K columns: K rolls
    # T layers: T trials
    # each element is a random integer between 1 and 6
    # return the matrix

    # create a 1-d array of size N x K x T and convert into N x K x T matrix
    simulated_result = np.random.randint(1, 7, (N * K * T, 1)).reshape(N, K, T)
    return simulated_result

# repeat the above simulation for T times
# define a function first
# output a dataframe of size N x T
def simulate(N: int, K: int, T: int)->pd.DataFrame:
    result = roll_dies_multi(N, K, T)
    # calculate sample mean per trial per experiment, output a matrix of size N x T
    sample_means = pd.DataFrame(result.mean(axis=1))
    # calculate the expanding mean for each row i.e. output a dataframe of size N x T
    expanding_mean = sample_means.expanding().mean()
    return expanding_mean

# test run
if __name__ == '__main__':

    # test run
    T = 20
    result = simulate(N=1000, K=50, T=T)
    # plot
    plt.plot(result)
    plt.show()

