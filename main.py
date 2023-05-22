import MetaTrader5 as mt5
import time
import sys

import login
import utils.trader as td
import utils.helper as helper

strategy = None
base_value = 23000
factors = [1, 1.43, 1.09, 1.57, 2.22, 3.17, 4.57, 6.65, 9.57]

orders = []
x = None
next = None

if __name__ == "__main__":
    """ get strategy provided by parameter """
    if int(sys.argv[1]) not in [0, 1]:
        print("Please provide strategy (0=Short, 1=Long)")
        exit()
    else:
        strategy = int(sys.argv[1])
    
    """ establish MetaTrader 5 connection to a specified trading account """
    if not mt5.initialize(login=login.login, server=login.server, password=login.password):
        print("initialize() failed, error code =",mt5.last_error())
        quit()

    c = int(mt5.account_info().equity/1000)

    if strategy == helper.LONG:
        """ first market order (LONG) """
        x = mt5.symbol_info_tick("EURUSD").ask
        buy_order = td.market_order_buy(volume=helper.calc_volume(base_value*c*factors[0]), price=x, take_profit=(x + 0.00240))
        orders.append(buy_order)
        helper.print_order(buy_order, "POSITION:BUY")

        """ first pending order (SHORT) """
        pending_order = td.pending_order_sell_stop(volume=helper.calc_volume(base_value*c*factors[1]), price=(x - 0.00080), take_profit=(buy_order.request.price - 0.00320))
        orders.append(pending_order)
        helper.print_order(pending_order, "ORDER:PENDING-SELL")

        next = helper.LONG
    elif strategy == helper.SHORT:
        """ first market order (SHORT) """
        x = mt5.symbol_info_tick("EURUSD").ask
        buy_order = td.market_order_sell(volume=helper.calc_volume(base_value*c*factors[0]), price=x, take_profit=(x - 0.00240))
        orders.append(buy_order)
        helper.print_order(buy_order, "POSITION:SELL")

        """ first pending order (LONG) """
        pending_order = td.pending_order_buy_stop(volume=helper.calc_volume(base_value*c*factors[1]), price=(x + 0.00080), take_profit=(buy_order.request.price + 0.00320))
        orders.append(pending_order)
        helper.print_order(pending_order, "ORDER:PENDING-BUY")

        next = helper.LONG
    else:
        print("strategy not valid")

    amount_positions = mt5.positions_total()
    amount_orders = mt5.orders_total()
    while len(orders) <= 9:
        time.sleep(0.5)
        print(mt5.orders_total(), ", ", mt5.positions_total())

        """ letzte pending order wurde ausgelöst (ist jetzt als Position gelistet) """
        if (mt5.orders_total() == amount_orders-1) and (mt5.positions_total() == amount_positions+1):
            amount_orders = mt5.orders_total()
            amount_positions = mt5.positions_total()

            """ neue pending order gegenläufig setzen """
            if next == helper.LONG:
                pending_order = td.pending_order_buy_stop(volume=helper.calc_volume(base_value*c*factors[len(orders)]), price=x, take_profit=(x + 0.00240))
                orders.append(pending_order)
                helper.print_order(pending_order, "ORDER:PENDING-BUY")
                next = helper.SHORT
            elif next == helper.SHORT:
                pending_order = td.pending_order_sell_stop(volume=helper.calc_volume(base_value*c*factors[len(orders)]), price=(x - 0.00080), take_profit=(x - 0.00320))
                orders.append(pending_order)
                helper.print_order(pending_order, "ORDER:PENDING-SELL")
                next = helper.LONG
            else:
                print("Error, variable next is not correctly set.")
        
        """ take profit von letzter position wurde erreicht """
        if mt5.positions_total == amount_positions-1:
            helper.close_all_and_shutdown(orders)
            break