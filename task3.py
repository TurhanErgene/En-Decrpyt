ALL_LETTERS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def encrypt(secret_key, file_name, method):

    text = readFile(file_name)

    if method == "s":
        result = substitution(text, secret_key, decrypt=False)
    else:
        result = transposition(text, secret_key, decrypt=False)

    writeFile(
        "output.txt", result
    )  # output.txt will be change to the name of the file that the user wants to process
    print("The file has been encrypted successfully")


def decrypt(secret_key, file_name, method):
    text = readFile(file_name)

    if method == "s":
        result = substitution(text, secret_key, decrypt=True)
    else:
        result = transposition(text, secret_key, decrypt=True)

    writeFile(
        "output.txt", result
    )  # output.txt will be change to the name of the file that the user wants to process
    print("The file has been decrypted successfully")


def substitution(text, secret_key, decrypt=False):
    result = ""
    for char in text:
        if char in ALL_LETTERS:
            pos = ALL_LETTERS.index(
                char
            )  # find the position of the letter in the alphabet
            if decrypt:
                result += ALL_LETTERS[(pos - secret_key) % len(ALL_LETTERS)]
            else:
                result += ALL_LETTERS[
                    (pos + secret_key) % len(ALL_LETTERS)
                ]  # shift the letter by the secret key
        else:
            result += char  # if the character is not a letter, keep it as it is
    # print(result)
    return result


def ceil(x):
    n = int(x)
    # For positive numbers, if there's a fractional part, add 1.
    if x > n:
        return n + 1
    # For negative numbers (or when x is already an integer), return n.
    else:
        return n

def transposition(text, secret_key, decrypt=False):
    if decrypt:
        # Calculate number of columns (grid width)
        num_of_cols = ceil(len(text) / secret_key)

        # Number of rows is determined by the secret key (grid height)
        num_of_rows = secret_key

        # Calculate how many empty (shaded) boxes exist at the end of the last row
        num_of_shaded_boxes = (num_of_cols * num_of_rows) - len(text)

        # Create a list to store plaintext characters, with one string per column
        plaintext = [""] * num_of_cols

        # Initialize column and row positions for filling the grid
        col = 0
        row = 0

        # Loop through each character in the encrypted text
        for symbol in text:
            plaintext[col] += symbol  # Append character to the correct column
            col += 1  # Move to the next column

            # If we reach the last column or the last valid position before shaded boxes, move to next row
            if (col == num_of_cols) or (col == num_of_cols - 1 and row >= num_of_rows - num_of_shaded_boxes):
                col = 0  # Reset to first column
                row += 1  # Move to next row

        # Join the plaintext columns row by row to reconstruct the original message
        result = "".join(plaintext)
    
    else:
        result = ""
        for i in range(secret_key):
            for j in range(i, len(text), secret_key):  # iterate through the text with the step of the secret key
                result += text[j]
    return result


def readFile(file):
    try:
        with open(file, "r") as f:
            text = f.read()
            return text
    except FileNotFoundError:
        print("File not found")
        menu()


def writeFile(file, text):
    with open(file, "w") as f:
        f.write(text)


def menu():

    print("=" * 60)
    encOrDec = input("Do you want to encrypt (E) or decrypt (D)? ").lower()
    method = input("Do you want to use substitution (S) or transposition (T)? ").lower()
    secret_key = input("Input the secret key: ").lower()
    file_name = input("Input the name of the file you want to process: ").lower()
    print("=" * 60)

    if encOrDec in ["e", "d"] and method in ["s", "t"] and secret_key.isdigit():
        secret_key = int(secret_key)
        if encOrDec == "e":
            encrypt(secret_key, file_name, method)
        else:
            decrypt(secret_key, file_name, method)
    else:
        print("Invalid input")
        menu()


menu()
