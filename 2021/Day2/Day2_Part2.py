# Advent of Code 2021, Day 2, Part2: Dive!

# 2D list
with open("Day2.txt", 'r') as file:
    moves = [moves.split() for moves in file]

# submarine only moves within xz-plane
x = 0       # horizontal position
z = 0       # vertical position
aim = 0

# Down is the positive z-axis direction, up is in the negative z-axis direction
for i in range(0, len(moves)):
    if moves[i][0] == 'forward':
        x += int(moves[i][1])
        z += aim*int(moves[i][1])
    elif moves[i][0] == 'down':
        aim += int(moves[i][1])
    elif moves[i][0] == 'up':
        aim -= int(moves[i][1])
print("Product = %d" %(x*z) )