# Step 1: Read the number of elements
n = int(input())

# Step 2: Read the space-separated integers and convert them into a tuple
t = tuple(map(int, input().split()))

# Step 3: Compute the hash of the tuple
result = hash(t)

# Step 4: Print the result
print(result)
