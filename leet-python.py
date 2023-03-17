s = "hello world"

# ==========
# SLICING
# ==========

# Slice starting from index 1
print(s[1:])

# Slice ending at index -1
print(s[:-1])

# Slice starting at index -1
print(s[-1:])

# Slice ending at index 1
print(s[:1])

# Iterate through list
print(s[::1])

# Iterate through list in reverse
print(s[::-1])


# ==========
# UTILITIES
# ==========

# Pointer initialisation
left, right = 0, len(s) - 1

# Counter function
d = {}
for l in s:
    if l not in d: d[l] = 1
    else: d[l] += 1

