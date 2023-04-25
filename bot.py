import MetaTrader5 as mt5
import login
 
# establish MetaTrader 5 connection to a specified trading account
if not mt5.initialize(login.login, login.server, login.password):
    print("initialize() failed, error code =",mt5.last_error())
    quit()
 
# display data on connection status, server name and trading account
print(mt5.account_info())
 
# shut down connection to the MetaTrader 5 terminal
mt5.shutdown()