import MetaTrader5 as mt5
import login
import time
 
# establish MetaTrader 5 connection to a specified trading account
if not mt5.initialize(login=login.login, server=login.server, password=login.password):
    print("initialize() failed, error code =",mt5.last_error())
    quit()

#buy
request = {
    "action": mt5.TRADE_ACTION_DEAL,
    "symbol": "EURUSD",
    "volume": 0.01, #float
    "type": mt5.ORDER_TYPE_BUY,
    "price": mt5.symbol_info_tick("EURUSD").ask,
    "sl": 0.0, #float
    "tp": 0.0, #float
    "deviation": 20, #int
    "magic": 234000, #int
    "comment": "python script open",
    "type_time": mt5.ORDER_TIME_GTC,
    "type_filling": mt5.ORDER_FILLING_IOC,
}
buy_order = mt5.order_send(request)
print(buy_order)

time.sleep(5)

#sell
request = {
    "action": mt5.TRADE_ACTION_DEAL,
    "symbol": "EURUSD",
    "volume": 0.01, #float
    "type": mt5.ORDER_TYPE_SELL,
    "position": buy_order.order,
    "price": mt5.symbol_info_tick("EURUSD").ask,
    "sl": 0.0, #float
    "tp": 0.0, #float
    "deviation": 20, #int
    "magic": 234000, #int
    "comment": "python script open",
    "type_time": mt5.ORDER_TIME_GTC,
    "type_filling": mt5.ORDER_FILLING_IOC,
}
sell_order = mt5.order_send(request)
print(sell_order)

# shut down connection to the MetaTrader 5 terminal
mt5.shutdown()