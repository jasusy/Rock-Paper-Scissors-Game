import time
from random import randint

def comp_play():
	#1, for rock, 2 for paper, 3 for scissors
	val = randint(1, 3)
	return val

def play_hand(comp, you):
	compChoice = ['rock', 'paper', 'scissors'];
	if compChoice[comp-1] == you:
		winner = 'tie'
	elif (comp == 1 and you == 'scissors') or(comp == 3 and you == 'paper') \
		or(comp == 2 and you =='rock'):
		winner = 'computer'
	else:
		winner = 'you'
	return winner

def play_game():
	playing = True
	comp_wins = 0
	you_wins = 0
	tie_wins = 0
	print("Let's start Rock, Paper and Scissors game!")
	while playing:
		print ("-------------------------")
		try:
			you = input("Type 'rock', 'paper', 'scissors' or 'quit' to end game ")
		except:
			print ('Invalid entry, please try again')
			continue

		you = you.lower()
		if you == 'quit':
			if you_wins > comp_wins:
				print("You beat the computer! you: %d / computer: %d, ties:  %d" %(you_wins, comp_wins, tie_wins))
			elif comp_wins > you_wins:
				print("The computer beat you! computer: %d / you: %d, ties : %d" %(comp_wins, you_wins, tie_wins))
			else :
				print("Finally ended in a draw! computer: %d / you: %d, ties : %d" %(comp_wins, you_wins, tie_wins))
			break
		elif you == 'paper' or you == 'scissors' or you == 'rock':
			comp = comp_play()
			winner = play_hand(comp, you)
			print ("The computer played %s, and you played %s" %(comp, you))
		else:
			print('Invalid entry, please try again')
			continue
		
		if winner == 'tie':
			print("It is a tie!")
			tie_wins += 1
		elif winner == 'computer':
			print("The computer wins!")
			comp_wins += 1
		elif winner == 'you':
			print ("You won!")
			you_wins += 1
	print()

play_game()