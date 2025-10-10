import numpy as np
import matplotlib.pyplot as plt

def plot_dat(filename, xlabel="x", ylabel="y", output="plot.pdf"):
    data = np.loadtxt(filename)
    x, y, yerr = data[:, 0], data[:, 1], data[:, 2]
    plt.rc('text', usetex=True)
    plt.rc('font', family='serif')
    plt.figure(figsize=(8, 6))
    plt.title('Sample', fontsize=20)
    plt.xlabel(fr"${xlabel}$", fontsize=20)
    plt.ylabel(fr"${ylabel}$", fontsize=20)
    plt.errorbar(x, y, yerr=yerr, fmt='o', color = 'b', capsize=3)
    plt.grid(True)
    plt.savefig(output)
    plt.close()

plot_dat("sample_noisy_data1.dat", xlabel="x", ylabel="y", output="output_filename.pdf")
