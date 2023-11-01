import ipaddress #library for ip addresses

#function to ask the user for inputs
def get_user_input(prompt): 
    while True:
        user_input = input(prompt)
        if user_input:
            return user_input

#In order to avoid issues with connectivity we should avoid, this tool was intented when I need to create a random IP block for any VPN (WireGuard, OpenVPN, etc)
def generate_ip_blocks():
    # Prompt the user for WAN and LAN network details
    wan_subnet = ipaddress.IPv4Network(get_user_input("Enter your WAN subnet (e.g., 192.168.1.0/24): "), strict=False)
    lan_subnet = ipaddress.IPv4Network(get_user_input("Enter your LAN subnet (e.g., 192.168.2.0/24): "), strict=False)

    # Calculate and print available IP address blocks
    private_ranges = [
        ipaddress.IPv4Network("10.0.0.0/8"),
        ipaddress.IPv4Network("192.168.0.0/16"),
        ipaddress.IPv4Network("172.16.0.0/12"),
    ]

    available_blocks = []

    for private_range in private_ranges:
        # Check if the private range overlaps with WAN or LAN
        if private_range.overlaps(wan_subnet) or private_range.overlaps(lan_subnet):
            continue
        available_blocks.append(private_range)

    if not available_blocks:
        print("No available IP address blocks found.")
        return

    print("Available IP address blocks:")
    for idx, block in enumerate(available_blocks, start=1):
        print(f"{idx}. {block}")

if __name__ == "__main__":
    print("IP Address Block Generator")
    generate_ip_blocks()
