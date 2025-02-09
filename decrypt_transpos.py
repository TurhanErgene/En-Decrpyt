def ceil(x):
    n = int(x)
    if x > n:
        return n + 1
    else:
        return n


def decrypt(text, secret_key):
    num_of_cols = ceil(len(text) / secret_key)
    num_of_rows = secret_key
    num_of_shaded_boxes = (num_of_cols * num_of_rows) - len(text)

    plaintext = [""] * num_of_cols

    col = 0
    row = 0

    for symbol in text:
        plaintext[col] += symbol
        col += 1

        if col == num_of_cols or (
            col == num_of_cols - 1 and row >= num_of_rows - num_of_shaded_boxes): # if the last column is filled or we are at the last row
            col = 0
            row += 1

    result = "".join(plaintext)
    return result


with open("sb224sc_transpos.txt", "r", encoding="utf-8", errors="replace") as f:
    text = f.read()


for i in range(1, 5):
    print(f"Key: {i}")
    print(decrypt(text, i))
    print()