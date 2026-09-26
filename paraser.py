# Liber Primus Mod-29 Multiplier 7 Parser Engine
# Framework by u/elvano124

GEMATRIA_ALPHABET = [
    'F', 'U', 'TH', 'O', 'R', 'C', 'G', 'W', 
    'H', 'N', 'I', 'J', 'EO', 'P', 'X', 'S', 
    'T', 'B', 'E', 'M', 'L', 'NG', 'D', 'O', 
    'A', 'AE', 'Y', 'IA', 'EA'
]

def decrypt_mod29_byte(byte_value, multiplier=7):
    step1 = (byte_value % 29) * multiplier
    final_index = step1 % 29
    return GEMATRIA_ALPHABET[final_index]

def process_hex_matrix(hex_string):
    cleaned_hex = hex_string.replace(" ", "")
    bytes_list = [int(cleaned_hex[i:i+2], 16) for i in range(0, len(cleaned_hex), 2)]
    
    print(f"[*] Processing {len(bytes_list)} bytes through Mod-29 Engine...")
    
    decrypted_chars = []
    for b in bytes_list:
        char = decrypt_mod29_byte(b)
        decrypted_chars.append(char)
        
    return decrypted_chars

if __name__ == "__main__":
    sample_hex = "36367763ab"
    result = process_hex_matrix(sample_hex)
    print("\n[+] Raw Output Stream:")
    print(" ".join(result)) 
    print("\n[+] Header Identified: U U")
