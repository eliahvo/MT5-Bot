import MetaTrader5 as mt5

"""
market orders
"""
def market_order_buy(volume, price, take_profit):
    request = {
        "action": mt5.TRADE_ACTION_DEAL,
        "symbol": "EURUSD",
        "volume": volume, #float
        "type": mt5.ORDER_TYPE_BUY,
        "price": price,
        "tp": take_profit, #float
        "comment": "python script",
        "type_filling": mt5.ORDER_FILLING_IOC,
    }
    return mt5.order_send(request)

def market_order_buy_close(position, volume, price):
    request = {
        "action": mt5.TRADE_ACTION_DEAL,
        "symbol": "EURUSD",
        "volume": volume, #float
        "type": mt5.ORDER_TYPE_SELL,
        "position": position,
        "price": price,
        "tp": 0.0, #float
        "comment": "python script",
        "type_filling": mt5.ORDER_FILLING_IOC,
    }
    return mt5.order_send(request)

def market_order_sell(volume, price, take_profit):
    request = {
        "action": mt5.TRADE_ACTION_DEAL,
        "symbol": "EURUSD",
        "volume": volume, #float
        "type": mt5.ORDER_TYPE_SELL,
        "price": price,
        "tp": take_profit, #float
        "comment": "python script",
        "type_filling": mt5.ORDER_FILLING_IOC,
    }
    return mt5.order_send(request)

def market_order_sell_close(position, volume, price):
    request = {
        "action": mt5.TRADE_ACTION_DEAL,
        "symbol": "EURUSD",
        "volume": volume, #float
        "type": mt5.ORDER_TYPE_BUY,
        "position": position,
        "price": price,
        "tp": 0.0, #float
        "comment": "python script",
        "type_filling": mt5.ORDER_FILLING_IOC,
    }
    return mt5.order_send(request)

"""
pending orders
"""
def pending_order_buy_stop(volume, price, take_profit):
    request = {
        "action": mt5.TRADE_ACTION_PENDING,
        "symbol": "EURUSD",
        "volume": volume, #float
        "type": mt5.ORDER_TYPE_BUY_STOP,
        "price": price,
        "tp": take_profit, #float
        "comment": "python script",
        "type_filling": mt5.ORDER_FILLING_IOC,
    }
    return mt5.order_send(request)

def pending_order_sell_stop(volume, price, take_profit):
    request = {
        "action": mt5.TRADE_ACTION_PENDING,
        "symbol": "EURUSD",
        "volume": volume, #float
        "type": mt5.ORDER_TYPE_SELL_STOP,
        "price": price,
        "tp": take_profit, #float
        "comment": "python script",
        "type_filling": mt5.ORDER_FILLING_IOC,
    }
    return mt5.order_send(request)

def close_order(order):
    request = {
        "action": mt5.TRADE_ACTION_REMOVE,
        "order": order,
    }
    return mt5.order_send(request)