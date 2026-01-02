# Read input
n = int(input())

# Generate and print all triples
for i in range(n):
    for j in range(n):
        for k in range(n):
            first = chr(ord('a') + i)
            second = chr(ord('a') + j)
            third = chr(ord('a') + k)
            print(f"{first}{second}{third}")
