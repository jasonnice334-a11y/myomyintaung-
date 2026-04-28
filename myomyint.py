#!/usr/bin/env python3
# -*- coding: utf-8 -*-

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

SHEET_ID = "1bpQMfIFQGKKeDFcCbGrpFBN8bRlfndrhfj_CdrDHAcw"
SHEET_CSV_URL = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/export?format=csv"

def get_system_key():
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

def banner():
    os.system('clear')
    print(f"""{bpurple}
┌──────────────────────────────────────┐
│        PREMIUM NETWORK ENGINE        │
│          BY JASON NICE 334           │
│         {bgreen}STATUS: ACTIVE ✓{bpurple}             │
└──────────────────────────────────────┘
{reset}""")

def check_approval():
    banner()
    print(f"\n{bcyan}[!] Authenticating system access...{reset}")
    
    system_key = get_system_key()
    try:
        response = requests.get(SHEET_CSV_URL, timeout=10)
        if response.status_code == 200:
            lines = response.text.strip().split('\n')
            for line in lines:
                parts = line.split(',')
                if len(parts) >= 2:
                    sheet_key = parts[0].strip().strip('"')
                    sheet_expiry = parts[1].strip().strip('"')
                    
                    if system_key == sheet_key:
                        try:
                            expiry_date = datetime.datetime.strptime(sheet_expiry, "%Y-%m-%d").date()
                            today = datetime.date.today()
                            remaining_days = (expiry_date - today).days
                            
                            if remaining_days < 0:
                                print(f"\n{bred}╔══════════════════════════════════════════════╗")
                                print(f"║          ❌ ACCESS EXPIRED ❌                ║")
                                print(f"╠══════════════════════════════════════════════╣")
                                print(f"║ Status: License ended on {expiry_date}       ║")
                                print(f"║ Contact: @jason4565999                       ║")
                                print(f"╚══════════════════════════════════════════════╝{reset}")
                                return False
                            
                            print(f"{white}[*] System Key : {system_key}{reset}")
                            print(f"{white}[*] Expiry Date: {expiry_date}{reset}")
                            day_color = bgreen if remaining_days > 7 else byellow
                            print(f"{white}[*] Time Left  : {day_color}{remaining_days} Days Remaining{reset}")
                            
                            print(f"\n{bgreen}╔══════════════════════════════════════╗")
                            print(f"║        ✅ ACCESS APPROVED ✅         ║")
                            print(f"║          JASON VIP VERSION           ║")
                            print(f"╚══════════════════════════════════════╝{reset}")
                            time.sleep(1.5)
                            return True
                        except ValueError:
                            continue
    except:
        print(f"{red}[!] Connection Error. Please check internet.{reset}")
        return False

    print(f"\n{bred}╔══════════════════════════════════════╗")
    print(f"║        ❌ KEY NOT APPROVED ❌        ║")
    print(f"╚══════════════════════════════════════╝{reset}")
    print(f"{yellow}[!] Your Key: {system_key}{reset}")
    print(f"{white}[*] Contact @jason4565999 for access{reset}")
    return False

def start_process():
    print(f"\n{bgreen}[+] Engine started successfully...{reset}")
    while True:
        try:
            print(f"{cyan}[*] Optimizing network stability...{reset}", end="\r")
            time.sleep(2)
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
        
