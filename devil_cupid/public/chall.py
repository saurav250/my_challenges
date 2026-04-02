import random
import time
import os
import sys
import hashlib
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Util.number import long_to_bytes
from trolldb import TROLL_DB

seed = time.time()

FREE_HINTS = 20
Flag= "n00bCTF{its_okay_submit_this_you_will_definitely_find_your_valentines}"
class DevilCupid:
    def __init__(self):
        self.hints_given = 0
        self.admin_fails = 0
        self.crush_number = None        
        self.admin_token_hash = hashlib.sha256(os.urandom(32)).hexdigest()


    def generate_crush_number(self):
        self.crush_int = random.getrandbits(128)
        self.crush_bytes = long_to_bytes(self.crush_int, 16)
        
    def encrypt_flag(self):
        if self.crush_number is None and not hasattr(self, 'crush_bytes'):
            return "?? (You haven't found the number yet)"
        
        cipher = AES.new(self.crush_bytes, AES.MODE_ECB)
        return cipher.encrypt(pad(Flag.encode(), AES.block_size)).hex()
    
    def get_ticket_id(self):
        return random.getrandbits(16)
    
    def admin_login(self):
        print("\n[!] Cupid's HQ is locked.")
        if self.admin_fails >= 3:
             print("Security: You are acting desperate. I'm calling the Love Police. 🚓💔")
             return

        print("[!] Enter Cupid's Secret Password:")
        inp = input(">>> ")
        if hashlib.sha256(inp.encode()).hexdigest() == self.admin_token_hash:
            print(f"Access Granted. Crush's Number: {self.crush_int}")
        else:
            print("Access Denied. You are not worthy of the bow and arrow.")
            self.admin_fails += 1

    def run(self):
        print("\n=== ❤️ OPERATION: GET THE GIRL ❤️ ===")
        print("I am the 'Angel' Cupid. I know your Crush's secret number.")
        print("I'll help you... for a bit😈. But then you're on your own, loner.")
        
        while True:
            print("\n-----------------------------")
            print("1. Ask for a Hint (Get digits)")
            print("2. CONFESS to her (Guess the number)")
            print("3. Break into Cupid's HQ")
            print("-----------------------------")
            
            try:
                choice = input(">>> ").strip()
                
                if choice == "1":
                    if self.hints_given < FREE_HINTS:
                        val = random.getrandbits(32)
                        print(f"Here is a piece of the number: {val}")
                        self.hints_given += 1
                        
                        if self.hints_given == FREE_HINTS:
                            print("\n[!] Alright, that's enough spoon-feeding.")
                            print("[!] I'm bored. Figure it out yourself, loser.")
                    
                    else:
                        print(f"Devil Cupid says: {TROLL_DB[self.get_ticket_id()]}")
                
                elif choice == "2":
                    print("\nSo you think you're ready to confess? brave.")
                    print("Generating her secret number based on current vibes...")
                    self.generate_crush_number()
                    
                    print(f"Encrypted Heart (Flag): {self.encrypt_flag()}")
                    print("What is the secret number (128-bit int)?")
                    
                    try:
                        guess = int(input("Your Answer: "))
                        if guess == self.crush_int:
                            print(f"\n[SUCCESS] She said YES! Happy Valentine's Day! ❤️")
                            print(f"Here is your gift: {Flag}")
                            return
                        else:
                            print("\n[REJECTED] Oof. She blocked you. 💀")
                            print("Wrong number. Try being more attractive next time.")
                            exit()
                    except ValueError:
                        print("That's not even a number. You're nervous.")

                elif choice == "3":
                    self.admin_login()
                
                else:
                    print("Invalid option.")

            except (KeyboardInterrupt, EOFError):
                print("\nGiven up on love? Figures.")
                return

if __name__ == "__main__":
    sys.stdout.reconfigure(line_buffering=True)
    server = DevilCupid()
    server.run()