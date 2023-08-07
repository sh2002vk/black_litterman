# -*- coding: utf-8 -*-
"""
THIS FILE HANDLES GENERATING ALL COMPONENTS OF THE BL MODEL OUTSIDE OF THE VIEWS
TODO: ADD MORE COMMENTS, CHECK UNUSED CODE
"""


def get_pi(S, w, lamda, frequency=1):
    try:
        # Check if the row indices of S and w match in ascending alphabetical order
        assert all(
            S.sort_index().index == w.sort_index().index), "Row indices of S and w should match in ascending alphabetical order."
    except AssertionError as e:
        raise AssertionError(
            str(e) + " Please make sure the row indices of S and w are in ascending alphabetical order and exactly the same.")

    assert len(S) == len(w), "Number of rows in S and w should be equal."

    # Check if the sum of market cap weights is equal to 1
    # if w.sum().item() != 1:
    #     raise ValueError("Sum of all Market Cap Weight Must Equal to 1.")

    pi = S.dot(w) * lamda
    adj_factor = 252 / frequency
    pi_annalized = (1 + pi) ** (252) - 1  # annualize assuming with compounding
    # TODO: return annualized version
    return pi


def get_lambda(market_return, risk_premiums, window=1260, frequency=1):
    assert len(market_return) == len(risk_premiums), "number of entries should be equal"
    market_return = market_return.head(window * frequency)
    risk_premiums = market_return.head(window * frequency)
    market_var = market_return.var()
    expected_rp = risk_premiums.mean()
    lamda = expected_rp / market_var

    return lamda


def get_S(historical_returns_df, window=1260, frequency=1):
    historical_return_subset = historical_returns_df.head(window * frequency)
    covariance_matrix = historical_returns_df.cov()
    return covariance_matrix


def get_w(market_cap_df):

    if market_cap_df.shape[0] == 1:  # Check if the DataFrame has only one row
        market_cap_column = market_cap_df.T
    elif market_cap_df.shape[1] == 1:  # Check if the DataFrame has only one column
        market_cap_column = market_cap_df
    else:
        raise ValueError("market_cap_df must be either a row DataFrame or a column DataFrame.")

    total_cap = market_cap_column.sum(axis=0)
    market_cap_weight = market_cap_column.divide(total_cap, axis=1)
    return market_cap_weight


def get_historical_returns(historical_returns_df, rf, window=1260, frequency=1):
    historical_return_subset = historical_returns_df.head(window * frequency)
    mean = historical_return_subset.mean(axis=0) - rf
    return mean

