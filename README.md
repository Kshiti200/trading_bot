# Binance Futures Testnet Trading Bot (Python)

This project is a simplified trading bot built using **Python 3** that can place orders on the **Binance USDT-M Futures Testnet**.

It was developed as part of a Junior Python Developer screening task to demonstrate:

- Clean project structure
- Binance Futures API interaction
- CLI-based order placement
- Proper validation, logging, and error handling

---

## Features

- Connects to Binance Futures Testnet (safe, no real money)
- Places Futures orders through CLI
- Supported order types:
  - MARKET Orders
  - LIMIT Orders
- Supports both BUY and SELL sides
- Input validation with meaningful errors
- Logs are stored cleanly in separate files:
  - MARKET logs
  - LIMIT logs
  - Error logs

---

## Project Structure

trading_bot/
│
├── bot/
│ ├── client.py # Binance Futures client wrapper
│ ├── orders.py # Order placement logic
│ ├── validators.py # CLI input validation
│ ├── logging_config.py # Logging setup (separate logs per order type)
│ └── init.py
│
├── cli.py # Command-line entry point
├── requirements.txt
├── README.md
├── logs/
│ ├── market_order.log # MARKET order logs
│ ├── limit_order.log # LIMIT order logs
│ └── errors.log # Error logs
│
└── .env (ignored)

---

## Setup Instructions

### 1. Install Dependencies

```bash
pip install -r requirements.txt
2. Create a .env File

Inside the root folder, create a file named .env:

BINANCE_API_KEY=your_testnet_api_key
BINANCE_SECRET_KEY=your_testnet_secret_key


Note: .env is excluded from GitHub using .gitignore.

How to Run

All orders are placed through the CLI.

MARKET Order Example :
py cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.01


This will log output into:

logs/market_order.log

LIMIT Order Example :
py cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.01 --price 85000


This will log output into:

logs/limit_order.log

Invalid Order Example (Error Logging)
py cli.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.01


Errors will be stored in:

logs/errors.log

Logging Output

This project maintains separate log files:

Log File	Contains
market_order.log	All MARKET order requests/responses
limit_order.log	All LIMIT order requests/responses
errors.log	API failures, validation errors, exceptions
Notes

Binance Futures applies price protection rules.
LIMIT orders must be placed close to the current market price, otherwise Binance will reject them.

Author

Built as part of the Junior Python Developer – Crypto Trading Bot hiring task.
```
