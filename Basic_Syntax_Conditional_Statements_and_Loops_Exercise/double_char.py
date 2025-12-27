# String Obfuscator: Doubling characters with specific keyword exclusion
while True:
    command = input()
    
    # Termination condition
    if command == "End":
        break
    
    # Keyword filtering: skip processing for specific strings
    if command == "SoftUni":
        continue
    
    # Advanced string manipulation: double every character in the string
    doubled_text = "".join([char * 2 for char in command])
    
    print(doubled_text)
