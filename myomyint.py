#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import re
import urllib3
import time
import threading
import logging
import random
import os
import sys
import json
import hashlib
from urllib.parse import urlparse, parse_qs, urljoin
from datetime import datetime, date, timedelta

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# ===============================
# COLOR SYSTEM
# ===============================
RED = "\033[91m"
GREEN = "\033[92m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
MAGENTA = "\033[95m"
WHITE = "\033[97m"
RESET = "\033[0m"

# ===============================
# KEY & LICENSE SETTINGS
# ===============================
SHEET_CSV_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRuFebZZ-vGXmobRjDU9C1dWRgcSjXwQ5YjK24Goh9rE0TQtoDXYaKBGWPs94_INOTUuzlXAiXAx42P/pub?output=csv"

LOCAL_KEYS_FILE = os.path.expanduser("~/.ruijie_approved_keys.txt")
KEY_STORAGE_FILE = os.path.expanduser("~/.ruijie_device_key.txt")
LICENSE_INFO_FILE = os.path.expanduser("~/.ruijie_license_info.txt")

# ===============================
# 6-DIGIT KEY SYSTEM
# ===============================
def get_system_key():
    """Generate or retrieve a 6-digit stable key"""
    if os.path.exists(KEY_STORAGE_FILE):
        with open(KEY_STORAGE_FILE, 'r') as f:
            return f.read().strip()
    
    try:
        import subprocess
        android_id = subprocess.check_output("settings get secure android_id", shell=True).decode().strip()
        # ၆ လုံးပဲ ယူရန် ပြင်ဆင်ထားသည်
        stable_key = hashlib.md5(f"OGGY_{android_id}".encode()).hexdigest().upper()[:6]
    except:
        stable_key = ''.join(random.choices("ABCDEF1234567890", k=6))
    
    with open(KEY_STORAGE_FILE, 'w') as f:
        f.write(stable_key)
    return stable_key

# ===============================
# DATE & LICENSE LOGIC
# ===============================
def get_days_left(expiry_date_str):
    try:
        expiry_date = datetime.strptime(expiry_date_str, "%Y-%m-%d").date()
        days = (expiry_date - date.today()).days
        return days
    except:
        return 0

def save_license_info(expiry_date_str):
    data = {"expiry": expiry_date_str, "valid": True}
    with open(LICENSE_INFO_FILE, 'w') as f:
        json.dump(data, f)

def load_license_info():
    if os.path.exists(LICENSE_INFO_FILE):
        try:
            with open(LICENSE_INFO_FILE, 'r') as f:
                return json.load(f)
        except: return None
    return None

def fetch_online_keys():
    keys_data = {}
    try:
        response = requests.get(SHEET_CSV_URL, timeout=8)
        if response.status_code == 200:
            for line in response.text.strip().split('\n'):
                parts = line.split(',')
                if len(parts) >= 3:
                    key = parts[0].strip().strip('"')
                    expiry = parts[2].strip().strip('"')
                    keys_data[key] = expiry
            # Cache it
            with open(LOCAL_KEYS_FILE, 'w') as f:
                json.dump(keys_data, f)
            return keys_data
    except:
        if os.path.exists(LOCAL_KEYS_FILE):
            with open(LOCAL_KEYS_FILE, 'r') as f:
                return json.load(f)
    return {}

def check_approval():
    system_key = get_system_key()
    print(f"\n{MAGENTA}╔════════════════════════════════════╗")
    print(f"║       OGGY PREMIUM SYSTEM          ║")
    print(f"╚════════════════════════════════════╝{RESET}")
    print(f"{WHITE}[*] YOUR KEY: {YELLOW}{system_key}{RESET}")
    print(f"{CYAN}[*] Verifying License...{RESET}")

    # Try Online First
    online_keys = fetch_online_keys()
    
    if system_key in online_keys:
        expiry_str = online_keys[system_key]
        days_left = get_days_left(expiry_str)
        
        if days_left >= 0:
            print(f"{GREEN}[✓] ACCESS GRANTED!{RESET}")
            print(f"{GREEN}[✓] Expire in: {days_left} days ({expiry_str}){RESET}")
            save_license_info(expiry_str)
            time.sleep(1)
            return True
        else:
            print(f"{RED}[✗] KEY EXPIRED ON {expiry_str}{RESET}")
            return False

    # Fallback to Offline/Saved License
    saved = load_license_info()
    if saved:
        days_left = get_days_left(saved['expiry'])
        if days_left >= 0:
            print(f"{GREEN}[✓] OFFLINE MODE ACTIVE{RESET}")
            print(f"{GREEN}[✓] Expire in: {days_left} days left{RESET}")
            time.sleep(1)
            return True

    print(f"{RED}[✗] KEY NOT REGISTERED{RESET}")
    print(f"{YELLOW}[!] Contact admin to activate key: {system_key}{RESET}")
    return False

# ===============================
# MAIN ENGINE
# ===============================
def start_process():
    print(f"\n{CYAN}[*] Turbo Engine Starting...{RESET}")
    # ... (ကျန်တဲ့ Bypass Logic များက အရင်အတိုင်း ဖြစ်ပါတယ်)
    # ဥပမာအနေနဲ့-
    while True:
        print(f"{GREEN}[✓] Connected to Server...{RESET}", end="\r")
        time.sleep(2)

if __name__ == "__main__":
    try:
        if check_approval():
            # ဒီနေရာမှာ အောက်က start_process() အစား သင့်ရဲ့ မူရင်း Bypass logic function ကို ထည့်ပေးပါ
            # start_process() 
            print(f"\n{CYAN}--- ENGINE ACTIVE ---{RESET}")
            # မူရင်း code ထဲက start_process() ကို ဒီအောက်မှာ ဆက်ရေးနိုင်ပါတယ်
        else:
            sys.exit()
    except KeyboardInterrupt:
        print(f"\n{RED}[!] Shutdown.{RESET}")
        
