import utils.trader as td
import MetaTrader5 as mt5

SHORT = 0
LONG  = 1

def calc_volume(actual_volume):
    return round(actual_volume / 100000.0, 2)

def close_all_positions(orders):
    #sell and/or close positions/orders
    for order in orders:
        print("**", order.order, "**")
        sell_order = td.close_order(order.order)
        print(sell_order)
        sell_order = td.market_order_buy_close(position=order.order, volume=order.request.volume, price=mt5.symbol_info_tick("EURUSD").ask)
        print(sell_order)

    #shut down connection to the MetaTrader 5 terminal
    mt5.shutdown()

    print("Done!")

def print_order(order, type):
    print(f"{type}: Order: {order.order}, Price: {order.price}, Volume: {order.volume}, Comment: {order.comment}")