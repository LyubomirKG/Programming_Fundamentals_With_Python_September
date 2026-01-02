text = input()
capital_indices = []

for i in range(len(text)):
    if text[i].isupper():
        capital_indices.append(i)

print(capital_indices)
