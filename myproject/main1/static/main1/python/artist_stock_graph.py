import yfinance as yf
import json
from datetime import datetime

def artist_stock_graph(artist):
    # For now, we'll use a placeholder ticker. In the future, you'll need to map artists to tickers.
    ticker = yf.Ticker("AAPL")
    data = ticker.history(period="10y")
    
    # Prepare data for JSON serialization
    chart_data = {
        'dates': [],
        'prices': []
    }
    for date, row in data.iterrows():
        chart_data['dates'].append(date.strftime('%Y-%m-%d'))
        chart_data['prices'].append(round(row['Close'], 2))
    
    return chart_data  # Return a dictionary instead of a JSON string

