repeat_string = lambda current_string, n: current_string * n

text = input()
counter = int(input())
result = repeat_string(text, counter)
print(result)
