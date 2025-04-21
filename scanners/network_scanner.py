# scanners/network_scanner.py
import subprocess
import platform
import ipaddress
import re
import socket

def is_linux():
    return platform.system().lower() == "linux"

def ping_sweep(subnet):
    if not is_linux():
        print("This tool only works on Linux systems.")
        return []

    live_hosts = []
    print(f"[*] Scanning subnet: {subnet}")

    for ip in ipaddress.IPv4Network(subnet, strict=False):
        ip_str = str(ip)
        try:
            result = subprocess.run(["ping", "-c", "1", "-W", "1", ip_str], stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
            if result.returncode == 0:
                print(f"[+] Host {ip_str} is up")
                live_hosts.append(ip_str)
        except Exception as e:
            print(f"Error scanning {ip_str}: {e}")

    return live_hosts

def get_local_ips():
    """Returns a list of local IP addresses on the machine."""
    local_ips = []
    hostname = socket.gethostname()
    try:
        local_ips.append(socket.gethostbyname(hostname))
        print(f"[*] Local IP: {hostname} -> {socket.gethostbyname(hostname)}")
    except socket.gaierror:
        print(f"[-] Unable to retrieve local IP address")
    return local_ips

if __name__ == "__main__":
    subnet = input("Enter subnet (e.g., 192.168.1.0/24): ")
    hosts = ping_sweep(subnet)
    print(f"\nDiscovered live hosts: {hosts}")

