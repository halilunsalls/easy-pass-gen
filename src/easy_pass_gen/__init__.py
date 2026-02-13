__version__ = "0.3.0"

from .generator import generate_password, generate_pin, generate_passphrase, estimate_strength

# Kısa kullanım için alias
generate = generate_password