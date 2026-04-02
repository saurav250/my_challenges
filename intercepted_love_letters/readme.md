# 💌 Intercepted Love Letters

**Category:** Cryptography  
**Difficulty:** Easy  
**Event:** n00bCTF  

## 📜 Scenario
Bob is in a bit of a panic. He intercepted some encrypted network traffic from Alice, who he suspects is trying to send him a secret message (or perhaps a love letter?). He managed to recover the Python script she used to encrypt the messages, but she generates a secure, randomized 16-byte key every time the script runs. 

Bob knows Alice is smart, but she dropped a hint: *"5 love letters were found in the world of leet, speaks volumes about her love."* Can you help Bob decipher Alice's true feelings and recover the hidden flag?

## 🔍 Technical Details
This challenge explores the mechanics of **AES encryption in CTR (Counter) mode**. 

You are provided with:
1. `challenge.py`: The source code Alice used to encrypt her messages.
2. `intercepted_chats.txt`: A file containing 6 lines of hex-encoded ciphertexts (5 secret messages + 1 flag).

**The Catch:** While the AES key is truly random and unknown (`os.urandom(16)`), look closely at how the `Counter` object is initialized inside the `send_love_letter` function. The same connection ID and counter prefix are used for every single message encrypted under the same key.

## 🎯 Objective
To get the flag, you must:
1. Analyze `challenge.py` to identify the cryptographic flaw in how AES-CTR is being utilized.
2. Exploit the resulting keystream reuse (Many-Time Pad attack).
3. Use crib dragging or known-plaintext guessing (keep the "leet" hint in mind!) to decipher the hex strings in `intercepted_chats.txt`.
4. Recover the `FLAG_INNER` and wrap it in the standard `n00bCTF{...}` format.

## ⚙️ Files Provided
* `challenge.py` - The encryption logic.
* `intercepted_chats.txt` - The intercepted ciphertexts to decrypt.

## 🛠️ Setup
If you want to run the script yourself to generate new test ciphertexts, ensure you have the required crypto libraries installed:
```bash
pip install pycryptodome