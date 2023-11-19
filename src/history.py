import refinitiv.data as rd

def history(universe, fields="", interval=""):
    return rd.get_history(universe=universe,fields=fields, interval=interval)

