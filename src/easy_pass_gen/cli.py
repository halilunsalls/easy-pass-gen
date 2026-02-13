import click
import pyperclip
import colorama
from colorama import Fore, Style
from .generator import generate_password, generate_pin, generate_passphrase, estimate_strength

# Initialize Colorama
colorama.init(autoreset=True)

@click.group()
@click.version_option()
def main():
    """Easy Pass Gen - Secure password and passphrase generator."""
    pass

def copy_to_clipboard(text, label="Password"):
    try:
        pyperclip.copy(text)
        click.echo(Fore.GREEN + f"✅ {label} copied to clipboard!")
    except Exception as e:
        click.echo(Fore.RED + f"❌ Clipboard copy error: {e}")

@main.command()
@click.option('--length', '-l', default=16, help='Password length.')
@click.option('--no-upper', is_flag=True, help='No uppercase.')
@click.option('--no-lower', is_flag=True, help='No lowercase.')
@click.option('--no-digits', is_flag=True, help='No digits.')
@click.option('--no-symbols', is_flag=True, help='No symbols.')
@click.option('--count', '-c', default=1, help='Number of passwords to generate.')
@click.option('--copy/--no-copy', default=False, help='Automatically copy to clipboard (only for single password generation).')
def generate(length, no_upper, no_lower, no_digits, no_symbols, count, copy):
    """Generates strong random passwords."""
    try:
        passwords = generate_password(
            length=length,
            use_upper=not no_upper,
            use_lower=not no_lower,
            use_digits=not no_digits,
            use_symbols=not no_symbols,
            count=count
        )
        
        if count == 1:
            passwords = [passwords]
            
        for pwd in passwords:
            strength = estimate_strength(pwd)
            color = Fore.WHITE
            if strength['score'] >= 4: color = Fore.GREEN
            elif strength['score'] == 3: color = Fore.YELLOW
            else: color = Fore.RED
            
            click.echo(f"Password: {Style.BRIGHT}{color}{pwd}{Style.RESET_ALL}  [{strength['label']}]")
            
        if copy and count == 1:
            copy_to_clipboard(passwords[0])
            
    except ValueError as e:
        click.echo(Fore.RED + f"Error: {e}")

@main.command()
@click.option('--words', '-w', default=4, help='Number of words.')
@click.option('--separator', '-s', default='-', help='Word separator.')
@click.option('--capitalize', is_flag=True, help='Capitalize words.')
@click.option('--count', '-c', default=1, help='Number of passphrases to generate.')
@click.option('--copy/--no-copy', default=False, help='Copy to clipboard.')
def passphrase(words, separator, capitalize, count, copy):
    """Generates memorable passphrases."""
    phrases = generate_passphrase(words=words, separator=separator, capitalize=capitalize, count=count)
    
    if count == 1:
        phrases = [phrases]
        
    for phrase in phrases:
        click.echo(f"Passphrase: {Style.BRIGHT}{Fore.CYAN}{phrase}{Style.RESET_ALL}")
        
    if copy and count == 1:
        copy_to_clipboard(phrases[0], label="Passphrase")

@main.command()
@click.option('--length', '-l', default=4, help='PIN length.')
@click.option('--count', '-c', default=1, help='Number of PINs to generate.')
@click.option('--copy/--no-copy', default=False, help='Copy to clipboard.')
def pin(length, count, copy):
    """Generates numeric PINs only."""
    pins = generate_pin(length=length, count=count)
    
    if count == 1:
        pins = [pins]
        
    for p in pins:
        click.echo(f"PIN: {Style.BRIGHT}{Fore.BLUE}{p}{Style.RESET_ALL}")
        
    if copy and count == 1:
        copy_to_clipboard(pins[0], label="PIN")

@main.command()
@click.argument('password')
def check(password):
    """Checks the strength of a given password."""
    strength = estimate_strength(password)
    
    color = Fore.WHITE
    if strength['score'] >= 4: color = Fore.GREEN
    elif strength['score'] == 3: color = Fore.YELLOW
    else: color = Fore.RED
    
    click.echo(f"Password: {password}")
    click.echo(f"Entropy: {strength['entropy']} bits")
    click.echo(f"Rating: {color}{strength['label']} ({strength['score']}/5){Style.RESET_ALL}")

if __name__ == '__main__':
    main()
