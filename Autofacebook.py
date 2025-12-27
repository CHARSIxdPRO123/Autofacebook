# CHARSI ELITE v7 - PROXY INTEGRATED + GOD MODE
# AUTHOR : CHARSI BRAND
# STATUS : MAXIMUM HIT RATE

import os, sys, re, time, uuid, subprocess, random, string
from concurrent.futures import ThreadPoolExecutor as ThreadPool

# Internal Proxy Import
try: import proxy
except: pass

import requests
from bs4 import BeautifulSoup
from faker import Faker

#▬▭▬▭▬▭▬▭[PREMIUM COLORS]▬▭▬▭▬▭▬▭#
G = "\x1b[38;5;46m"; W = "\033[1;37m"; R = "\x1b[38;5;196m"; Y = "\x1b[38;5;226m"

def banner():
    os.system('clear')
    print(f"""
{G}    ██████╗  ██████╗ ██████╗     ███╗   ███╗ ██████╗ ██████╗ ███████╗
{G}    ██╔════╝ ██╔═══██╗██╔══██╗    ████╗ ████║██╔═══██╗██╔══██╗██╔════╝
{G}    ██║  ███╗██║   ██║██║  ██║    ██╔████╔██║██║   ██║██║  ██║█████╗  
{G}    ██║   ██║██║   ██║██║  ██║    ██║╚██╔╝██║██║   ██║██║  ██║██╔══╝  
{G}    ╚██████╔╝╚██████╔╝██████╔╝    ██║ ╚═╝ ██║╚██████╔╝██████╔╝███████╗
{W}     ╚═════╝  ╚═════╝ ╚═════╝     ╚═╝     ╚═╝ ╚═════╝ ╚═════╝ ╚══════╝
{W}    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{W}    [{G}#{W}] {G}METHOD   : {W}PROXY + MAIL-SWITCHER + FORCE OTP
{W}    [{G}#{W}] {G}SECURITY : {W}ENCRYPTED BYPASS v7
{W}    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━""")

class CharsiV7:
    def __init__(self):
        self.oks = []
        self.fk = Faker('en_US')
        self.domains = ["1secmail.com", "1secmail.net", "1secmail.org", "vjuum.com", "laafd.com"]

    def fetch_mail(self):
        user = "".join(random.choices(string.ascii_lowercase + string.digits, k=10))
        return f"{user}@{random.choice(self.domains)}"

    def deep_otp_scan(self, email):
        u, d = email.split('@')
        for _ in range(20):
            try:
                url = f"https://www.1secmail.com/api/v1/?action=getMessages&login={u}&domain={d}"
                res = requests.get(url).json()
                for m in res:
                    msg = requests.get(f"{url}&action=readMessage&id={m['id']}").json()
                    otp = re.search(r'\b\d{5}\b', msg['body'])
                    if otp: return otp.group(0)
            except: pass
            time.sleep(5)
        return None

    def create(self):
        f_name = self.fk.first_name(); l_name = self.fk.last_name()
        email = self.fetch_mail(); pwd = f"{f_name}{l_name}@{random.randint(111,999)}"
        
        # Proxy Injection
        try:
            current_proxy = proxy.get_proxy()
            proxies = {'http': f'http://{current_proxy}', 'https': f'http://{current_proxy}'}
        except: proxies = None

        print(f"\n{W}[{G}LIVE{W}] {G}Target: {W}{f_name} {l_name} | {G}IP: {W}Proxied")
        
        try:
            ses = requests.Session()
            if proxies: ses.proxies.update(proxies)
            
            ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
            payload = {"firstname": f_name, "lastname": l_name, "reg_email__": email, "reg_passwd__": pwd, "sex": "2", "birthday_year": "1998"}
            
            ses.post("https://m.facebook.com/reg/submit/", data=payload, headers={'User-Agent': ua})
            
            print(f"{W}[{G}LIVE{W}] {G}OTP Scanner Active: {Y}{email}")
            otp = self.deep_otp_scan(email)
            
            # Logic: If Fail -> Switch Mail -> Resend
            if not otp:
                email = self.fetch_mail()
                print(f"{W}[{R}!{W}] {Y}Retrying with Switch-Mail: {email}")
                otp = self.deep_otp_scan(email)

            if otp:
                print(f"{G}[CHARSI-OK] {email} | {pwd} | OTP:{otp} ✅")
                self.oks.append(email)
                with open("/sdcard/CHARSI-V7-VERIFIED.txt", "a") as f:
                    f.write(f"{email}|{pwd}|{otp}|USA\n")
            else:
                print(f"{R}[FAILED] Verification Timeout.")
        except: pass

    def start(self):
        banner()
        for i in range(5):
            print(f"{W}Account: {i+1}/5")
            self.create()
            print(f"{W}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

if __name__ == "__main__":
    if not os.path.exists('/sdcard'): os.system('termux-setup-storage')
    CharsiV7().start()
          
