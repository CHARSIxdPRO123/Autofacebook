#!/bin/bash
# CHARSI BRAND - SYSTEM OPTIMIZER v2025
clear
echo -e "\e[1;32m[+] Optimizing System for Charsi God-Mode..."
pkg update -y && pkg upgrade -y
pkg install python openssl git -y
termux-setup-storage
pip install --upgrade pip
pip install requests bs4 faker fake-useragent
echo -e "\e[1;32m[+] SUCCESS: Environment Optimized. Now run proxy setup."
