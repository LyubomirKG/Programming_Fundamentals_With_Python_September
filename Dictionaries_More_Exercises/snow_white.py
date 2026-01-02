dwarfs = {}           # key: (name, color), value: physics
color_count = {}      # key: color, value: how many dwarfs have that hat color
order_index = {}      # to preserve input order in case all sorting fails
index = 0

while True:
    line = input()
    if line == "Once upon a time":
        break

    name, color, physics = [x.strip() for x in line.split("<:>")]
    physics = int(physics)
    key = (name, color)

    if key not in dwarfs:
        dwarfs[key] = physics
        color_count[color] = color_count.get(color, 0) + 1
        order_index[key] = index
        index += 1
    else:
        # Same name & color → update only if higher physics
        if dwarfs[key] < physics:
            dwarfs[key] = physics
        # No change to color_count (same dwarf)

# ----- SORT THE DWARFS -----
# Sort by:
# 1. Physics descending
# 2. Count of dwarfs with same color descending
# 3. Input order if needed
sorted_dwarfs = sorted(
    dwarfs.items(),
    key=lambda x: (-x[1], -color_count[x[0][1]], order_index[x[0]])
)

# ----- PRINT -----
for (name, color), physics in sorted_dwarfs:
    print(f"({color}) {name} <-> {physics}")
