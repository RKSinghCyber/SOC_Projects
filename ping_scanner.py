import os
import subprocess

# --- This script performs a basic host reachability check (ICMP Ping) ---

# Step 1: Prompt user for the target IP or domain
target_ip = input("Enter the IP address or hostname to ping: ")

print(f"\n[INFO] Attempting to ping: {target_ip}...")

# Step 2: Execute the ping command
# '-c 1' sends only one ICMP packet
# subprocess.DEVNULL suppresses the output, we only care about the return code
response = subprocess.call(['ping', '-c', '1', target_ip], 
                           stdout=subprocess.DEVNULL, 
                           stderr=subprocess.DEVNULL)

# Step 3: Check the return code (0 means success) and report the result
if response == 0:
    print(f"\n[SUCCESS] Host {target_ip} is UP and reachable. \n")
else:
    print(f"\n[FAIL] Host {target_ip} is DOWN or unreachable. \n")