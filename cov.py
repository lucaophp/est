'''Apenas teste'''
import numpy as np
from scipy.stats import pearsonr
import matplotlib.pyplot as plt

np.random.seed(1)
data1 = 20 * np.random.randn(1000) +10
data2 = data1 + (10 * np.random.randn(1000) + 50)

plt.scatter(data1, data2)
plt.show()

covariancia = np.cov(data1, data2)
print(covariancia)
print(np.std([data1, data2]))
print(np.correlate(data1, data2))
print(np.correlate(data2, data2))

corr, p = pearsonr(data1, data2)
print('Correlação Pearson: {:.2f} - p-value: {}'.format(corr, p))

x = np.array([0.2, 6.4, 3.0, 1.6])
bins = np.array([0.0, 1.0, 2.5, 4.0, 10.0])
inds = np.digitize(x, bins)
for n in range(x.size):
	print(bins[inds[n]-1], "<=", x[n], "<", bins[inds[n]])
