import random
greetIntent = ["hi", "hello", "hey", "hi there", "hello there", "hey there"]

while True:
    msg = input("Enter your message : ")
    msg = msg.lower()
    if msg in greetIntent:
        ans = random.choice(greetIntent)
        print(ans.title())
    elif msg == "bye":
        print("Bye..Take Care")
        break
    else:
        print("I don't understand...")