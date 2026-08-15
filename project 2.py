questions = (
    "1. Daily water intake=?",
    "2. Weekly workout goal=?",
    "3. Ideal sleep for adults=?",
    "4. Common step goals=?"
)

options = (
    ("A) 1L", "B) 2-3L", "C) 5L", "D) 7L"),
    ("A) 60 min", "B) 90 min", "C) 150 min", "D) 300 min"),
    ("A) 4-5 hrs", "B) 5-6 hrs", "C) 7-9 hrs", "D) 10-12 hrs"),
    ("A) 3000", "B) 5000", "C) 8000", "D) 10000")
)

answers = ["B", "C", "C", "D"]
guesses = []
questionno = 0
score = 0

for question in questions:
    print("----------")
    print(question)

    for option in options[questionno]:
        print(option)

    guess = input("Enter your guess: ").upper()
    guesses.append(guess)

    if guess == answers[questionno]:
        score += 1
        print("Correct")
    else:
        print("Incorrect")
        print(f"The correct answer for question {questionno + 1} is {answers[questionno]}")

    questionno += 1

print("RESULT")

print("ANSWERS: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("GUESSES: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")