import random
target_num, guess_num = random.randint(1, 10), 0
while target_num != guess_num:
    guess_num = int(input('Guess the number (Below 10) : '))
print('Well guessed!')
