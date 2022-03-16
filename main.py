import art
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_cards(cards):
    return random.choice(cards)

def calculate_cards(cards):
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append (1)
        #print(sum(cards))
        #print(cards)
        return cards
    else:
        return cards

def calculate_score(cards):
    return(sum(cards))

def determine_winner(user_score, computer_score):
    if user_score > computer_score and user_score <= 21:
        print("You win")
    elif user_score < computer_score and computer_score > 21:
        print("Computer went over. You win")
    elif user_score > computer_score and user_score > 21:
        print("You went over. You lose")
    elif computer_score > user_score and computer_score <= 21:
        print("Computer wins")
    elif user_score == computer_score:
        print("It's a tie")

test = True
while True:
    def game():
        user_cards = []
        comp_cards = []
        user1_score = 0
        for num in range(2):
            user_cards.append(random.choice(cards))
            comp_cards.append(random.choice(cards))

        play_game = True
        print(art.logo)
        user_cards = calculate_cards(user_cards)
        user1_score = calculate_score(user_cards)
        comp1_score = calculate_score(comp_cards)
        print(f" Your cards: {user_cards}, current score: {user1_score}")
        print(f"Computer's first card: {comp_cards[0]}")
        while play_game:
            user1_score = calculate_score(user_cards)
            if user1_score < 21:
                another_card = input("Type 'y' to get another card, type 'n' to pass")
                if another_card == 'y':
                    user_cards.append(random.choice(cards))
                    user1_score = sum(user_cards)
                    print(f" Your cards: {user_cards}, current score: {user1_score}")
                    print(f"Computer's first card: {comp_cards[0]}")
                else:
                    print(f"Your final hand {user_cards}, final score: {user1_score}")
                    play_game = False
            else:
                print(f"Your final hand {user_cards}, final score: {user1_score}")
                play_game = False

        comp_game = True

        while comp_game:
            if comp1_score < 16:
                comp_cards.append(random.choice(cards))
                comp_cards = calculate_cards(comp_cards)
                comp1_score = sum(comp_cards)
            else:
                comp_game = False
                comp1_score = sum(comp_cards)
                print(f"Computers final hand {comp_cards}, the final score {comp1_score}")
                determine_winner(user1_score, comp1_score)
    if input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
        game()
    else:
        exit()

