#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import urllib3
import time
import os
import sys
import datetime
import hashlib
import csv
import io

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# ===============================
# COLOR SETTINGS (FIXED)
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
blue = "\033[0;34m"
bblue = "\033[1;34m"
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
        else:
            out = "DEVICE-ID-7788"
        
        # 6-character short key
        short_id = hashlib.md5(out.encode()).hexdigest().upper()[:6]
        return f"{short_id}"
    except:
        return "VIP99X"

def banner():
    os.system('clear')
    print(f"""{bcyan}
╔══════════════════════════════════════════╗
║   {bpurple}⚡ PREMIUM NETWORK TURBO ENGINE ⚡{bcyan}     ║
╠══════════════════════════════════════════╣
║   {white}DEVELOPED BY  : JASON NICE 334{bcyan}         ║
║   {white}VERSION       : 2.5 (STABLE){bcyan}           ║
║   {white}STATUS        : {bgreen}ACTIVE ✓{bcyan}               ║
╚══════════════════════════════════════════╝{reset}""")

def check_approval():
    banner()
    print(f"\n{bpurple}»» {white}Authenticating System Access...{reset}")
    
    system_key = get_system_key()
    try:
        response = requests.get(SHEET_CSV_URL, timeout=10)
        if response.status_code == 200:
            f = io.StringIO(response.text)
            reader = csv.reader(f)
            for row in reader:
                # Read Column A (Key) and Column B (Expiry)
                if len(row) >= 2:
                    sheet_key = row[0].strip()
                    sheet_expiry = row[1].strip()
                    
                    if system_key == sheet_key:
                        try:
                            expiry_date = datetime.datetime.strptime(sheet_expiry, "%Y-%m-%d").date()
                            today = datetime.date.today()
                            remaining_days = (expiry_date - today).days
                            
                            if remaining_days < 0:
                                print(f"\n{bred}✖ ACCESS EXPIRED ON {expiry_date} ✖{reset}")
                                return False
                            
                            print(f"{white}ID  : {bcyan}{system_key}{reset}")
                            day_color = bgreen if remaining_days > 7 else byellow
                            print(f"{white}LEFT: {day_color}{remaining_days} Days Remaining{reset}")
                            
                            print(f"\n{bgreen}⚡══════════════════════════════════════⚡")
                            print(f"║       💎 ACCESS GRANTED 💎           ║")
                            print(f"╚══════════════════════════════════════╝{reset}")
                            time.sleep(1.5)
                            return True
                        except ValueError:
                            continue
    except:
        print(f"{red}✖ Connection Error!{reset}")
        return False

    print(f"\n{bred}✖══════════════════════════════════════✖")
    print(f"║       🛑 KEY NOT APPROVED 🛑         ║")
    print(f"╚══════════════════════════════════════╝{reset}")
    print(f"{yellow}[!] YOUR KEY: {system_key}{reset}")
    print(f"{white}[*] Please contact Admin for activation.{reset}")
    return False

def start_process():
    print(f"\n{bgreen}»» Engine initialization complete...{reset}")
    while True:
        try:
            print(
                
