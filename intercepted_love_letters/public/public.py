from Crypto.Cipher import AES
from Crypto.Util import Counter
import os

# ==============================================================================
#  HEY! BOB HERE...
#
#  I think Alice is trying to send me something, but I just don't understand it.
#  I found her working on this script a while ago.
#  
#  Can you guess what she is trynna say? 
#  I am nervous... she said something about "Leet" speaking volumes?
# ==============================================================================

FLAG_INNER = "REDACTED" # The secret message she is hiding...
FLAG = f"n00bCTF{{{FLAG_INNER}}}" # I know the wrapper, just not the inside.

# 5 LOVE LETTERS WERE FOUND IN THE WORLD OF LEET, SPEAKS VOLUMES ABOUT HER LOVE.
MESSAGES = [
    b"REDACTED_MESSAGE_1",
    b"REDACTED_MESSAGE_2",
    b"REDACTED_MESSAGE_3",
    b"REDACTED_MESSAGE_4",
    b"REDACTED_MESSAGE_5"
]

# She generates a new key every time she runs it... 
# so I can't just decrypt the file I found :(
KEY = os.urandom(16)

# She hid the Connection ID in her environment variables... she is so smart, beauty with brains frr.
CONN_ID = os.getenv("CONN_ID", "default_id").encode()
 
def send_love_letter(msg, key):
    """
    Encrypts a single message using our secure channel.
    """
    ctr = Counter.new(64, prefix=CONN_ID)
    
    
    cipher = AES.new(key, AES.MODE_CTR, counter=ctr)
    return cipher.encrypt(msg)


# --- Simulation of what happened ---
output_data = []

print("[-] Alice is encrypting her messages...")
for i, msg in enumerate(MESSAGES):
    ciphertext = send_love_letter(msg, KEY)
    output_data.append(ciphertext.hex())

# She sent the inner part of the flag separately at the end
flag_ciphertext = send_love_letter(FLAG_INNER.encode(), KEY)
output_data.append(flag_ciphertext.hex())

# This is the file I recovered from her computer
# I have attached 'intercepted_chats.txt' for you to look at.
# Good luck! - Bob