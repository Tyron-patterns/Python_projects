# *===========================================================================================
# PROGRAM 1: CAESAR CIPHER — HARDCODED STRUCTURE TO TEST SHIFT LOGIC
# This version uses two separate loops: one to convert characters to shifted indexes,
# and another to handle wrap-around logic. It was a first attempt to understand
# and build encryption manually.
# *===========================================================================================

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
            'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(text, shift):
    new_alphabet = []
    encrypted = []
    not_alphabet = [' ', '$']  # handling non-letter characters

    for x in text:
        if x not in alphabet:
            new_alphabet.append(not_alphabet[1])
        elif x == ' ':
            new_alphabet.append(not_alphabet[0])
        else:
            new_alphabet.append(alphabet.index(x) + shift)  # store shifted index

    for i in new_alphabet:  # handle wrap-around for large indices
        if i >= len(alphabet):
            encrypted.append(alphabet[i % len(alphabet)])
        else:
            encrypted.append(alphabet[i])

    print(''.join(encrypted))


# *===========================================================================================
# PROGRAM 2: CAESAR CIPHER — CLEANED-UP ENCRYPTION FUNCTION WITH SINGLE LOOP
# This improved version merges the two loops into one.
# It directly appends characters to the encrypted list with wrap-around logic using modulo.
# Non-alphabet characters are replaced with placeholder symbols (' ' or '$').
# *===========================================================================================

def encrypt(text, shift):
    encrypted = []
    not_alphabet = [' ', '$']

    for x in text:
        if x in alphabet:
            shifted_index = (alphabet.index(x) + shift) % len(alphabet)
            encrypted.append(alphabet[shifted_index])  # wrapped around if needed
        elif x == ' ':
            encrypted.append(not_alphabet[0])  # keep spaces intact
        else:
            encrypted.append(not_alphabet[1])  # replace unknown characters with $

    print(''.join(encrypted))


# *===========================================================================================
# PROGRAM 3: CAESAR CIPHER — DECRYPT FUNCTION MIRRORING ENCRYPTION LOGIC
# This function mirrors Program 2 but subtracts the shift instead of adding it.
# It allows decoding encrypted messages using the same Caesar Cipher method.
# *===========================================================================================

def decrypt(text, shift):
    decrypted = []
    not_alphabet = [' ', '$']

    for x in text:
        if x in alphabet:
            shifted_index = (alphabet.index(x) - shift) % len(alphabet)
            decrypted.append(alphabet[shifted_index])  # wrap-around handled by modulo
        elif x == ' ':
            decrypted.append(not_alphabet[0])
        else:
            decrypted.append(not_alphabet[1])

    print(''.join(decrypted))
