import math
from scipy.stats import norm

# underlying_Price is S in classical Black-Scholes formula, in currency A
# strike_price is K, in currency A
# volatility is sigma σ, in % per year
# risk_free_interest_rate is r, in % per year
# dividend_yield is q, in % per year
# time_to_expiration is t, in % of a year

# this formula account for dividend as S is replaced by S*math.e(-q*t) and q is used is d1

def black_scholes_pricer_call (S, K, σ, r, q, t):
    # usually called N(x)
    C = S*math.e(-q*t)*N(d1(S, K, σ, r, q, t))-K*math.e(-r*t)*N(d2(S, K, σ, r, q, t))

def black_scholes_pricer_put (S, K, σ, r, q, t):
    # usually called N(x)
    P = K * math.e(-r*t)*N(-d2(S, K, σ, r, q, t))-S*math.e(-q*t)*N(-d1(S, K, σ, r, q, t))

# standard normal cumulative distribution
def N(x):
    return norm.cdf(x)

def d1(S, K, σ, r, q, t):
    return (math.log(S/K) + t*(r - q + (σ**2)/2)) / (σ*math.sqrt(t))

def d2(S, K, σ, r, q, t):
    return d1(S, K, σ, r, q, t) - (σ*math.sqrt(t))

# standard normal probability density
def N_prime(S, K, σ, r, q, t):
    return (1/math.sqrt(2*math.pi))*math.e( (-d1(S, K, σ, r, q, t)**2) /2 )

# greeks

def delta_call (S, K, σ, r, q, t):
    return math.e(-q*t)*N(d1(S, K, σ, r, q, t))

def delta_put (S, K, σ, r, q, t):
    return math.e(-q*t)*(N(d1(S, K, σ, r, q, t))-1)

def gamma (S, K, σ, r, q, t):
    return ( math.e(-q*t) / S*σ*math.sqrt(t))*N_prime(d1(S, K, σ, r, q, t))

#T is the number of days, 365 for a year, 252 for the trading days
# negative theta means the option will lose value as time passes
def theta_call (S, K, σ, r, q, t, T):
    return 1/T * (-( (S*σ*math.e(-q*t))/(2*math.sqrt(t))*N_prime(d1(S, K, σ, r, q, t)))
                    -r*K*math.e(-r*t)*N(d2(S, K, σ, r, q, t)+q*S*math.e(-q*t)*N(d1(S, K, σ, r, q, t))) )

def theta_put (S, K, σ, r, q, t, T):
    return 1/T * (-( (S*σ*math.e(-q*t))/(2*math.sqrt(t))*N_prime(d1(S, K, σ, r, q, t)))
                    +r*K*math.e(-r*t)*N(-d2(S, K, σ, r, q, t)-q*S*math.e(-q*t)*N(-d1(S, K, σ, r, q, t))) )

def vega (S, K, σ, r, q, t, T):
    return 1/100*S*math.e(-q*t)*math.sqrt(t)*N_prime(d1(S, K, σ, r, q, t))

def rho_call (S, K, σ, r, q, t, T):
    return 1/100 * K * t * math.e(-r*t)*N(d2(S, K, σ, r, q, t))

def rho_call (S, K, σ, r, q, t, T):
    return 1/100 * K * t * math.e(-r*t)*N(-d2(S, K, σ, r, q, t))