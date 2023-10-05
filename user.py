# DO NOT CHANGE OR REMOVE THIS COMMENT, and do not change this import otherwise all tests will fail.
# Use randint to generate random cards. 
from random import randint
from end_status import blackjack_or_bust
from value import card_value
from name import draw
# Write all of your part 2B code below this comment. DO NOT CHANGE OR REMOVE THIS COMMENT.
def play_human_turn():
    card1= randint(1,13)
    print(draw(card1))
    card2= randint(1,13)
    print(draw(card2))
    hand = card_value(card1)+ card_value(card2)
    while hand<21:
        hit=input('You have '+ str(hand)+'. Hit (y/n)? ')
        if hit=='y' or hit=='Y' or hit=='Yes' or hit=='yes':
            new_card=randint(1,13)
            print(draw(new_card))
            hand+=card_value(new_card)
        elif hit=='n' or hit=='N' or hit=='no' or hit=='No':
            break
        else:
            print('Sorry I didn\'t get that.')
    print ('Final hand: '+ str(hand)+'.')
    if hand==21 or (hand > 21 and hand <= 31):
        print(blackjack_or_bust(hand))
