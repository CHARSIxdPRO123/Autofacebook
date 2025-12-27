import requests
import random

def get_proxy():
    """Fetches high-speed fresh proxies from public API"""
    try:
        # Fetching fresh USA/UK proxies
        url = "https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=US,GB&ssl=all&anonymity=all"
        res = requests.get(url).text
        proxies = res.split('\r\n')
        return random.choice([p for p in proxies if p])
    except:
        return None
