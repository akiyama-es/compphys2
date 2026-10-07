import numpy as np


def make_noisy_data(output_filename, x, func, error_func):

    y_true = func(x)
    y_err = error_func(x)
    y_noisy = y_true + np.random.normal(0, y_err)

    data_to_save = np.column_stack((x, y_noisy, y_err))

    np.savetxt(output_filename, data_to_save,
               fmt="%.8f", comments="")


# ========================================
# Data 1: Gaussian
# ========================================

alpha = 0.1
normalization = np.sqrt(np.pi / alpha)

def func1(x):
    return np.exp(-alpha * x**2) / normalization

def error_func1(x):
    base_sigma = 0.002
    return base_sigma * (1 + 0.5 * np.abs(x))

x1 = np.linspace(-10, 10, 50)

make_noisy_data("noisy_data1.dat", x1, func1, error_func1)


# ========================================
# Data 2: Sine
# ========================================

def func2(x):
    return np.sin(x)

def error_func2(x):
    return 0.1 * np.ones_like(x)

x2 = np.linspace(0, 2 * np.pi, 50)

make_noisy_data("noisy_data2.dat", x2, func2, error_func2)


# ========================================
# Data 3: Exponential 
# ========================================

def func3(x):
    return np.exp(-0.5 * x)

def error_func3(x):
    return 0.02 * (1 + 0.2 * x)

x3 = np.linspace(0, 10, 50)

make_noisy_data("noisy_data3.dat", x3, func3, error_func3)