import random
import webbrowser

# Read domains from a file with specified encoding
def load_domains(filename, encoding='utf-8'):
    with open(filename, 'r', encoding=encoding) as file:
        # Read all lines and strip whitespace (including newlines)
        return [line.strip() for line in file]

# Load the list of domains
try:
    domains = load_domains('domain-names.txt')
except UnicodeDecodeError as e:
    print(f"Error reading the file: {e}")
    print("Try using a different encoding, e.g., 'latin-1' or 'ISO-8859-1'.")
    raise

# Open 5 random domains in a web browser
for _ in range(1):
    random_domain = random.choice(domains)
    url = f"http://{random_domain}"  # Assuming domains are to be accessed over HTTP
    print(f"Opening: {url}")
    webbrowser.open(url)
