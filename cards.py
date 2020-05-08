"""
Program: cards.py
Programmer: Michael Harris
Date: November 8th, 2019
Version: 0
Build a card game
"""
from random import randint as rng
from random import shuffle
import os

#Lists and declarations
values = ["A","2","3","4","5","6","7","8","9","1","J","Q","K"]
suits = ["S","C","H","D"]
deck = []
card = None

#Dictionaries
valueDict = {
	"A": "Ace",
	"2": "Two",
	"3": "Three",
	"4": "Four",
	"5": "Five",
	"6": "Six",
	"7": "Seven",
	"8": "Eight",
	"9": "Nine",
	"1": "Ten",
	"J": "Jack",
	"Q": "Queen",
	"K": "King"
}

suitDict = {
	"S": "Spades",
	"C": "Clubs",
	"H": "Hearts",
	"D": "Diamonds"
}

#Building the deck, then shuffling it.
for v in values:
	for s in suits:
		deck.append(v+s)
shuffle(deck)

#Function for clearing screen
def clear():
	if os.name == "nt":
		os.system("cls")
	else:
		os.system("clear")
		
#Function that draws a card, and, if possible, places old card at bottom of deck
def draw():
	global card
	try:
		deck.append(card)
	except NameError:
		pass
	card = deck.pop(0)

#Choice Checker
def checkChoice(answer, choice):
	if choice == answer:
		return True
	elif choice != answer:
		gameStart()

#Winner function
def win():
	clear()
	input(f"You won! The card is the {valueDict[card.value]} of {suitDict[card.suit]}!\n(Press ENTER to play again)")
	gameStart()

#Value functions
def gameStart():
	draw()
	clear()
	choice = input("(1) Greater than eight\n(2) Eight and lower\nEnter Choice: ")
	if card.value in values[8:]:
		if checkChoice("1", choice):
			greaterThanEight()
	elif card.value in values[:8]:
		if checkChoice("2", choice):
			lessThanEight()

def greaterThanEight():
	clear()
	choice = input("(1) Nine, ten and jack\n(2) Queen and king\nEnter Choice: ")
	if card.value in values[8:11]:
		if checkChoice("1", choice):
			nineTenJack()
	elif card.value in values[11:]:
		if checkChoice("2", choice):
			queenKing()

def lessThanEight():
	clear()
	choice = input("(1) One, two, three and four\n(2) Five, six, seven and eight\nEnter Choice: ")
	if card.value in values[:4]:
		if checkChoice("1", choice):
			oneTwoThreeFour()
	elif card.value in values[4:8]:
		if checkChoice("2", choice):
			fiveSixSevenEight()

def nineTenJack():
	clear()
	choice = input("(1) Nine\n(2) Ten\n(3) Jack\nEnter Choice: ")
	if card.value in values[8]:
		if checkChoice("1", choice):
			suitStart()
	elif card.value in values[9]:
		if checkChoice("2", choice):
			suitStart()
	elif card.value in values[10]:
		if checkChoice("3", choice):
			suitStart()

def queenKing():
	clear()
	choice = input("(1) Queen\n(2) King\nEnter Choice: ")
	if card.value in values[11]:
		if checkChoice("1", choice):
			suitStart()
	elif card.value in values[12]:
		if checkChoice("2", choice):
			suitStart()

def oneTwoThreeFour():
	clear()
	choice = input("(1) One and two\n(2) Three and four\nEnter Choice: ")
	if card.value in values[0:2]:
		if checkChoice("1", choice):
			oneTwo()
	elif card.value in values[2:4]:
		if checkChoice("2", choice):
			threeFour()

def fiveSixSevenEight():
	clear()
	choice = input("(1) Five and six\n(2) Seven and eight\nEnter Choice: ")
	if card.value in values[4:6]:
		if checkChoice("1", choice):
			fiveSix()
	elif card.value in values[6:8]:
		if checkChoice("2", choice):
			sevenEight()

def oneTwo():
	clear()
	choice = input("(1) One\n(2) Two\nEnter Choice: ")
	if card.value in values[0]:
		if checkChoice("1", choice):
			suitStart()
	elif card.value in values[1]:
		if checkChoice("2", choice):
			suitStart()

def threeFour():
	clear()
	choice = input("(1) Three\n(2) Four\nEnter Choice: ")
	if card.value in values[2]:
		if checkChoice("1", choice):
			suitStart()
	elif card.value in values[3]:
		if checkChoice("2", choice):
			suitStart()

def fiveSix():
	clear()
	choice = input("(1) Five\n(2) Six\nEnter Choice: ")
	if card.value in values[4]:
		if checkChoice("1", choice):
			suitStart()
	elif card.value in values[5]:
		if checkChoice("2", choice):
			suitStart()

def sevenEight():
	clear()
	choice = input("(1) Seven\n(2) Eight\nEnter Choice: ")
	if card.value in values[6]:
		if checkChoice("1", choice):
			suitStart()
	elif card.value in values[7]:
		if checkChoice("2", choice):
			suitStart()

#Suit Functions
def suitStart():
	clear()
	choice = input("(1) Black\n(2) Red\nEnter Choice: ")
	if card.suit in suits[:2]:
		if checkChoice("1", choice):
			black()
	elif card.suit in suits[2:]:
		if checkChoice("2", choice):
			red()

def black():
	clear()
	choice = input("(1) Spades\n(2) Clubs\nEnter Choice: ")
	if card.suit in suits[0]:
		if checkChoice("1", choice):
			win()
	elif card.suit in suits[1]:
		if checkChoice("2", choice):
			win()

def red():
	clear()
	choice = input("(1) Hearts\n(2) Diamonds\nEnter Choice: ")
	if card.suit in suits[2]:
		if checkChoice("1", choice):
			win()
	elif card.suit in suits[3]:
		if checkChoice("2", choice):
			win()

print("Welcome to the card guessing game! Your goal is to answer the questions to guess the card.")
gameStart()