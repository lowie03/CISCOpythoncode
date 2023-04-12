userName = input(str('Enter your name: '))
#\033[1m***\033[0m used to bolden a word.
print('\033[1m Hey there', userName, 'welcome to L\'ounge special guessing game\033[0m.\n'
    'You have just one trail for each game.\nQuestions can be brought from any concept.\n'
    'Each level carries 2 points and at the end of the game your scores are counted.')
print('Note: \033[1mlet all your answers begin in capital letter. (Example: Voice)\033[0m')
print('LEVEL 1')

def level1():
    totalScore = 0
    question_1 = input(str("What 5 letter word used to exchange pleasantries?\n"))
    if question_1 == 'Hello':
       print('congratulations')
       totalScore += 2
    else:
         print('your total score is', totalScore, 'try again')
         level1()

print(level1())

print('LEVEL 2')
def level2():
    totalScore = 2
    question_2 = input(str("What state in Nigeria is vast in agriculture?\n "))
    if question_2 == 'Yobe':
        print('congratulations')
        totalScore += 2
    else:
        print('your total score is', totalScore, 'try again')
        level1()

print(level2())

print('LEVEL 3')
def level3():
    totalScore = 4
    question_3 = input(str("Who was the first president of Nigeria?\n "))
    if question_3 == 'Abubakar Tafawa Balewa':
        print('congratulations')
        totalScore += 2
    else:
        print('your total score is', totalScore, 'try again')
        level1()
print(level3())

print('LEVEl 4')
def level4():
    totalScore = 6
    question_4 = input(str("What country has the most powerful and strongest army in the world\n"))
    if question_4 == 'United States':
        print('congratulations')
        totalScore += 2
    else:
        print('your total score is', totalScore, 'try again')
        level1()

print(level4())

print('LEVEL 5')
def level5():
    totalScore = 8
    question_5 = input(str("What country is pop music from?\n"))
    if question_5 == 'United States' or 'United Kingdom':
        print('congratulations')
        totalScore += 2
    else:
        print('your total score is', totalScore, 'try again')
        level1()

print(level5())

print('LEVEL 6')
def level6():
    totalScore = 10
    question_6 = input(str("What is the most used and downloaded application\n"))
    if question_6 == 'Tiktok':
        print('congratulations')
        totalScore += 2
    else:
        print('your total score is', totalScore, 'try again')
        level1()

print(level6())


print('LEVEL 7')
def level7():
    totalScore = 12
    question_7 = input(str("What is the motto of Veritas university\n"))
    if question_7 == 'Seeking the truth':
        print('congratulations')
        totalScore += 2
    else:
        print('your total score is', totalScore, 'try again')
        level1()

print(level7())