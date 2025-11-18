import matplotlib.pyplot as plt
import numpy as np

def make_plot(cxs, cys, dxs, dys, output_figname):
    plt.rc('text', usetex=True)
    plt.rc('font', family='serif')
    plt.figure(figsize=(8, 6))
    plt.title(r'$f(x)=\exp\left[\left(x\sin(\alpha x)\right)^{2}\right]$', fontsize=12)
    plt.xlabel(r'$x$', fontsize=12)
    plt.ylabel(r'$f(x)$', fontsize=12)
    plt.xlim(0,10)
    #plt.ylim(-1.0,1.0)
    plt.yscale('log')
    plt.plot(cxs, cys, 'r-', label=r'$\alpha = 1$')
    plt.plot(dxs, dys, 'b-', label=r'$\alpha = 5$')
    plt.legend()
    #plt.grid(True)
    #plt.show()
    plt.savefig(output_figname)
    plt.close()

cxs = [0.01*i for i in range(1000)]
cys = [np.exp((x*np.sin(x))**2) for x in cxs]

dxs = [0.01*i for i in range(1000)]
dys = [np.exp((x*np.sin(5*x))**2) for x in dxs]

make_plot(cxs, cys, dxs, dys, "functions.pdf")