import random
num=random.randint(1,100)
while True:
    n=int(input('Guess a number between 1-100: '))
    if n>num:
        print('Your number is larger. Try again')
    elif n<num:
        print('Your number is smaller. Try again')
    elif n==num:
        print('You guessed itcorrectly')
        break
    else:
        print('Invalid')