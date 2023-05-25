import this

print('-'*40)
key = this.d

message = this.s
decoded = ''

for char in message:

    if key.get(char) is None:
        decoded += char
    else:
        decoded += key.get(char)


print(decoded)
