import math
from scipy.stats import norm

# underlying_Price is S in classical Black-Scholes formula, in currency A
# strike_price is K, in currency A
# volatility is sigma sigma, in % per year
# risk_free_interest_rate is r, in % per year
# dividend_yield is q, in % per year
# time_to_expiration is t, in % of a year

# this formula account for dividend as S is replaced by S*math.exp(-q*t) and q is used is d1

def black_scholes_pricer_call (S, K, sigma, r, q, t):
    # usually called N(x)
    return S*math.exp(-q*t)*N(d1(S, K, sigma, r, q, t))-K*math.exp(-r*t)*N(d2(S, K, sigma, r, q, t))

def black_scholes_pricer_put (S, K, sigma, r, q, t):
    # usually called N(x)
    return K * math.exp(-r*t)*N(-d2(S, K, sigma, r, q, t))-S*math.exp(-q*t)*N(-d1(S, K, sigma, r, q, t))

# standard normal cumulative distribution
def N(x):
    return norm.cdf(x)

def d1(S, K, sigma, r, q, t):
    return (math.log(S/K) + t*(r - q + (sigma**2)/2)) / (sigma*math.sqrt(t))

def d2(S, K, sigma, r, q, t):
    return d1(S, K, sigma, r, q, t) - (sigma*math.sqrt(t))

# standard normal probability density
def N_prime(d1):
    return (1/math.sqrt(2*math.pi))*math.exp( (-d1**2) /2 )

# greeks

def delta_call (S, K, sigma, r, q, t):
    return math.exp(-q*t)*N(d1(S, K, sigma, r, q, t))

def delta_put (S, K, sigma, r, q, t):
    return -math.exp(-q*t)*N(-d1(S, K, sigma, r, q, t))

def gamma (S, K, sigma, r, q, t):
    return ( math.exp(-q*t) / (S*sigma*math.sqrt(t)))*N_prime(d1(S, K, sigma, r, q, t))

#T is the number of days, 365 for a year, 252 for the trading days
# negative theta means the option will lose value as time passes
def theta_call (S, K, sigma, r, q, t, T):
    return 1/T * (-( (S*sigma*math.exp(-q*t))/(2*math.sqrt(t))*N_prime(d1(S, K, sigma, r, q, t)))
                    -r*K*math.exp(-r*t)*N(d2(S, K, sigma, r, q, t)+q*S*math.exp(-q*t)*N(d1(S, K, sigma, r, q, t))) )

def theta_put (S, K, sigma, r, q, t, T):
    return 1/T * (-( (S*sigma*math.exp(-q*t))/(2*math.sqrt(t))*N_prime(d1(S, K, sigma, r, q, t)))
                    +r*K*math.exp(-r*t)*N(-d2(S, K, sigma, r, q, t)-q*S*math.exp(-q*t)*N(-d1(S, K, sigma, r, q, t))) )

def vega (S, K, sigma, r, q, t):
    return S*math.exp(-q*t)*math.sqrt(t)*N_prime(d1(S, K, sigma, r, q, t))

def rho_call (S, K, sigma, r, q, t):
    return K * t * math.exp(-r*t)*N(d2(S, K, sigma, r, q, t))

def rho_put (S, K, sigma, r, q, t):
    return K * t * math.exp(-r*t)*N(-d2(S, K, sigma, r, q, t))