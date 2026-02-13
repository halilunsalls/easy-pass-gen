import string
import secrets
import math
import base64
from .wordlist import WORD_LIST

def generate_password(
    length=12, 
    use_upper=True, 
    use_lower=True, 
    use_digits=True, 
    use_symbols=True, 
    avoid_ambiguous=False,
    count=1
):
    """
    Generates a password.
    """
    # Define character pools
    pool = ""
    if use_upper: pool += string.ascii_uppercase
    if use_lower: pool += string.ascii_lowercase
    if use_digits: pool += string.digits
    if use_symbols: pool += string.punctuation

    # Remove ambiguous characters (optional)
    if avoid_ambiguous:
        for char in "Il1O0":
            pool = pool.replace(char, "")

    if not pool:
        raise ValueError("At least one character type must be selected!")

    passwords = []
    for _ in range(count):
        pwd = ''.join(secrets.choice(pool) for _ in range(length))
        passwords.append(pwd)

    return passwords if count > 1 else passwords[0]

def generate_pin(length=4, count=1):
    """
    Generates a numeric PIN.
    """
    if length < 1:
        raise ValueError("PIN length must be at least 1.")
    
    pins = []
    for _ in range(count):
        pin = ''.join(secrets.choice(string.digits) for _ in range(length))
        pins.append(pin)
        
    return pins if count > 1 else pins[0]

def generate_passphrase(words=4, separator="-", capitalize=False, count=1):
    """
    Generates a word-based passphrase. E.g., correct-horse-battery-staple
    """
    passphrases = []
    for _ in range(count):
        selected_words = [secrets.choice(WORD_LIST) for _ in range(words)]
        if capitalize:
            selected_words = [w.capitalize() for w in selected_words]
        
        passphrases.append(separator.join(selected_words))
        
    return passphrases if count > 1 else passphrases[0]

def estimate_strength(password):
    """
    Calculates password complexity (entropy) and rates it.
    """
    if not password:
        return {"entropy": 0, "score": 0, "label": "Empty"}
        
    # Estimate pool size
    pool_size = 0
    if any(c.islower() for c in password): pool_size += 26
    if any(c.isupper() for c in password): pool_size += 26
    if any(c.isdigit() for c in password): pool_size += 10
    if any(c in string.punctuation for c in password): pool_size += 32
    
    # Calculate entropy
    entropy = len(password) * math.log2(pool_size) if pool_size > 0 else 0
    entropy = round(entropy, 2)
    
    # Rating (Simple scale)
    if entropy < 28:
        score = 1
        label = "Very Weak"
    elif entropy < 36:
        score = 2
        label = "Weak"
    elif entropy < 60:
        score = 3
        label = "Moderate"
    elif entropy < 128:
        score = 4
        label = "Strong"
    else:
        score = 5
        label = "Very Strong"
    
    
    return {"entropy": entropy, "score": score, "label": label}


def get_entropy(length, pool_size):
    """Old function - for backward compatibility, estimate_strength is recommended."""
    if pool_size <= 0: return 0
    entropy = length * math.log2(pool_size)
    return round(entropy, 2)


def generate_url_safe_token(nbytes=32):
    """
    Generates a secure URL-safe text string.
    """
    return secrets.token_urlsafe(nbytes)


def generate_hex_token(nbytes=32):
    """
    Generates a secure hex string.
    """
    return secrets.token_hex(nbytes)


def generate_totp_secret(length=32):
    """
    Generates a base32 secret for TOTP (Time-based One-Time Password).
    Useful for MFA applications (e.g., Google Authenticator).
    """
    # Generate random bytes
    random_bytes = secrets.token_bytes(length)
    # Encode to base32
    secret = base64.b32encode(random_bytes).decode('utf-8')
    # Remove padding usually not needed for TOTP apps
    return secret.rstrip('=')

