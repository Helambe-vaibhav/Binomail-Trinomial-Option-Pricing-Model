#CRR MODEL VALUE
import numpy as np
def CRR(n, S, K, r,v,q,t,l,PutCall,OpStyle):
    At = t/(n) #time step
    u = np.exp(v*np.sqrt(At)) #up factor
    d = 1/u #down factor
    p = (np.exp((r-q)*At)-d) / (u-d)

    #Binomial price tree

    stockvalue = np.zeros((n+1,n+1)) #stock price tree
    stockvalue[0,0] = S #initial stock price
    for i in range(1,n+1):
        stockvalue[i,0] = stockvalue[i-1,0]*u #up movement
        #print(stockvalue[i,0])
        for j in range(1,i+1):
            stockvalue[i,j] = stockvalue[i-1,j-1]*d #down movement
            #print(stockvalue[i,j])

    #option value at final node
    optionvalue = np.zeros((n+1,n+1)) #option price tree
    for j in range(n+1):
        if PutCall=="C": # Call
            optionvalue[n,j] = max(0, stockvalue[n,j]-K) #payoff at maturity
            #print(optionvalue[n,j])
        elif PutCall=="P": #Put
            optionvalue[n,j] = max(0, K-stockvalue[n,j]) #payoff at maturity
            #print(optionvalue[n,j])

    #backward calculation for option price
    for i in range(n-1,-1,-1):
        for j in range(i+1):
            if OpStyle == 'B': #Bermudan option
                if i==l:
                    optionvalue[i,j] =  np.exp(-r*At)*(p*optionvalue[i+1,j]+(1-p)*optionvalue[i+1,j+1])
                else:
                    if PutCall=="P":
                        optionvalue[i,j] = max(0, K-stockvalue[i,j], np.exp(-r*At)*(p*optionvalue[i+1,j]+(1-p)*optionvalue[i+1,j+1]))
                    elif PutCall=="C":
                        optionvalue[i,j] = max(0, stockvalue[i,j]-K, np.exp(-r*At)*(p*optionvalue[i+1,j]+(1-p)*optionvalue[i+1,j+1]))
                #print(optionvalue[i,j])
            elif OpStyle== 'E': #European option
                optionvalue[i,j] =  np.exp(-r*At)*(p*optionvalue[i+1,j]+(1-p)*optionvalue[i+1,j+1])
            else: #American option
                if PutCall=="P":
                    optionvalue[i,j] = max(0, K-stockvalue[i,j], np.exp(-r*At)*(p*optionvalue[i+1,j]+(1-p)*optionvalue[i+1,j+1]))
                elif PutCall=="C":
                    optionvalue[i,j] = max(0, stockvalue[i,j]-K, np.exp(-r*At)*(p*optionvalue[i+1,j]+(1-p)*optionvalue[i+1,j+1]))
                #print(optionvalue[i,j])
    return optionvalue[0,0]

# Inputs
n =1000 #number of steps
S = 100 #initial underlying asset price
r =0.03 #risk-free interest rate
q =0.07 #dividend yield
l = 500 #exercise date
K = 100 #strike price
v =0.20 #volatility
t = 3. #time to maturity in years


Eur_call_result = CRR(n, S, K, r, v, q,t,l, PutCall="C",OpStyle='E')
American_call_result = CRR(n, S, K, r, v, q,t,l, PutCall="C",OpStyle='A')
Bermudan_call_result = CRR(n, S, K, r, v, q,t,l, PutCall="C",OpStyle='B')


Eur_put_result = CRR(n, S, K, r, v, q,t,l, PutCall="P",OpStyle='E')
American_put_result = CRR(n, S, K, r, v, q,t,l, PutCall="P",OpStyle='A')
Bermudan_put_result = CRR(n, S, K, r, v, q,t,l, PutCall="P",OpStyle='B')


#Print the output of the results
print('The price of the European call option is equal to ' +str(Eur_call_result))
print('The price of the American call option is equal to ' +str(American_call_result))
print('The price of the Bermudan call option is equal to ' +str(Bermudan_call_result))

print('The price of the European put option is equal to ' +str(Eur_put_result))
print('The price of the American put option is equal to ' +str(American_put_result))
print('The price of the Bermudan put option is equal to ' +str(Bermudan_put_result))