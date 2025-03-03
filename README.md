# 📈 Options Pricing using Binomial and Trinomial Models

## 📌 Overview

This repository provides an in-depth analysis of **options pricing** using the **Binomial and Trinomial models**—two widely used techniques in **quantitative finance**. These models help estimate option values by simulating potential price movements of an asset over time, allowing traders and analysts to make informed decisions.

- The **Binomial Model** assumes an asset price can move **up or down** in each time step, forming a discrete-time **binomial tree**.
- The **Trinomial Model** extends this approach by introducing a **third possible outcome**, creating a more refined and accurate pricing structure.

Both models are fundamental in derivative pricing and serve as the building blocks for more sophisticated options pricing models.

---

## ⚡ Binomial Model: Step-by-Step Breakdown

The **Binomial Option Pricing Model** follows a **recombining tree structure**:

1. **Define Time Steps:** The option's time to maturity is divided into small intervals.
2. **Calculate Up and Down Factors:** The asset price moves up (**u**) or down (**d**) at each step.
3. **Compute Option Payoffs:** Start at the final step and work **backward through the tree**.
4. **Discount Future Payoffs:** Use the **risk-free rate** to determine the present value of future payoffs.

🔹 **Strengths:**

- Intuitive and easy to implement.
- Provides stepwise control over price movements.
- Useful for pricing **American options** (which can be exercised before expiry).

🔹 **Limitations:**

- Can become computationally expensive for a large number of steps.

---

## ⚡ Trinomial Model: A More Granular Approach

The **Trinomial Option Pricing Model** is an extension of the **Binomial model**, introducing a **third possible state**:

- **Upward movement (u)**
- **Downward movement (d)**
- **No movement (m)** (a stable middle price)

📌 **Why use the Trinomial Model?**

- More **accurate approximation** of continuous-time models like **Black-Scholes**.
- Provides better handling of **high volatility scenarios**.
- Converges faster than the Binomial model for **longer expiration periods**.

---

## 🛠️ How to Use

To compute option prices using these models, the following **input parameters** are required:

- **S (Current Asset Price)**: The price of the underlying asset.
- **K (Strike Price)**: The agreed price for option execution.
- **r (Risk-free Rate)**: The theoretical return on a risk-free investment.
- **T (Time to Expiration)**: The duration before the option expires.
- **u & d (Price Movement Factors)**: Determine how much the price moves per step.
- **n or m (Steps in the Model)**: The number of time intervals in the tree.

### 🚀 Running the Code

```bash
python options_pricing.py  # Replace with actual script name
```

---

## 📊 Conclusion

The **Binomial and Trinomial models** are powerful tools for pricing **options and derivatives**, enabling traders to evaluate risk and execute better strategies. While the **Binomial model** is simpler and widely used, the **Trinomial model** provides greater precision, especially for longer-term and volatile options.

These models are **crucial in quantitative finance**, forming the foundation for more advanced techniques in options pricing and risk management.

🔹 **Applications:**

- Derivatives trading strategies.
- Portfolio risk assessment.
- Academic research and financial modeling.

---

## ⚠️ Disclaimer

This project is for **educational purposes only** and should not be considered financial advice. Options trading involves risk, and users should conduct their own research before making investment decisions.

📌 **Feel free to contribute or discuss improvements!** 🚀



