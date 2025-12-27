# User Segmentation based on age brackets
user_age = int(input())

# Determine category using sequential interval checking
if user_age <= 14:
    category_drink = "toddy"
elif user_age <= 18:
    category_drink = "coke"
elif user_age <= 21:
    category_drink = "beer"
else:
    category_drink = "whisky"

print(f"drink {category_drink}")
