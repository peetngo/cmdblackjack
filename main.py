# main functions of program will go in here
import random

# this function will check if the cards equals to 21
# TODO: Why doesn't this work?
def checkCards(hand):
    print(hand)
    for i in hand:
        if (i == "J" or i == "K" or i == "Q"):
            i = 10
        if (i == "A"):
            i = 11

    if(hand[0] + hand[1] == 21):
        print("you have won!")

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
    checkCards(playerhand)
    print("Your cards: ", playerhand)
    #print(cpuhand)

    print("lets play some blackjack dog")


if __name__ == "__main__":
   start()