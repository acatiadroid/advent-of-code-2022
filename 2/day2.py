#  A  X = Rock
#  B  Y = Paper
#  C  Z = Scissors

score = 0

rock = 1
paper = 2
scissors = 3

lost = 0
draw = 3
win = 6

a = "A"
b = "B"
c = "C"
x = "X"
y = "Y"
z = "Z"

def convert_value(letter):
    if letter == x:
        return rock
    elif letter == y:
        return paper
    else:
        return scissors

with open("input.txt") as f:
    games = f.readlines()

for game in games:
    game = game.split(" ")

    opponent = game[0]
    me = game[1].strip()

    # DRAWS

    if opponent == a and me == x:
        score += draw
        score += convert_value(x)

    if opponent == b and me == y:
        score += draw
        score += convert_value(y)
    
    if opponent == c and me == z:
        score += draw
        score += convert_value(z)
    
    # WINS

    if opponent == a and me == y:
        score += win
        score += convert_value(y)
    
    if opponent == b and me == z:
        score += win
        score += convert_value(z)
    
    if opponent == c and me == x:
        score += win
        score += convert_value(x)
    
    # LOSES

    if opponent == a and me == z:
        score += convert_value(z)
    
    if opponent == b and me == x:
        score += convert_value(x)
    
    if opponent == c and me == y:
        score += convert_value(y)

print(score)
