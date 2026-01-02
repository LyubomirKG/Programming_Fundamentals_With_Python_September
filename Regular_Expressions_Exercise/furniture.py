import re

furniture_list = []
total_cost = 0.0

pattern = r'>>(?P<name>[A-Za-z]+)<<(?P<price>\d+(\.\d+)?)!(?P<quantity>\d+)'

while True:
    line = input()
    if line == "Purchase":
        break

    match = re.match(pattern, line)
    if match:
        name = match.group("name")
        price = float(match.group("price"))
        quantity = int(match.group("quantity"))
        total_cost += price * quantity
        furniture_list.append(name)

print("Bought furniture:")
for item in furniture_list:
    print(item)
print(f"Total money spend: {total_cost:.2f}")
