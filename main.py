#Generate a random number between 1 and 151 to use as the Pokemon ID number
from random import randint
import requests


def getData(randomNumber):
    html = "https://pokeapi.co/api/v2/pokemon/{}".format(randomNumber)
    response = requests.get("https://pokeapi.co/api/v2/pokemon/{}".format(randomNumber))
    return response.json()

def createPokemonDict(randomNumber):
    data=getData(randomNumber)
    id = data["id"]
    name = data["name"]
    height = data["height"]
    weight = data["weight"]
    pokemonDict={
        "id":id,
        "name":name,
        "height":height,
        "weight":weight
    }
    return pokemonDict


def listOfCards():
    listOfPokemonCards =[]
    for _ in range(10):
        randomNumber = randint(1, 151)
        getData(randomNumber)
        pokemonCard =createPokemonDict(randomNumber)
        listOfPokemonCards.append(pokemonCard)
    return listOfPokemonCards
# listOfCards()

# def displayCards():
#     cards= listOfCards()
#     print(cards)
#     print("Here are all your cards . Do you want to view a specific card?")
#     x= input()
#     while x=="yes":
#         print("select 1-10 to view")
#         number = int(input());
#         print(cards[number])
#         print("Do you want to view another card")
#         x = input()
#     return cards
def selectCard():
    cards = listOfCards()
    print(cards)
    print("Here are all your cards . Do you want to view a specific card?")
    x = input()
    while x == "yes":
        print("select 1-10 to view")
        number = int(input())-1
        print(cards[number])
        print("Do you want to view another card")
        x = input()
    print("which card would you like to select: 1-10")
    x=int(input())-1
    print("you have selected this card")
    print(cards[x])
    print("Which stat do you want to use: id, height or weight")
    stat = input();
    selected1 = cards[x].get(stat)
    print('You have selected stat : {} = {}'.format(stat, selected1))
    dict={
        stat:selected1
    }
    return dict

def selectCardPlayer2():
    cards = listOfCards()
    print(cards)
    print("Here are all your cards . Do you want to view a specific card?")
    x = input()
    while x == "yes":
        print("select 1-10 to view")
        number = int(input()) - 1
        print(cards[number])
        print("Do you want to view another card")
        x = input()
    print("which card would you like to select: 1-10")
    x = int(input()) - 1
    print("you have selected this card")
    print(cards[x])
    return cards[x]

def enterInfo():
    print('Enter your name:')
    x = input()
    print('Hello, ' + x)
    return x

def startGame():
    print("Hi Player 1")
    player1Name= enterInfo()
    statSelectedPlayer1 =selectCard()
    key, value=statSelectedPlayer1.popitem()
    print("Hi Player 2")
    player2Name= enterInfo()
    cardSelectedPlayer2=selectCardPlayer2()
    value1=value
    value2 =cardSelectedPlayer2.get(key)
    if value1>value2:
        print("{} won".format(player1Name))
    else:
        print("{} won".format(player2Name))
    print("{} got {} while {} got {}".format(player1Name,player2Name,value1,value2))

startGame()




