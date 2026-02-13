__version__ = "0.5.1"

from .generator import (
    generate_password, 
    generate_pin, 
    generate_passphrase, 
    estimate_strength,
    generate_url_safe_token,
    generate_hex_token,
    generate_totp_secret
)

# Kısa kullanım için alias
generate = generate_password