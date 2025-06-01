import numpy as np
import matplotlib.pyplot as plt

import pricer
from pricer import N
from pricer import d1
from pricer import d2
from pricer import N_prime
from pricer import delta_call
from pricer import delta_put
from pricer import gamma
from pricer import theta_call
from pricer import theta_put
from pricer import vega
from pricer import rho_call
from pricer import rho_put


# for delta gamma theta and vega
def greek_vs_underlying_price(K=100, sigma=0.2, r=0.05, q=0.05, t=1, T=365):

    rng = np.random.default_rng()
    strike_prices = np.sort(rng.uniform(0,K*2,500))
    #strike_prices = np.random.uniform(low=0, high=K*10, size=(500,))

    deltas_call = []
    deltas_put = []
    gammas = []
    thetas_call = []
    thetas_put = []
    vegas = []
    rhos_call = []
    rhos_put = []
    for s in strike_prices:
        deltas_call.append(delta_call(s, K, sigma, r, q, t))
        deltas_put.append(delta_put(s, K, sigma, r, q, t))
        gammas.append(gamma(s, K, sigma, r, q, t))
        thetas_call.append(theta_call(s, K, sigma, r, q, t, T))
        thetas_put.append(theta_put(s, K, sigma, r, q, t, T))
        vegas.append(vega(s, K, sigma, r, q, t))
        rhos_call.append(rho_call(s, K, sigma, r, q, t))
        rhos_put.append(rho_put(s, K, sigma, r, q, t))

    fig, axs = plt.subplots(3, 2, figsize=(14, 10))
    fig.suptitle("Greeks vs. Underlying Price (S)", fontsize=16)

    axs[0, 0].plot(strike_prices, deltas_call, label="Delta Call")
    axs[0, 0].plot(strike_prices, deltas_put, label="Delta Put")
    axs[0, 0].set_title("Delta")
    axs[0, 0].legend()
    axs[0, 0].grid(True)

    axs[0, 1].plot(strike_prices, gammas, color="orange", label="Gamma")
    axs[0, 1].set_title("Gamma")
    axs[0, 1].legend()
    axs[0, 1].grid(True)

    axs[1, 0].plot(strike_prices, thetas_call, label="Theta Call")
    axs[1, 0].plot(strike_prices, thetas_put, label="Theta Put")
    axs[1, 0].set_title("Theta")
    axs[1, 0].legend()
    axs[1, 0].grid(True)

    axs[1, 1].plot(strike_prices, vegas, color="green", label="Vega")
    axs[1, 1].set_title("Vega")
    axs[1, 1].legend()
    axs[1, 1].grid(True)

    axs[2, 0].plot(strike_prices, rhos_call, label="Rho Call")
    axs[2, 0].plot(strike_prices, rhos_put, label="Rho Put")
    axs[2, 0].set_title("Rho")
    axs[2, 0].legend()
    axs[2, 0].grid(True)

    axs[2, 1].axis("off")

    for ax in axs.flat:
        ax.set(xlabel="Underlying Price (S)", ylabel="Value")

    plt.tight_layout(rect=[0, 0, 1, 0.96])
    plt.show()

    # todo 2. Volatility 
    # vary strike price
    # smile implied volatility vs moneyness

    
greek_vs_underlying_price()