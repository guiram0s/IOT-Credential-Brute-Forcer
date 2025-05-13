import json
import os

def load_credentials():
    
    base_dir = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(base_dir, "..", "defaults", "common_credentials.json")

    try:
        with open(filepath, "r") as f:
            data = json.load(f)
        creds = []
        for vendor_creds in data.values():
            for cred in vendor_creds:
                creds.append((cred["username"], cred["password"]))
        return list(set(creds))  # remove duplicados
    except Exception as e:
        print(f"[!] Failed to load credentials: {e}")
        return []
