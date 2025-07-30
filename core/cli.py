#!/usr/bin/env python3
import sys

def main():
    cmd = sys.argv[1:]

    if not cmd:
        print("Use -help to see available options.")
        return

    if "-install" in cmd:
        print("[+] Installing system modules...")
    elif "-u" in cmd:
        print("[*] Updating system...")
    elif "-s" in cmd:
        print("[~] Showing status...")
    else:
        print("[!] Unknown command. Use -help.")

if __name__ == "__main__":
    main()
