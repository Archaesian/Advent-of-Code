# Advent of Code 2021, Day 1: Sonar Sweep, Part 2

# if (x1 + x2 + x3) < (x2 + x3 + x4), then depth increased  
# ==>  if (x1 < x4), then depth increased  ==>  arr[i+3]>arr[i] = increased depth

with open("Day1.txt", 'r') as file:
    depths = list( map(int, file.readlines()) )
    
accum = 0
x = range(0, len(depths))

for i in x:
    if i < (max(x)-2):
        if depths[i] < depths[i+3]:
            accum += 1
print("Number of increases: %d" %accum)
