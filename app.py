from flask import Flask, render_template, request
from src.utils.whois_lookup import get_whois_info # type: ignore
from src.utils.dns_lookup import get_dns_info # type: ignore
from src.utils.reverse_ip import reverse_ip_lookup # type: ignore
import os

# Initialize Flask app with the correct template folder path
app = Flask(__name__, template_folder=os.path.join('src', 'web', 'templates'))

@app.route('/')
def home():
    return render_template('index.html')  # Flask should find the index.html here

@app.route('/analyze', methods=['POST'])
def analyze():
    domain = request.form['domain']
    whois_data = get_whois_info(domain)
    dns_data = get_dns_info(domain)
    reverse_ip_data = reverse_ip_lookup(domain)

    return render_template('results.html', domain=domain, whois_data=whois_data, dns_data=dns_data, reverse_ip_data=reverse_ip_data)

if __name__ == '__main__':
    app.run(debug=True)
