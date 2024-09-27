"# Main entry point for CLI or web-based interaction" 
from src.report.report_generator import generate_report
from utils import whois_lookup, dns_lookup, reverse_ip, api_calls

def main():
    domain = input("Enter a domain name: ")
    print(f"Analyzing domain: {domain}")
    
    # Perform WHOIS lookup
    whois_data = whois_lookup.get_whois_info(domain)
    
    # Perform DNS lookup
    dns_data = dns_lookup.get_dns_records(domain)
    
    # Historical data from SecurityTrails API
    historical_dns = api_calls.get_historical_dns(domain)
    
    # Reverse IP lookup
    ip = dns_lookup.get_ip(domain)
    reverse_ip_data = reverse_ip.get_hosted_sites(ip)
    
    # Combine the results
    generate_report(domain, whois_data, dns_data, historical_dns, reverse_ip_data)

if __name__ == "__main__":
    main()
