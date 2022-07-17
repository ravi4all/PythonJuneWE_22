# Chatbot
# Basic Greet - hi, hello, hey
# date or time
# play music
# tell me today's news
# weather
while True:
    msg = input("Enter your message : ")
    msg = msg.lower()
    if msg == "hi" or msg == "hello" or msg == "hey":
        print("Hello User...")
    elif msg == "bye":
        print("Bye..Take Care")
        break
    else:
        print("I don't understand...")