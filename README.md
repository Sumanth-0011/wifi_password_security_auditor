Name:G Sumanth 
Project Name:wifi password strength auditor
NO OF WEEKS: 6 weeks 
Project Scope:Wi-Fi Security Assessment Tool
Intern ID:CITS2197     
                                                  Wi-Fi Configuration Security Auditor

A Windows-based security auditing tool that assesses the configuration and security status of nearby wireless networks. This utility leverages native Windows networking commands to identify insecure network protocols.

Features:

Protocol Analysis: Detects Authentication (e.g., WPA2, WPA3) and Encryption standards.

Vulnerability Flagging: Automatically categorizes networks as "Secure" or "INSECURE (WEP or Open)."

Automated Reporting: Generates a structured CSV report for documentation and security review.

Native Execution: Uses built-in Windows netsh commands, requiring no external packet-sniffing drivers or high-privilege monitor mode.

Technical Implementation:
Language: Python 3.x

Libraries Used: - subprocess: Executes native Windows shell commands (netsh).

re: Parses and cleans the output for structured analysis.

csv: Exports audit data to a readable format.

How it Works:
The script interacts with the Windows Wireless Local Area Network (WLAN) service:

It executes netsh wlan show networks mode=bssid to gather raw wireless environment data.

It processes the raw text output using Regular Expressions to extract SSID, Authentication, and Encryption data.

It applies a security logic layer to identify protocols known to be vulnerable (e.g., WEP, Open).

The findings are compiled and saved to wifi_audit_report.csv.

Usage:
Ensure you are running Python 3.x on a Windows machine.

Run the script:

Bash
python wifi_auditor.py
The script will output the audit status to the console and generate a CSV file in the same directory.

Security & Ethical Warning:
CRITICAL: This tool is for educational and authorized security auditing purposes only. Use this tool only on networks you own or have explicit written permission to audit. The tool performs passive configuration discovery, but always adhere to local laws and company security policies.
