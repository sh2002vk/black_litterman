from data_handler import *
from bl_model import BlackLittermanModel

# GLOBAL VARIABLES
RF = 0.05
historical_returns_df = get_historical_returns()
market_cap = get_market_cap()
risk_premiums = get_risk_premiums()
market_return = get_market_return()
views = get_view_dummy()


# DRIVER CODE
model = BlackLittermanModel(
    rf=RF,
    historical_returns_df=historical_returns_df,
    market_return=market_return,
    market_cap=market_cap,
    risk_premiums=risk_premiums,
    views=views,
    tau=1
)

s, pi = model.generate_s_pi()
print("generated s and pi")
p, q = model.generate_p_q()
print("generated p and q")
o = model.generate_view_confidence(p=p, s=s)
print("generated view confidence")
r = model.generate_return(s=s, pi=pi, p=p, q=q, o=o)
print(r.shape)


