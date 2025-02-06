import os
import subprocess

def install_dependencies():
    """Installs OpenVPN and EasyRSA."""
    print("Installing OpenVPN and EasyRSA...")
    os.system("sudo apt update && sudo apt install -y openvpn easy-rsa")

def setup_vpn_server():
    """Sets up the OpenVPN server."""
    print("Setting up OpenVPN server...")
    os.system("make-cadir ~/openvpn-ca")
    os.chdir("~/openvpn-ca")
    
    # Initialize PKI
    os.system("./easyrsa init-pki")
    os.system("./easyrsa build-ca nopass")
    os.system("./easyrsa gen-req server nopass")
    os.system("./easyrsa sign-req server server")
    os.system("./easyrsa gen-dh")
    os.system("openvpn --genkey --secret keys/ta.key")

def configure_openvpn():
    """Configures OpenVPN server settings."""
    print("Configuring OpenVPN server...")
    os.system("cp ~/openvpn-ca/keys/{ca.crt,server.crt,server.key,ta.key,dh.pem} /etc/openvpn")
    
    vpn_config = """
    port 1194
    proto udp
    dev tun
    ca /etc/openvpn/ca.crt
    cert /etc/openvpn/server.crt
    key /etc/openvpn/server.key
    dh /etc/openvpn/dh.pem
    auth SHA256
    cipher AES-256-CBC
    user nobody
    group nogroup
    persist-key
    persist-tun
    verb 3
    """
    
    with open("/etc/openvpn/server.conf", "w") as config_file:
        config_file.write(vpn_config)

def enable_ip_forwarding():
    """Enables IP forwarding."""
    print("Enabling IP forwarding...")
    os.system("echo 1 > /proc/sys/net/ipv4/ip_forward")
    os.system("iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE")

def start_vpn_server():
    """Starts OpenVPN server."""
    print("Starting OpenVPN server...")
    os.system("systemctl start openvpn@server")
    os.system("systemctl enable openvpn@server")
    print("VPN Server is now running!")

def main():
    install_dependencies()
    setup_vpn_server()
    configure_openvpn()
    enable_ip_forwarding()
    start_vpn_server()

if __name__ == "__main__":
    main()
