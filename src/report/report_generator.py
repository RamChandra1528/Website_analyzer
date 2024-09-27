"# Function to combine all findings into a report" 
def generate_report(domain, whois_data, dns_data, historical_dns, reverse_ip_data):
    print("\nReport for domain:", domain)
    
    # WHOIS Information
    print("\nWHOIS Data:")
    print(whois_data)
    
    # DNS Records
    print("\nDNS Records:")
    print(dns_data)
    
    # Historical DNS
    print("\nHistorical DNS Data:")
    print(historical_dns)
    
    # Reverse IP Lookup
    print("\nReverse IP Data (Other hosted domains):")
    print(reverse_ip_data)
