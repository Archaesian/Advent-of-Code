# Advent of Code 2021, Day 1: Sonar Sweep, Part 1
# Second (and successful) attempt

with open("Day1.txt", 'r') as file:
    depths = list( map(int, file.readlines()) )
    
accum = 0
x = range(0, len(depths))

for i in x:
    if i < max(x):
        if depths[i] < depths[i+1]:
            accum += 1
print("Number of increases: %d" %accum)
