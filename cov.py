'''Apenas teste'''
import numpy as np
from scipy.stats import pearsonr
import matplotlib.pyplot as plt

data1 = 20 * np.random.randn(1000) +10
data2 = data1 + (10 * np.random.randn(1000) + 50)

plt.scatter(data1, data2)
plt.show()

covariancia = np.cov(data1, data2)
print(covariancia)

corr, p = pearsonr(data1, data2)
print('Correlação Pearson: {:.2f} - p-value: {}'.format(corr, p))
