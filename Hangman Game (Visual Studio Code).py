import random
import time

#Steps to invite to game
print("\nWelcome to Hangman game by Aquil\n")
name=input("Enter your name:")
print("\nWelcome\t",name,".Best of Luck!\n")
time.sleep(2)
print("The game is about to start!\nLet's play Hangman.\n")
time.sleep(3)
def main():
    global count
    global display
    global word
    global already_guessed
    global length
    global play_game
    global guess_word
    words_to_guess=["image","film","promise","kids","lungs","rhyme","plants"]
    word= guess_word=random.choice(words_to_guess)
    length=len(word)
    count=0
    display="*" * length
    already_guessed=[]
    play_games=""

#Loop to restart game when one round ends
def play_loop():
    global play_game
    play_game=input("\nDo you want to play again?\n Y=Yes, N=No\n")
    while play_game not in ["Y","y","N","n"]:
        play_game=input("\nDo you want to play again?\n Y=Yes, N=No\n")
    if play_game == "y" or play_game == "Y":
        main()
    elif play_game == "n" or play_game == "N":
        print("\nThanks for Playing!\n")
        exit()
    
#Initial conditions for Hangman game
def hangman():
    global count
    global display
    global word
    global already_guessed
    global length
    global play_game
    global guess_word
    limit = 5
    guess=input("\nThis is your Hangman word:"+display+"\nEnter your guess:")
    guess=guess.strip()
    if len(guess.strip())==0 or len(guess.strip())>=2 or guess<="9":
        print("\nInvalid Input! Try a letter\n")
        hangman()
    elif guess in word: 
        already_guessed.extend([guess])
        index= word.find(guess)
        word=word[:index]+'_'+word[index+1:]
        display=display[:index]+guess+display[index+1:]
        print("\nWell Done! Your guess is right!\n")
        print(display,"\n")
        index=''
    elif guess in already_guessed:
        print("Letter already guessed! Try another letter!\n")
    else:
        count+=1
        if count==1:
            time.sleep(1)
            print("   _______\n"
                  "  |       |\n"
                  "  |       \n"
                  "  |       \n"
                  "  |       \n"
                  "  |       \n"
                  "  |       \n"
                  "__|__\n")
            print("Wrong Guess!\t"+ str(limit-count)+ "\tguesses remaining!\n")
        elif count==2:
            time.sleep(1)
            print("   _______ \n"
                  "  |       |\n"
                  "  |       |\n"
                  "  |        \n"
                  "  |        \n"
                  "  |        \n"
                  "__|__\n")
            print("Wrong Guess!\t"+ str(limit-count)+ "\tguesses remaining!\n")
        elif count ==3:
            time.sleep(1)
            print("   _______ \n"
                  "  |       |\n"
                  "  |       |\n"
                  "  |       O\n"
                  "  |        \n"
                  "  |        \n"
                  "__|__\n")
            print("Wrong Guess!\t"+ str(limit-count)+ "\tguesses remaining!\n")
        elif count==4:
            time.sleep(1)
            print("   _______ \n"
                  "  |       |\n"
                  "  |       |\n"
                  "  |       O \n"
                  "  |      /|\ \n"
                  "  |        \n"
                  "__|__\n")
            print("Wrong Guess!\t"+ str(limit-count)+ "\tguesses remaining!\n")
        elif count ==5:
            time.sleep(1)
            print("   _______ \n"
                  "  |       |\n"
                  "  |       |\n"
                  "  |       O\n"
                  "  |      /|\ \n"
                  "  |      / \ \n"
                  "__|__\n")
            print("Wrong Guess! You are hanged. GAME OVER!!!\n")
            print("Your word was: ",guess_word)
            play_loop()
    
    if word == '_'*length:
        print("\nCongratulations!!! You have guessed the word correctly!\n")
        play_loop()

    elif count!=limit:
        hangman()
main()
hangman()


        

                 
                    
            
            
            
            
                         

    



