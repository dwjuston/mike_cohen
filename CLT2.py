# CLT has another aspect: random linear mixture of signals that have non Gaussian distributions
# will tend towards a combined signal that tends towards a Gaussian distribution.

import numpy as np

# First distribution: pure sine wave
x = np.linspace(0, 6 * np.pi, 10001)
y1 = np.sin(x)

# Second distribution: uniform distribution noise
# Pay attention to the scale: the magnitude should be similar to the sine wave y range (-1, 1)
y2 = np.random.uniform(-1, 1, 10001)

# Plot 3 things separately and horizontally: pure sine wave, uniform distribution noise, and their sum
# plot corresponding distributions
# ultimately 2 rows and 3 columns for 6 plots
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')

fig, ax = plt.subplots(2, 3, figsize=(12, 8))
# plot pure sine wave
ax[0, 0].plot(x, y1)
ax[0, 0].set_title('pure sine wave')
# plot uniform distribution noise
ax[0, 1].hist(y2, bins=100)
ax[0, 1].set_title('uniform distribution noise')
# plot the sum of the two
ax[0, 2].plot(x, y1 + y2)
ax[0, 2].set_title('sum of the two')
# plot pure sine wave distribution
ax[1, 0].hist(y1, bins=100)
ax[1, 0].set_title('pure sine wave distribution')
# plot uniform distribution noise
ax[1, 1].hist(y2, bins=100)
ax[1, 1].set_title('uniform distribution noise')
# plot the sum of the two
ax[1, 2].hist(y1 + y2, bins=100)
ax[1, 2].set_title('sum of the two')
plt.show()
