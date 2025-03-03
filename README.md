# 📈 Precision Pricing: Binomial & Trinomial Option Models

## Overview

This repository provides a comprehensive implementation of **options pricing** using the **Binomial** and **Trinomial tree models**. These models are fundamental tools in quantitative finance for estimating the fair value of options by simulating asset price movements over time.

### Why These Models?

- The Binomial Model assumes an asset price can move up or down in each time step, forming a discrete-time binomial tree.
- The **Trinomial model** extends this concept by incorporating a middle state, improving accuracy and stability.

Both models allow pricing for **European, American, and Bermudan options** while considering factors like volatility, risk-free rate, and dividends.

---

## 📊 Binomial Tree Model

### 🔬 Model Description

The **Binomial Option Pricing Model (CRR Model)** assumes that an asset price can either increase (**up factor, u**) or decrease (**down factor, d**) at each time step. The option price is determined using a **backward induction approach**.

**Key Formulas:**

- Upward Factor: \(u = e^{\sigma \sqrt{\Delta t}}\)
- Downward Factor: \(d = \frac{1}{u}\)
- Risk-Neutral Probability: \(p = \frac{e^{(r - q) \Delta t} - d}{u - d}\)
- Option Value at Each Node: \(V = e^{-r \Delta t} (p V_{up} + (1 - p) V_{down})\)
-
The **Binomial Option Pricing Model** follows a **recombining tree structure**:

1. **Define Time Steps:** The option's time to maturity is divided into small intervals.
2. **Calculate Up and Down Factors:** The asset price moves up (**u**) or down (**d**) at each step.
3. **Compute Option Payoffs:** Start at the final step and work **backward through the tree**.
4. **Discount Future Payoffs:** Use the **risk-free rate** to determine the present value of future payoffs.

### 📊 Implementation

We implemented the **Cox-Ross-Rubinstein (CRR)** binomial model with support for **European, American, and Bermudan** options.

```python
# Example Usage for Binomial Model
Eur_call_result = CRR(n=1000, S=100, K=100, r=0.03, v=0.20, q=0.07, t=3, l=500, PutCall="C", OpStyle='E')
print(f"European Call Option Price: {Eur_call_result}")
```

🔹 **Strengths:**

- Intuitive and easy to implement.
- Provides stepwise control over price movements.
- Useful for pricing **American options** (which can be exercised before expiry).

🔹 **Limitations:**

- Can become computationally expensive for a large number of steps.

---

## 📊 Trinomial Tree Model

### 🔬 Model Description

The **Trinomial Option Pricing Model** extends the binomial approach by introducing an additional state (**middle movement**), making it more accurate for **longer-dated options** and highly volatile markets.

📌 **Why use the Trinomial Model?**

- More **accurate approximation** of continuous-time models like **Black-Scholes**.
- Provides better handling of **high volatility scenarios**.
- Converges faster than the Binomial model for **longer expiration periods**.

**Key Formulas:**

- Upward Factor: \(u = e^{\sigma \sqrt{2\Delta t}}\)
- Downward Factor: \(d = e^{-\sigma \sqrt{2\Delta t}}\)
- Risk-Neutral Probabilities:
  - \(p_u = \left( \frac{e^{(b \Delta t /2)} - e^{-\sigma \sqrt{\Delta t/2}}}{e^{\sigma \sqrt{\Delta t/2}} - e^{-\sigma \sqrt{\Delta t/2}}} \right)^2\)
  - \(p_d = \left( \frac{e^{\sigma \sqrt{\Delta t/2}} - e^{(b \Delta t /2)}}{e^{\sigma \sqrt{\Delta t/2}} - e^{-\sigma \sqrt{\Delta t/2}}} \right)^2\)
  - \(p_m = 1 - p_u - p_d\)

### 📊 Implementation

The **Trinomial Model** supports both **American and European** options.

```python
# Example Usage for Trinomial Model
option_price, u, d, pu, pd, pm = TrinomialTreeOption(AmeEurFlag="a", CallPutFlag="c", S=100, X=100, Time=3, r=0.03, b=-0.04, sigma=0.2, n=9)
print(f"Trinomial American Call Option Price: {option_price}")
```

---

## 🌟 Comparison: Binomial vs. Trinomial Models

| Feature          | Binomial Model     | Trinomial Model                    |
| ---------------- | ------------------ | ---------------------------------- |
| Price Movements  | Up, Down           | Up, Down, Middle                   |
| Accuracy         | Moderate           | Higher                             |
| Computation Time | Faster             | Slightly Slower                    |
| Use Case         | Short-term options | Long-term options, high volatility |

---


## 📊 Conclusion

The **Binomial and Trinomial models** are powerful tools for pricing **options and derivatives**, enabling traders to evaluate risk and execute better strategies. While the **Binomial model** is simpler and widely used, the **Trinomial model** provides greater precision, especially for longer-term and volatile options.

These models are **crucial in quantitative finance**, forming the foundation for more advanced techniques in options pricing and risk management.

🔹 **Applications:**

- Derivatives trading strategies.
- Portfolio risk assessment.
- Academic research and financial modeling.

---
📈 **Skills Used:** Python, Options Pricing, Quantitative Finance, Numerical Methods, Risk Management, Data Visualization.

---

## ⚠️ Disclaimer

This project is for **educational purposes only** and should not be considered financial advice. Options trading involves risk, and users should conduct their own research before making investment decisions.

📌 **Feel free to contribute or discuss improvements!** 🚀


