# Easy Pass Gen

**Easy Pass Gen** is a fast and modern Python library for generating secure passwords, memorable passphrases, and PIN codes. It can be used both via the Command Line Interface (CLI) and as a library in your Python projects.

## Features

- 🔒 **Cryptographically Secure**: Uses the `secrets` module to generate unpredictable passwords.
- 🔑 **Various Modes**:
  - Standard complex passwords.
  - Memorable passphrases (e.g., `Correct-Horse-Battery-Staple`).
  - Numeric PIN codes.
- 🖥️ **CLI Support**: Generate passwords quickly from the terminal.
- 📋 **Clipboard Support**: Automatically copy generated passwords to the clipboard.
- 🛡️ **Strength Checker**: Calculates password entropy and rates its strength.

## Installation

```bash
pip install easy-pass-gen
```

## Usage (CLI)

You can access all features via the `easy-pass-gen` command in the terminal.

### 1. Standard Password Generation
```bash
easy-pass-gen generate
```
**Options:**
- `--length` / `-l`: Length (default: 16)
- `--no-symbols`: Do not use symbols.
- `--no-digits`: Do not use digits.
- `--copy`: Copy to clipboard.

**Example:**
```bash
easy-pass-gen generate --length 20 --copy
# Output: Password: aB3$kL9#mP2!xY7zQ5wE  [Very Strong]
```

### 2. Passphrase Generation
Generates memorable, word-based passwords.
```bash
easy-pass-gen passphrase
```
**Options:**
- `--words` / `-w`: Number of words (default: 4).
- `--separator` / `-s`: Separator character (default: -).
- `--capitalize`: Capitalize first letter of each word.

**Example:**
```bash
easy-pass-gen passphrase --words 5 --capitalize
# Output: Passphrase: Table-Green-Future-Window-Light
```

### 3. PIN Generation
Generates numeric-only codes.
```bash
easy-pass-gen pin --length 6
# Output: PIN: 482915
```

### 4. Strength Check
Test the strength of an existing password.
```bash
easy-pass-gen check "MySuperPas$word123"
```

## Usage (Python)

To use it as a library in your projects:

```python
from easy_pass_gen import generate_password, generate_passphrase, generate_pin, estimate_strength

# 1. Standard Password
password = generate_password(length=16, use_symbols=True)
print(f"Password: {password}")

# 2. Passphrase
phrase = generate_passphrase(words=4, separator=".")
print(f"Passphrase: {phrase}")
# Output: tree.apple.sky.blue

# 3. PIN
pin = generate_pin(length=6)
print(f"PIN: {pin}")

# 4. Strength Check
strength = estimate_strength(password)
print(f"Strength: {strength['label']} (Score: {strength['score']}/5)")
# 5. Security Tokens
token = generate_url_safe_token(32)
print(f"Token: {token}")

hex_token = generate_hex_token(32)
print(f"Hex: {hex_token}")

totp_secret = generate_totp_secret()
print(f"TOTP Secret: {totp_secret}")
```

## Version History

- **0.5.0** (2026-02-13)
  - Added `generate_url_safe_token`.
  - Added `generate_hex_token`.
  - Added `generate_totp_secret`.

- **0.4.0** (2026-02-13)
  - Added GitHub Actions for automatic publishing.

- **0.3.0** (2026-02-13)
  - Added GitHub Actions for automatic publishing.

- **0.2.0** (2026-02-13)
  - Added GitHub Actions for automatic publishing.

- **0.1.0** (2026-02-13)
  - Initial public release.
  - Features: Password, Passphrase, PIN generation.
  - CLI and Library support included.

## License

This project is licensed under the MIT License.
