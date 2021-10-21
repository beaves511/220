# Add your encryption methods here
def encode(message, key):
    acc = ""
    for i in message:
        num = ord(i)
        add = num + key
        cha = chr(add)
        acc = acc + cha
    return acc


def encode_better(message, key_word):
    acc = ""
    for i in range(len(message)):
        char = message[i]
        key = key_word[i % len(key_word)]
        char_val = ord(char)
        key_val = ord(key) - 97
        code = char_val + key_val
        code_char = chr(code)
        acc = acc + code_char
    return acc
