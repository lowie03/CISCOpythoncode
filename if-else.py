for m in range(0,4):
    password = input(str("Enter Password: "))
    if password == 'VERITAS':
        print('Welcome to VUNA')
        userName = input(str('What is your name? '))
        lvl = input(str('What level are you? '))
        course = input(str('What course are you studying? '))
        if lvl == 100:
          print('congratulation', userName,)
        if lvl == 200:
            print('Do well to study hard')
    else:
        print('failed')
    continue
print('try again in an hour time')


#create a guessing game, input a word you want the user to spell, if the person user fails 3 attempts
#game over, if he gets it, he passes the level (every level is 2 point), the level changes till the person
#fails and put together the general score

