import random

wordlist = ['admire', 'gesture',\
            'phenomenon','ultimate','power','dedication','passion']
randword = random.choice(wordlist)
# print(randword)
count = 5

temp =''
guessed = ''
dash_value = len(randword)
space_value = dash_value - 1
print('Its a ',dash_value,'letter word')

for dash in range(dash_value):
    for space in range(space_value):
        print('_', end ='')
    print(' ',end='')

while count>=1:
    print()
    guess = input("Make a Guess: ")
    if len(guess) != 1:
        print('Guess one letter at a time')
    elif guess not in 'abcdefghijklmnopqrstuvwxz':
        print('Only letters are allowed')
    guessed += guess
    print(guessed)
    if guess in randword:
        temp = temp +guess
        print('Correct' )
    else:
        count -= 1
        print('Guess is incorrect!', count, 'more attempts left')
    # if guess not in randword:
    #     count -= 1
    #     print('Guess is incorrect!', count, 'more attempts left')
    newBlanks =' '.join(c if c in guessed else '_' for c in randword)
    print('Word:', newBlanks)

    if temp == randword:
        print('Congratulations')
        break

# i=6
# while i >=1:
#     print(i)
#     i -=1