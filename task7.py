from itertools import combinations

# Input the length of the list, the list of letters, and the number of indices to be selected
N = int(input())
letters = input().split()
K = int(input())

# Count the number of combinations where at least one index contains the letter 'a'
combinations_with_a = 0
for combo in combinations(range(1, N + 1), K):
    if 'a' in [letters[i - 1] for i in combo]:
        combinations_with_a += 1

# Calculate the total number of combinations of indices
total_combinations = len(list(combinations(range(1, N + 1), K)))

# Calculate the probability
probability = combinations_with_a / total_combinations

# Print the probability rounded to 4 decimal places
print("{:.4f}".format(probability))
