# scanners/network_scanner.py
import subprocess
import platform
import ipaddress
import socket
import os

def is_linux():
    return platform.system().lower() == "linux"

def ping_sweep(subnet):
    """Ping sweep to detect live hosts on the subnet."""
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

def get_local_ip():
    """Returns the local IP address of the host."""
    hostname = socket.gethostname()
    try:
        local_ip = socket.gethostbyname(hostname)
        print(f"[*] Local IP: {hostname} -> {local_ip}")
        return local_ip
    except socket.gaierror:
        print(f"[-] Unable to retrieve local IP address")
        return None

def get_network_range(local_ip):
    """Returns the network range (subnet) based on the local IP."""
    if not local_ip:
        return None
    
    ip_obj = ipaddress.IPv4Address(local_ip)
    
    if ip_obj.is_private:
        network = ipaddress.IPv4Network(f"{local_ip}/24", strict=False)
        print(f"[*] Local network: {network}")
        return str(network)
    else:
        print("[-] Public IPs are not supported for local scanning.")
        return None

def get_local_ips():
    """Returns a list of live IP addresses in the local network."""
    local_ip = get_local_ip()
    if not local_ip:
        return []

    subnet = get_network_range(local_ip)
    if not subnet:
        return []

    live_ips = ping_sweep(subnet)
    return live_ips

if __name__ == "__main__":
    hosts = get_local_ips()
    print(f"\nDiscovered live hosts: {hosts}")
