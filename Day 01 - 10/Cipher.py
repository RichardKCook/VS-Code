alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = ""
text = ""
shift = ""


def caesar(text, shift, direction):
    cipher = ""
    if direction == "decode":
        shift *= -1
    if shift >= 26:
        shift = shift % 26
    for letter in text:
        if letter == " " or letter in str(set(range(0, 10))):
            cipher += letter
        else:
            position = alphabet.index(letter)
            newpos = position + shift
            if newpos >= 25:
                newpos -= 26
            if newpos <= 0:
                newpos += 26
            cipher += alphabet[newpos]
    print(cipher)


def run():
    on = True
    while on:
        direction = input(
            "Type 'encode' to encrypt, 'decode' to decrypt, or type 'stop' to end:\n")
        if direction == "stop":
            return (0)
        elif direction != "encode" and direction != "decode":
            print("You didn't enter a valid selection.")
            run()
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        caesar(text, shift, direction)


run()
