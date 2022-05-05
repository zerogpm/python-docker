alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(plain_text, shift_amount):
    encrypt_text = []
    for char in plain_text:
        position = alphabet.index(char)
        new_position = position + shift_amount
        if new_position > len(alphabet) - 1:
            new_position = new_position - len(alphabet)
        encrypt_text.append(alphabet[new_position])
    return encrypt_text

print(encrypt(plain_text=text, shift_amount=shift))