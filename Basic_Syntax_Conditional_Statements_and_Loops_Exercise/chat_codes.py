# Signal Decoder: Translating numeric codes into messages
number_of_messages = int(input())

for _ in range(number_of_messages):
    signal_code = int(input())

    # Specific command handling (ASCII-like logic)
    if signal_code == 88:
        print("Hello")
    elif signal_code == 86:
        print("How are you?")
    elif signal_code < 88:
        print("GREAT!")
    else:
        print("Bye.")
