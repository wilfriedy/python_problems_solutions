import random

while True:
    numbers = list('1234567890')
    random.shuffle(numbers)
    MAX_GUESS = 5
    secret = '981'
    user_guess = ''
    # for i in range(3):
    #     secret += numbers[i]
    # print(secret)
    attempts = 1
    while attempts <= MAX_GUESS:
        responses = []
        print(f"Guess the secret number : {attempts} guesses")
        user_guess = input('> ')
        if len(user_guess) < len(secret) or not user_guess.isdecimal() or len(user_guess) > len(secret):
            print(f"Here is a clue the secret is {len(secret)} numbers long")
        else:
            if user_guess == secret:
                print(f"Congratulations you guessed the secret {secret}")
                break
            else:
                for i in range(len(secret)):
                    if user_guess[i] == secret[i]:
                        responses.append('Fermi')
                    elif user_guess[i] in secret:
                        responses.append('Pico')
                    else:
                        responses.append('Bagels')
                    # if i in secret:
                    #     if user_guess.index(i) == secret.index(i):
                    #         responses.append('Fermi')
                    #     else:
                    #         responses.append('Pico')
                    # else:
                    #     responses.append('Bagels')
                print(responses)
            attempts += 1
    if not input(f"The secret was {secret} \nWould you like to play again ? (Yes(y) or No(n) > ").lower().startswith('y'):
        break




# In Bagels, a deductive logic game, you
# must guess a secret three-digit number
# based on clues. The game offers one of
# the following hints in response to your guess:
# “Pico” when your guess has a correct digit in the
# wrong place, “Fermi” when your guess has a correct
# digit in the correct place, and “Bagels” if your guess
# has no correct digits. You have 10 tries to guess the
# secret number.

# How It Works
# Keep in mind that this program uses not integer values but rather string
# values that contain numeric digits. For example, '426' is a different value
# than 426. We need to do this because we are performing string comparisons
# with the secret number, not math operations. Remember that '0' can be
# a leading digit: the string '026' is different from '26', but the integer 026 is
# the same as 26.

