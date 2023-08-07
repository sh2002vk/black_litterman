# The Black-Litterman Model

A mathematical approach to portfolio allocations.

## Formula

E[R] = $[\{\tau\sum}^{-1} + P'{\Omega}^{-1}P]^{-1}\times[\({\tau\sum}^{-1}\times\pi)+P'{\Omega}^{-1}Q]$

where:
𝛕 -> tau scalar
𝝅 -> Implied Equilibrium Excess Returns
∑-> Covariance Matrix of Excess Returns
Q -> View Matrix
P -> Pick Matrix for views
𝝮 -> View Confidence Matrix (P(𝛕∑)P’)
E[R] -> adjusted expected return matrix

## To Run

1. git clone the project
2. pip install numpy and pandas
3. run ```python test_model.py```

## TODO

Calculate optimal asset allocation weights with mean-variance optimization
