
# 🔐 CTF Challenge Series – Flags & Fun!

Welcome to the **CTF Challenge Series**! This repository contains three beginner-friendly challenges and a Python application to help you explore cybersecurity concepts like encoding, decoding, and puzzle solving.

---

## 📁 Files in This Repository

- `challenge1.txt` – First flag challenge (Hexadecimal decoding)  
- `challenge2.txt` – Second challenge (Base64 or Caesar Cipher)  
- `challenge3.txt` – Third challenge (XOR or logic-based puzzle)  
- `app.py` – A helper Python file to decode and interact with the challenges  

---

## 🚩 How to Get the Flags – Step-by-Step Guide

Each challenge contains a string that hides a flag. All flags are in this format:

```
FLAG{your_flag_here}
```

---

### 🔹 Challenge 1: Hexadecimal Decoding

- **File**: `challenge1.txt`
- **What to Expect**: A long string of hexadecimal values like:
  ```
  464c41477b636f6f6b69655f6d6f6e737465727d
  ```

#### ✅ Steps to Solve:
1. Open `challenge1.txt` and copy the hex string.
2. Use an online tool like https://cryptii.com or write a Python script:
   ```python
   print(bytes.fromhex("464c41477b636f6f6b69655f6d6f6e737465727d").decode())
   ```
3. Output:
   ```
   FLAG{cookie_monster}
   ```

---

### 🔹 Challenge 2: Base64 or Caesar Cipher

- **File**: `challenge2.txt`
- **What to Expect**: Either a suspicious string that ends in `==` or a scrambled sentence with readable characters.

#### ✅ Steps to Solve:

##### 🅰️ Option 1: Base64 Decoding
1. Copy the content from `challenge2.txt`.
2. Use an online Base64 decoder like https://www.base64decode.org/  
   OR run:
   ```python
   import base64
   encoded = "paste_base64_string_here"
   print(base64.b64decode(encoded).decode())
   ```

##### 🅱️ Option 2: Caesar Cipher
1. If it looks like a normal English sentence but jumbled:
2. Try online tools like: https://www.dcode.fr/caesar-cipher
3. Enter the text and try all shifts (brute force is usually an option).
4. Find the output that reveals:
   ```
   FLAG{...}
   ```

---

### 🔹 Challenge 3: XOR or Logical Puzzle

- **File**: `challenge3.txt`
- **What to Expect**: You may see a list of numbers like:
  ```python
  [70, 76, 65, 71, 123, 120, 111, 114, 95, 108, 111, 118, 101, 125]
  ```

#### ✅ Steps to Solve:

1. Guess or find the XOR key used to encrypt the message. Try this code:
   ```python
   encrypted = [70, 76, 65, 71, 123, 120, 111, 114, 95, 108, 111, 118, 101, 125]
   for key in range(256):
       flag = ''.join([chr(c ^ key) for c in encrypted])
       if "FLAG{" in flag:
           print(f"Key {key} -> {flag}")
   ```
2. The output will include the correct flag when the key matches:
   ```
   FLAG{xor_love}
   ```

---

## 🐍 app.py – Python Decoder Script

You can use `app.py` to automate solving the challenges. Example usage:

```bash
python app.py --challenge 1
```

Modify or extend the script to support more decoding methods like Base64, Caesar Cipher, or XOR.

---

## 🏁 Flag Format

All flags follow this format:

```
FLAG{your_flag_here}
```

Make sure to preserve the format exactly as shown above (uppercase "FLAG", curly braces `{}`).



## 💬 Contributing

Contributions are welcome! You can:
- Add new challenges
- Improve `app.py`
- Share encoding ideas
- Help expand this for others to learn and have fun!


## 🛡️ Disclaimer

This project is created for **educational purposes only**.  
Please use this knowledge ethically and avoid any illegal or unauthorized activities.


Happy Hacking & Enjoy the Flags! 🧠💻🔥  
