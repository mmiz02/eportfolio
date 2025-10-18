import requests

# Hard-coded my access key. Best practice is to store in environment variables or external configuration files.
ACCESS_KEY = "69cea2c10120f0374ebb2af2302642bb"

# Example public IP to query
test_ip = "134.201.250.155"

# Construct API request URL
url = f"https://api.ipstack.com/{test_ip}?access_key={ACCESS_KEY}"

try:
    # Make HTTPS request with certificate verification
    resp = requests.get(url, verify=True, timeout=10)
    resp.raise_for_status()  # Raise error for HTTP errors
    data = resp.json()

    # Print retrieved geolocation data
    print(data)

except requests.exceptions.RequestException as e:
    print("Error connecting to IPstack API:", e)
