#!/bin/bash
# tool to create private ip address when preparing a local network for VPN or Local Network
# Rev. 2023.07.25 

generate_random_octet() {
  echo $((RANDOM % 256))
}

generate_random_ip_class_a() {
  echo "10.$(generate_random_octet).$(generate_random_octet).$(generate_random_octet)"
}

generate_random_ip_class_b() {
  echo "172.$((16 + RANDOM % 16)).$(generate_random_octet).$(generate_random_octet)"
}

generate_random_ip_class_c() {
  echo "192.168.$(generate_random_octet).$(generate_random_octet)"
}

echo "Choose the IP class for the private IP address:"
echo "A) Class A (10.0.0.0/8)"
echo "B) Class B (172.16.0.0/12)"
echo "C) Class C (192.168.0.0/16)"
read -r choice

case $choice in
  "A" | "a")
    random_ip=$(generate_random_ip_class_a)
    ;;
  "B" | "b")
    random_ip=$(generate_random_ip_class_b)
    ;;
  "C" | "c")
    random_ip=$(generate_random_ip_class_c)
    ;;
  *)
    echo "Invalid choice. Exiting."
    exit 1
    ;;
esac

echo "Random Private IP Address: $random_ip"
# Further steps for setting up WireGuard VPN with the generated IP can be added here.
