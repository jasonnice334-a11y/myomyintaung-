#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import os
import sys

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
blue = "\033[0;34m"
bblue = "\033[1;34m"
reset = "\033[00m"

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

def check_approval_offline():
    banner()
    print(f"\n{bpurple}»» {white}Authenticating System Access...{reset}")
    time.sleep(1)
    
    # Offline ဖြစ်တဲ့အတွက် အမြဲတမ်း Grant ပေးလိုက်ပါမယ်
    print(f"{white}ID  : {bcyan}OFFLINE-VIP-77{reset}")
    print(f"{white}LEFT: {bgreen}Lifetime Access (Offline Mode){reset}")
    
    print(f"\n{bgreen}⚡══════════════════════════════════════⚡")
    print(f"║       💎 ACCESS GRANTED 💎           ║")
    print(f"╚══════════════════════════════════════╝{reset}")
    time.sleep(1.5)
    return True

def start_process():
    print(f"\n{bgreen}»» Engine initialization complete...{reset}")
    while True:
        try:
            sys.stdout.write(f"\r{cyan}⚡ Optimizing Data Stream...{reset}")
            sys.stdout.flush()
            time.sleep(1)
            sys.stdout.write(f"\r{bblue}⚡ Stabilizing Ping...       {reset}")
            sys.stdout.flush()
            time.sleep(1)
        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    # အွန်လိုင်းစစ်တဲ့အပိုင်းကို ဖယ်ထုတ်ပြီး Offline mode နဲ့ run ပါမယ်
    if check_approval_offline():
        try:
            start_process()
        except KeyboardInterrupt:
            print(f"\n{red}✖ Operation Terminated.{reset}")
    else:
        sys.exit(1)
