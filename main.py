import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


#making random card choice
def card_score(card_input):
    if sum(card_input) == 21 and len(card_input) == 2:
        return 0
    if 11 in card_input and sum(card_input) > 21:
        card_input.remove(11)
        card_input.append(1)

    return sum(card_input)


again = True
#making statment of start
while again:
    start = input("Do you want to play Blackjack? type 'y' or 'n': ")
    if start.lower() == "y":
        from art import logo
        print(logo)
        #find my total and dealers total
        my_cards = []
        computer_cards = []

        for _ in range(2):
            my_cards.append(random.choice(cards))
            computer_cards.append(random.choice(cards))

        mine = card_score(my_cards)
        dealer = card_score(computer_cards)
        while dealer != 0 and dealer < 17:
            another_card = random.choice(cards)
            computer_cards.append(another_card)
            dealer = card_score(computer_cards)

        repeat = True

        #make a request for another number
        while repeat:
            print(f"  Your cards: {my_cards}, current score: {mine}")
            print(f"  Computer's first card: {computer_cards[0]}")
            if mine == 0 or dealer == 0:
                break
            hit = input("Type 'y' to get another card, type 'n' to pass: ")
            if hit.lower() == "y":
                another_card = random.choice(cards)
                my_cards.append(another_card)
                mine = card_score(my_cards)
                if sum(my_cards) > 17:
                    repeat = False
            else:
                repeat = False

        print(f"  Your final hand:{my_cards}, final score: {mine}")
        print(
            f"  Computer's final hand:{computer_cards}, final score: {dealer}")
        if mine == 0:
            print("You win with a Blackjack!")
        elif dealer == 0:
            print("Computer wins with a Blackjack!. You lose.")
        elif mine > 21:
            print("You went over. You lose")
        elif dealer > 21:
            print("Oppenent went over. You Win")
        elif mine > dealer:
            print("You win.")
        elif mine < dealer:
            print("You lose.")
        else:
            print("Draw.")
    else:
        again = False
