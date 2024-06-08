from itertools import groupby

def compress_string(s):
    compressed_string = ''
    for key, group in groupby(s):
        compressed_string += f"({len(list(group))}, {key}) "
    return compressed_string.strip()

# Input string
s = input().strip()

# Call the function and print the output
print(compress_string(s))
