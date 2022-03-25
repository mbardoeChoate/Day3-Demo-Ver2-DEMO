
def friend(my_text):

    responses ={"Hello" : "How are you?",
                "Fine" : "Wow, me too.",
                "I have to go.": "I will miss you"}
    if my_text in responses.keys():
        print(responses[my_text])
    else:
        print("Interesting")


if __name__ == '__main__':
    friend("Hello")

