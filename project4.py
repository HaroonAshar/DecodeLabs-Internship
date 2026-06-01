score = 0

print("Welcome to the Quiz Game!")
print("-" * 30)

# Question 1
answer1 = input("Q1: What is the capital of France? ")
if answer1.strip().lower() == "paris":
    print("Correct!")
    score += 1
else:
    print("Wrong! The answer is Paris.")

# Question 2
answer2 = input("Q2: How many days are in a week? ")
if answer2.strip() == "7":
    print("Correct!")
    score += 1
else:
    print("Wrong! The answer is 7.")

# Question 3
answer3 = input("Q3: What is 5 x 5? ")
if answer3.strip() == "25":
    print("Correct!")
    score += 1
else:
    print("Wrong! The answer is 25.")

print("-" * 30)
print("Game Over! Your final score:", score, "/ 3")