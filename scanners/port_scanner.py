# scanners/port_scanner.py
import socket

def scan_ports(host, ports=[22, 23, 80, 443, 8080, 5000]):
    open_ports = []
    print(f"[*] Scanning ports on {host}")
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((host, port))
        if result == 0:
            open_ports.append(port)
            print(f"[+] Port {port} is open on {host}")
        sock.close()
    return open_ports

if __name__ == "__main__":
    target = input("Enter target IP: ")
    ports = scan_ports(target)
    print(f"\nOpen ports: {ports}")
