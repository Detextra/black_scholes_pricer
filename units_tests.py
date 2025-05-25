import unittest
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


class TestGreeks(unittest.TestCase):
    
    def setUp(self):
        self.S = 100      # underlying price
        self.K = 100      # strike price
        self.sigma = 0.2  # volatility
        self.r = 0.05     # risk_free_interest_rate
        self.q = 0.02     # dividend_yield
        self.t = 1        # time to expiration

        self.expected_delta_call = 0.58
        self.expected_delta_put = -0.38
        self.expected_gamma = 0.018
        self.expected_vega = 37.5
        self.expected_theta_call = -6.5 / 365
        self.expected_theta_put = -2.5 / 365
        self.expected_rho_call = 53.1
        self.expected_rho_put = -25.2

        self.tolerance = 0.01

    def test_delta(self):
        result_call = delta_call(self.S, self.K, self.sigma, self.r, self.q, self.t)
        result_put = delta_put(self.S, self.K, self.sigma, self.r, self.q, self.t)
        self.assertTrue(0 < result_call < 1, f"delta_call should be between 0 and 1, got {result_call}")
        self.assertTrue(-1 < result_put < 0, f"delta_put should be between -1 and 0, got {result_put}")

        self.assertAlmostEqual(result_call, self.expected_delta_call, delta=self.tolerance,
                               msg=f"delta_call expected approx {self.expected_delta_call} but got {result_call}")
        self.assertAlmostEqual(result_put, self.expected_delta_put, delta=self.tolerance,
                               msg=f"delta_put expected approx {self.expected_delta_put} but got {result_put}")

    def test_gamma(self):
        result = gamma(self.S, self.K, self.sigma, self.r, self.q, self.t)

        self.assertGreater(result, 0, f"Gamma should be > 0, got {result}")
        self.assertAlmostEqual(result, self.expected_gamma, delta=self.tolerance,
                               msg=f"Gamma expected approx {self.expected_gamma} but got {result}")

    def test_theta(self):
        result_call = theta_call(self.S, self.K, self.sigma, self.r, self.q, self.t, 365)
        result_put = theta_put(self.S, self.K, self.sigma, self.r, self.q, self.t, 365)

        self.assertLess(result_call, 0, f"theta_call should be < 0 for call options nearing expiry, got {result_call}")
        self.assertLess(result_put, 0, f"theta_put should be < 0 for call options nearing expiry, got {result_put}")
        self.assertAlmostEqual(result_call, self.expected_theta_call, delta=self.tolerance,
                               msg=f"theta_call expected approx {self.expected_theta_call} but got {result_call}")
        self.assertAlmostEqual(result_put, self.expected_theta_put, delta=self.tolerance,
                               msg=f"theta_put expected approx {self.expected_theta_put} but got {result_put}")

    def test_vega(self):
        result = vega(self.S, self.K, self.sigma, self.r, self.q, self.t)
        self.assertGreater(result, 0, f"Vega should be > 0, got {result}")
        # bigger tolerance for vega
        self.assertAlmostEqual(result, self.expected_vega, delta=1,
                               msg=f"Vega expected approx {self.expected_vega} but got {result}")

    def test_rho(self):
        result_call = rho_call(self.S, self.K, self.sigma, self.r, self.q, self.t)
        result_put = rho_put(self.S, self.K, self.sigma, self.r, self.q, self.t)

        self.assertGreater(result_call, 0, f"rho_call should be > 0 for call options, got {result_call}")
        self.assertGreater(result_put, 0, f"rho_put should be > 0 for call options, got {result_put}")
        self.assertAlmostEqual(result_call, self.expected_rho_call, delta=1,
                               msg=f"rho_call expected approx {self.expected_rho_call} but got {result_call}")
        self.assertAlmostEqual(result_put, self.expected_rho_put, delta=1,
                               msg=f"rho_put expected approx {self.expected_rho_put} but got {result_put}")

if __name__ == '__main__':
    unittest.main()