# Default stat values
DEFAULT_DAMAGE = 45
DEFAULT_HEALTH = 250
DEFAULT_ARMOR = 10

n = int(input())

dragons = {}        # {type: {name: {'damage': x, 'health': y, 'armor': z}}}
order_of_types = []  # preserve type order as input gives them

for _ in range(n):
    parts = input().split()
    d_type, d_name = parts[0], parts[1]
    raw_damage, raw_health, raw_armor = parts[2], parts[3], parts[4]

    damage = int(raw_damage) if raw_damage != "null" else DEFAULT_DAMAGE
    health = int(raw_health) if raw_health != "null" else DEFAULT_HEALTH
    armor = int(raw_armor) if raw_armor != "null" else DEFAULT_ARMOR

    if d_type not in dragons:
        dragons[d_type] = {}
        order_of_types.append(d_type)

    # Overwrite existing dragon or add new
    dragons[d_type][d_name] = {
        'damage': damage,
        'health': health,
        'armor': armor
    }

# ----- PRINT RESULTS -----
for d_type in order_of_types:
    type_dragons = dragons[d_type]

    # Calculate averages
    avg_damage = sum(d['damage'] for d in type_dragons.values()) / len(type_dragons)
    avg_health = sum(d['health'] for d in type_dragons.values()) / len(type_dragons)
    avg_armor = sum(d['armor'] for d in type_dragons.values()) / len(type_dragons)

    # Print type header
    print(f"{d_type}::({avg_damage:.2f}/{avg_health:.2f}/{avg_armor:.2f})")

    # Print dragons sorted by name
    for name in sorted(type_dragons.keys()):
        stats = type_dragons[name]
        print(f"-{name} -> damage: {stats['damage']}, health: {stats['health']}, armor: {stats['armor']}")
