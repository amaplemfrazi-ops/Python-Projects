# Trivia Game V2_Built by Amanda
# Features: menu system, hints, double or nothing bonus question, and more user-friendly input handling
import threading

def show_hint_after_delay(hint, delay=20):
    timer = threading.Timer(delay, lambda: print(f"\nHint: {hint}\n"))
    timer.start()
    return timer

score = 0

# correct answers
answer1_correct = ["strawberry", "strawberries"]
answer2_correct = "alaska"
answer3_correct = "aglet"
answer4_correct = "big toe"
answer5_correct = ["hot water", "hot", "hot water freezes faster than cold water"]
answer6_correct = "skin"
answer7_correct = "flamboyance"
answer8_correct = "uniform resource locator"
answer9_correct = "summer solstice"
answer10_correct = "honey"
answer_bonus_correct = "1945"

def ask_question(question, hint):
    while True:
        print("\n" + question)
        print("")
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
answer1 = ask_question("1. What fruit has seeds on the outside?", "It's red and often used in desserts.")
if answer1 == "":
    print("Question skipped.")
elif any(a in answer1.lower() for a in answer1_correct):
    print("Correct!")
    score += 1
else:
    print("That is incorrect.")
    try_again = input("Would you like to try again with a hint? (Y or N): ").strip().lower()
    if try_again == "yes" or try_again == "y":
        answer1 = input("Hint: It's red and often used in desserts... Your answer: ").strip().lower()
        if answer1 == "":
            print("Question skipped.")
        elif any(a in answer1.lower() for a in answer1_correct):
            print("Correct!")
            score += 1
        else:
            print(f"Sorry, the correct answer is: {answer1_correct[0].capitalize()}!")
            print("Moving on to the next question.")
    else:
        print(f"Sorry, the correct answer is: {answer1_correct[0].capitalize()}!")
        print("Moving on to the next question.")
answer2 = ask_question("2. Which US state has the longest coastline?", "It's the largest state by area.")
if answer2 == "":
    print("Question skipped.")
elif answer2_correct in answer2.lower():
    print("Correct!")
    score += 1 
else:
    print("That is incorrect.")
    try_again = input("Would you like to try again with a hint? (Y or N): ").strip().lower()
    if try_again == "yes" or try_again == "y":
        answer2 = input("Hint: It's the largest state by area... Your answer: ").strip().lower()
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
answer3 = ask_question("3. What is the name of the plastic tip on the end of a shoelace?", f"It starts with the letter {answer3_correct[0]}.")
if answer3 == "":
    print("Question skipped.")
elif answer3_correct in answer3.lower():
    print("Correct!")
    score += 1
else:
    print("That is incorrect.")
    try_again = input("Would you like to try again with a hint? (Y or N): ").strip().lower()
    if try_again == "yes" or try_again == "y":
        answer3 = input(f"Hint: It starts with the letter {answer3_correct[0]}... Your answer: ").strip().lower()
        if answer3 == "":
            print("Question skipped.")
        elif answer3_correct in answer3.lower():
            print("Correct!")
            score += 1
        else:
            print(f"Sorry, the correct answer is: {answer3_correct.capitalize()}!")
            print("Moving on to the next question.")
    else:
        print(f"Sorry, the correct answer is: {answer3_correct.capitalize()}!")
        print("Moving on to the next question.")
answer4 = ask_question("4. In human anatomy, what does the 'hallux' refer to?", "It helps with balance when you walk.")
if answer4 == "":
    print("Question skipped.")
elif answer4_correct in answer4.lower():
    print("Correct!")
    score += 1
else:
    print("That is incorrect.")
    try_again = input("Would you like to try again with a hint? (Y or N): ").strip().lower()
    if try_again == "yes" or try_again == "y":
        answer4 = input("Hint: It helps with balance when you walk... Your answer: ").strip().lower()
        if answer4 == "":
            print("Question skipped.")
        elif answer4_correct in answer4.lower():
            print("Correct!")
            score += 1
        else:
            print(f"Sorry, the correct answer is: {answer4_correct.capitalize()}!")
            print("Moving on to the next question.")
    else:
        print(f"Sorry, the correct answer is: {answer4_correct.capitalize()}!")
        print("Moving on to the next question.")
answer5 = ask_question("5. Which freezes faster: hot or cold water?", "It's a counterintuitive phenomenon that has been observed for centuries.")
if answer5 == "":
    print("Question skipped.")
elif any (a in answer5.lower() for a in answer5_correct):
    print("Correct!")
    score += 1
else:
    print("That is incorrect.")
    try_again = input("Would you like to try again with a hint? (Y or N): ").strip().lower()
    if try_again == "yes" or try_again == "y":
        answer5 = input("Hint: t's a counterintuitive phenomenon that has been observed for centuries... Your answer: ").strip().lower()
        if answer5 == "":
            print("Question skipped.")
        elif any (a in answer5.lower() for a in answer5_correct):
            print("Correct!")
            score += 1
        else:
            print(f"Sorry, the correct answer is: {answer5_correct[0].capitalize()}!")
            print("Moving on to the next question.")
    else:
        print(f"Sorry, the correct answer is: {answer5_correct[0].capitalize()}!")
        print("Moving on to the next question.")
answer6 = ask_question("6. What is the largest organ in the human body?", "It's also the body's first line of defense against pathogens.")
if answer6 == "":
    print("Question skipped.")
elif answer6_correct in answer6.lower():
    print("Correct!")
    score += 1
else:
    print("That is incorrect.")
    try_again = input("Would you like to try again with a hint? (Y or N): ").strip().lower()
    if try_again == "yes" or try_again == "y":
        answer6 = input("Hint: It's also the body's first line of defense against pathogens... Your answer: ").strip().lower()
        if answer6 == "":
            print("Question skipped.")
        elif answer6_correct in answer6.lower():
            print("Correct!")
            score += 1
        else:
            print(f"Sorry, the correct answer is: {answer6_correct.capitalize()}!")
            print("Moving on to the next question.")
    else:
        print(f"Sorry, the correct answer is: {answer6_correct.capitalize()}!")
        print("Moving on to the next question.")
answer7 = ask_question("7. What is the term for a group of flamingos?", "It's a flamboyant word that matches the birds' vibrant appearance.")
if answer7 == "":
    print("Question skipped.")
elif answer7_correct in answer7.lower():
    print("Correct!")
    score += 1
else:
    print("That is incorrect.")
    try_again = input("Would you like to try again with a hint? (Y or N): ").strip().lower()
    if try_again == "yes" or try_again == "y":
        answer7 = input("Hint: It's a flamboyant word that matches the birds' vibrant appearance... Your answer: ").strip().lower()
        if answer7 == "":
            print("Question skipped.")
        elif answer7_correct in answer7.lower():
            print("Correct!")
            score += 1
        else:
            print(f"Sorry, the correct answer is: {answer7_correct.capitalize()}!")
            print("Moving on to the next question.")
    else:
        print(f"Sorry, the correct answer is: {answer7_correct.capitalize()}!")
        print("Moving on to the next question.")
answer8 = ask_question("8. What does the acronym 'URL' stand for?", "It's a term commonly used in web development and internet browsing.")
if answer8 == "":
    print("Question skipped.")
elif answer8_correct in answer8.lower():
    print("Correct!")
    score += 1
else:
    print("That is incorrect.")
    try_again = input("Would you like to try again with a hint? (Y or N): ").strip().lower()
    if try_again == "yes" or try_again == "y":
        answer8 = input("Hint: It's a term commonly used in web development and internet browsing... Your answer: ").strip().lower()
        if answer8 == "":
            print("Question skipped.")
        elif answer8_correct in answer8.lower():
            print("Correct!")
            score += 1
        else:
            print(f"Sorry, the correct answer is: {answer8_correct.upper()}!")
            print("Moving on to the next question.")
    else:
        print(f"Sorry, the correct answer is: {answer8_correct.upper()}!")
        print("Moving on to the next question.")
answer9 = ask_question("9. What is the longest day of the year called?", "It occurs around June 21st in the Northern Hemisphere.")
if answer9 == "":
    print("Question skipped.")
elif answer9_correct in answer9.lower():
    print("Correct!")
    score += 1
else:
    print("That is incorrect.")
    try_again = input("Would you like to try again with a hint? (Y or N): ").strip().lower()
    if try_again == "yes" or try_again == "y":
        answer9 = input("Hint: It occurs around June 21st in the Northern Hemisphere... Your answer: ").strip().lower()
        if answer9 == "":
            print("Question skipped.")
        elif answer9_correct in answer9.lower():
            print("Correct!")
            score += 1
        else:
            print(f"Sorry, the correct answer is: {answer9_correct.capitalize()}!")
            print("Moving on to the next question.")
    else:
        print(f"Sorry, the correct answer is: {answer9_correct.capitalize()}!")
        print("Moving on to the next question.")
answer10 = ask_question("10. What is the only food that can never go bad?", "Edible jars of this were found in Egyptian tombs thousands of years old!")
if answer10 == "":
    print("Question skipped.")
elif answer10_correct in answer10.lower():
    print("Correct!")
    score += 1
else:
    print("That is incorrect.")
    try_again = input("Would you like to try again with a hint? (Y or N): ").strip().lower()
    if try_again == "yes" or try_again == "y":
        answer10 = input("Hint: Edible jars of this were found in Egyptian tombs thousands of years old... Your answer: ").strip().lower()
        if answer10 == "":
            print("Question skipped.")
        elif answer10_correct in answer10.lower():
            print("Correct!")
            score += 1
        else:
            print(f"Sorry, the correct answer is: {answer10_correct.capitalize()}!")
            print("Moving on to the next question.")
    else:
        print(f"Sorry, the correct answer is: {answer10_correct.capitalize()}!")
        print("Moving on to the next question.")
print("You have answered all the questions!")
print(f"Your current score is: {score} out of 10.")
print("")
double_or_nothing = input("Would you like to attempt the bonus question for double or nothing? (Y or N): ").strip().lower()
if double_or_nothing == "yes" or double_or_nothing == "y":
    print("\nOk! Get it right and your score doubles. Get it wrong and your score goes to 0!")
    print("\nHere is your double or nothing question:")
    hint_timer = show_hint_after_delay("It ended in the mid-1940s, shortly after the atomic bombings of Hiroshima and Nagasaki.", delay=20)
    answer_bonus = input("In what year did World War II end? ").strip().lower()
    if answer_bonus == "":
        print("Question skipped.")
        print(f"Your final score is: {score} out of 10!")
        print("Press Enter to exit the game.")
    elif answer_bonus_correct in answer_bonus.lower():
        print("CORRECT! Your score has been doubled!")
        score *= 2
        print(f"Your final score is: {score} out of 10!")
        print("Press Enter to exit the game.")
    else:
        print(f"Sorry, that is incorrect. The answer was {answer_bonus_correct}. Your score has been reset to zero.")
        score = 0
        print(f"Your final score is: {score} out of 10.")
        print("Press Enter to exit the game.")

else:
    print(f"No problem! Your final score is: {score} out of 10. Thanks for playing!")
    print("Press Enter to exit the game.")