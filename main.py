import random

def friend():
    prompt="Hello"
    other_responseses=["Interesting", "Okay", "That's true, sometimes."]
    while True:
        my_text=input(prompt+": ")
        responses ={"Hello" : "How are you?",
                    "Fine" : "Wow, me too.",
                    "I have to go.": "I will miss you"}
        if my_text in responses.keys():
            prompt=responses[my_text]
        else:
            prompt=random.choice(other_responseses)


if __name__ == '__main__':
    friend()

