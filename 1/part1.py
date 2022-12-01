with open("input.txt") as f:
    calories = f.readlines()

elf = 1
total_elves = {}

# Total up the calories for each elf
for item in range(0, len(calories) - 1):
    if calories[item] != "\n":
        if total_elves.get(elf):
            total_elves[elf] = int(total_elves[elf]) + int(calories[item].strip())
        else:
            total_elves[elf] = int(calories[item].strip())
    else:
        elf += 1

# Get the elf with the most calories
most_cals = max(total_elves.values())

print(total_elves)

for key, value in total_elves.items():
    if most_cals == value:
        print(f"elf with most calories is elf #{key}")