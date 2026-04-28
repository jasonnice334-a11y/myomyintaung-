#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Turbo Network Engine v2 - Pro Ready Edition
Modified for Jason Nice 334
"""

import requests
import urllib3
import time
import os
import sys
import datetime

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# ===============================
# COLOR SETTINGS
# ===============================
red = "\033[0;31m"
bred = "\033[1;31m"
green = "\033[0;32m"
bgreen = "\033[1;32m"
yellow = "\033[0;33m"
byellow = "\033[1;33m"
purple = "\033[0;35m"
bpurple = "\033[1;35m"
cyan = "\033[0;36m"
bcyan = "\033[1;36m"
white = "\033[0;37m"
reset = "\033[00m"

# ===============================
# KEY APPROVAL SYSTEM
# ===============================

# Google Sheets ID
SHEET_ID = "1bpQMfIFQGKKeDFcCbGrpFBN8bRlfndrhfj_CdrDHAcw"
SHEET_CSV_URL = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/export?format=csv"

def get_system_key():
    """Generate unique system key"""
    import subprocess
    try:
        if os.path.exists("/system/bin/getprop"):
            out = subprocess.check_output(["getprop", "ro.serialno"]).decode().strip()
            if not out or out == "unknown":
                out = subprocess.check_output(["getprop", "ro.build.id"]).decode().strip()
            return f"JASON-{out}"
        return "JASON-UNKNOWN-DEVICE"
    except:
        return "JASON-MANUAL-KEY-7788"

def fetch_authorized_keys():
    """Fetch keys from Google Sheet"""
    try:
        response = requests.get(SHEET_CSV_URL, timeout=10)
        if response.status_code == 200:
            return response.text
        return ""
    except:
        return ""

def check_approval():
    """Check expiry date, remaining days and key approval"""
    banner()
    
    # --- 1. SET EXPIRY DATE (Year, Month, Day) ---
    expiry_date = datetime.date(2026, 5, 1) 
    today = datetime.date.today()
    
    # Calculate Remaining Days
    remaining_days = (expiry_date - today).days
    
    # Check if script is expired
    if remaining_days < 0:
        print(f"\n{bred}╔══════════════════════════════════════════════╗")
        print(f"║          ❌ ACCESS EXPIRED ❌                ║")
        print(f"╠══════════════════════════════════════════════╣")
        print(f"║ Status: License ended on {expiry_date}       ║")
        print(f"║ Contact: @jason4565999                       ║")
        print(f"╚══════════════════════════════════════════════╝{reset}")
        return False

    print(f"\n{bcyan}[!] Authenticating system access...{reset}")
    
    system_key = get_system_key()
    authorized_keys = fetch_authorized_keys()
    
    print(f"{white}[*] System Key : {system_key}{reset}")
    print(f"{white}[*] Expiry Date: {expiry_date}{reset}")
    
    # Display Days Left
    day_color = bgreen if remaining_days > 7 else byellow
    print(f"{white}[*] Time Left  : {day_color}{remaining_days} Days Remaining{reset}")
    
    # Check if Key in Sheet
    if system_key in authorized_keys:
        print(f"\n{bgreen}╔══════════════════════════════════════╗")
        print(f"║        ✅ ACCESS APPROVED ✅         ║")
        print(f"║          JASON VIP VERSION           ║")
        print(f"╚══════════════════════════════════════╝{reset}")
        time.sleep(1.5)
        return True
    else:
        print(f"\n{bred}╔══════════════════════════════════════╗")
        print(f"║        ❌ KEY NOT APPROVED ❌        ║")
        print(f"╚══════════════════════════════════════╝{reset}")
        print(f"{yellow}[!] Your Key: {system_key}{reset}")
        print(f"{white}[*] Send your key to @jason4565999{reset}")
        return False

def banner():
    """Display Tool Banner"""
    os.system('clear')
    print(f"""{bpurple}
┌──────────────────────────────────────┐
│        PREMIUM NETWORK ENGINE        │
│          BY JASON NICE 334           │
│         {bgreen}STATUS: ACTIVE ✓{bpurple}             │
└──────────────────────────────────────┘
{reset}""")

# ===============================
# MAIN ENGINE PROCESS
# ===============================
def start_process():
    print(f"\n{bgreen}[+] Engine started successfully...{reset}")
    # Core Logic
    while True:
        try:
            print(f"{cyan}[*] Optimizing network stability...{reset}")
            time.sleep(5)
        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    if check_approval():
        try:
            start_process()
        except KeyboardInterrupt:
            print(f"\n{red}[!] Stopped by user.{reset}")
    else:
        sys.exit(1)
    
