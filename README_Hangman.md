# 📈 Stock Portfolio Tracker — CodeAlpha Task 2

A command-line **Stock Portfolio Tracker** built in Python as part of the **CodeAlpha Python Programming Internship**.

---

## 📌 About the Project

This tool lets users input their stock holdings and instantly see the total value of their investment portfolio. It uses a built-in dictionary of stock prices and optionally saves the results to a CSV file.

---

## ✨ Features

- 📋 Displays a list of 8 popular stocks with current (hardcoded) prices
- ✏️ User inputs stock symbol + number of shares owned
- 💰 Calculates per-stock value and total portfolio value
- 💾 Saves results to `portfolio.csv` (optional)
- ⚠️ Input validation — handles invalid symbols and non-numeric quantities
- 🔁 Supports multiple stocks in one session

---

## 📊 Available Stocks

| Symbol | Company | Price (USD) |
|--------|---------|-------------|
| AAPL | Apple Inc. | $180 |
| TSLA | Tesla Inc. | $250 |
| GOOGL | Alphabet (Google) | $140 |
| AMZN | Amazon.com | $185 |
| MSFT | Microsoft Corp. | $415 |
| META | Meta Platforms | $510 |
| NVDA | NVIDIA Corp. | $900 |
| NFLX | Netflix Inc. | $630 |

---

## 🛠️ Concepts Used

| Concept | Usage |
|---|---|
| Dictionary | Stores stock names and prices |
| Input/Output | Interactive user interface |
| Arithmetic | Calculates investment values |
| CSV file handling | Saves portfolio to file |
| Functions | Clean, modular code structure |

---

## 🚀 How to Run

Make sure Python 3 is installed on your system. No external libraries needed.

```bash
# Clone the repository
git clone https://github.com/YourUsername/CodeAlpha_StockPortfolioTracker.git

# Navigate to the folder
cd CodeAlpha_StockPortfolioTracker

# Run the tracker
python stock_tracker.py
```

---

## 📸 Sample Output

```
=======================================================
      💹  STOCK PORTFOLIO TRACKER  💹
=======================================================

📈  Available Stocks:
-----------------------------------
  Symbol   Company              Price (USD)
-----------------------------------
  AAPL     Apple Inc.           $180.00
  TSLA     Tesla Inc.           $250.00
  ...
-----------------------------------

Stock symbol (e.g. AAPL): AAPL
  How many shares of AAPL do you own? 10
  ✅  Added 10 share(s) of AAPL.

=======================================================
           📊  YOUR STOCK PORTFOLIO SUMMARY
=======================================================
  Stock      Qty        Price    Total Value
-------------------------------------------------------
  AAPL        10      $180.00      $1,800.00
-------------------------------------------------------
  TOTAL INVESTMENT                 $1,800.00
=======================================================
```

---

## 👤 Author

**[Your Name]**
CodeAlpha Python Programming Internship

---

## 🏢 Internship

This project was built as **Task 2** of the CodeAlpha Python Programming Internship.

🔗 [CodeAlpha Website](https://www.codealpha.tech)
