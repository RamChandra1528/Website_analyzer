import socket

def get_dns_info(domain):
    try:
        return socket.gethostbyname_ex(domain)
    except socket.gaierror as e:
        return f"Error fetching DNS info: {e}"

def reverse_ip_lookup(domain):
    try:
        ip_address = socket.gethostbyname(domain)
        return f"IP Address: {ip_address}"
    except socket.gaierror as e:
        return f"Error fetching Reverse IP info: {e}"
