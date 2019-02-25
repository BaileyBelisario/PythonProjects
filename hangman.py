def addplayers(num_player):
    players = {}
    for x in range(num_player):
        new_player = input("Enter the player's name: ")
        players[new_player] = 0
    return players
        
def blank_list(guess_word):
    clear_list = []
    for x in range(len(guess_word)):
        clear_list.append("_ ")
    return clear_list

def guess(player_list, guess_char, clear_list, guess_word):
    return clear_list

def check(guess_char, guessed_letters):
    while guess_char in guessed_letters:
        guess_char = input("Enter a letter: ")
    return guess_char
def checkphrase(guess_char, guessed_letters):
    while guess_char in guessed_letters:
        guess_char = input("Enter a letter: ")
    return guess_char

def main():
    print("\n\n====Welcome to Hangman====\n")
    num_player = int(input("How many players: "))
    guess_word = list("hello")

    guessed_letters = []
    guessed_phrases = []
    player_list = addplayers(num_player)

    clear_list = blank_list(guess_word)

    while not clear_list == guess_word:
        for key, value in player_list.items():
            print(" ".join(clear_list))
            print(guessed_letters)
            print("Guessed Letters: ", end='')
            print_list = ' '.join(set(guessed_letters))
            print(print_list.upper())
            
            print(key)
            
            guess_char = input("Enter a letter: ")
                
            if guess_char in guessed_letters:
                print("LETTER USED\nGUESS AGAIN!!!")
                check(guess_char, guessed_letters)
                clear_list = guess(player_list, guess_char, clear_list, guess_word)
                guessed_letters.append(''.join(guess_char))
            elif len(guess_char) > 1:
                clear_list = guess(player_list, guess_char, clear_list, guess_word)
                guess_char = guess_char.split()
                guessed_phrases += guess_char
                checkphrase(guess_char, guessed_phrases)
            else:
                clear_list = guess(player_list, guess_char, clear_list, guess_word)
                guessed_letters.append(''.join(guess_char))
            
            if clear_list == guess_word:
                break


if __name__ == '__main__':
    main()
