import random

random_number = random.randint(1, 100)
guess = 0
guess_count = 0
last_guess = 0

while random_number != guess:
    guess = int(input('Guess a number between 1 and 100: '))
    if guess < 1 or guess > 100:
        print('OUT OF BOUNDS')

    elif guess_count == 0:
        if random_number - guess < 10:
            print('Warm')
            guess_count += 1
            last_guess = guess
        else:
            print('Cold')
            guess_count += 1
            last_guess = guess

    elif abs(random_number - guess) < abs(random_number - last_guess):
        print('Warmer')
        guess_count += 1
        last_guess = guess

    else:
        print('Colder')
        guess_count += 1
        last_guess = guess

print(f'You guessed correctly, it took {guess_count} tries.')
input()
