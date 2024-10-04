import yfinance as yf

def artist_stock():
    ticker = yf.Ticker("AAPL")
    info = ticker.info
    
    # Extract the requested information
    stock_data = {
        "current_price": info.get("currentPrice"),
        "price_change": info.get("regularMarketChange"),
        "market_cap": info.get("marketCap"),
        "fifty_two_week_high": info.get("fiftyTwoWeekHigh"),
        "fifty_two_week_low": info.get("fiftyTwoWeekLow"),
        "pe_ratio": info.get("trailingPE")
    }
    
    return stock_data

