








































































text = "ABCCDABCD"
pattern = "ABCD"

n = len(text)
m = len(pattern)

found = False

for i in range(n - m + 1):
    substring = text[i:i + m]

    if hash(substring) == hash(pattern):
        if substring == pattern:
            print("Pattern found at index:", i)
            found = True

if not found:
    print("Pattern not found")
