s = "cdiiddwpgswtgt"
i = 0

def shift_letter(c):
    if c == 'z':
        return 'a'
    return chr(ord(c) + 1)

while i < 24:
    s = ''.join(shift_letter(l) for l in s)
    i += 1
    print(s)
