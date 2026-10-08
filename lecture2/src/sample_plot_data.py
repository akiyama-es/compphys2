import matplotlib.pyplot as plt
import numpy as np

def plot_dat(input_filename, output_figname):
    data = np.loadtxt(input_filename)
    x, y = data[:, 0], data[:, 1]
    plt.figure(figsize=(8, 6))
    plt.title(f"Visualization of {input_filename}", fontsize=20)
    plt.xlabel("x", fontsize=20)
    plt.ylabel("y", fontsize=20)
    plt.plot(x, y, "o-")
    #plt.errorbar(x, y, yerr=yerr, fmt="o", color = "b", capsize=3)
    plt.grid(True)
    plt.savefig(output_figname)
    plt.close()

plot_dat("input.dat", "output.pdf")

