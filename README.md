# 🚀 Binance Futures Trading Bot (Testnet)

## 📌 Project Overview

This project is a simple Python-based trading bot that interacts with the Binance Futures Testnet (USDT-M).
It allows users to place MARKET and LIMIT orders using a command-line interface (CLI).

The application is designed with a clean, modular structure and includes input validation, logging, and proper error handling.

---

## ⚙️ Features

* Place **MARKET** and **LIMIT** orders
* Supports both **BUY** and **SELL**
* CLI-based input using argparse
* Input validation before API calls
* Structured logging of requests, responses, and errors
* Exception handling for safe execution
* Uses Binance Futures Testnet (no real money involved)

---

## 🛠️ Tech Stack

* Python 3.x
* python-binance
* argparse
* logging
* dotenv

---

## 📂 Project Structure

```
trading_bot/
│
├── bot/
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   ├── logging_config.py
│
├── cli.py
├── .env
├── requirements.txt
├── README.md
└── logs/
```

---

## 🔑 Setup Instructions

### 1. Clone the repository

```
git clone <your-repo-link>
cd trading_bot
```

### 2. Create virtual environment

```
python -m venv venv
```

### 3. Activate environment

**Windows:**

```
venv\Scripts\activate
```

**Mac/Linux:**

```
source venv/bin/activate
```

### 4. Install dependencies

```
pip install -r requirements.txt
```

### 5. Add API Keys

Create a `.env` file:

```
API_KEY=your_api_key
API_SECRET=your_api_secret
```

---

## ▶️ How to Run

### MARKET Order

```
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.002
```

### LIMIT Order

```
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.002 --price 60000
```

---

## 📊 Sample Output

```
📤 Order Request:
Symbol: BTCUSDT
Side: BUY
Type: MARKET
Quantity: 0.002

📥 Order Response:
Order ID: 12994072683
Status: NEW
Executed Qty: 0.000
Avg Price: 0.00

✅ Order placed successfully!
```

---

## 🧠 Assumptions

* Binance Futures Testnet is used (no real trading)
* Minimum order value must be ≥ 100 USDT
* API keys are valid and have trading permissions

---

## 📝 Logging

All requests, responses, and errors are logged in:

```
logs/trading.log
```

---

## ❗ Error Handling

* Input validation errors are handled before API calls
* API and unexpected errors are logged and handled gracefully

---

## 👨‍💻 Author

Abhilash Addagatla
