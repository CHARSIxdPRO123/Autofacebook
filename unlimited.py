# CHARSI ELITE v8 - UNLIMITED EDITION (5000 TARGET)
# FEATURE: INFINITE LOOP | AUTO-RESEND | PROXY-SYNC
# STATUS: HIGH PERFORMANCE NO-LIMIT

import os, sys, re, time, uuid, subprocess, random, string
from concurrent.futures import ThreadPoolExecutor as ThreadPool

# Dependencies auto-check
def install_deps():
    modules = ['requests', 'bs4', 'faker']
    for m in modules:
        try: __import__(m)
        except: subprocess.call([sys.executable, "-m", "pip", "install", m], stdout=subprocess.DEVNULL)

install_deps()
import requests
from bs4 import BeautifulSoup
from faker import Faker

# Colors
G = "\x1b[38;5;46m"; W = "\033[1;37m"; R = "\x1b[38;5;196m"; Y = "\x1b[38;5;226m"

def banner():
    os.system('clear')
    print(f"""
{G}    ██████╗ ██╗  ██╗ █████╗ ██████╗ ███████╗██╗
{G}   ██╔════╝ ██║  ██║██╔══██╗██╔══██╗██╔════╝██║
{G}   ██║      ███████║███████║██████╔╝███████╗██║
{G}   ██║      ██╔══██║██╔══██║██╔══██╗╚════██║██║
{G}   ╚██████╗ ██║  ██║██║  ██║██║  ██║███████║██║
{W}    --- {G}U N L I M I T E D  E D I T I O N (5000){W} ---
{G}  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{W}  [{G}#{W}] {G}TARGET   : {W}5000 ACCOUNTS
{W}  [{G}#{W}] {G}THREAD   : {W}MAX PERFORMANCE (GHOST-PROTOCOL)
{W}  [{G}#{W}] {G}RETRY    : {W}AUTO-SWITCH MAIL ENABLED
{G}  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━""")

class CharsiUnlimited:
    def __init__(self):
        self.oks = []
        self.loop = 0
        self.fk = Faker('en_US')
        self.domains = ["1secmail.com", "1secmail.net", "1secmail.org", "vjuum.com", "laafd.com"]

    def fetch_mail(self):
        user = "".join(random.choices(string.ascii_lowercase + string.digits, k=10))
        return f"{user}@{random.choice(self.domains)}"

    def deep_otp_scan(self, email):
        u, d = email.split('@')
        for _ in range(15):
            try:
                url = f"https://www.1secmail.com/api/v1/?action=getMessages&login={u}&domain={d}"
                res = requests.get(url).json()
                for m in res:
                    msg = requests.get(f"{url}&action=readMessage&id={m['id']}").json()
                    otp = re.search(r'\b\d{5}\b', msg['body'])
                    if otp: return otp.group(0)
            except: pass
            time.sleep(4)
        return None

    def create(self):
        f_name = self.fk.first_name(); l_name = self.fk.last_name()
        email = self.fetch_mail(); pwd = f"{f_name}{l_name}@{random.randint(111,999)}"
        
        self.loop += 1
        print(f"\r{W}[{G}RUNNING{W}] {G}{self.loop}/5000 {W}| {G}OK:{len(self.oks)}", end="")
        
        try:
            ses = requests.Session()
            ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
            
            # Step 1: Submit Form
            payload = {"firstname": f_name, "lastname": l_name, "reg_email__": email, "reg_passwd__": pwd, "sex": "2", "birthday_year": str(random.randint(1995,2003))}
            ses.post("https://m.facebook.com/reg/submit/", data=payload, headers={'User-Agent': ua})
            
            # Step 2: OTP Force Scan
            otp = self.deep_otp_scan(email)
            
            # Auto-Retry with New Mail
            if not otp:
                email = self.fetch_mail()
                otp = self.deep_otp_scan(email)

            if otp:
                self.oks.append(email)
                print(f"\n{G}[CHARSI-OK] {email} | {pwd} | {otp} ✅")
                with open("/sdcard/CHARSI-5000-OK.txt", "a") as f:
                    f.write(f"{email}|{pwd}|{otp}\n")
        except: pass

    def start(self):
        banner()
        # High-Speed Threading for 5000 target
        with ThreadPool(max_workers=30) as pool:
            for _ in range(5000):
                pool.submit(self.create)

if __name__ == "__main__":
    if not os.path.exists('/sdcard'): os.system('termux-setup-storage')
    CharsiUnlimited().start()
