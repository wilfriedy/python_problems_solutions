num_digits = 3
max_guess = 10
secrets = "100"
while True:
    guess = ''
    attemps = 1

    while attemps <= max_guess:
            print(f"Guess {attemps}")
            guess = input('> ')

            if len(guess) == num_digits and guess.isdecimal():
                if guess == secrets:
                    print('Congrats')
                    break

            attemps += 1


    print('Do you want to play again ? (yes or no)')
    if not input(' >').lower().startswith('y'):
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

