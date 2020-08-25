from random import choice

questions = ["What is your favorite ice cream?: ", "What do you like watching?: ", "What do you like to play?:"]
question = choice(questions)
answer = input(question).strip().lower()
while answer != "just because":
    answer = input("Why?: ").strip().lower()
print("Oh ok like that")
