"""Functions to help the company calculate their power usage."""


def get_extra_hours(hours):
    return (hours+3)%24
    
    '''if hours+3==24:
        return 0
    #elif hours%24>=0 and hours%24<=24:
        #return hours%24 + 3
    else:
        return hours%24 + 3
    """Return the amount of hours.

    :param: hours: int - amount of hours.
    :return: int - amount of "extra" hours.
    """
    pass
'''

def get_kW_amount(watts):
    return round(watts/1000,1)
    """Return the kW amount of a given watt amount.

    :param: watts: int - watt amount.
    :return: float - kW amount.
    """
    pass


def get_kwh_amount(watts):
    if (round(watts/(1000*3600),1))<1.0:
        return (0)
    else:
        return(int(round(watts/(1000*3600),0)))
    """Return the kWh amount of a given watt amount and hours.

    :param: watts: int - watt amount.
    :return: int - kilowatt hour amount.
    """
    pass


def get_efficiency(power_factor):
    return power_factor/100
    """Return the efficiency calculated from the power factor.

    :param: power_factor: float.
    :return: float - efficiency.
    """
    pass


def get_cost(watts, power_factor, price):
    return float(get_kwh_amount(watts) / get_efficiency(power_factor) * price)
    """Calculate the cost of a given kWh value, efficiency and price.

    :param: watts: int - watt value.
    :param: power_factor: float - efficiency.
    :param: price: float - price of kWh.
    :return: float - cost of kWh.
    """
    pass
