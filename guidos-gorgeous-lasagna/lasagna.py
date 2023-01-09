EXPECTED_BAKE_TIME=40
PREPARATION_TIME=2

def bake_time_remaining(actual):
    """Return remaining baking time.This function takes expected bking time-actual time elapsed."""
    return EXPECTED_BAKE_TIME-actual

def preparation_time_in_minutes(layers):
    """Return preparation time.This function takes layers and calculates the total preperation time."""
    return layers*PREPARATION_TIME

def elapsed_time_in_minutes(layers,elapsed_bake_time):
    """Return elapsed cooking time.This function takes two numbers representing the number of layers & the time already spent baking and calculates the total elapsed minutes spent cooking the lasagna."""
    return (layers*PREPARATION_TIME) + elapsed_bake_time