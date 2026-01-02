import re

demons = [d.strip() for d in input().split(",")]

result = {}

for demon in demons:
    # --- HEALTH ---
    health = sum(ord(ch) for ch in demon if ch not in "0123456789+-*/.")

    # --- BASE DAMAGE: extract all signed integers or floats ---
    numbers = re.findall(r"[+-]?\d+(?:\.\d+)?", demon)
    damage = sum(float(num) for num in numbers)

    # --- APPLY MULTIPLIERS/DIVIDERS IN ORDER ---
    for ch in demon:
        if ch == '*':
            damage *= 2
        elif ch == '/':
            damage /= 2

    result[demon] = (health, damage)

# --- SORT DEMONS ---
for name in sorted(result):
    health, damage = result[name]
    print(f"{name} - {health} health, {damage:.2f} damage")
