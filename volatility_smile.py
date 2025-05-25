import pricer
import numpy as np
from pricer import black_scholes_pricer_call
from pricer import black_scholes_pricer_put

def volatility_smile (S=100, K=100, r=0.05, q=0.05, t=1, T=365):
    rng = np.random.default_rng()
    strike_prices = np.sort(rng.uniform(0,K*2,500))

    realistic_volatility = 0.2
    call_price = black_scholes_pricer_call(S, K, realistic_volatility, r, q, t)

