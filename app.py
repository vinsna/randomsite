from flask import Flask, render_template, request
import random

app = Flask(__name__)

# Load domains from a file
def load_domains(filename, encoding='utf-8'):
    with open(filename, 'r', encoding=encoding) as file:
        return [line.strip() for line in file]

# Load the list of domains
domains = load_domains('domain-names.txt')

@app.route('/')
def index():
    # Select 5 random domains
    random_domains = random.sample(domains, 5)
    return render_template('index.html', domains=random_domains)

if __name__ == '__main__':
    app.run(debug=True)
