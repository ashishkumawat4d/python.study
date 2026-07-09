

score = 0

questions = [
    "1. What is the capital of India?",
    "2. Which language is known as the programming language of AI?",
    "3. Who developed Python?",
    "4. Which symbol is used for comments in Python?",
    "5. What is 5 + 10?"
]

answers = ["A", "B", "C", "B", "D"]



options = [
    ["A. Delhi", "B. Mumbai", "C. Jaipur", "D. Kolkata"],
    ["A. Java", "B. Python", "C. C++", "D. HTML"],
    ["A. Dennis Ritchie", "B. James Gosling", "C. Guido van Rossum", "D. Elon Musk"],
    ["A. //", "B. #", "C. /* */", "D. --"],
    ["A. 20", "B. 5", "C. 12", "D. 15"]
]


for i in range(len(questions)):

    print()
    print(questions[i])

    for option in options[i]:
        print(option)

    user_answer = input("Enter your answer (A/B/C/D): ").upper()

    if user_answer == answers[i]:
        print("Correct Answer")
        score += 1
    else:
        print("Wrong Answer")
        print("Correct Answer is:", answers[i])


print()
print("Quiz Finished")
print("Your Score:", score, "/", len(questions))


