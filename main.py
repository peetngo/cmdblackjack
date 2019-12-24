# main functions of program will go in here
import random

# this function will deal the cards
def dealCards(cards):
    hand = []
    random.shuffle(cards)
    for x in range(2):
        dealCard = cards.pop()
        if (dealCard == 11):
            dealCard = "J"
            hand.append(dealCard)
        elif(dealCard == 12):
            dealCard = "Q"
            hand.append(dealCard)
        elif(dealCard == 13):
            dealCard = "K"
            hand.append(dealCard)
        elif(dealCard == 1):
            dealCard = "A"
            hand.append(dealCard)
        else:
            hand.append(dealCard)

    print(hand)


# this is going to start the game
def start():
    # lets start with the deck itself
    # going to use an array to hold the values of the cards

    cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    #random.shuffle(cards)
    dealCards(cards)

    print("lets play some blackjack dog")


if __name__ == "__main__":
   start()