players = {}   # { player: { position: skill } }

def total_skill(player):
    return sum(players[player].values())

while True:
    line = input()
    if line == "Season end":
        break

    if "->" in line:
        # "{player} -> {position} -> {skill}"
        player, position, skill = line.split(" -> ")
        skill = int(skill)

        if player not in players:
            players[player] = {}

        # Add or update position
        if position not in players[player]:
            players[player][position] = skill
        else:
            if players[player][position] < skill:
                players[player][position] = skill

    else:
        # "{player1} vs {player2}"
        p1, p2 = line.split(" vs ")

        if p1 in players and p2 in players:
            # Check for common positions
            common = set(players[p1].keys()) & set(players[p2].keys())

            if common:
                p1_total = total_skill(p1)
                p2_total = total_skill(p2)

                if p1_total > p2_total:
                    del players[p2]   # p2 demoted
                elif p2_total > p1_total:
                    del players[p1]   # p1 demoted
                # If equal, nothing happens

# ----- PRINT RESULTS -----

# Sort players by total skill desc, then name asc
sorted_players = sorted(players.items(),
                        key=lambda x: (-sum(x[1].values()), x[0]))

for player, positions in sorted_players:
    total = sum(positions.values())
    print(f"{player}: {total} skill")

    # Sort positions by skill desc, then name asc
    sorted_positions = sorted(positions.items(),
                              key=lambda x: (-x[1], x[0]))

    for pos, skill in sorted_positions:
        print(f"- {pos} <::> {skill}")
