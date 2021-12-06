# someone else's solution
with open("Day1.txt", "r") as f:
    input_values = [int(n) for n in f.read().splitlines()]

# ------------------ #

increased = 0

for i, _ in enumerate(input_values):
    if input_values[i] > input_values[i-1]:
        increased += 1

print(f"Increased {increased} times!")