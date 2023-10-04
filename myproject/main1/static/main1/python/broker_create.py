import math 
import random
import time
import pandas as pd
from datetime import datetime
import uuid 

#This should somewhat simulate exchange and broker behavior
#Create random orders coming in
#We are going to impliment limits on num_shares of stock num_shares you can trade

buy_order = []
buy_shares = []
buy_ordertype = []
buy_price = []
buy_time = []
buy_id = []

sell_order = []
sell_shares = []
sell_ordertype = []
sell_price = []
sell_time = []
sell_id = []

curr_price = 100

for i in range(1,20):
    
    current_timestamp = datetime.now()
    
    # make a random order 0==buy 1==sell
    buysell = random.choices(['buy','sell'])[0]
    shares = random.randrange(1,20)
    marketlimit = random.choices(['market','limit'])[0]
    pct_price = abs(round(random.gauss(0, 2),1))
    order_id= str(uuid.uuid4())
    

    if buysell == 'buy':
        buy_order.append(buysell)
        buy_shares.append(shares)
        buy_ordertype.append(marketlimit)
        buy_time.append(current_timestamp)
        buy_id.append(order_id)
        if marketlimit == 'limit':
            proposed_price = curr_price - ((curr_price*pct_price) / 100)
            buy_price.append(proposed_price)
        else:
            buy_price.append(curr_price)
        
        
    elif buysell == 'sell':
        sell_order.append(buysell)
        sell_shares.append(shares)
        sell_ordertype.append(marketlimit)
        sell_time.append(current_timestamp)
        sell_id.append(order_id)

        if marketlimit == 'limit':
            proposed_price = curr_price + ((curr_price*pct_price) / 100)
            sell_price.append(proposed_price)
        else:
            sell_price.append(curr_price)
        
    
        

    #Now we need to match orders then pop and update current price 
    
    
    
    print(buysell, shares, marketlimit, curr_price, current_timestamp)
    
    time.sleep(random.randrange(0,2))
    
Buy_Book = pd.DataFrame({'Order_ID': buy_id, 'Order': buy_order, 'Shares': buy_shares, 'Order_Type': buy_ordertype, 'Price': buy_price, 'Time': buy_time})
Sell_Book = pd.DataFrame({'Order_ID': sell_id, 'Order': sell_order, 'Shares': sell_shares, 'Order_Type': sell_ordertype, 'Price': sell_price, 'Time': sell_time})

Combo_MatchBook = pd.concat([Sell_Book, Buy_Book]).sort_values(by='Time').reset_index(drop=True)