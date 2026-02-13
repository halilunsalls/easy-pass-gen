
from easy_pass_gen import generate_url_safe_token, generate_hex_token, generate_totp_secret

print("URL Safe Token:", generate_url_safe_token())
print("Hex Token:", generate_hex_token())
print("TOTP Secret:", generate_totp_secret())
