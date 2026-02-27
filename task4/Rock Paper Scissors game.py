import random

# Welcome the player nicely
print("\n" + "🌟"*25)
print("\n    HEY THERE! Let's play Rock-Paper-Scissors! 🎮\n")
print("🌟"*25)

print("\nHere's a quick reminder:")
print("   ✊ Rock smashes ✂️ Scissors")
print("   ✋ Paper covers ✊ Rock")
print("   ✂️ Scissors cut ✋ Paper\n")

# Set up the scores
user_score = 0
computer_score = 0

# Let's play multiple rounds!
playing = True

while playing:
    # Ask the user what they want to pick
    print("\n" + "-"*40)
    user_choice = input("What do you pick? (rock, paper, or scissors): ").lower().strip()
    
    # Make sure they enter a valid choice
    while user_choice not in ['rock', 'paper', 'scissors', 'r', 'p', 's']:
        print("Oops! That's not a valid choice. Try again! 😊")
        user_choice = input("Pick rock, paper, or scissors: ").lower().strip()
    
    # Convert short forms to full words
    short_forms = {'r': 'rock', 'p': 'paper', 's': 'scissors'}
    if user_choice in short_forms:
        user_choice = short_forms[user_choice]
    
    # Computer picks something random
    options = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(options)
    
    # Show what everyone picked
    print("\n" + "="*40)
    print(f"You picked:  {user_choice}")
    print(f"Computer picked: {computer_choice}")
    print("="*40)
    
    # Figure out who won
    if user_choice == computer_choice:
        print("\n🤝 It's a tie! We both picked the same thing!")
        
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        print(f"\n🎉 Yay! You won! {user_choice} beats {computer_choice}!")
        user_score += 1
        
    else:
        print(f"\n😢 Oh no! {computer_choice} beats {user_choice}. Computer wins!")
        computer_score += 1
    
    # Show current score
    print(f"\n📊 SCORE: You = {user_score} | Computer = {computer_score}")
    
    # Ask if they want to keep playing
    print("\n" + "-"*40)
    again = input("Want to play again? (yes/no): ").lower().strip()
    
    # Check if they want to quit
    if again not in ['yes', 'y', 'yeah', 'yep']:
        playing = False
        
        # Show final score and goodbye message
        print("\n" + "🎉"*20)
        print("\n   GAME OVER! Thanks for playing! 🎉\n")
        
        if user_score > computer_score:
            print(f"🏆 FINAL SCORE: You {user_score} - {computer_score} Computer")
            print("   Congratulations! You are the champion! 🎊\n")
        elif user_score < computer_score:
            print(f"🏆 FINAL SCORE: You {user_score} - {computer_score} Computer")
            print("   Better luck next time! 💪\n")
        else:
            print(f"🏆 FINAL SCORE: You {user_score} - {computer_score} Computer")
            print("   It's a tie! Great game! 🤝\n")
        
        print("🎉"*20 + "\n")

print("Hope to see you again soon! Have a great day! 👋")
