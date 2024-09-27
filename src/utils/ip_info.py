"# Functions to retrieve info from IP addresses" 
import requests

def get_ip_info(ip_address):
    try:
        # Example IP info API (replace with a real one)
        api_url = f"http://ip-api.com/json/{ip_address}"
        response = requests.get(api_url)
        return response.json()  # Assuming the API returns JSON
    except Exception as e:
        return f"Error fetching IP information: {str(e)}"
