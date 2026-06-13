import subprocess
import re
import csv

def get_wifi_data():
    """Runs netsh to get network details."""
    try:
        # Run the command to list networks with BSSID details
        result = subprocess.check_output("netsh wlan show networks mode=bssid", shell=True).decode('utf-8', errors='ignore')
        return result
    except subprocess.CalledProcessError:
        print("[-] Error: Could not run netsh. Ensure you are on Windows.")
        return None

def parse_data(raw_data):
    """Parses the netsh output using regex."""
    networks = []
    # Split the output into individual network blocks
    blocks = re.split(r'SSID \d+ :', raw_data)
    
    for block in blocks[1:]:
        ssid = block.split('\n')[0].strip()
        auth = re.search(r'Authentication\s+:\s(.*)', block)
        enc = re.search(r'Encryption\s+:\s(.*)', block)
        
        auth_val = auth.group(1).strip() if auth else "Unknown"
        enc_val = enc.group(1).strip() if enc else "Unknown"
        
        # Security logic: Flag weak protocols
        security_level = "Secure"
        if "WEP" in auth_val or "None" in auth_val:
            security_level = "INSECURE (WEP or Open)"
        
        networks.append({"SSID": ssid, "Authentication": auth_val, "Encryption": enc_val, "Status": security_level})
    return networks

def save_report(networks):
    """Saves the parsed data to a CSV."""
    with open('wifi_audit_report.csv', 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=["SSID", "Authentication", "Encryption", "Status"])
        writer.writeheader()
        writer.writerows(networks)
    print("\n[*] Audit complete. Report saved to 'wifi_audit_report.csv'")

if __name__ == "__main__":
    print("[*] Auditing nearby networks... (This may take a moment)")
    raw_data = get_wifi_data()
    if raw_data:
        networks = parse_data(raw_data)
        for net in networks:
            print(f"SSID: {net['SSID']} | Auth: {net['Authentication']} | Status: {net['Status']}")
        save_report(networks)