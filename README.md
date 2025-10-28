# 🛡️ SOC_Projects: Basic Python Ping Scanner

## 💡 Project Overview

This repository hosts my initial automation project as part of my Security Operations Center (SOC) Analyst learning journey.

It includes a foundational **`ping_scanner.py`** Python script designed to perform simple network host reachability checks using the **ICMP (Internet Control Message Protocol) Ping**.

This tool is fundamental for basic network monitoring, troubleshooting, and verifying host status—a common task in a Level 1 SOC environment.

## ⚙️ How to Use (Usage Guide)

1.  **Run the Script:**
    Execute the Python script from your Kali Linux terminal:
    ```bash
    python3 ping_scanner.py
    ```

2.  **Input:** The script will prompt you to enter the Target IP Address or Hostname.
    ```
    Enter the IP address or hostname to ping: 8.8.8.8
    ```

3.  **Output:** The script reports whether the host is UP or DOWN based on the ICMP response.

## ⭐ SOC Skills Demonstrated

This project showcases the following essential skills required for a security analyst role:

* **Python Scripting:** Practical application of Python for network automation tasks.
* **Networking Fundamentals:** Understanding of the ICMP protocol and its use in checking basic connectivity (a core SOC analysis skill).
* **Subprocess Module:** Ability to securely execute operating system commands (`ping`) from within Python code.
* **Automation Mindset:** Focus on converting repetitive manual checks into automated processes, essential for efficiency in a SOC.

## 🤝 Contributor

**R K Singh**
