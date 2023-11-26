import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.stats as stats

n1 = 30
n2 = 40
mu1 = 1    # population mean of group 1
mu2 = 1.5  # population mean of group 2

# generate data
data1 = np.random.randn(n1) + mu1
data2 = np.random.randn(n2) + mu2

# plot data
plt.plot(data1, "ko", markerfacecolor='w', markersize=10)
plt.plot(data2, "ro", markerfacecolor='w', markersize=10)

# two sample t test
t, p = stats.ttest_ind(data1, data2, equal_var=True)
df = n1 + n2 - 2
# add a title
plt.title(f"t value: {t:.4f}, p value: {p:.4f}")
plt.show()
