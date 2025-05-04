s = "cdiiddwpgswtgt"
i = 0

def shift_letter(c):
    if 'a' <= c <= 'z':
        return chr((ord(c) - ord('a') + 1) % 26 + ord('a'))
    elif 'A' <= c <= 'Z':
        return chr((ord(c) - ord('A') + 1) % 26 + ord('A'))
    else:
        return c  # ignore non-letter chars

while i < 24:
    s = ''.join(shift_letter(l) for l in s)
    i += 1
    print(s)
