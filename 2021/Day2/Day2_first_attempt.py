# Advent of Code 2021, Day 2, Part1: Dive!
# First attempt

# 2D list. Outer list contains lists as elements, inner lists have a direction as first element and magnitude as second element
with open("Day2.txt", 'r') as file:
    moves = [moves.split() for moves in file]

# submarine only moves within xz-plane
x = 0       # horizontal position
z = 0       # vertical position
indexes = range(0, len(moves))

for i in indexes:
    moves[i][1] = int(moves[i][1])
print('\n\n')
# print(moves)

# Down is the positive z-axis direction, up is in the negative z-axis direction
for i in indexes:
    if moves[i][0] == 'forward':
        x += moves[i][1]
    elif moves[i][0] == 'down':
        z += moves[i][1]
    elif moves[i][0] == 'up':
        z -= moves[i][1]
print("Depth: \t\t  z = %d" %z)
print("Horizontal dist:  x = %d" %x)
print("Product of x and z: %d" %(x*z) )
print('\n\n')
