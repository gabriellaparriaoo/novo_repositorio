# Dupla: Gabriella Parrião e Mariana Cerqueira
# Atividade 5 - Seu próprio algoritmo de criptografia

def cesar_cipher(message, shift):
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            shifted_char = chr(((ord(char) - 97 + shift) % 26) + 97)
            if is_upper:
                shifted_char = shifted_char.upper()
            encrypted_message += shifted_char
        else:
            encrypted_message += char
    return encrypted_message

def cesar_decipher(encrypted_message, shift):
    return cesar_cipher(encrypted_message, -shift)

def transposition_cipher(message, group_size):
    encrypted_message = ""
    for i in range(group_size):
        j = i
        while j < len(message):
            encrypted_message += message[j]
            j += group_size
    return encrypted_message

def transposition_decipher(encrypted_message, group_size):
    num_rows = len(encrypted_message) // group_size
    num_cols = group_size
    num_shaded_boxes = len(encrypted_message) % group_size

    plaintext = [''] * group_size
    col = 0
    row = 0

    for symbol in encrypted_message:
        plaintext[col] += symbol
        col += 1
        if (col == group_size) or (col == group_size - 1 and row >= num_rows - num_shaded_boxes):
            col = 0
            row += 1

    return ''.join(plaintext)

# Ao invés de ser: Hello, Word!. Vai ser: Eai, Virgina!
message = "Eai, Virginia!"
cesar_shift = 3
cesar_encrypted = cesar_cipher(message, cesar_shift)
print("Mensagem criptografada com a cifra:", cesar_encrypted)
cesar_decrypted = cesar_decipher(cesar_encrypted, cesar_shift)
print("Mensagem descriptografada com a cifra:", cesar_decrypted)

transposition_group_size = 4
transposition_encrypted = transposition_cipher(message, transposition_group_size)
print("Mensagem criptografada com criptografia de transposição:", transposition_encrypted)
transposition_decrypted = transposition_decipher(transposition_encrypted, transposition_group_size)
print("Mensagem descriptografada com criptografia de transposição:", transposition_decrypted)
