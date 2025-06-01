import unittest

from pricer import (
    black_scholes_pricer_call,
    black_scholes_pricer_put,
    d1,
    d2,
    N,
    N_prime
)

class TestBlackScholesPricer(unittest.TestCase):
    def setUp(self):
        self.S = 100
        self.K = 100
        self.sigma = 0.2
        self.r = 0.05
        self.q = 0.0
        self.t = 1

    def test_call_price(self):
        expected_call = 10.4506
        calculated = black_scholes_pricer_call(self.S, self.K, self.sigma, self.r, self.q, self.t)
        self.assertAlmostEqual(calculated, expected_call, places=4)

    def test_put_price(self):
        expected_put = 5.5735
        calculated = black_scholes_pricer_put(self.S, self.K, self.sigma, self.r, self.q, self.t)
        self.assertAlmostEqual(calculated, expected_put, places=4)

    def test_d1(self):
        expected = 0.35
        calculated = d1(self.S, self.K, self.sigma, self.r, self.q, self.t)
        self.assertAlmostEqual(calculated, expected, places=2)

    def test_d2(self):
        expected = 0.15
        calculated = d2(self.S, self.K, self.sigma, self.r, self.q, self.t)
        self.assertAlmostEqual(calculated, expected, places=2)

    def test_N(self):
        self.assertAlmostEqual(N(0), 0.5, places=5)
        self.assertAlmostEqual(N(1.96), 0.975, places=2)

    def test_N_prime(self):
        self.assertAlmostEqual(N_prime(0), 1 / (2 * 3.1415926535)**0.5, places=5)
        self.assertAlmostEqual(N_prime(1), 0.24197, places=5)

if __name__ == '__main__':
    unittest.main()