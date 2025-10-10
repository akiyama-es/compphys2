import numpy as np
import matplotlib.pyplot as plt

def plot_dat(input_filename, output_figname):
    data = np.loadtxt(input_filename)
    x, y, yerr = data[:, 0], data[:, 1], data[:, 2]
    plt.rc('text', usetex=True)
    plt.rc('font', family='serif')
    plt.figure(figsize=(8, 6))
    plt.title('Sample', fontsize=20)
    plt.xlabel(r"$x$", fontsize=20)
    plt.ylabel(r"$y$", fontsize=20)
    plt.errorbar(x, y, yerr=yerr, fmt='o', color = 'b', capsize=3)
    plt.grid(True)
    #plt.show()
    plt.savefig(output_figname)
    plt.close()

plot_dat("noisy_data.dat", "noisy_data.pdf")
