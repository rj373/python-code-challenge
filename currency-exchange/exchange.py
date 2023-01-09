def exchange_money(budget, exchange_rate):
    """This function return the value of the exchanged currency."""
    return budget/exchange_rate
    
def get_change(budget, exchanging_value):
    """This function return the amount of money that is left from the budget."""
    return budget-exchanging_value
    
def get_value_of_bills(denomination, number_of_bills):
    """This function return only the total value of the bills (excluding fractional amounts) the booth would give back"""
    return denomination*number_of_bills
    
def get_number_of_bills(budget, denomination):
    """This function return the number of new currency bills that you can receive within the given budget."""
    return int(budget/denomination)
    
def get_leftover_of_bills(budget, denomination):
    """This function return the leftover amount that cannot be exchanged from your budget given the denomination of bills."""
    return float(budget%denomination)
    
def exchangeable_value(budget, exchange_rate, spread, denomination):
    """This function return the maximum value of the new currency after calculating the exchange rate plus the spread."""
    return int(budget/(exchange_rate+(exchange_rate*spread*0.01))/denomination)*denomination