# DO NOT CHANGE OR REMOVE THIS COMMENT, and do not change this import otherwise all tests will fail.
# Use randint to generate random cards. 
from random import randint
from end_status import blackjack_or_bust
from value import card_value
from name import draw
# Write all of your part 2A code below this comment. DO NOT CHANGE OR REMOVE THIS COMMENT.
def play_dealer_turn():
    card1= randint(1,13)
    print(draw(card1))
    card2= randint(1,13)
    print(draw(card2))
    hand = card_value(card1)+ card_value(card2)
    while hand<17:
        print ('Dealer has '+ str(hand)+'.')
        new_card= randint(1,13)
        hand+=card_value(new_card)
        print(draw(new_card))
    print('Final hand: '+ str(hand)+ '.')
    if hand==21 or hand>21 and hand<=31:
        print(blackjack_or_bust(hand))
