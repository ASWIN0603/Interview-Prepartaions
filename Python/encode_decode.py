# encoding formula if position(alphabet) == even then replace by alphabet and its opposite alphabet
#if it is odd the replace by its opposite alphabet alone

#Encoding Function
def encoding(data):
    encoded = []
    for letter in data:
        number = ord(letter.upper()) - 64
        if number % 2 == 0:
            alphabet1 = chr(number + 64)
            alphabet2 = chr((27 - number) + 64)
            final = (alphabet1 + alphabet2)
            encoded.append(final)
        else:
            alphabet3 = chr((27 - number) + 64)
            encoded.append(alphabet3)
    return encoded

#Decoding Function
def decoding(encoded_data):
    decoded = []
    for encoded_letter in encoded_data:
        if len(encoded_letter) == 2:
            original_letter = encoded_letter[0]
            decoded.append(original_letter)
        else:
            number = (27 - (ord(encoded_letter.upper()) - 64)) + 64
            original_letter = chr(number)
            decoded.append(original_letter)
    return decoded

#Test For Given InputData
input_data = ['ABC', 'XYZ', 'GHI', 'NOP', 'JKL', 'UTS']
for data in input_data:
    encoded_data = encoding(data)
    decoded_data = decoding(encoded_data)
    print('Input String:', data)
    print("Encoded string:", ''.join(encoded_data))
    print("Decoded string:", ''.join(decoded_data))