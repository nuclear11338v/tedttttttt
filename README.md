# FBH 🔥

**Hide your code like a pro!**  
FBH (BotForgeHub) is a sleek, secure, and powerful tool to encrypt and decrypt your code files (.py, .js, .php, and more) with military-grade AES-256 encryption. Whether you want to lock your files with a password or make them untouchable forever, FBH has got your back. 💪

---

## 🚀 Features That Rock
- **Unbreakable Encryption**: AES-256 GCM mode ensures your files are locked tight with integrity protection.
- **Password-Protected Mode**: Secure your files with a password only you know.
- **No-Password Mode**: Hide files permanently with no way to decrypt—perfect for ultimate secrecy. 🕵️
- **Embedded Instructions**: Every encrypted file comes with built-in instructions and credits, so you always know what's up.
- **Cross-Platform**: Works on any file type (.py, .js, .php, etc.) and any OS (Windows, macOS, Linux).
- **Slick CLI**: Easy-to-use commands that make encryption feel like a breeze.
- **Team X OG Vibes**: Built with passion and swagger by [Your Name] and Team X OG. 😎

---

## 🛠️ Installation
Get FBH up and running in seconds:
```bash
pip install fbh
```

> **Pro Tip**: Make sure you have Python 3.6+ and `pycryptodome` installed.

---

## 🎮 How to Use
FBH is all about simplicity. Fire up your terminal and let the magic happen!

### 🔒 Encrypt a File with a Password
Lock your file with a secret password:
```bash
FBH hide mysecretpassword example.py
```
**Output**: `example.py.fbh` (encrypted file)

### 🛡️ Encrypt a File Forever (Non-Decryptable)
Hide your file with no way back—pure stealth mode:
```bash
FBH hide - example.py
```
**Output**: `example.py.fbh` (locked forever)

### 🔓 Decrypt a File
Unlock your file with the right password:
```bash
FBH decode mysecretpassword example.py.fbh
```
**Output**: `example.py.dec` (original file restored)

> **Note**: Files encrypted with `FBH hide -` cannot be decrypted. Choose wisely! 😈

---

## 💡 Example in Action
1. Create a file `secret.py`:
   ```python
   print("This is top-secret code!")
   ```
2. Encrypt it:
   ```bash
   FBH hide mypassword secret.py
   ```
3. Decrypt it:
   ```bash
   FBH decode mypassword secret.py.fbh
   ```
4. Want it gone forever?:
   ```bash
   FBH hide - secret.py
   ```

Boom! Your code is safe. 🛡️

---

## 🔐 Security Highlights
- **AES-256 GCM**: Industry-standard encryption with built-in integrity checks.
- **PBKDF2 Key Derivation**: Passwords are transformed into secure keys.
- **Random Salt**: Every encryption is unique, even with the same password.
- **No-Password Mode**: Uses a random key that's never stored—decryption is impossible.
- **Embedded Metadata**: Instructions and credits are encrypted with your file, revealed only on decryption.

---

## ⚠️ Important Notes
- **Lost Password?**: No password, no decryption. Use a password manager to stay safe.
- **Non-Decryptable Files**: Files hidden with `FBH hide -` are locked forever. Perfect for sensitive data you want to bury.
- **Big Files?**: FBH handles them like a champ, but for massive files, stay tuned for chunk-based updates!

---

## 📜 Credits
Crafted with 💥 by **[Mr arman]** and **Team X OG**.  
We’re all about keeping your code safe and your vibe cooler than ever.

---

## 📞 Get in Touch
Got questions? Ideas? Hit us up:
- **Email**: armanhacker95@gmail.com

**FBH: Hide it. Lock it. Own it.** 😎
```