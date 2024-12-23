# Magic 8 Ball Program, inspired by Codecademy project

import random

# random.randint() is a random number generator
random_number = random.randint(1, 11)

# check random number generator is working
# print(random_number)

# variables
name = input("What is your name? ")
question = input("What is your question? ")

# responses
if random_number == 1:
    response = "Absolutely"
elif random_number == 2:
    response = "Nope!"
elif random_number == 3:
    response = "Eh, maybe"
elif random_number == 4:
    response = "I'm busy, ask me again later"
elif random_number == 5:
    response = "Let's just say I wouldn't quit your day job"
elif random_number == 6:
    response = "u serious rn?"
elif random_number == 7:
    response = "[Shrugs]"
elif random_number == 8:
    response = "[8 Ball just smiles and nods]"
elif random_number == 9:
    response = "Yeah, sure, why not"
elif random_number == 10:
    response = "Not a chance in hell"
elif random_number == 11:
    response = "Hahahaha"
else:
    response = "Error"
    
# output and basic control flow
print("""
""")
if question == "":
    print("A question is required!\n")
elif name == "":
    print(f"Question: {question}\n")
    print(f"Magic 8 Ball's response: {response}\n")
else:
    print(f"{name} asks: {question}\n")
    print(f"Magic 8 Ball's response: {response}\n")

# Future work
# 1. Get the program to reprompt the user if they don't enter a question
# 2. Perhaps create a dictionary of possible responses?
# 3. An advanced project would be to have an option to set the tone of the responses
# and then use some kind of LLM to generate the responses based on the tone selected
# 4. Add more theatrical responses to the output with italics if possible: 
# {name} shakes the magic 8-ball vigorously. A number and response materializes from the inky blackness: