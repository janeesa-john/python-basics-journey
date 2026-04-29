questions = {
    "Capital of India": "delhi",
    "5 + 5": "10",
    "Color of sky": "blue"
}

score = 0

print("🧠 Welcome to Quiz App")

for question, answer in questions.items():
    user_answer = input(question + ": ").lower()

    if user_answer == answer:
        print("Correct!\n")
        score += 1
    else:
        print("Wrong! Correct answer is", answer, "\n")

print("Final Score:", score, "/", len(questions))