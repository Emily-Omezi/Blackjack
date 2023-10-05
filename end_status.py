# Write code here to print out the game outcome given a hand value.
def blackjack_or_bust(n):
    if n==21:
        return 'BLACKJACK!'
    elif n<21 and n>5:
        return None
    elif n>21 and n<=31:
        return 'BUST.'
    elif n>31 or n<4:
        return 'BAD HAND VALUE!'
