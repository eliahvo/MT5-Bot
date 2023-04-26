import MetaTrader5 as mt5
import time

import login
import utils.trader as td
import utils.helper as helper

strategy = helper.LONG
base_value = 23000
factors = [1.43, 1.09, 1.57, 2.22, 3.17, 4.57, 6.65, 9.57]

orders = []

#establish MetaTrader 5 connection to a specified trading account
if not mt5.initialize(login=login.login, server=login.server, password=login.password):
    print("initialize() failed, error code =",mt5.last_error())
    quit()

c = int(mt5.account_info().equity/1000)

if strategy == helper.LONG:
    #first market order (LONG)
    #buy_order = td.market_order_buy(volume=helper.calc_volume(base_value*c), price=mt5.symbol_info_tick("EURUSD").ask, take_profit=(mt5.symbol_info_tick("EURUSD").ask + 0.00240))
    buy_order = td.market_order_buy(volume=0.01, price=mt5.symbol_info_tick("EURUSD").ask, take_profit=(mt5.symbol_info_tick("EURUSD").ask + 0.00240))
    orders.append(buy_order)
    print("buy", buy_order)
    #first pending order (SHORT)
    #pending_order = td.pendig_order_sell_stop(volume=helper.calc_volume(base_value*c*factors[0]), price=(buy_order.request.price - 0.00080), take_profit=(buy_order.request.price - 0.00320))
    pending_order = td.pending_order_sell_stop(volume=helper.calc_volume(base_value*c*factors[0]), price=(buy_order.request.price - 0.00080), take_profit=(buy_order.request.price - 0.00320))
    orders.append(pending_order)
    print(buy_order)
elif strategy == helper.SHORT:
    pass
else:
    print("strategy not valid")

#LOOP
#while True:
#    time.sleep(0.5)


time.sleep(5)


#sell
for order in orders:
    print("**", order.order, "**")
    sell_order = td.close_order(order.order)
    print(sell_order)
    sell_order = td.market_order_buy_close(position=order.order, volume=order.request.volume, price=mt5.symbol_info_tick("EURUSD").ask)
    print(sell_order)

#shut down connection to the MetaTrader 5 terminal
mt5.shutdown()