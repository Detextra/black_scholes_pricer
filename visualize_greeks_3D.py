import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from pricer import gamma, delta_call, delta_put, theta_call, theta_put, vega

def greeks_3D(S=100, K=100, sigma=0.2, r=0.05, q=0.05, T=365):
    strike_prices = np.linspace(50, 150, 100)
    time_to_expiration = np.linspace(0.01, 1, 100)

    S_grid, T_grid = np.meshgrid(strike_prices, time_to_expiration)

    # Dictionnaire des fonctions et initialisation des grilles
    greeks = {
        "Gamma": {"func": lambda s, t: gamma(s, K, sigma, r, q, t), "grid": None, "cmap": "viridis"},
        "Vega": {"func": lambda s, t: vega(s, K, sigma, r, q, t), "grid": None, "cmap": "plasma"},
        "Delta Call": {"func": lambda s, t: delta_call(s, K, sigma, r, q, t), "grid": None, "cmap": "coolwarm"},
        "Delta Put": {"func": lambda s, t: delta_put(s, K, sigma, r, q, t), "grid": None, "cmap": "coolwarm"},
        "Theta Call": {"func": lambda s, t: theta_call(s, K, sigma, r, q, t, T), "grid": None, "cmap": "cividis"},
        "Theta Put": {"func": lambda s, t: theta_put(s, K, sigma, r, q, t, T), "grid": None, "cmap": "cividis"},
    }

    # Calcul des grilles
    for greek in greeks.values():
        grid = np.zeros_like(S_grid)
        for i in range(S_grid.shape[0]):
            for j in range(S_grid.shape[1]):
                s, t = S_grid[i, j], T_grid[i, j]
                grid[i, j] = greek["func"](s, t)
        greek["grid"] = grid

    # Affichage
    fig = plt.figure(figsize=(16, 12))
    fig.suptitle("Greeks vs. Underlying Price (s) and Time to Maturity (t)", fontsize=16)

    for idx, (name, greek) in enumerate(greeks.items(), start=1):
        ax = fig.add_subplot(3, 2, idx, projection='3d')
        surf = ax.plot_surface(S_grid, T_grid, greek["grid"], cmap=greek["cmap"])
        ax.set_title(f"{name} Surface")
        ax.set_xlabel("Underlying Price (s)")
        ax.set_ylabel("Time to Maturity (t)")
        ax.set_zlabel(name)

    plt.tight_layout(rect=[0, 0, 1, 0.96])
    plt.show()

greeks_3D()
