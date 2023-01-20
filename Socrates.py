import random

def get_random_question(input_text):
    questions = ["What makes you think that way?", "How?", "Why?, Why do you think so?", "How did this idea form?", "How did you come up with this idea?"]
    selected_question = random.choice(questions)
    return selected_question

input_text = input("What's on your mind?: ")
first_time = True

while True:
    if first_time:
        first_time = False
    else:
        input_text = input("")
    selected_question = get_random_question(input_text)
    print("Hm,", selected_question)
    if input_text.lower() in ["exit", "stop"]:
        break

