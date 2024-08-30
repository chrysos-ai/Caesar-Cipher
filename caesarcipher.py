import caesarart
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(encode_or_decode):
    if encode_or_decode == 'encrypt':
        def encrypt(original_text, shift_amount):
            encode = ''
            for char in original_text:
                if char in alphabet:
                    original_index = alphabet.index(char)
                    new_index = (original_index + shift_amount) % 26
                    encode += alphabet[new_index]
                else:
                    encode += char
            print(f'Your encoded word is {encode}')
        encrypt(original_text=text, shift_amount=shift)
    elif encode_or_decode == 'decode':
        def decode (original_text, shift_amount):
            decoder = ''
            for char in original_text:
                if char in alphabet:
                    decode_position = (alphabet.index(char) - shift_amount)% len(alphabet)
                    decoder += alphabet[decode_position]
                else:
                    decoder += char
            print(f'Your decoded word is {decoder}')
        decode(original_text=text, shift_amount=shift)




print(caesarart.logo)
start_over = True
while start_over:
    direction = input("Type 'encrypt' to encrypt, type 'decode' to decode: \n").lower()
    text = input("Type your message: \n").lower()
    shift = int(input("What is the shift number: \n"))

    caesar(encode_or_decode=direction)

    restart = input("Would you like to start over, 'yes' or 'no' ").lower()
    if restart == 'no':
        start_over = False
        print('Goodbye')









