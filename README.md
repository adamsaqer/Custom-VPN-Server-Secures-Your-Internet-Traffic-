# Custom VPN Server 🌍🔒

## Overview
This project sets up a **self-hosted VPN server** using **OpenVPN** to secure internet traffic.

## Features
- 🔐 **Secure AES-256 encryption**
- 🚀 **Automated OpenVPN installation & setup**
- 🌍 **Self-hosted solution for privacy**
- ⚡ **Supports UDP for fast, secure connections**

## Installation & Setup
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/adamsaqer/custom-vpn-server.git
cd custom-vpn-server
```

### 2️⃣ Run the Script
```bash
sudo python3 custom_vpn_server.py
```

This will:
✅ Install **OpenVPN** and **EasyRSA**
✅ Generate **encryption keys**
✅ Configure the **server**
✅ Enable **IP forwarding**
✅ Start the VPN service

## Configuration
- Edit `/etc/openvpn/server.conf` to modify settings.
- Restart VPN service after changes:
```bash
sudo systemctl restart openvpn@server
```

## Connecting to the VPN
1️⃣ Generate client config:
```bash
sudo ./easyrsa gen-req client1 nopass
sudo ./easyrsa sign-req client client1
```
2️⃣ Transfer `.ovpn` file to your device.
3️⃣ Import the file into **OpenVPN Client** and connect!

## License
This project is licensed under the **MIT License**.
