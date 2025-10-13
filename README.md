# saudiStockMarket

A minimal Flask API that returns the latest daily closing price for a Yahoo Finance ticker symbol. Useful for quick integrations or demos, including Saudi Exchange (Tadawul) tickers (e.g., `2222.SR`).

## Features
- Simple HTTP endpoint to fetch latest daily close
- JSON responses
- Works with any Yahoo Finance ticker (e.g., `AAPL`, `GOOGL`, `2222.SR`)

## Tech Stack
- Python + Flask
- [yfinance](https://pypi.org/project/yfinance/) for market data
- [gunicorn](https://gunicorn.org/) for production serving

## Getting Started

### Prerequisites
- Python 3.8+

### Install
```bash
# From the repository root
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Run (development)
```bash
# Uses Flask's built-in dev server on http://127.0.0.1:5000
flask --app app run --debug
```

### Run (production)
```bash
# Binds on port 8000 by default below; adjust as needed
gunicorn -w 2 -b 0.0.0.0:8000 app:app
```

## API

### GET /price/{ticker}
Returns the latest daily close for a given Yahoo Finance ticker.

- **Path params**
  - `ticker` (string): Ticker symbol (e.g., `AAPL`, `MSFT`, `2222.SR`).

- **200 OK**
```json
{
  "ticker": "2222.SR",
  "price": 29.35
}
```

- **500 Error**
```json
{
  "error": "could not get price"
}
```

### Examples
```bash
# Saudi Aramco (Tadawul) example
curl http://127.0.0.1:5000/price/2222.SR

# US example
curl http://127.0.0.1:5000/price/AAPL
```

## Notes & Limitations
- Uses Yahoo Finance data via `yfinance`. Symbols and availability are subject to Yahoo Finance.
- Values returned are the latest daily close, not real-time or intraday quotes.
- Error handling is intentionally simple; production systems may want retries, caching, logging, and better error messages.

## Project Structure
```
.
├── app.py            # Flask app exposing /price/<ticker>
├── requirements.txt  # Python dependencies
└── README.md         # This file
```

## Contributing
Issues and PRs are welcome. For larger changes, please open an issue first to discuss what you would like to change.

## License
No license specified. If you plan to use or distribute this project, please add an appropriate `LICENSE` file.
