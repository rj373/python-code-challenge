#Functions to help play and score a game of blackjack.

def value_of_card(card):
    if card in ('J','Q','K'):
        return int(10)
    elif card=='A':
        return int(1)
    else:
        return int(card)     
def higher_card(card_one, card_two):
    val_card_one=value_of_card(card_one)
    val_card_two = value_of_card(card_two)
    if val_card_one>val_card_two:
        return card_one
    elif val_card_one==val_card_two:
        return (card_one,card_two)
    else:
        return card_two
def value_of_ace(card_one, card_two):
    v1 = 11 if card_one == ('A') else value_of_card(card_one)
    v2 = 11 if card_two == ('A') else value_of_card(card_two)
    total_score = v1 + v2 + 11
    return 1 if total_score > 21 else 11
   
def is_blackjack(card_one, card_two):
    v1 = 11 if card_one == ('A') else value_of_card(card_one)
    v2 = 11 if card_two == ('A') else value_of_card(card_two)
    total_score = v1 + v2
    return total_score == 21
    
def can_split_pairs(card_one, card_two):
    return value_of_card(card_one) == value_of_card(card_two)
    
def can_double_down(card_one, card_two):
    total_score = value_of_card(card_one) + value_of_card(card_two)
    return total_score in (9,10,11)