# main.py
from scanners.network_scanner import get_local_ips
from scanners.port_scanner import scan_ports
from scanners.device_identifier import identify_device
from bruteforce.http_bruteforce import http_bruteforce
from bruteforce.ssh_bruteforce import ssh_bruteforce
from bruteforce.telnet_bruteforce import telnet_bruteforce


def main():
    ips = get_local_ips()
    for ip in ips:
        print(f"\n[+] Scanning IP: {ip}")
        identify_device(ip)
        open_ports = scan_ports(ip)

        if 80 in open_ports:
            http_bruteforce(ip)
        if 22 in open_ports:
            ssh_bruteforce(ip)
        if 23 in open_ports:
            telnet_bruteforce(ip)


if __name__ == "__main__":
    main()
