from ddgs import DDGS
from getpass import getpass
from pyfiglet import Figlet
from colorama import Fore, Style, init
import os
import time
import re
import sys

init(autoreset=True)

R = Fore.RED
G = Fore.GREEN
C = Fore.CYAN
Y = Fore.YELLOW
M = Fore.MAGENTA
W = Fore.WHITE
B = Fore.BLUE
RESET = Style.RESET_ALL
BOLD = Style.BRIGHT


def clear_screen():
    os.system("clear" if os.name != "nt" else "cls")


def banner():
    clear_screen()
    f = Figlet(font="slant")
    ascii_art = f.renderText("ZYRR3")
    print(f"{C}{BOLD}{ascii_art}{RESET}")
    print(f"{R}{'=' * 50}")
    print(f"{W}{BOLD}       OSINT Social Media Recon Tool{RESET}")
    print(f"{R}{'=' * 50}{RESET}")
    print(f"{Y}  [*] Author  : Zyrr3")
    print(f"  [*] Version : 2.0")
    print(f"  [*] Engine  : DuckDuckGo{RESET}")
    print(f"{R}{'=' * 50}{RESET}\n")


def loading(msg, duration=1.5):
    sys.stdout.write(f"\r  {C}[>>]{RESET} {W}{msg}...{RESET}")
    sys.stdout.flush()
    time.sleep(duration)
    sys.stdout.write(f"\r  {G}[OK]{RESET} {W}{msg}      \n")
    sys.stdout.flush()


def clean_url(url):
    url = url.split("?")[0].rstrip("/")
    if "/video/" in url:
        url = url.split("/video/")[0]
    if "/photo/" in url:
        url = url.split("/photo/")[0]
    return url


def is_valid_profile_url(url, platform):
    if not url or len(url) < 15:
        return False
    if platform == "Facebook":
        if "facebook.com" not in url:
            return False
        for block in ["/videos/", "/public/", "/groups/", "profile.php",
                      "l.facebook.com", "/p/", "/photos/", "/permalink/",
                      "/posts/", "facebook.com/events", "/about"]:
            if block in url:
                return False
    elif platform == "Instagram":
        if "instagram.com" not in url:
            return False
        for block in ["/p/", "/tv/", "/reel/", "/stories/", "/reels", "/channel"]:
            if block in url:
                return False
        if url.rstrip("/") == "https://www.instagram.com":
            return False
    elif platform == "TikTok":
        if "tiktok.com" not in url:
            return False
        if not re.search(r'tiktok\.com/@[a-zA-Z0-9._]+', url):
            return False
        if "/video/" in url or "/photo/" in url:
            return False
    elif platform == "Twitter/X":
        if "twitter.com" not in url and "x.com" not in url:
            return False
        for block in ["/status/", "help.twitter", "help.x.com",
                       "support.twitter", "support.x.com"]:
            if block in url:
                return False
    return True


PLATFORM_COLORS = {
    "Facebook": B,
    "Instagram": M,
    "TikTok": C,
    "Twitter/X": G,
}


def search_social_media_accounts(name):
    ddgs = DDGS()
    platforms = [
        ("Facebook", [f'"{name}" site:facebook.com', f'{name} facebook profile']),
        ("Instagram", [f'"{name}" site:instagram.com', f'{name} instagram profile']),
        ("TikTok", [f'"{name}" site:tiktok.com/@', f'{name} tiktok.com/@']),
        ("Twitter/X", [f'"{name}" site:twitter.com', f'{name} site:x.com']),
    ]

    total_found = 0

    for platform, queries in platforms:
        color = PLATFORM_COLORS.get(platform, W)
        print(f"\n  {color}{BOLD}[{platform}]{RESET}")

        urls = []
        seen = set()

        for query in queries:
            loading(f"Mencari {platform}...", 1.2)
            try:
                results = list(ddgs.text(query, max_results=10))
            except Exception as e:
                print(f"  {R}[!]{RESET} Error: {e}")
                time.sleep(2)
                try:
                    results = list(ddgs.text(query, max_results=10))
                except Exception:
                    results = []

            for r in results:
                url = clean_url(r.get("href", ""))
                if not url or url in seen:
                    continue
                if is_valid_profile_url(url, platform):
                    seen.add(url)
                    urls.append(url)

            time.sleep(1)

        if not urls:
            print(f"  {R}[-]{RESET} Tidak ditemukan hasil.\n")
            continue

        print(f"  {G}[*]{RESET} Ditemukan {color}{len(urls)}{RESET} akun:\n")
        for i, url in enumerate(urls[:10], 1):
            print(f"    {Y}{i:>2}.{RESET} {color}{url}{RESET}")
        total_found += len(urls[:10])
        print()

    print(f"{R}{'=' * 50}")
    print(f"  {G}{BOLD}[+]{RESET} Total : {Y}{total_found}{RESET} akun ditemukan")
    print(f"{R}{'=' * 50}")


def main():
    banner()

    name = input(f"  {C}[?]{RESET} Masukkan nama target : {W}").strip()
    if not name:
        print(f"\n  {R}[!]{RESET} Nama tidak boleh kosong.")
        return

    key = getpass(f"  {C}[?]{RESET} Masukkan kunci : {W}").strip()
    if key != "1107":
        print(f"\n  {R}[!]{RESET} Kunci tidak valid. Akses ditolak.")
        return

    print(f"\n  {G}[+]{RESET} Target : {Y}{name}{RESET}")
    print(f"  {G}[+]{RESET} Memulai reconnaissance...\n")

    search_social_media_accounts(name)


if __name__ == "__main__":
    main()
