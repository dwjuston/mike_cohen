import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.stats as stats

N = 20
data = np.random.randn(N) + 0.05

plt.plot(data, "ko", markerfacecolor='w', markersize=10)
plt.show()

"""
manual t test
"""

H0_value = 0

t_num = data.mean() - H0_value
t_den = data.std(ddof=1) / np.sqrt(N)
t_val = t_num / t_den

df = N - 1
pval = 1 - stats.t.cdf(abs(t_val), df=df) # one tail

# plot t-distribution with df, and a vertical line from pval
x = np.linspace(-3, 3, 100)
plt.plot(x, stats.t.pdf(x, df=df))
plt.axvline(abs(t_val), color='red')


"""
use scipy
"""
t, p = stats.ttest_1samp(data, H0_value, alternative='greater')
# add title to show p value and t value from both manual and scipy
plt.title(f"p value: {pval:.4f}, t value: {t_val:.4f}\nscipy p value: {p:.4f}, scipy t value: {t:.4f}")
plt.show()
