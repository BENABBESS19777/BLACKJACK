#########BLACKJACK GAME##########
import random

def deal_card():
    """ Returns a random card from the deck """
    cards = [11,1,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """ Take a list of cards and return the score calculated from the cards """
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    
    return sum(cards)


user_card = []
computer_card = []
is_game_over = False

for _ in range (2):
    user_card.append(deal_card())
    computer_card.append(deal_card())

user_score = calculate_score(user_card) 
computer_score = calculate_score(computer_card) 

print(f"Your cards : {user_card}, current score : {user_score}") 
print(f"Computer's first card : {computer_card[0]}")

if computer_score == 0 or user_score == 0 or user_score > 21 :
    is_game_over = True   

    

