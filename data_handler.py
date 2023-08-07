import numpy as np
import pandas as pd

"""
THIS FILES CONTAINS A TEMPORARY METHOD FOR GENERATING TO DATA TO TEST THE MODEL
WILL BE REFACTORED TO PULL FROM DATABASE ONCE THE DATABASE IS COMPLETED
"""

# ----------------------------------------------------Retrieved Data--------------------------------------------

# risk premiums
risk_premiums_path = r"risk_premiums.csv"  # this need to be adjusted
risk_premiums_df_raw = pd.read_csv(risk_premiums_path, index_col=0)
risk_premiums_df = risk_premiums_df_raw.loc[:202304]
risk_premiums_df["market_return"] = risk_premiums_df["Mkt-RF"] + risk_premiums_df["RF"]
market_return = risk_premiums_df["market_return"]
risk_premiums = risk_premiums_df["Mkt-RF"]

# real stock data
# stock_data_path = r"C:\School\UBC_Tading Group\CRSP_stocks_clean.csv "  # this need to be adjusted. This is currently not used.
# real_stock_df = pd.read_csv(stock_data_path, index_col=0)
# pivot_df = real_stock_df.pivot_table(index='date', columns='TICKER', values='RET', aggfunc='mean')
# pivot_df.sort_values(by='date', ascending=False, inplace=True)

# ------------------------------------------------Simulated Data -------------------------------------------
# simulate a dataframe of random returns
start_date = '2008-06-01'
end_date = '2023-06-01'
dates = pd.date_range(start=start_date, end=end_date, freq='D')
dates = dates[::-1]
num_columns = 200
stock_data = np.random.uniform(low=-1, high=1, size=(len(dates), num_columns))
historical_returns_df = pd.DataFrame(stock_data, index=dates, columns=[f"Stock {i}" for i in range(1, num_columns + 1)])

# simulate a dataframe of random market cap

market_cap_simulated = np.random.uniform(low=50_000_000, high=200_000_000_000, size=num_columns)
market_cap_df = pd.DataFrame([market_cap_simulated], columns=[f"Stock {i}" for i in range(1, num_columns + 1)])

# Simulate Betas

n_stocks = 200
beta_values = np.random.uniform(low=-1, high=1, size=n_stocks)
# Create the beta DataFrame
beta = pd.DataFrame({'Beta': beta_values}, index=[f"Stock {i}" for i in range(1, n_stocks + 1)])
# ------------------------------------------------Simulated Data -------------------------------------------
# simulate a dataframe of random returns
start_date = '2008-06-01'
end_date = '2023-06-01'
dates = pd.date_range(start=start_date, end=end_date, freq='D')
num_columns = 200
stock_data = np.random.uniform(low=-1, high=1, size=(len(dates), num_columns))
historical_returns_df = pd.DataFrame(stock_data, index=dates, columns=[f"Stock {i}" for i in range(1, num_columns + 1)])

# simulate a data-frame of random market cap

market_cap_simulated = np.random.uniform(low=50_000_000, high=200_000_000_000, size=num_columns)
market_cap_df = pd.DataFrame([market_cap_simulated], columns=[f"Stock {i}" for i in range(1, num_columns + 1)])

view_dummy = np.random.uniform(0, 1, size=(200, 1))


def get_historical_returns():
    return historical_returns_df


def get_market_return():
    return market_return


def get_risk_premiums():
    return risk_premiums


def get_market_cap():
    return market_cap_df

def get_view_dummy():
    return view_dummy

