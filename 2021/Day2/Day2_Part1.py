# Advent of Code 2021, Day 2, Part1: Dive!
# Second attempt

# 2D list
with open("Day2.txt", 'r') as file:
    moves = [moves.split() for moves in file]

# submarine only moves within xz-plane
x = 0       # horizontal position
z = 0       # vertical position

# Down is the positive z-axis direction, up is in the negative z-axis direction
for i in range(0, len(moves)):
    if moves[i][0] == 'forward':
        x += int(moves[i][1])
    elif moves[i][0] == 'down':
        z += int(moves[i][1])
    elif moves[i][0] == 'up':
        z -= int(moves[i][1])
print("Product = %d" %(x*z) )