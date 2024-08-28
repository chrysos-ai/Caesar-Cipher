alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encrypt' to encrypt, type 'decode' to decode: ").lower()
text = input("Type your message: ").lower()
shift = int(input("What is the shift number: "))


def caesar(directon):
    if directon == 'encrypt':
        def encrypt(original_text, shift_amount):
            encode = ''
            for char in original_text:
                if char in alphabet:
                    original_index = alphabet.index(char)
                    new_index = (original_index + shift_amount) % 26
                    encode += alphabet[new_index]
                else:
                    encode += char
            print(f'Your Encoded word is {encode}')
        encrypt(original_text=text, shift_amount=shift)
    elif directon == 'decode':
        def decode (original_text, shift_amount):
            decoder = ''
            for char in original_text:
                if char in alphabet:
                    decrypt = (alphabet.index(char) - shift_amount)% len(alphabet)
                    decoder += alphabet[decrypt]
                else:
                    decoder += char
            print(f'Your decoded word is {decoder}')
        decode(original_text=text, shift_amount=shift)
    else:
        print('Please type the correct options')


caesar(direction)