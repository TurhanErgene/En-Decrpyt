ALL_LETTERS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ" 



def encrypt(secret_key, file_name, method):
    
    text = readFile(file_name)

    if method == "s":
        result = substitution(text, secret_key, decrypt=False)
    else:
        result = transposition(text, secret_key, decrypt=False)

    writeFile("output.txt", result) # output.txt will be change to the name of the file that the user wants to process
    print("The file has been encrypted successfully")


def decrypt(secret_key, file_name, method):
    text = readFile(file_name)

    if method == "s":
        result = substitution(text, secret_key, decrypt=True)
    else:
        result = transposition(text, secret_key, decrypt=True)

    writeFile("output.txt", result) # output.txt will be change to the name of the file that the user wants to process
    print("The file has been decrypted successfully")
    


def substitution(text, secret_key, decrypt=False):
    result=""
    for char in text:
        if char in ALL_LETTERS:
            pos = ALL_LETTERS.index(char) # find the position of the letter in the alphabet  
            if decrypt:
                result += ALL_LETTERS[(pos-secret_key) % len(ALL_LETTERS)]
            else:
                result += ALL_LETTERS[(pos+secret_key) % len(ALL_LETTERS)] # shift the letter by the secret key
        else:
            result += char # if the character is not a letter, keep it as it is
    # print(result)
    return result


def transposition(text, secret_key, decrypt=False):
    pass    


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
