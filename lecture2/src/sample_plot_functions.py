import matplotlib.pyplot as plt
import numpy as np

def make_plot(cxs, cys, dxs, dys):
    plt.rc('text', usetex=True)
    plt.rc('font', family='serif')
    plt.figure(figsize=(8, 6))
    plt.title('Sample', fontsize=20)
    plt.xlabel(r'$x$', fontsize=20)
    plt.ylabel(r'$f(x)$', fontsize=20)
    #plt.xlim(0,2.0*np.pi)
    #plt.ylim(-1.0,1.0)
    plt.plot(cxs, cys, 'r-', label='function A')
    plt.plot(dxs, dys, 'b--', label='function B')
    plt.legend()
    #plt.grid(True)
    #plt.show()
    plt.savefig("output_make_plot.pdf")
    plt.close()

cxs = [0.1*i for i in range(100)]
cys = [np.sin(x) for x in cxs]

dxs = [0.1*i for i in range(100)]
dys = [np.cos(x) for x in dxs]

make_plot(cxs, cys, dxs, dys)