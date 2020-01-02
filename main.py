# main functions of program will go in here
import random


def welcome():
    print("Welcome to BlackJack!")
    print("Dealing your cards...")


def hit(hand, cards):
    dealCard = cards.pop()
    if (dealCard == 11):
        dealCard = "J"
        hand.append(dealCard)
    elif (dealCard == 12):
        dealCard = "Q"
        hand.append(dealCard)
    elif (dealCard == 13):
        dealCard = "K"
        hand.append(dealCard)
    elif (dealCard == 1):
        dealCard = "A"
        hand.append(dealCard)
    else:
        hand.append(dealCard)
    return hand

# this function will check cards
def checkCards(hand):
    num = 0
    for card in hand:
        if (card == "Q" or card == "J" or card == "K"):
            num = num + 10
        elif (card == "A"):
            if (num > 11):
                num = num + 1
            else:
                num = num + 11
        else:
            num = num + card
    return num

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
    return(hand)

# this is going to start the game
def start():
    # lets start with the deck itself
    # going to use an array to hold the values of the cards

    # when you start the game define a deck of cards
    # TODO: this is not a full deck, make it a full deck with 52 cards
    cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    playerhand = dealCards(cards)
    cpuhand = dealCards(cards)

    welcome()
    print("Your cards: ", playerhand)
    print("Your total: ", checkCards(playerhand))
    print("your cards now: ", hit(playerhand, cards))


if __name__ == "__main__":
   start()