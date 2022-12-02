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

print(f"most calories is {most_cals}")

# PART 2

top3 = sorted(total_elves.values(), reverse=True)
total = top3[0] + top3[1] + top3[2]

print(f"total calories of top 3 elfs is {total}")
