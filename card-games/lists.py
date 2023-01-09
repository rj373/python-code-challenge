"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""


def get_rounds(number):
    return [number, number+1, number+2]
def concatenate_rounds(rounds_1, rounds_2):
    return rounds_1+rounds_2
def list_contains_round(rounds, number):
    return number in rounds
def card_average(hand):
    return sum(hand)/len(hand)
def approx_average_is_average(hand):
    avg=card_average(hand)
    middle=(hand[0]+hand[-1])/2
    length=(len(hand)//2)
    return avg == middle or avg==hand[length]
def average_even_is_average_odd(hand):
    return sum(hand[1::2])/len(hand[1::2]) == sum(hand[0::2])/len(hand[0::2])
def maybe_double_last(hand):
    if hand[-1]==11:
        hand[-1]=hand[-1]*2
        return hand
    else:
        return hand