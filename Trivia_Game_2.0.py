score = 0

# correct answers
answer1_correct = "strawberry", "strawberries"
answer2_correct = "alaska"
answer3_correct = "anglet"
answer4_correct = "big toe"
answer5_correct = "hot water"
answer6_correct = "skin"
answer7_correct = "flamboyance"
answer8_correct = "url"
answer9_correct = "summer solstice"
answer10_correct = "honey"
answer_bonus_correct = "1945"

def ask_question(question, hint):
    while True:
        print("\n" + question)
        print("1. Answer the question")
        print("2. Get a hint")
        print("3. Skip the question")

        choice = input("Enter your choice (1, 2, or 3): ").strip()

        if choice == "1":
            return input("Your answer: ").strip().lower()
        elif choice == "2":
            print(f"Hint: {hint}")
        elif choice == "3":
            return ""
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
#Questions
answer1 = ask_question("What fruit has seeds on the outside?", "It's red and often used in desserts.")
if answer1 == "":
    print("Question skipped.")
elif any(a in answer1.lower() for a in answer1_correct):
    print("Correct!")
    score += 1
else:
    print("That is incorrect.")
    try_again = input("Would you like to try again? (Y or N): ").strip().lower()
    if try_again == "yes" or try_again == "y":
        answer1 = input("Your answer: ").strip().lower()
        if answer1 == "":
            print("Question skipped.")
        elif any(a in answer1.lower() for a in answer1_correct):
            print("Correct!")
            score += 1
        else:
            print(f"Sorry, the correct answer is: {', '.join(answer1_correct).capitalize()}!")
            print("Moving on to the next question.")
    else:
        print(f"Sorry, the correct answer is: {', '.join(answer1_correct).capitalize()}!")
        print("Moving on to the next question.")
answer2 = ask_question("Which US state has the longest coastline?", "It's the largest state by area.")
if answer2 == "":
    print("Question skipped.")
elif answer2_correct in answer2.lower():
    print("Correct!")
    score += 1 
else:
    print("That is incorrect.")
    try_again = input("Would you like to try again? (Y or N): ").strip().lower()
    if try_again == "yes" or try_again == "y":
        answer2 = input("Your answer: ").strip().lower()
        if answer2 == "":
            print("Question skipped.")
        elif answer2_correct in answer2.lower():
            print("Correct!")
            score += 1
        else:
            print(f"Sorry, the correct answer is: {answer2_correct.capitalize()}!")
            print("Moving on to the next question.")
    else:
        print(f"Sorry, the correct answer is: {answer2_correct.capitalize()}!")
        print("Moving on to the next question.")