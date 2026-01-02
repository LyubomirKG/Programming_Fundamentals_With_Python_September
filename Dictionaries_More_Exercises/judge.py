contests = {}          # { contest: { username: points } }
user_totals = {}       # { username: total_points_across_all_contests }
contest_order = []     # Track order of contests as they first appear

while True:
    line = input()
    if line == "no more time":
        break

    username, contest, points = line.split(" -> ")
    points = int(points)

    # Track contest order
    if contest not in contests:
        contests[contest] = {}
        contest_order.append(contest)

    # Update contest record
    if username not in contests[contest]:
        contests[contest][username] = points
    else:
        # Update with only the higher score
        if points > contests[contest][username]:
            contests[contest][username] = points

# ----- CALCULATE USER TOTAL POINTS -----
user_totals = {}
for contest in contests.values():
    for user, pts in contest.items():
        user_totals[user] = user_totals.get(user, 0) + pts

# ----- PRINT CONTEST RANKINGS -----
for contest in contest_order:
    participants = contests[contest]
    print(f"{contest}: {len(participants)} participants")

    # Sort: points DESC, name ASC
    sorted_participants = sorted(
        participants.items(),
        key=lambda x: (-x[1], x[0])
    )

    for i, (user, pts) in enumerate(sorted_participants, start=1):
        print(f"{i}. {user} <::> {pts}")

# ----- PRINT INDIVIDUAL STANDINGS -----
print("Individual standings:")

sorted_totals = sorted(
    user_totals.items(),
    key=lambda x: (-x[1], x[0])
)

for i, (user, total) in enumerate(sorted_totals, start=1):
    print(f"{i}. {user} -> {total}")
