from market_handler import get_historical_returns, get_lambda, get_S, get_w, get_pi
import numpy as np
import math


class BlackLittermanModel:

    def __init__(self, rf, historical_returns_df, market_return, risk_premiums, market_cap, views, tau):
        self.rf = rf
        self.historical_returns_df = historical_returns_df
        self.market_return = market_return
        self.risk_premiums = risk_premiums
        self.market_cap = market_cap
        self.views = views
        self.tau = tau

    def generate_s_pi(self):
        historical_excess = get_historical_returns(self.historical_returns_df, self.rf)
        lambda_ = get_lambda(self.market_return, self.risk_premiums)
        S = get_S(self.historical_returns_df)
        w = get_w(self.market_cap)
        pi = get_pi(S, w, lambda_)
        return S, pi

    def generate_p_q(self):
        """ Builds view and pick matrix from column vector of views

        :return: pick and view matrix suitable for BL implementation
        p -> KxN matrix
        q -> Nx1 matrix
        """
        p = []  # assets involved
        q = []  # view itself
        count = 0
        for i in range(len(self.views)):
            for x in range(len(self.views)):
                # No duplicates or negative differences
                if i == x or self.views[i][0] - self.views[x][0] <= 0:
                    continue
                difference = self.views[i][0] - self.views[x][0]
                q.append(difference)
                new_row = np.zeros(len(self.views))  # each index in view corresponds to an asset
                new_row[i] = 1
                new_row[x] = -1
                p.append(new_row)

        return np.array(p), np.array(q)

    def generate_view_confidence(self, p, s):
        tau_s = s*self.tau
        transposed_p = p.T
        comb = p.dot(tau_s)
        omega = comb.dot(transposed_p)
        return omega

    def generate_return(self, s, pi, p, q, o):
        try:
            inv_omega = np.linalg.inv(o)
            tau_s = self.tau*s
            inv_s = np.linalg.inv(tau_s)
            p1 = inv_s + (p.T.dot(inv_omega).dot(p))
            p1_inv = np.linalg.inv(p1)
            p2 = inv_s.dot(pi) + (p.T.dot(inv_omega).dot(q))
            output = p1_inv.dot(p2)
            return output
        except Exception as e:
            print(f"matrix operation errors: {e}")
