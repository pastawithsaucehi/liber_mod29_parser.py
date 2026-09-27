# Liber Primus Advanced Mod-29 Multiplier Parser Engine
# Framework by u/elvano124 (Upgraded Edition)
import os

GEMATRIA_ALPHABET = [
    'F', 'U', 'TH', 'O', 'R', 'C', 'G', 'W', 
    'H', 'N', 'I', 'J', 'EO', 'P', 'X', 'S', 
    'T', 'B', 'E', 'M', 'L', 'NG', 'D', 'O', 
    'A', 'AE', 'Y', 'IA', 'EA'
]

def decrypt_mod29_byte(byte_value, multiplier):
    """Processes a single byte through the u/elvano124 Mod-29 framework."""
    step1 = (byte_value % 29) * multiplier
    final_index = step1 % 29
    return GEMATRIA_ALPHABET[final_index]

def process_hex_matrix(hex_string, multiplier=7):
    """Cleans a hex string and parses it with a specific multiplier."""
    cleaned_hex = hex_string.replace(" ", "").replace("\n", "").strip()
    
    # Handle odd-length hex strings gracefully
    if len(cleaned_hex) % 2 != 0:
        cleaned_hex = cleaned_hex[:-1]
        
    bytes_list = [int(cleaned_hex[i:i+2], 16) for i in range(0, len(cleaned_hex), 2)]
    
    decrypted_chars = []
    for b in bytes_list:
        char = decrypt_mod29_byte(b, multiplier)
        decrypted_chars.append(char)
        
    return " ".join(decrypted_chars)

def run_bruteforce(hex_string):
    """Loops through all possible Mod-29 multipliers to find patterns."""
    print("\n=== STARTING MULTIPLIER BRUTEFORCE (1-28) ===")
    for m in range(1, 29):
        output = process_hex_matrix(hex_string, multiplier=m)
        print(f"[Multiplier {m:02d}]: {output}")

if __name__ == "__main__":
    input_file = "hex_input.txt"
    
    # Check if input file exists; if not, create it with your sample hex
    if not os.path.exists(input_file):
        with open(input_file, "w") as f:
            f.write("36 36 77 63 ab")
        print(f"[*] Created '{input_file}' with your sample hex string.")

    # Read the hex data from the file
    with open(input_file, "r") as f:
        hex_data = f.read()

    print(f"[*] Loaded data from {input_file}")
    
    # Mode Selection: Change to True if you want to bruteforce multiple multipliers
    BRUTEFORCE_MODE = False 
    
    if BRUTEFORCE_MODE:
        run_bruteforce(hex_data)
    else:
        # Default run using your exact Multiplier 7 framework
        result = process_hex_matrix(hex_data, multiplier=7)
        print(f"\n[+] Framework Output (Multiplier: 7):")
        print(result)
