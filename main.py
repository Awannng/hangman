import random

attempts = 12
miss = 5
fruit = ("grape", "orange", "lemon", "mango")
sport = ("golf", "surfing", "skating", "boxing")
movie = ("it", "friends", "m3gan", "joker")
category = ['fruit', 'sport', 'movie']
word = ''
guess = ''
guessed_letter = []


def start_game():
    global word
    global attempts
    global miss
    global guess

    choice = random.choice(category)
    if choice == 'fruit':
        word = random.choice(fruit)
    elif choice == 'sport':
        word = random.choice(sport)
    else:
        word = random.choice(movie)

    print("Category of the guess word: ", choice)
    print_hint(word)
    dash = "_"*len(word)
    print(dash)

    while miss > 0:
        char = input("Enter a letter: ").lower()
        attempts -= 1
        print("You have {} attempts left".format(attempts))
        if char not in word:
            miss -= 1
            guessed_letter.append(char)
            check_miss()
            print("Guessed letter: ", guessed_letter)
        else:
            guess += char
            for i in word:
                if i in guess:
                    dash = "{}".format(i)
                    print(dash, end='')
                else:
                    dash = "_"
                    print(dash, end='')
            print()

        if len(guess) == len(word):
            print("Congratulation")
            break

        if attempts == 0 or miss == 0:
            game_over()

def check_miss():
    if miss == 4:
        print('''     
                     -------
                    |      |
                    |      |
                    |      o
                    |  
                    |
                    |
                   _|_
                ''')
    elif miss == 3:
        print('''     
                    -------
                    |      |
                    |      |
                    |      o
                    |      |
                    |
                    |
                   _|_
                ''')
    elif miss == 2:
        print('''     
                    -------
                    |      |
                    |      |
                    |      o
                    |      |
                    |      |
                    |
                   _|_
                ''')
    elif miss == 1:
        print('''     
                    -------
                    |      |
                    |      |
                    |      o
                    |      |
                    |      |
                    |     /
                   _|_
                ''')
    elif miss == 0:
        print('''     
                    -------
                    |      |
                    |      |
                    |      o
                    |      |
                    |      |
                    |     / \\
                   _|_
                ''')

def game_over():
    print("Sorry, you did not guess the word :(")

def print_hint(word):
    if word == 'grape':
        print("Hint: This can be turned into a wine")
    elif word == 'orange':
        print("Hint: This can be a color")
    elif word == 'lemon':
        print("Hint: This is sour and might be bitter")
    elif word == 'mango':
        print("Hint: This can also be called Mangifera indica")
    elif word == 'golf':
        print("Hint: This is to hit a ball into a hole")
    elif word == 'surfing':
        print("Hint: This is mostly practiced near beach")
    elif word == 'skating':
        print("Hint: This is on the ice")
    elif word == 'boxing':
        print("Hint: This is two people with gloves")
    elif word == 'it':
        print("Hint: This is in horror genre")
    elif word == 'friends':
        print("Hint: This is about friendship")
    elif word == 'm3gan':
        print("Hint: This is about AI horror")
    elif word == 'joker':
        print("Hint: This is inspired on Conrad Veidt")

def restart():
    global miss
    global guess
    global attempts
    global guessed_letter

    miss = 5
    guess = ''
    attempts = 12
    guessed_letter = []
    start_game()


print("Welcome to HangMan!!")
print("You have {} attempts and {} misses to guess the word, good luck!!".format(attempts, miss))
running = True
start_game()

while running:
    play_again = input("Do you want to play again? (yes or no)")
    if play_again == 'yes':
        restart()
    else:
        running = False
        print("Thank you for playing the game! :)")