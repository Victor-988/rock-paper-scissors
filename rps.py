# name
# Rock paper scissor
# variables
import random
pScore = 0
cScore = 0
ties = 0
computerChoices = ["r", "p", "s"]

# Welcome message 
# print the message
print("welcome to Rock Paper Scissors")
#prompt for players name
pName = input("what is your name?")



# Final score
def printScore():
# write message
 print("The score is: ")
#Write players score
print(pName + ": " + str(pScore))
# write computer score
print("computer: " + str(cScore))
print("Ties: " + str(ties))

# game loop
# make a forever loop
while True:
# Print current score
 printscore()
#Prompt for a choice (r(rock), p (paper), s(scissors), q(quit))
pChoice = input("enter r (Rock), p (paper), s (scissors) or q (to quit):")
# deal with player enterring q
if pChoise == "q":
	  break 
# get random computer choice ( random)
cchoice = random.choice(computerChoices)

# compare for player entering r 
if pChoice == "r":
	print(pName + " picked Rock")
	#if compuer is r
	if cChoice == "r":
		print("computer picked rock")
		print("This is a tie")
		ties = ties + 1
		# if computer is p 
	elif cChoice == "p":
		print("Computer picked  paper")
		print("Paper covers rock")
		cScore = cScore + 1
		#if computer is s 
	else:
		Print("computer picked scissors")
		print("rock breaks scissors")
		pScore = pScore + 1 
# compare for player entering p 
elif pChoice == "p":
	pass 
	# compare for player entering s 
	elif pChoice == "s":
	pass 