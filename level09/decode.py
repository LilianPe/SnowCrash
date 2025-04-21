import sys

token = sys.argv[1]
decrypted_hash = ""
for i in range(0, len(token)):
    decrypted_hash += chr(ord(token[i]) - i)
print(decrypted_hash)