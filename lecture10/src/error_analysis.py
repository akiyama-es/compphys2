import numpy as np
import matplotlib.pyplot as plt

sampling_points = np.linspace(0,10,10)
original_values = np.exp(-sampling_points/10)  

N = 10
data = np.zeros((len(sampling_points),N))

for i in range(N):
    random_values = np.random.normal(0, 1, len(sampling_points)) * 0.1 
    measured_values = original_values + random_values
    data[:,i] = measured_values[:]

estimated_means = np.mean(data, axis=1)
estimated_errors = np.std(data, axis=1, ddof=1) / np.sqrt(N)

x = np.linspace(0,10,10000)
true_values = np.exp(-x/10)  

plt.errorbar(sampling_points, estimated_means, yerr=estimated_errors, fmt='o', capsize=2, label='Estimation')
plt.plot(x, true_values, label='True values')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.savefig("error_analysis.pdf")
