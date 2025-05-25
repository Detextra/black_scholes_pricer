import math
from scipy.stats import norm

# underlying_Price is S in classical Black-Scholes formula, in currency A
# strike_price is K, in currency A
# volatility is sigma σ, in % per year
# risk_free_interest_rate is r, in % per year
# dividend_yield is q, in % per year
# time_to_expiration is t, in % of a year

def black_scholes_pricer (underlying_Price, strike_price, volatility, risk_free_interest_rate, dividend_yield, time_to_expiration):
    # usually called N(x)
    std_normal_cumu_distrib = 1 / math.sqrt(2*math.pi) 
    * 

# standard normal cumulative distribution
def N(x):
    return norm.cdf(x)

def d1(underlying_Price, strike_price, volatility, risk_free_interest_rate, dividend_yield, time_to_expiration):
    return math.log(underlying_Price/strike_price) + time_to_expiration*(risk_free_interest_rate - dividend_yield + (volatility*volatility)/2) / (volatility*math.sqrt(time_to_expiration))

def d2(underlying_Price, strike_price, volatility, risk_free_interest_rate, dividend_yield, time_to_expiration):
    d1(underlying_Price, strike_price, volatility, risk_free_interest_rate, dividend_yield, time_to_expiration) - (volatility*math.sqrt(time_to_expiration))