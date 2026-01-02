# Read the number of centuries
centuries = int(input())

# Basic time conversions
years = centuries * 100
# Calculate days using the tropical year average for accuracy
days = int(years * 365.2422)
hours = days * 24
minutes = hours * 60

# Output the formatted result
print(f"{centuries} centuries = {years} years = {days} days = {hours} hours = {minutes} minutes")
