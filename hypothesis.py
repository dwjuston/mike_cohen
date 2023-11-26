# sample estimates distribution
# sampling variability and noise
# inferential statistics

# given distribution H_0 and H_a
# how different are they?
# = difference of centers / widths of distributions
# = signal / noise

# distribution here is of sample parameter estimates, not actual data
# h_0: null hypothesis has a formula
# h_a: just one value

# Question: how likely is the observed value to occur if H_0 is true?

# We cannot prove that H_a is true. We can only test whether
# given null hypothesis is true, how likely can we observe a value
# p value, significance threshold

# 2% means there is 2% chance that the observed value is due to chance or sampling variability

# standard distribution: P-Z combinations
# two tailed
# 68.3%: z = 1
# 95.5%: z = 2
# 99.7%: z = 3

# one tailed
# p = 0.05: z = 1.64
# p = 0.01: z = 2.32
# p = 0.001: z = 3.09

# degrees of freedom (df)
# x = {a,b,c,d}, x_bar = 5
# Question: given 5, what are a, b, c, d?
# Answer: a, b, c, d can be anything

# Question: what if I also tell you a, b, c = 1, 2, 3?
# Answer: d = 15
# It means the last value is not free to vary

# Therefore, df = 3 in this case
# one outcome variable, four samples
# any three would determine the fourth

# Another example
# If we have {a,b,c,d}, and we know population mean is 5
# what is the degree of freedom?
# Answer: 4!! The population mean does not constrain the sample values


# Why df is important?
# It determines the shape of the null hypothesis distribution
# Higher df, more power to reject H_0, more statistical power
# Helps understand experimental design

# We can make mistakes in hypothesis testing
# Type I error: tell a man he is pregnant
# Type II error: tell a woman not pregnant when she is

# To minimize statistical errors, we can reduce overlapping bettwen H_0 and H_a
# i.e. more distance (bigger effects)
# plus reduce width

# usally a parametric test has a non-parametric equivalent
# e.g. 1-sample t-test => Wilcoxon signed rank test
# e.g. Pearson correlation => Spearman correlation
# e.g. ANOVA => Kruskal-Wallis test


# If performing multiple tests on same data set, we need to adjust the p-value
# Bonferroni correction
# P(H1|H0) = 0.05
# P(H2|H0) = 0.05
# P(H3|H0) = 0.05
# P(H1 and H2 and H3 | H0) = 1 - 0.95^3 = 0.143 < 0.15 = 3 * 0.05
# Familywise Error Rata: FWE
# Hard to estimate it due to interdependence of tests
# Instead, estimate the maximum FWE
# FWD <= 1 - (1 - alpha)^m <= m * alpha
# This is a ok estimate if the number of tests not too many
# threshold = alpha / m, assuming FWE

