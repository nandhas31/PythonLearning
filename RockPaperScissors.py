import random
plays = ['rock', 'paper', 'scissors']

def comparator(comp, user):
    if (comp == user):
        print('There is a tie!')
    elif ((plays.index(comp) == 2) and (plays.index(user) == 0)):
        print ('You Win!')
    elif ((plays.index(comp)) == 0 and (plays.index(user) == 2)):
        print ('You Lose!')
    elif (plays.index(comp) > plays.index(user)):
        print ('You Lose!')
    else:
        print ('You Win!')

keepPlaying = True
while (keepPlaying):
    userChoice = int(input('Enter 1 for rock, 2 for paper, and 3 for scissors: '))
    userPlay = plays[userChoice-1]
    computerChoice = random.randrange(1,4)
    computerPlay = plays[computerChoice-1]
    print('You played ' + userPlay + ', computer played ' + computerPlay)
    comparator(computerPlay, userPlay)
    keepPlayingPrompt = input('Would you like to quit? (y/n)')
    if (keepPlayingPrompt == 'y'):
        keepPlaying = False
    


    
