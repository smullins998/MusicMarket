import math 
import random
import time
import pandas as pd
from datetime import datetime
import uuid 

#We now append characteristics of the trades made to some lists
last_trade_price = {100:None}
bid_price = {}
ask_price = {}
completed_orders = {}
start_time=time.time()


for m_idx, m_order_id, m_order, m_shares, m_order_type, m_price, m_time in zip(
                                                                        Combo_MatchBook.index, 
                                                                        Combo_MatchBook.Order_ID, 
                                                                        Combo_MatchBook.Order,
                                                                        Combo_MatchBook.Shares,
                                                                        Combo_MatchBook.Order_Type,
                                                                        Combo_MatchBook.Price,
                                                                        Combo_MatchBook.Time):
    print(m_order, m_shares, m_order_type, m_price)
    #Logic for the Market SELLING order
    if m_order_type == 'market' and m_order == 'sell':
        while Combo_MatchBook.loc[m_idx, 'Shares']>0:
       
            #Get the SELLING current row and subtract
            curr_sell_id = m_idx
            Combo_MatchBook.loc[curr_sell_id, 'Shares'] -= 1

            #Get the BEST buying row and subtract
            buy_book = Combo_MatchBook[(Combo_MatchBook.Order == 'buy') & (Combo_MatchBook.Shares >0)].sort_values(by='Price', ascending=False)
            
            #Block to get the next buying ID, not enough if the book is empty
            try:
                curr_buy_id = buy_book.iloc[0,0]
            except:
                print('there are not enough buyers in the market')
                
                break
                
            curr_buy_price = buy_book.iloc[0,4]
            condition = Combo_MatchBook['Order_ID'] == curr_buy_id

            # Subtract 1 from 'Shares' for the row where the condition is True
            Combo_MatchBook.loc[condition, 'Shares'] -= 1
            
            #Let's append some information like last traded price
            last_trade_price[curr_buy_id] = ['sold', curr_buy_price, time.time()]
    
            
        print('Sell Order Complete')
        
        
        
    #Logic for the Market SELLING order
    if m_order_type == 'market' and m_order == 'buy':
        while Combo_MatchBook.loc[m_idx, 'Shares']>0:

            #Get the BUYING current row and subtract
            curr_buy_id = m_idx
            Combo_MatchBook.loc[curr_buy_id, 'Shares'] -= 1

            #Get the BEST buying row and subtract
            sell_book = Combo_MatchBook[(Combo_MatchBook.Order == 'sell') & (Combo_MatchBook.Shares >0)].sort_values(by='Price', ascending=True)
            
            #Block to get the next buying ID, not enough if the book is empty
            try:
                curr_sell_id = sell_book.iloc[0,0]
            except:
                print('there are not enough sellers in the market')
                
                break
            curr_sell_price = sell_book.iloc[0,4]
        
            condition = Combo_MatchBook['Order_ID'] == curr_sell_id

            # Subtract 1 from 'Shares' for the row where the condition is True
            Combo_MatchBook.loc[condition, 'Shares'] -= 1
            
            #Let's append some information like last traded price
            last_trade_price[curr_sell_id] = ['bought', curr_sell_price, time.time()]

            
        print('Buy Order Complete')
    
    #Now we need to get the best limit sell and best limit buy with shares>0 and append to ask/bid
    bid_list = Combo_MatchBook[(Combo_MatchBook.Shares > 0) & (Combo_MatchBook.Order == 'buy') &  (Combo_MatchBook.Order_Type == 'limit')].Price.values
    ask_list = Combo_MatchBook[(Combo_MatchBook.Shares > 0) & (Combo_MatchBook.Order == 'sell') &  (Combo_MatchBook.Order_Type == 'limit')].Price.values
    try:
        ask_price[time.time()] = min(ask_list)
        bid_price[time.time()] = max(bid_list)
    except:
        continue
    
end_time=time.time()
print('Total Time', end_time-start_time)