#!/bin/bash
sudo apt update
sudo apt install dnsmasq -y
sudo systemctl stop systemd-resolved
sudo systemctl disable systemd-resolved
echo "address=/libertotfg.test/192.168.222.144" | sudo tee /etc/dnsmasq.conf
sudo systemctl restart dnsmasq
sudo systemctl enable dnsmasq
