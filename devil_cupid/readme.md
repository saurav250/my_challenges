# 💘 Devil Cupid

**Category:** Cryptography / PRNG Exploitation  
**Difficulty:** Medium  

## 📜 Scenario
It's Valentine's Day, and "Devil Cupid" is gatekeeping your crush's phone number. He offers to give you a few "free hints" to win her over, but he gets bored quickly and starts mocking you. If you want to confess and win her heart (the flag), you'll need to outsmart his twisted games, predict the exact 128-bit crush number, and bypass his AES encryption.

## 🔍 Technical Details
This challenge focuses on the vulnerabilities of using non-cryptographically secure pseudo-random number generators (CSPRNGs)—specifically Python's default `random` module, which is powered by the **Mersenne Twister (MT19937)** algorithm.

1. **The Tease (Free Hints):** Cupid gives the user 20 direct 32-bit outputs from the PRNG. However, cloning the MT19937 state requires 624 outputs.
2. **The Leak (Troll Database):** After the free hints run out, Cupid responds to hint requests with randomized troll messages. The index of these messages is generated using `random.getrandbits(16)`.
3. **The Lock:** The target 128-bit number is generated right before the confession. It is also used as the AES-ECB key to encrypt the flag. 

## 🎯 Objective
To get the flag, the player must:
1. Collect the initial 20 direct 32-bit PRNG outputs.
2. Continue querying the "Hint" function and map the resulting troll messages back to their 16-bit generator values.
3. Stitch the leaked bits together to collect 624 full states.
4. Clone the MT19937 PRNG state.
5. Predict the upcoming 128-bit `crush_int`.
6. Submit the predicted number to trigger the "SUCCESS" condition and receive the decrypted flag.

## ⚙️ How to Run

1. Ensure you have Python 3 installed.
2. Install the required cryptographic library:
   ```bash
   pip install pycryptodome