# scanners/device_identifier.py
import socket

def identify_device(ip):
    try:
        hostname = socket.gethostbyaddr(ip)
        print(f"[+] Device at {ip} has hostname: {hostname[0]}")
        return hostname[0]
    except socket.herror:
        print(f"[-] Could not resolve hostname for {ip}")
        return None

if __name__ == "__main__":
    ip = input("Enter IP address to identify: ")
    identify_device(ip)
