import numpy as np
import matplotlib.pyplot as plt

def throw_darts(N):

    points = np.random.uniform(0, 1, size=(N, 2))

    data = np.zeros(N)
    data = np.linalg.norm(points, axis=1) <= 1

    inside_sphere = np.average(data)
    estimated_pi= 4 * inside_sphere
    error = 4 * np.std(data,ddof=1)/np.sqrt(N)
    return estimated_pi, error

if __name__ == "__main__":

    num_MC = 20
    N_values = np.logspace(1, 5, num=num_MC, base=10, dtype=int)  

    estimated_values = []
    estimated_errors = []

    for N in N_values:
        estimated_pi, error = throw_darts(N)
        estimated_values.append(estimated_pi)
        estimated_errors.append(error)

    plt.figure(figsize=(10, 6))
    plt.errorbar(N_values, estimated_values, yerr=estimated_errors, fmt="o", capsize=5, label="Estimation")
    plt.axhline(np.pi, color='red', linestyle='--', label="Exact")
    plt.xlabel(r'$N$', fontsize=12)
    plt.xscale('log')
    plt.legend()
    plt.grid(alpha=0.3)
    plt.savefig("estimated_pi.pdf")
