questions = []
answers = []


def add_flashcard():
    question = input("Enter the question: ")
    answer = input("Enter the answer: ")

    questions.append(question)
    answers.append(answer)

    print("Flashcard saved")


def play():
    for i in range(len(questions)):
        print("Question:", questions[i])
        user_answer = input("Your Answer: ")

        if user_answer.lower() == answers[i].lower():
            print("Correct!")
        else:
            print("Wrong!")
            print("Correct Answer:", answers[i])


while True:
    print("1. Add Flashcard")
    print("2. Play")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_flashcard()

    elif choice == "2":
        play()

    elif choice == "3":
        break

    else:
        print("Invalid choice.")