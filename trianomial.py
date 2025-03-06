# Helambe Vaibhav

import numpy as np

def TrinomialTreeOption(AmeEurFlag, CallPutFlag, S, X, Time, r, b, sigma, n):
    # initialize the option value
    OptionValue = np.zeros(2*n+1)
    # set the sign of the option value
    if CallPutFlag == "c":
        z = 1
    if CallPutFlag == "p":
        z = -1
    # calculate the parameters
    dt = Time/n
    u = np.exp(sigma * np.sqrt(2*dt))
    d = np.exp(-sigma * np.sqrt(2*dt))
    # calculate the probabilities
    pu = ((np.exp(b * dt/2) - np.exp(-sigma * np.sqrt(dt/2))) /
          (np.exp(sigma * np.sqrt(dt/2)) - np.exp(-sigma * np.sqrt(dt/2)))) ** 2
    pd = ((np.exp(sigma * np.sqrt(dt/2)) - np.exp(b * dt/2)) /
          (np.exp(sigma * np.sqrt(dt/2)) - np.exp(-sigma * np.sqrt(dt/2)))) ** 2
    pm = 1 - pu - pd
    # calculate the discount factor
    Df = np.exp(-r*dt)
    # calculate the option value
    for i in range(0, 2*n+1):
        OptionValue[i] = max(0, z*(S*u**(max(i-n, 0)) *
                                   d**(max(n*2-n-i, 0)) - X))
    # backward induction
    for j in range(n-1, -1, -1):
        for i in range(0, j*2+1):
            if AmeEurFlag == "e":
                OptionValue[i] = (pu * OptionValue[i+2] +
                                  pm * OptionValue[i+1] +
                                  pd * OptionValue[i]) * Df
            if AmeEurFlag == "a":
                OptionValue[i] = max(z*(S*u**(max(i-j, 0)) *
                                        d**(max(j*2-j-i, 0)) - X), (pu * OptionValue[i+2] +
                                                                    pm * OptionValue[i+1] +
                                                                    pd * OptionValue[i]) * Df)
    # return the option value
    TrinomialTree = OptionValue[0]
    return TrinomialTree, u, d, pu, pd, pm

# Example:
AmeEurFlag = "a"    # get the flag for American or European option
CallPutFlag = "c"   # get the flag for call or put option
S = 100             # get the current stock price
X = 100             # get the strike price
Time = 3            # get the time to maturity in years
r = 0.03            # get the risk-free interest rate
b = -0.04           # get the cost of carry
sigma = 0.2         # get the volatility
n = 9               # get the number of steps

output = TrinomialTreeOption(AmeEurFlag, CallPutFlag, S, X, Time, r, b, sigma, n)
print('The option value is: ', output[0])
print('The up factor is: ', output[1])
print('The down factor is: ', output[2])
print('The up probability is: ', output[3])
print('The down probability is: ', output[4])
print('The middle probability is: ', output[5])
