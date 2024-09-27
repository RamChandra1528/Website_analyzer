import requests

def make_api_call(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()  # Assuming the API returns JSON
    except requests.exceptions.RequestException as e:
        return f"Error making API call: {str(e)}"
