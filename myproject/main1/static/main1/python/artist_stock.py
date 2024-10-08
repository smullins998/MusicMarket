import yfinance as yf

def artist_stock():
    ticker = yf.Ticker("AAPL")
    info = ticker.info
    
    # Calculate percent change
    current_price = info.get("currentPrice")
    previous_close = info.get("previousClose")
    if current_price and previous_close:
        percent_change = ((current_price - previous_close) / previous_close) * 100
    else:
        percent_change = None
    
    # Extract the requested information
    stock_data = {
        "current_price": current_price,
        "price_change_percent": percent_change,
        "market_cap": info.get("marketCap"),
        "fifty_two_week_high": info.get("fiftyTwoWeekHigh"),
        "fifty_two_week_low": info.get("fiftyTwoWeekLow"),
        "pe_ratio": info.get("trailingPE")
    }
    
    return stock_data

