import yfinance as yf
import json
from datetime import datetime

def artist_stock_graph(artist_name):
    ticker = yf.Ticker(artist_name)
    data = ticker.history(period="10y")
    
    # Prepare data for JSON serialization
    chart_data = []
    for date, row in data.iterrows():
        chart_data.append({
            'date': date.strftime('%Y-%m-%d'),
            'price': round(row['Close'], 2)
        })
    
    return json.dumps(chart_data)

# Remove the matplotlib code as we'll use JavaScript for rendering

