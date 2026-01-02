# Read the initial deck of cards
deck_of_cards = input().split()
number_of_shuffles = int(input())

for current_shuffle in range(number_of_shuffles):
    # Find the midpoint to split the deck into two equal halves
    middle_of_the_deck = len(deck_of_cards) // 2
    left_part = deck_of_cards[:middle_of_the_deck]
    right_part = deck_of_cards[middle_of_the_deck:]
    
    deck_after_shuffling = []
    
    # Interleave the cards: one from the left half, then one from the right half
    for card_index in range(len(left_part)):
        deck_after_shuffling.append(left_part[card_index])
        deck_after_shuffling.append(right_part[card_index])
    
    # Update the deck for the next shuffle iteration
    deck_of_cards = deck_after_shuffling.copy()

# Print the final state of the deck
print(deck_of_cards)
