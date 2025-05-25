import numpy as np
import matplotlib.pyplot as plt

from pricer import gamma


def gamma_2D (S=100, K=100, sigma=0.2, r=0.05, q=0.05, t=1, T=365):
    strike_prices = np.linspace(50, 150, 100) 
    time_to_expiration = np.linspace(0.01, 1, 100)      

    S_grid, T_grid = np.meshgrid(strike_prices, time_to_expiration)
    gamma_grid = np.zeros_like(S_grid)

    for i in range(S_grid.shape[0]):
        for j in range(S_grid.shape[1]):
            s = S_grid[i, j]
            t = T_grid[i, j]
            gamma_grid[i, j] = gamma(s, K, sigma, r, q, t)

    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(S_grid, T_grid, gamma_grid, cmap='viridis')
    ax.set_xlabel("Underlying Price (S)")
    ax.set_ylabel("Time to Maturity (T)")
    ax.set_zlabel("Gamma")
    ax.set_title("Gamma Surface")
    plt.show()  

gamma_2D()
