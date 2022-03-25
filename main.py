
def friend():
    prompt="Hello"
    responses = {"Hello": "How are you?",
                 "Fine": "Wow, me too.",
                 "I have to go.": "I will miss you"}
    while True:
        my_text=input(prompt+": ")

        if my_text in responses.keys():
            prompt=responses[my_text]
        else:
            prompt="Interesting"


if __name__ == '__main__':
    friend()

