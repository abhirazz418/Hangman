# Name:- Abhay Kumar Modi

import random
import string
def choose_word():
	file=open("wordlist.txt",'r')
	s=file.readline()
	wordlist=s.split()
	return random.choice(wordlist)

def is_word(s,r):
	if(r==s):
		return True
	else:
		return False

def main():
	guessTaken=0
	k=0
	m=0
	print("Hello! Welcome to the game 'Hangman':")
	print("Enter your Name:")
	myName=str(input())
	print(f"Well {myName},Let's Play the game!")
	print("I am going to select a word!")
	r=choose_word()
	l=len(r)
	print("1.Easy \n2.Medium \n3.Hard")
	z=int(input("Enter the choice of level '1 for Easy' '2 for Medium' '3 for Hard' :-"))
	if(z==1):
		n=20
		print(f"You have {n} chances to Guess what i have thought.\nIf you succedd to guess thr right word then you will win or otherwise you will loose.")
	elif(z==2):
		n=15
		print(f"You have {n} chances to Guess what i have thought.\nIf you succedd to guess thr right word then you will win or otherwise you will loose.")
	elif(z==3):
		n=10
		print(f"You have {n} chances to Guess what i have thought.\nIf you succedd to guess thr right word then you will win or otherwise you will loose.")
	else:
		print("Enter a valid code for selection of level")

	list1=[]
	list2=[]
	for i in range(0,l):
		list1.append(r[i])
		list2.append('_')
	while (guessTaken<n):
		print("Take a guess. What is in my mind")
		guess=str(input())
		guessTaken=guessTaken+1
		if(len(guess)!=1):
			result=is_word(guess,r)
			if(result==True):
				print(f"Congratulations!!! {myName},you have a sharp mind.you have cracked it what i have guessed in just {guessTaken} guesss!")
			else:
				print(f"Nopes! {myName},your guess is not matched,you have left {n-guessTaken} chances left")
		else:
			for i in range(0,l):
				if(list1[i]==guess):
					k+=1
			if(k>0):
				for i in range(0,l):
					if(list1[i]==guess):
						list2[i]=guess
				if(list1!=list2):
					for i in range(0,l):
						if(list2[i]!='_'):
							m+=1
					if(m>0):
						print(f"{list2} \nyou are close to the answer. You have {n-guessTaken} chances left")
				else:
					print(f"Congratulations!!! {myName},you have a sharp mind.you have cracked it what i have guessed in just {guessTaken} guesss!")
			else:
				print(f"{myName}, the letter you have entered that is not in present in the word! \n you have now only {20-guessTaken} chances left")
	if(guess!=r):
		print(f"Nope!,{myName} you loose the game")
main()
input("Press <enter> key to quit game")