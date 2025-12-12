from netmiko import ConnectHandler
from datetime import datetime

# Routers we want to check
routers = [
    {
        'device_type': 'cisco_ios',
        'host': '10.0.0.1',   # R1
        'username': 'admin',
        'password': 'cisco',
    },
    {
        'device_type': 'cisco_ios',
        'host': '10.0.1.2',   # R2
        'username': 'admin',
        'password': 'cisco',
    }
]

# Commands we want to run on each router
commands = [
    "show ip route",
    "show ip ospf neighbor",
    "show ip bgp summary"
]

# Create a timestamp so every run has a unique file
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
logfile = f"routing_status_{timestamp}.txt"

# Open a file to save the output
with open(logfile, "w") as f:
    for router in routers:
        f.write(f"\n===== Router {router['host']} =====\n")

        # Connect to the router
        connection = ConnectHandler(**router)

        # Run each command
        for cmd in commands:
            f.write(f"\n--- {cmd} ---\n")
            output = connection.send_command(cmd)
            f.write(output + "\n")

        # Close SSH connection
        connection.disconnect()

print(f"Routing status saved to {logfile}")
