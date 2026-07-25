
import subprocess
import sys

def print_crash_banner():
    CYAN    = "\033[96m"
    YELLOW  = "\033[93m"
    GREEN   = "\033[92m"
    MAGENTA = "\033[95m"
    RED     = "\033[91m"
    BLUE    = "\033[94m"
    WHITE   = "\033[97m"
    BOLD    = "\033[1m"
    RESET   = "\033[0m"

    banner = f"""
{CYAN}{BOLD}
╔══════════════════════════════════════════════════════════════════════╗
║                                                                      ║
║{RED}   ░█████╗░██████╗░░█████╗░░██████╗██╗░░██╗  ░█████╗░████████╗██████╗░{CYAN}  ║
║{RED}   ██╔══██╗██╔══██╗██╔══██╗██╔════╝██║░░██║  ██╔══██╗╚══██╔══╝██╔══██╗{CYAN}  ║
║{RED}   ██║░░╚═╝██████╔╝███████║╚█████╗░███████║  ██║░░██║░░░██║░░░██████╔╝{CYAN}  ║
║{RED}   ██║░░██╗██╔══██╗██╔══██║░╚═══██╗██╔══██║  ██║░░██║░░░██║░░░██╔═══╝░{CYAN}  ║
║{RED}   ╚█████╔╝██║░░██║██║░░██║██████╔╝██║░░██║  ╚█████╔╝░░░██║░░░██║░░░░░{CYAN}  ║
║{RED}   ░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝  ░╚════╝░░░░╚═╝░░░╚═╝░░░░░{CYAN}  ║
║                                                                      ║
║{YELLOW}  ╭──────────────────────────────────────────────────────────╮{CYAN}          ║
║{YELLOW}  │                                                          │{CYAN}          ║
║{YELLOW}  │   ⚡  S E N D A K O  —  O T P  E N G I N E  v4  ⚡    │{CYAN}          ║
║{YELLOW}  │                                                          │{CYAN}          ║
║{YELLOW}  │   ◈  Dev      →  C R A S H  [ @FK_AY ]                 │{CYAN}          ║
║{YELLOW}  │   ◈  System   →  Multi-Panel Smart OTP Bot             │{CYAN}          ║
║{YELLOW}  │   ◈  Panels   →  Static ╋ Dynamic ╋ API               │{CYAN}          ║
║{YELLOW}  │   ◈  DB       →  SQLite  [ Auto-Backup  ✓ ]           │{CYAN}          ║
║{YELLOW}  │   ◈  OTP      →  Instant Delivery  [ Guaranteed ✓ ]  │{CYAN}          ║
║{YELLOW}  │                                                          │{CYAN}          ║
║{YELLOW}  ╰──────────────────────────────────────────────────────────╯{CYAN}          ║
║                                                                      ║
║{GREEN}  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓{CYAN}      ║
║{MAGENTA}         🔥  STATUS: ONLINE  │  ALL SYSTEMS GO  │  2026 🔥{CYAN}           ║
║{GREEN}  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓{CYAN}      ║
║                                                                      ║
╚══════════════════════════════════════════════════════════════════════╝
{RESET}"""
    print(banner)

    import time as _t
    steps = [
        (f"{BLUE}[BOOT]{RESET} Loading system modules       ", 0.08),
        (f"{BLUE}[BOOT]{RESET} Connecting to database        ", 0.08),
        (f"{BLUE}[BOOT]{RESET} Initializing panel engines    ", 0.08),
        (f"{BLUE}[BOOT]{RESET} Starting Telegram bot         ", 0.08),
        (f"{BLUE}[BOOT]{RESET} Mounting panel monitors       ", 0.08),
        (f"{GREEN}[BOOT]{RESET} ✅ All systems operational     ", 0.05),
    ]
    bar_len = 30
    for label, delay in steps:
        for i in range(bar_len + 1):
            filled = "█" * i
            empty  = "░" * (bar_len - i)
            pct    = int(i / bar_len * 100)
            print(f"\r  {label}  [{CYAN}{filled}{RESET}{empty}] {YELLOW}{pct}%{RESET}", end="", flush=True)
            _t.sleep(delay / bar_len)
        print()

    print(f"\n{CYAN}{'═'*72}{RESET}\n")

print_crash_banner()


def _cprint(tag, msg, color="\033[96m", tag_color="\033[93m"):
    RESET  = "\033[0m"
    BOLD   = "\033[1m"
    DIM    = "\033[2m"
    now    = datetime.now().strftime("%H:%M:%S")
    print(f"{DIM}[{now}]{RESET} {tag_color}{BOLD}[{tag}]{RESET} {color}{msg}{RESET}")


def _panel_box(panel_name, number="", sms="", status="NEW"):
    import time as _t
    RESET   = "\033[0m"
    BOLD    = "\033[1m"
    DIM     = "\033[2m"

    PANEL_COLORS = [
        "\033[96m",  # Cyan
        "\033[93m",  # Yellow
        "\033[92m",  # Green
        "\033[95m",  # Magenta
        "\033[94m",  # Blue
        "\033[91m",  # Red
        "\033[97m",  # White
    ]
    color = PANEL_COLORS[hash(panel_name) % len(PANEL_COLORS)]

    STATUS_MAP = {
        "NEW":   ("\033[92m", "📨 NEW OTP"),
        "WARN":  ("\033[93m", "⚠️  WARNING"),
        "ERR":   ("\033[91m", "❌ ERROR"),
        "INFO":  ("\033[96m", "ℹ️  INFO"),
        "LOGIN": ("\033[95m", "🔐 LOGIN"),
        "EMPTY": ("\033[90m", "📭 NO MSG"),
    }
    sc, slabel = STATUS_MAP.get(status, ("\033[92m", f"• {status}"))

    now   = _t.strftime("%H:%M:%S")
    width = 56

    top    = f"┌{'─'*width}┐"
    bottom = f"└{'─'*width}┘"
    sep    = f"├{'─'*width}┤"

    _strip_codes = [BOLD, RESET, DIM, color, sc,
        "\033[90m","\033[92m","\033[91m","\033[93m",
        "\033[95m","\033[94m","\033[97m","\033[96m"]

    def row(content):
        visible = content
        for c in _strip_codes:
            visible = visible.replace(c, "")
        spaces = max(0, width - len(visible) - 2)
        return f"│ {content}{' ' * spaces} │"

    title_str = f"{BOLD}{color}⚡ {panel_name.upper()}{RESET}"
    time_str  = f"{DIM}🕐 {now}{RESET}"
    status_str = f"{sc}{BOLD}{slabel}{RESET}"
    num_str   = f"{BOLD}📱 {number}{RESET}" if number else ""
    sms_short = (sms[:46] + "…") if len(sms) > 46 else sms
    sms_str   = f"💬 {sms_short}" if sms else ""

    print(f"{color}{top}{RESET}")
    print(f"{color}{row(title_str + '   ' + time_str)}{RESET}")
    print(f"{color}{sep}{RESET}")
    print(f"{color}{row(status_str)}{RESET}")
    if num_str:
        print(f"{color}{row(num_str)}{RESET}")
    if sms_str:
        print(f"{color}{row(sms_str)}{RESET}")
    print(f"{color}{bottom}{RESET}")


def upgrade_telebot():
    try:
        print("[UPDATER] جاري التحقق من تحديث مكتبة pyTelegramBotAPI...")
        result = subprocess.run(
            [sys.executable, "-m", "pip", "install", "--upgrade", "pyTelegramBotAPI", "--quiet"],
            capture_output=True,
            text=True,
            timeout=60
        )
        if result.returncode == 0:
            print("[UPDATER] ✅ تم تحديث المكتبة إلى أحدث إصدار بنجاح")
        else:
            print(f"[UPDATER] ⚠️ لا توجد حاجة للتحديث أو فشل: {result.stderr[:100]}")
    except Exception as e:
        print(f"[UPDATER] ❌ فشل تحديث المكتبة: {e}")

upgrade_telebot()

import time
import requests
import json
import urllib3
import traceback
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import re
import io
import base64
import os
import hashlib
from datetime import datetime, date, timedelta
from urllib.parse import quote_plus
import sqlite3
import telebot
from telebot import types
import threading
import random
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor, as_completed

DB_PATH = "sendako.db"
BOT_TOKEN = ""
CHAT_IDS = [""]
ADMIN_IDS = []

REFRESH_INTERVAL = 1
PARALLEL_FETCH = True
MAX_WORKERS = 50

_panel_check_cache = {}
_panel_last_code_time = {}
_panel_last_code_lock = threading.Lock()
_bot_error_log = []
_bot_error_lock = threading.Lock()

def _log_bot_error(error_msg, exc=None):
    with _bot_error_lock:
        entry = {
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "msg": str(error_msg)[:300],
            "trace": traceback.format_exc()[:500] if exc else ""
        }
        _bot_error_log.append(entry)
        if len(_bot_error_log) > 100:
            _bot_error_log.pop(0)
_panel_check_lock  = threading.Lock()

MAINTENANCE_MODE = False

BOT_IMAGE_BYTES = None
MAINTENANCE_IMAGE_BYTES = None
FORCE_SUB_IMAGE_BYTES = None

def to_bold(text):
    bold_map = {
        'A': '𝗔', 'B': '𝗕', 'C': '𝗖', 'D': '𝗗', 'E': '𝗘', 'F': '𝗙', 'G': '𝗚', 'H': '𝗛', 'I': '𝗜',
        'J': '𝗝', 'K': '𝗞', 'L': '𝗟', 'M': '𝗠', 'N': '𝗡', 'O': '𝗢', 'P': '𝗣', 'Q': '𝗤', 'R': '𝗥',
        'S': '𝗦', 'T': '𝗧', 'U': '𝗨', 'V': '𝗩', 'W': '𝗪', 'X': '𝗫', 'Y': '𝗬', 'Z': '𝗭',
        'a': '𝗮', 'b': '𝗯', 'c': '𝗰', 'd': '𝗱', 'e': '𝗲', 'f': '𝗳', 'g': '𝗴', 'h': '𝗵', 'i': '𝗶',
        'j': '𝗷', 'k': '𝗸', 'l': '𝗹', 'm': '𝗺', 'n': '𝗻', 'o': '𝗼', 'p': '𝗽', 'q': '𝗾', 'r': '𝗿',
        's': '𝘀', 't': '𝘁', 'u': '𝘂', 'v': '𝘃', 'w': '𝘄', 'x': '𝘅', 'y': '𝘆', 'z': '𝘇',
        '0': '𝟬', '1': '𝟭', '2': '𝟮', '3': '𝟯', '4': '𝟰', '5': '𝟱', '6': '𝟲', '7': '𝟳', '8': '𝟴', '9': '𝟵'
    }
    return ''.join(bold_map.get(ch, ch) for ch in text)

STATIC_DASHBOARDS = [

    {
        "name": "Bolt SMS",
        "type": "traditional",
        "base_url": "http://93.190.143.35/ints",
        "login_page": "/Login",
        "login_post": "/signin",
        "ajax_path": "/agent/res/data_smscdr.php",
        "username": "",
        "password": "",
        "short": "BT", "short_bold": to_bold("BT"),
        "source": "static", "idx_date": 0, "idx_number": 2, "idx_sms": 5,
        "timeout": 30, "refresh_interval": 1,
    },

    {
        "name": "Time SMS",
        "type": "api_token",
        "api_url": "http://147.135.212.197/crapi/time/viewstats",
        "api_token": "",
        "short": "TM", "short_bold": to_bold("TM"),
        "source": "static",
        "data_keys": {"date": "dt", "number": "num", "sms": "message", "service": "cli"},
        "refresh_interval": 1,
    },

    {
        "name": "XAP SMS",
        "type": "traditional",
        "base_url": "http://147.135.212.148",
        "login_page": "/ints/login",
        "login_post": "/ints/signin",
        "ajax_path": "/ints/agent/res/data_smscdr.php",
        "username": "",
        "password": "",
        "short": "XP", "short_bold": to_bold("WS"),
        "source": "static", "idx_date": 0, "idx_number": 2, "idx_sms": 5,
        "timeout": 10, "refresh_interval": 1,
    },


    {
        "name": "Hadi SMS",
        "type": "api_token",
        "api_url": "http://147.135.212.197/crapi/had/viewstats",
        "api_token": "",
        "short": "HD", "short_bold": to_bold("HD"),
        "source": "static",
        "data_keys": {"date": "dt", "number": "num", "sms": "message", "service": "cli"},
        "refresh_interval": 1,
    },


    {
        "name": "Sniper SMS",
        "type": "traditional",
        "base_url": "http://135.125.222.224",
        "login_page": "/ints/login",
        "login_post": "/ints/signin",
        "ajax_path": "/ints/agent/res/data_smscdr.php",
        "username": "",
        "password": "",
        "short": "SN", "short_bold": to_bold("SN"),
        "source": "static", "idx_date": 0, "idx_number": 2, "idx_sms": 5,
        "timeout": 10, "refresh_interval": 1,
    },

    {
        "name": "Squad SMS",
        "type": "traditional",
        "base_url": "http://51.77.221.209",
        "login_page": "/ints/login",
        "login_post": "/ints/signin",
        "ajax_path": "/ints/agent/res/data_smscdr.php",
        "username": "",
        "password": "",
        "short": "SQ", "short_bold": to_bold("SQ"),
        "source": "static", "idx_date": 0, "idx_number": 2, "idx_sms": 5,
        "timeout": 30, "refresh_interval": 1,
    },

    {
        "name": "44 Numbers",
        "type": "traditional",
        "base_url": "http://185.177.124.145",
        "login_page": "/ints/login",
        "login_post": "/ints/signin",
        "ajax_path": "/ints/agent/res/data_smscdr.php",
        "stats_page": "/ints/agent/SMSCDRStats",
        "username": "",
        "password": "",
        "short": "44", "short_bold": to_bold("WS"),
        "source": "static", "idx_date": 0, "idx_number": 2, "idx_sms": 5,
        "timeout": 10, "refresh_interval": 1,
    },

    {
        "name": "Lamix SMS",
        "type": "traditional",
        "base_url": "http://139.99.208.63",
        "login_page": "/ints/login",
        "login_post": "/ints/signin",
        "ajax_path": "/ints/agent/res/data_smscdr.php",
        "username": "",
        "password": "",
        "short": "LM", "short_bold": to_bold("WS"),
        "source": "static", "idx_date": 0, "idx_number": 2, "idx_sms": 5,
        "timeout": 10, "refresh_interval": 1,
    },

    {
        "name": "GROUP SMS",
        "type": "traditional",
        "base_url": "http://139.99.63.204",
        "login_page": "/ints/login",
        "login_post": "/ints/signin",
        "ajax_path": "/ints/agent/res/data_smscdr.php",
        "username": "",
        "password": "",
        "short": "GR", "short_bold": to_bold("WS"),
        "source": "static", "idx_date": 0, "idx_number": 2, "idx_sms": 5,
        "timeout": 10, "refresh_interval": 1,
    },

    {
        "name": "MSI SMS",
        "type": "traditional",
        "base_url": "http://145.239.130.45",
        "login_page": "/ints/login",
        "login_post": "/ints/signin",
        "ajax_path": "/ints/agent/res/data_smscdr.php",
        "username": "",
        "password": "",
        "short": "MS", "short_bold": to_bold("WS"),
        "source": "static", "idx_date": 0, "idx_number": 2, "idx_sms": 5,
        "timeout": 10, "refresh_interval": 1,
    },

    {
        "name": "Proton SMS",
        "type": "traditional",
        "base_url": "http://109.236.84.81/ints",
        "login_page": "/login",
        "login_post": "/signin",
        "ajax_path": "/agent/res/data_smscdr.php",
        "username": "",
        "password": "",
        "short": "PR", "short_bold": to_bold("WS"),
        "source": "static", "idx_date": 0, "idx_number": 2, "idx_sms": 5,
        "timeout": 10, "refresh_interval": 1,
    },

    {
        "name": "IMS SMS",
        "type": "ims_panel",
        "base_url": "http://45.82.67.20",
        "login_page": "/ints/login",
        "login_post": "/ints/signin",
        "ajax_path": "/ints/agent/res/data_smscdr.php",
        "dashboard_path": "/ints/agent/SMSCDRReports",
        "username": "",
        "password": "",
        "source": "static", "idx_date": 0, "idx_number": 2, "idx_sms": 5,
        "timeout": 8, "refresh_interval": 1, "records": 10,
    },


    {
        "name": "Roxy SMS",
        "type": "api_token",
        "api_url": "http://51.77.216.195/crapi/rx/viewstats",
        "api_token": "",
        "short": "RX", "short_bold": to_bold("WS"),
        "source": "static",
        "data_keys": {"date": None, "number": "num", "sms": "message", "service": "cli"},
        "refresh_interval": 1,
    },

    {
        "name": "D-Group SMS",
        "type": "api_token",
        "api_url": "http://51.77.216.195/crapi/dgroup/viewstats",
        "api_token": "",
        "short": "DG", "short_bold": to_bold("WS"),
        "source": "static",
        "data_keys": {"date": "dt", "number": "num", "sms": "message", "service": "cli"},
        "refresh_interval": 1,
    },

    {
        "name": "Numper Panel",
        "type": "api",
        "api_url": "http://147.135.212.197/crapi/st/viewstats",
        "api_token": "",
        "short": "NP", "short_bold": to_bold("WS"),
        "source": "static",
        "idx_date": 3, "idx_number": 1, "idx_sms": 2,
        "refresh_interval": 1,
    },

    {
        "name": "Konecta Panel",
        "type": "traditional",
        "base_url": "https://www.konektapremium.net",
        "login_page": "/sign-in",
        "login_post": "/signin",
        "ajax_path": "/agent/res/data_smscdr.php",
        "username": "",
        "password": "",
        "short": "KN", "short_bold": to_bold("WS"),
        "source": "static", "idx_date": 0, "idx_number": 2, "idx_sms": 5,
        "timeout": 15, "refresh_interval": 1,
    },

    {
        "name": "SEVEN1TEL SMS",
        "type": "api_token",
        "api_url": "http://147.135.212.197/crapi/s1t/viewstats",
        "api_token": "",
        "short": "S1", "short_bold": to_bold("WS"),
        "source": "static",
        "data_keys": {"date": "dt", "number": "num", "sms": "message", "service": "cli"},
        "refresh_interval": 1,
    },

    {
        "name": "SHARK SMS",
        "type": "traditional",
        "base_url": "http://93.190.143.157",
        "login_page": "/ints/login",
        "login_post": "/ints/signin",
        "ajax_path": "/ints/agent/res/data_smscdr.php",
        "username": "",
        "password": "",
        "short": "SK", "short_bold": to_bold("SK"),
        "source": "static", "idx_date": 0, "idx_number": 2, "idx_sms": 5,
        "timeout": 30, "refresh_interval": 1,
    },

    {
        "name": "PROOF SMS",
        "type": "traditional",
        "base_url": "http://217.182.195.194",
        "login_page": "/ints/login",
        "login_post": "/ints/signin",
        "ajax_path": "/ints/agent/res/data_smscdr.php",
        "username": "",
        "password": "",
        "short": "PF", "short_bold": to_bold("PF"),
        "source": "static", "idx_date": 0, "idx_number": 2, "idx_sms": 5,
        "timeout": 30, "refresh_interval": 1,
    },

    {
        "name": "CHOICE SMS",
        "type": "traditional",
        "base_url": "http://51.77.52.79",
        "login_page": "/ints/login",
        "login_post": "/ints/signin",
        "ajax_path": "/ints/agent/res/data_smscdr.php",
        "username": "",
        "password": "",
        "short": "CH", "short_bold": to_bold("CH"),
        "source": "static", "idx_date": 0, "idx_number": 2, "idx_sms": 5,
        "timeout": 30, "refresh_interval": 1,
    },

    {
        "name": "PC CALL",
        "type": "api_token",
        "api_url": "http://pscall.net/restapi/smsreport",
        "api_token": "",
        "short": "PC", "short_bold": to_bold("PC"),
        "source": "static",
        "data_keys": {"date": "dt", "number": "num", "sms": "message", "service": "cli"},
        "refresh_interval": 1,
    },

    {
        "name": "FIRE SMS",
        "type": "traditional",
        "base_url": "http://54.39.104.241",
        "login_page": "/ints/login",
        "login_post": "/ints/signin",
        "login_page_url": "http://54.39.104.241/ints/login",
        "login_post_url": "http://54.39.104.241/ints/signin",
        "ajax_path": "/ints/agent/res/data_smscdr.php",
        "username": "",
        "password": "",
        "short": "FS", "short_bold": to_bold("FS"),
        "source": "static", "idx_date": 0, "idx_number": 2, "idx_sms": 5,
        "timeout": 15, "refresh_interval": 1,
    },

    {
        "name": "Green SMS",
        "type": "traditional",
        "base_url": "http://139.99.9.4",
        "login_page": "/ints/login",
        "login_post": "/ints/signin",
        "login_page_url": "http://139.99.9.4/ints/login",
        "login_post_url": "http://139.99.9.4/ints/signin",
        "ajax_path": "/ints/agent/res/data_smscdr.php",
        "username": "",
        "password": "",
        "short": "GN", "short_bold": to_bold("GN"),
        "source": "static", "idx_date": 0, "idx_number": 2, "idx_sms": 5,
        "timeout": 15, "refresh_interval": 1,
    },

    {
        "name": "Konekta API",
        "type": "api_token",
        "api_url": "http://51.77.216.195/crapi/konek/viewstats",
        "api_token": "",
        "short": "KA", "short_bold": to_bold("KA"),
        "source": "static",
        "data_keys": {"date": "dt", "number": "num", "sms": "message", "service": "cli"},
        "refresh_interval": 1,
    },

    {
        "name": "Fly Panel New",
        "type": "ims_panel",
        "base_url": "https://flysms.net",
        "login_page": "/login",
        "login_post": "/signin",
        "ajax_path": "/agent/res/data_smscdr.php",
        "dashboard_path": "/agent/SMSCDRReports",
        "username": "",
        "password": "",
        "short": "FN", "short_bold": to_bold("FN"),
        "source": "static", "idx_date": 0, "idx_number": 2, "idx_sms": 5,
        "timeout": 30, "refresh_interval": 1, "records": 50,
    },

]


PANEL_SETTINGS_FILE = "panel_accounts.json"

PANEL_SITES = {
    "Bolt":     {"name":"Bolt SMS",      "short":"BT","base_url":"http://93.190.143.35/ints","login_page":"/Login","login_post":"/signin","ajax_path":"/agent/res/data_smscdr.php","type":"traditional","idx_date":0,"idx_number":2,"idx_sms":5,"timeout":30,"refresh_interval":1,"username":"","password":""},
    "TimeSMS":  {"name":"Time SMS", "short":"TM", "type":"api_token", "api_url":"http://147.135.212.197/crapi/time/viewstats", "api_token":"", "data_keys":{"date":"dt","number":"num","sms":"message","service":"cli"}, "refresh_interval":1},
    "XAP":      {"name":"XAP SMS",       "short":"XP","base_url":"http://147.135.212.148",        "login_page":"/ints/login", "login_post":"/ints/signin", "ajax_path":"/ints/agent/res/data_smscdr.php",    "type":"traditional","idx_date":0,"idx_number":2,"idx_sms":5,"timeout":10,"refresh_interval":1,"username":"",         "password":""},
    "Hadi":     {"name":"Hadi SMS",      "short":"HD","api_url":"http://147.135.212.197/crapi/had/viewstats","api_token":"","type":"api_token","refresh_interval":1,"data_keys":{"date":"dt","number":"num","sms":"message","service":"cli"}},
    "Num44":    {"name":"44 Numbers",    "short":"44","base_url":"http://185.177.124.145",        "login_page":"/ints/login", "login_post":"/ints/signin", "ajax_path":"/ints/agent/res/data_smscdr.php",    "type":"traditional","idx_date":0,"idx_number":2,"idx_sms":5,"timeout":10,"refresh_interval":1,"username":"",         "password":""},
    "Lamix":    {"name":"Lamix SMS",     "short":"LM","base_url":"http://139.99.208.63",          "login_page":"/ints/login", "login_post":"/ints/signin", "ajax_path":"/ints/agent/res/data_smscdr.php",    "type":"traditional","idx_date":0,"idx_number":2,"idx_sms":5,"timeout":10,"refresh_interval":1,"username":"",         "password":""},
    "GROUP":    {"name":"GROUP SMS",     "short":"GR","base_url":"http://139.99.63.204",          "login_page":"/ints/login", "login_post":"/ints/signin", "ajax_path":"/ints/agent/res/data_smscdr.php",    "type":"traditional","idx_date":0,"idx_number":2,"idx_sms":5,"timeout":10,"refresh_interval":1,"username":"","password":""},
    "MSI":      {"name":"MSI SMS",       "short":"MS","base_url":"http://145.239.130.45",         "login_page":"/ints/login", "login_post":"/ints/signin", "ajax_path":"/ints/agent/res/data_smscdr.php",    "type":"traditional","idx_date":0,"idx_number":2,"idx_sms":5,"timeout":10,"refresh_interval":1,"username":"","password":""},
    "Proton":   {"name":"Proton SMS",    "short":"PR","base_url":"http://109.236.84.81/ints",     "login_page":"/login",      "login_post":"/signin",      "ajax_path":"/agent/res/data_smscdr.php",         "type":"traditional","idx_date":0,"idx_number":2,"idx_sms":5,"timeout":10,"refresh_interval":1,"username":"",  "password":""},
    "IMS":      {"name":"IMS SMS",       "short":"IM","base_url":"http://45.82.67.20",            "login_page":"/ints/login", "login_post":"/ints/signin", "ajax_path":"/ints/agent/res/data_smscdr.php",    "type":"ims_panel",  "idx_date":0,"idx_number":2,"idx_sms":5,"timeout":15,"refresh_interval":1,"username":"","password":"","dashboard_path":"/ints/agent/SMSCDRReports","records":50},
    "Konecta":  {"name":"Konecta Panel", "short":"KN","base_url":"https://www.konektapremium.net","login_page":"/sign-in",    "login_post":"/signin",      "ajax_path":"/agent/res/data_smscdr.php",         "type":"traditional","idx_date":0,"idx_number":2,"idx_sms":5,"timeout":15,"refresh_interval":1,"username":"","password":""},
    "FairSMS":  {"name":"FIRE SMS",     "short":"FS","base_url":"http://54.39.104.241","login_page":"/ints/login","login_post":"/ints/signin","login_page_url":"http://54.39.104.241/ints/login","login_post_url":"http://54.39.104.241/ints/signin","ajax_path":"/ints/agent/res/data_smscdr.php","type":"traditional","idx_date":0,"idx_number":2,"idx_sms":5,"timeout":15,"refresh_interval":1,"username":"","password":""},
    "GreenSMS": {"name":"Green SMS",   "short":"GN","base_url":"http://139.99.9.4","login_page":"/ints/login","login_post":"/ints/signin","login_page_url":"http://139.99.9.4/ints/login","login_post_url":"http://139.99.9.4/ints/signin","ajax_path":"/ints/agent/res/data_smscdr.php","type":"traditional","idx_date":0,"idx_number":2,"idx_sms":5,"timeout":15,"refresh_interval":1,"username":"","password":""},
    "KonektaAPI":{"name":"Konekta API","short":"KA","api_url":"http://51.77.216.195/crapi/konek/viewstats","api_token":"","type":"api_token","refresh_interval":1,"data_keys":{"date":"dt","number":"num","sms":"message","service":"cli"}},
    "FlyNew":   {"name":"Fly Panel New", "short":"FN","base_url":"https://flysms.net",            "login_page":"/login",      "login_post":"/signin",      "ajax_path":"/agent/res/data_smscdr.php",         "type":"ims_panel",  "idx_date":0,"idx_number":2,"idx_sms":5,"timeout":10,"refresh_interval":2,"username":"",         "password":"", "dashboard_path":"/agent/SMSCDRReports"},
    "S1T":      {"name":"SEVEN1TEL SMS",     "short":"S1","api_url":"http://147.135.212.197/crapi/s1t/viewstats","api_token":"","type":"api_token","refresh_interval":1,"data_keys":{"date":"dt","number":"num","sms":"message","service":"cli"}},
    "Sniper":   {"name":"Sniper SMS",    "short":"SN","base_url":"http://135.125.222.224",        "login_page":"/ints/login", "login_post":"/ints/signin", "ajax_path":"/ints/agent/res/data_smscdr.php",    "type":"traditional","idx_date":0,"idx_number":2,"idx_sms":5,"timeout":10,"refresh_interval":1,"username":"",  "password":""},
    "Squad":    {"name":"Squad SMS",     "short":"SQ","base_url":"http://51.77.221.209",          "login_page":"/ints/login", "login_post":"/ints/signin", "ajax_path":"/ints/agent/res/data_smscdr.php",    "type":"traditional","idx_date":0,"idx_number":2,"idx_sms":5,"timeout":30,"refresh_interval":1,"username":"",   "password":""},
    "Shark":    {"name":"SHARK SMS",     "short":"SK","base_url":"http://93.190.143.157",          "login_page":"/ints/login", "login_post":"/ints/signin", "ajax_path":"/ints/agent/res/data_smscdr.php",    "type":"traditional","idx_date":0,"idx_number":2,"idx_sms":5,"timeout":30,"refresh_interval":1,"username":"",   "password":""},
    "Proof":    {"name":"PROOF SMS",     "short":"PF","base_url":"http://217.182.195.194",         "login_page":"/ints/login", "login_post":"/ints/signin", "ajax_path":"/ints/agent/res/data_smscdr.php",    "type":"traditional","idx_date":0,"idx_number":2,"idx_sms":5,"timeout":30,"refresh_interval":1,"username":"",   "password":""},
    "Choice":   {"name":"CHOICE SMS",    "short":"CH","base_url":"http://51.77.52.79",             "login_page":"/ints/login", "login_post":"/ints/signin", "ajax_path":"/ints/agent/res/data_smscdr.php",    "type":"traditional","idx_date":0,"idx_number":2,"idx_sms":5,"timeout":30,"refresh_interval":1,"username":"",   "password":""},
    "PcCall":   {"name":"PC CALL",       "short":"PC","api_url":"http://pscall.net/restapi/smsreport","api_token":"","type":"api_token","refresh_interval":1,"timeout":30,"data_keys":{"date":"dt","number":"num","sms":"message","service":"cli"}},
    # ── MBC Panel ── https://mbcs-ms.com
    "MBC":      {"name":"MBC SMS",       "short":"MB","api_url":"https://mbcs-ms.com/crapi/mbc/viewstats","api_token":"","type":"api_token","refresh_interval":1,"timeout":15,"data_keys":{"date":"dt","number":"num","sms":"message","service":"cli"}},
}


def load_panel_accounts():
    saved = {}
    if os.path.exists(PANEL_SETTINGS_FILE):
        try:
            with open(PANEL_SETTINGS_FILE, "r", encoding="utf-8") as f:
                saved = json.load(f)
        except:
            saved = {}

    result = {}
    for sk, site in PANEL_SITES.items():
        result[sk] = {"accounts": []}
        seen_users = set()

        site_type = site.get("type", "traditional")

        if site_type in ("api", "api_token"):
            token = site.get("api_token", "").strip()
            if token:
                result[sk]["accounts"].append({
                    "id": "default_api",
                    "api_token": token,
                    "username": "API",
                    "password": "",
                    "source": "default"
                })
        else:
            uname = site.get("username", "").strip()
            passwd = site.get("password", "").strip()
            if uname and passwd:
                result[sk]["accounts"].append({
                    "id": f"default_{uname}",
                    "username": uname,
                    "password": passwd,
                    "source": "default"
                })
                seen_users.add(uname)

            for acc in saved.get(sk, {}).get("accounts", []):
                uname2 = acc.get("username", "").strip()
                passwd2 = acc.get("password", "").strip()
                if uname2 and passwd2 and uname2 not in seen_users:
                    result[sk]["accounts"].append(acc)
                    seen_users.add(uname2)

    return result

def save_panel_accounts(data):
    to_save = {}
    for sk, v in data.items():
        to_save[sk] = {
            "accounts": [a for a in v.get("accounts", [])
                         if a.get("source") != "default"]
        }
    with open(PANEL_SETTINGS_FILE, "w", encoding="utf-8") as f:
        json.dump(to_save, f, ensure_ascii=False, indent=2)

def get_panel_accounts(site_key):
    data = load_panel_accounts()
    return data.get(site_key, {}).get("accounts", [])

def add_panel_account(site_key, username, password):
    saved = {}
    if os.path.exists(PANEL_SETTINGS_FILE):
        try:
            with open(PANEL_SETTINGS_FILE, "r", encoding="utf-8") as f:
                saved = json.load(f)
        except:
            saved = {}
    if site_key not in saved:
        saved[site_key] = {"accounts": []}
    account = {"id": str(int(time.time() * 1000)), "username": username, "password": password}
    saved[site_key]["accounts"].append(account)
    with open(PANEL_SETTINGS_FILE, "w", encoding="utf-8") as f:
        json.dump(saved, f, ensure_ascii=False, indent=2)
    return account

def delete_panel_account(site_key, account_id):
    if account_id.startswith("default_"):
        return False
    saved = {}
    if os.path.exists(PANEL_SETTINGS_FILE):
        try:
            with open(PANEL_SETTINGS_FILE, "r", encoding="utf-8") as f:
                saved = json.load(f)
        except:
            saved = {}
    if site_key not in saved:
        return False
    before = len(saved[site_key].get("accounts", []))
    saved[site_key]["accounts"] = [a for a in saved[site_key]["accounts"] if a["id"] != account_id]
    if len(saved[site_key]["accounts"]) < before:
        with open(PANEL_SETTINGS_FILE, "w", encoding="utf-8") as f:
            json.dump(saved, f, ensure_ascii=False, indent=2)
        stop_ev = _panel_stop_events.pop(f"{site_key}_{account_id}", None)
        if stop_ev:
            stop_ev.set()
        return True
    return False

_panel_stop_events = {}
_panel_threads = {}

_global_sent_otps: set = set()
_global_sent_lock = threading.Lock()
_global_sent_max = 50000  # حد أقصى للذاكرة

def _is_otp_already_sent(number: str, sms: str, date_str: str = "") -> bool:
    """يتحقق إذا الكود ده اتبعت قبل كده - thread-safe"""
    key = f"{date_str}|{str(number).strip()}|{str(sms).strip()[:30]}"
    with _global_sent_lock:
        if key in _global_sent_otps:
            return True
        _global_sent_otps.add(key)
        if len(_global_sent_otps) > _global_sent_max:
            old_list = list(_global_sent_otps)
            _global_sent_otps.clear()
            _global_sent_otps.update(old_list[_global_sent_max//2:])
        return False

def start_panel_account_monitor(site_key, account):
    account_id = account["id"]
    key = f"{site_key}_{account_id}"
    if key in _panel_threads and _panel_threads[key].is_alive():
        return
    stop_ev = threading.Event()
    _panel_stop_events[key] = stop_ev
    def _run():
        _monitor_panel_account(site_key, account, stop_ev)
    t = threading.Thread(target=_run, daemon=True)
    _panel_threads[key] = t
    t.start()
    print(f"[Panel Monitor] ▶️  \033[92m{PANEL_SITES[site_key]['name']}\033[0m / \033[96m{account['username']}\033[0m — بدأت المراقبة")

def start_all_panel_monitors():
    for site_key in PANEL_SITES:
        for account in get_panel_accounts(site_key):
            start_panel_account_monitor(site_key, account)

def _monitor_panel_account(site_key, account, stop_event):
    site        = PANEL_SITES[site_key]
    account_id  = account["id"]
    short_bold  = to_bold(site["short"])
    site_type   = site.get("type", "traditional")
    interval    = site.get("refresh_interval", 3)

    if site_type in ("api", "api_token"):
        api_token = account.get("api_token") or site.get("api_token", "")
        api_url   = site.get("api_url", "")

        # ── MBC: يسمح بالـ login بـ username/password لو مفيش token ──
        is_mbc = (site_key == "MBC" or "mbcs-ms.com" in api_url)
        uname_acc  = account.get("username","").strip()
        passwd_acc = account.get("password","").strip()

        if not api_token and is_mbc and uname_acc and passwd_acc:
            # هنجيب الـ token من الـ login وقت التشغيل
            _sess_tmp = requests.Session()
            api_token = _mbc_login(_sess_tmp, uname_acc, passwd_acc)
            if api_token:
                account["api_token"] = api_token
                _mbc_token_cache[uname_acc] = {"token": api_token, "expires": time.time() + 3600}
                print(f"[MBC] {uname_acc} — تم الحصول على token بنجاح")
            else:
                print(f"[MBC] {uname_acc} — فشل الحصول على token، سيتم المحاولة مجدداً")

        if not api_token and not is_mbc:
            if not api_url:
                print(f"[SKIP] {site['name']} - لا يوجد API token/url")
                return

        sent_file   = f"sent_messages_{site_key}_{account_id}.json"
        sent_local  = set()
        try:
            if os.path.exists(sent_file):
                with open(sent_file) as _f:
                    sent_local = set(json.load(_f))
        except: pass

        def _save_sent_api():
            try:
                with open(sent_file, "w") as _f:
                    json.dump(list(sent_local)[-500:], _f)
            except: pass

        print(f"[{site['name']}] 🌐 API مراقبة بدأت...")
        while not stop_event.is_set():
            try:
                today = datetime.now()
                params = {
                    "token":   api_token,
                    "records": 50,
                    "dt1": (today - timedelta(days=1)).strftime("%Y-%m-%d 00:00:00"),
                    "dt2":  today.strftime("%Y-%m-%d 23:59:59"),
                }
                r = requests.get(api_url, params=params, timeout=site.get("timeout", 30))
                if r.status_code == 200:
                    raw_text = r.text.strip()
                    if not raw_text:
                        _panel_box(site['name'], sms="Empty response", status="WARN")
                        stop_event.wait(min(interval, 1))
                        continue
                    try:
                        data = r.json()
                    except Exception as json_err:
                        _panel_box(site['name'], sms=f"JSON err: {str(json_err)[:40]}", status="ERR")
                        stop_event.wait(min(interval, 1))
                        continue
                    rows = []
                    if isinstance(data, dict):
                        if data.get("status") == "success" and data.get("data"):
                            rows = data["data"]
                        else:
                            for k in ("data", "aaData", "rows", "result"):
                                if k in data and isinstance(data[k], list):
                                    rows = data[k]; break
                    elif isinstance(data, list):
                        rows = data

                    new_msgs = []
                    for row in rows:
                        dkeys = site.get("data_keys", {})
                        if isinstance(row, dict):
                            num = clean_number(str(row.get(dkeys.get("number","num"), "")))
                            sms = clean_html(str(row.get(dkeys.get("sms","message"), "")))
                            dt  = str(row.get(dkeys.get("date","dt"), ""))
                        elif isinstance(row, (list,tuple)):
                            i_d = site.get("idx_date",0); i_n = site.get("idx_number",1); i_s = site.get("idx_sms",2)
                            dt  = clean_html(str(row[i_d])) if len(row)>i_d else ""
                            num = clean_number(str(row[i_n])) if len(row)>i_n else ""
                            sms = clean_html(str(row[i_s])) if len(row)>i_s else ""
                        else:
                            continue
                        if not num or not sms or len(num)<7: continue
                        mk = f"{dt}|{num}|{sms[:50]}"
                        if mk not in sent_local:
                            new_msgs.append((dt, num, sms)); sent_local.add(mk)
                    if new_msgs:
                        _panel_box(site['name'], sms=f"{len(new_msgs)} رسالة جديدة", status="INFO")
                        _save_sent_api()
                        for dt,num,sms in new_msgs:
                            _panel_box(site['name'], mask_number(num), sms[:60], status="NEW")
                            send_otp_to_user_and_group(dt, num, sms,
                                panel_name=site["name"], short_bold=short_bold)
                    else:
                        _panel_box(site['name'], status="EMPTY")
                else:
                    _panel_box(site['name'], sms=f"HTTP {r.status_code}", status="WARN")
                    # ── MBC: لو 401 نجدد الـ token ──
                    if is_mbc and r.status_code == 401 and uname_acc and passwd_acc:
                        _sess_tmp2 = requests.Session()
                        new_tok = _mbc_login(_sess_tmp2, uname_acc, passwd_acc)
                        if new_tok:
                            api_token = new_tok
                            account["api_token"] = new_tok
                            _mbc_token_cache[uname_acc] = {"token": new_tok, "expires": time.time() + 3600}
                            print(f"[MBC] token جُدِّد بنجاح لـ {uname_acc}")
            except Exception as e:
                _panel_box(site['name'], sms=str(e)[:50], status="ERR")
                _log_bot_error(f"[{site['name']}] خطأ: {e}", exc=e)
            stop_event.wait(min(interval, 1))
        return

    uname  = account.get("username","").strip()
    passwd = account.get("password","").strip()
    if not uname or not passwd:
        print(f"[SKIP] {site['name']} - حساب بدون يوزر/باسورد")
        return

    username = uname
    password = passwd

    base_url       = site.get("base_url","")
    login_page_url = site.get("login_page_url") or (base_url.rstrip("/")+site.get("login_page",""))
    login_post_url = site.get("login_post_url") or (base_url.rstrip("/")+site.get("login_post",""))
    ajax_path      = site.get("ajax_path", "/ints/agent/res/data_smscdr.php")
    ajax_url       = base_url.rstrip("/") + ajax_path
    TIMEOUT        = site.get("timeout", 30)
    CHECK_INTERVAL = interval

    last_msg_file  = f"last_message_{site_key}_{account_id}.txt"
    sent_msgs_file = f"sent_messages_{site_key}_{account_id}.json"
    last_seen_key  = ""
    sent_msgs_local= set()
    _last_sent_dt  = None

    def _load_state():
        nonlocal last_seen_key, sent_msgs_local, _last_sent_dt
        try:
            if os.path.exists(last_msg_file):
                with open(last_msg_file,"r",encoding="utf-8") as f: last_seen_key = f.read().strip()
        except: pass
        try:
            if os.path.exists(sent_msgs_file):
                with open(sent_msgs_file) as f:
                    data = json.load(f)
                    if isinstance(data, dict):
                        sent_msgs_local = set(data.get("keys", []))
                        dt_str = data.get("last_dt", "")
                        if dt_str:
                            try:
                                _last_sent_dt = datetime.strptime(dt_str, "%Y-%m-%d %H:%M:%S")
                            except: pass
                    elif isinstance(data, list):
                        sent_msgs_local = set(data)
        except: pass

    def _save_state():
        try:
            with open(last_msg_file,"w",encoding="utf-8") as f: f.write(last_seen_key)
        except: pass
        try:
            with open(sent_msgs_file,"w") as f:
                json.dump({
                    "keys": list(sent_msgs_local)[-500:],
                    "last_dt": _last_sent_dt.strftime("%Y-%m-%d %H:%M:%S") if _last_sent_dt else ""
                }, f)
        except: pass

    session = requests.Session()
    session.verify = False
    session.headers.update({
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9,ar;q=0.8",
        "Accept-Encoding": "gzip, deflate",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "Cache-Control": "max-age=0",
    })

    is_logged_in   = False
    current_sesskey = None

    def do_login():
        nonlocal is_logged_in, current_sesskey
        nonlocal username, password
        _accounts_fresh = get_panel_accounts(site_key)
        _acc = next((a for a in _accounts_fresh if a.get('id') == account_id), None)
        if _acc and _acc.get('username'):
            username = _acc.get('username', username).strip()
            password = _acc.get('password', password).strip()
        elif PANEL_SITES.get(site_key, {}).get('username'):
            username = PANEL_SITES[site_key].get('username', username).strip()
            password = PANEL_SITES[site_key].get('password', password).strip()
        print(f"[{site['name']}] ({username}) 🔐 تسجيل الدخول...")
        try:
            resp = session.get(login_page_url, timeout=TIMEOUT)
            if resp.status_code != 200:
                print(f"[{site['name']}] ({username}) ⚠️ صفحة الدخول: {resp.status_code}")
                return False

            match = re.search(r'What is (\d+) \+ (\d+)', resp.text)
            if not match:
                match = re.search(r'(\d+)\s*\+\s*(\d+)', resp.text)
            if match:
                captcha_answer = str(int(match.group(1)) + int(match.group(2)))
                print(f"[{site['name']}] ({username}) 🧮 captcha={captcha_answer}")
            else:
                captcha_answer = ""
                print(f"[{site['name']}] ({username}) ⚠️ captcha غير موجود، محاولة بدونه")

            crlf_match = re.search(r"name=['\"]crlf['\"].*?value=['\"]([^'\"]+)['\"]", resp.text)
            if not crlf_match:
                crlf_match = re.search(r"value=['\"]([^'\"]+)['\"].*?name=['\"]crlf['\"]", resp.text)

            payload = {}
            payload.update(_extract_hidden_fields(resp.text))
            payload["username"] = username
            payload["password"] = password
            if captcha_answer:
                payload["capt"] = captcha_answer
            if crlf_match:
                payload["crlf"] = crlf_match.group(1)
                print(f"[{site['name']}] ({username}) 🔑 crlf مستخرج")

            headers = {
                "Content-Type": "application/x-www-form-urlencoded",
                "Referer":  login_page_url,
                "Origin":   base_url.rstrip("/"),
                "Accept":   "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            }
            r2 = session.post(login_post_url, data=payload, headers=headers,
                              timeout=max(TIMEOUT,20), allow_redirects=True)
            print(f"[{site['name']}] ({username}) 📊 URL بعد login: {r2.url}")

            success_kw = ["dashboard","logout","agent","reports","smscdr"]
            r2_url_lower  = r2.url.lower()
            r2_text_lower = r2.text.lower()
            import re as _re
            _has_login_form = bool(_re.search(
                r'<input[^>]+type=["\']password["\']', r2.text, _re.IGNORECASE
            ))
            is_success = (
                any(kw in r2_url_lower  for kw in success_kw) or
                any(kw in r2_text_lower for kw in ["dashboard","logout","smscdr","signout","sign out"]) or
                (r2.url != login_page_url
                 and "login"  not in r2_url_lower
                 and "signin" not in r2_url_lower) or
                (r2.status_code == 200
                 and not _has_login_form
                 and len(r2.text) > 2000)
            )

            if not is_success:
                for sp in ["/ints/agent/SMSCDRReports", "/agent/SMSCDRReports",
                           "/ints/agent/SMSCDRStats", "/agent/SMSCDRStats"]:
                    try:
                        tr = session.get(base_url.rstrip("/")+sp, timeout=10)
                        if (tr.status_code == 200
                                and "login" not in tr.url.lower()
                                and "signin" not in tr.url.lower()
                                and "password" not in tr.text.lower()):
                            is_success = True; break
                    except: pass

            if is_success:
                is_logged_in = True
                for sp in ["/ints/agent/SMSCDRReports","/agent/SMSCDRReports",
                           "/ints/agent/SMSCDRStats",  "/agent/SMSCDRStats"]:
                    try:
                        sr = session.get(base_url.rstrip("/")+sp, timeout=8)
                        sk = re.search(r'sesskey=([A-Za-z0-9=+/]{10,})', sr.text)
                        if not sk:
                            sk = re.search(r'sesskey[\s"\'=:]+([A-Za-z0-9=+/]{10,})', sr.text)
                        if sk:
                            current_sesskey = sk.group(1)
                            print(f"[{site['name']}] 🔑 sesskey OK")
                            break
                    except: continue
                print(f"\033[92m[{site['name']}] ({username}) ✅ دخل بنجاح\033[0m")
                return True
            else:
                print(f"[{site['name']}] ({username}) ❌ فشل الدخول")
                return False
        except Exception as e:
            print(f"[{site['name']}] ({username}) ❌ خطأ login: {e}")
            return False

    def fetch_sms_data():
        nonlocal is_logged_in, current_sesskey

        today      = datetime.now()
        start_date = (today - timedelta(days=1)).strftime("%Y-%m-%d")
        end_date   = (today + timedelta(days=1)).strftime("%Y-%m-%d")

        sms_page = base_url.rstrip("/")+"/ints/agent/SMSCDRReports"
        for attempt in range(2):
            try:
                page_resp = session.get(sms_page, timeout=TIMEOUT)
                if page_resp.status_code == 200:
                    _has_pw_form = bool(re.search(
                        r'<input[^>]+type=["\']password["\']', page_resp.text, re.IGNORECASE
                    ))
                    if _has_pw_form:
                        is_logged_in = False
                        print(f"[{site['name']}] ({username}) ⚠️ جلسة منتهية")
                        return None
                    sk = re.search(r'sesskey=([A-Za-z0-9=+/]+)', page_resp.text)
                    if sk:
                        current_sesskey = sk.group(1)
                elif page_resp.status_code in (502,503,504):
                    time.sleep(3 + attempt*2); continue
                break
            except Exception as e:
                time.sleep(2); continue

        payload = {
            "fdate1": f"{start_date} 00:00:00",
            "fdate2": f"{end_date} 23:59:59",
            "frange":"","fclient":"","fnum":"","fcli":"",
            "fgdate":"","fgmonth":"","fgrange":"",
            "fgclient":"","fgnumber":"","fgcli":"",
            "fg":"0","sEcho":"1",
            "iColumns":"9","sColumns":"",
            "iDisplayStart":"0","iDisplayLength":"100",
            "mDataProp_0":"0","mDataProp_1":"1","mDataProp_2":"2",
            "mDataProp_3":"3","mDataProp_4":"4","mDataProp_5":"5",
            "mDataProp_6":"6","mDataProp_7":"7","mDataProp_8":"8",
            "sSearch":"","bRegex":"false",
            "iSortCol_0":"0","sSortDir_0":"desc","iSortingCols":"1",
        }
        if current_sesskey:
            payload["sesskey"] = current_sesskey

        ajax_headers = {
            "X-Requested-With": "XMLHttpRequest",
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Referer": sms_page,
            "Accept-Language": "en-US,en;q=0.9,ar;q=0.8",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        }

        for retry in range(3):
            try:
                resp = session.post(ajax_url, data=payload,
                                    headers=ajax_headers, timeout=TIMEOUT)
                if resp.status_code == 200:
                    try:
                        data = resp.json()
                        for k in ("aaData","data","rows"):
                            if k in data and isinstance(data[k], list):
                                return data[k]
                        if isinstance(data, list):
                            return data
                        _ajax_has_pw = bool(re.search(r'<input[^>]+type=["\']password["\']', resp.text, re.IGNORECASE))
                        if _ajax_has_pw:
                            is_logged_in = False
                            return None
                        return []
                    except:
                        _ajax_has_pw2 = bool(re.search(r'<input[^>]+type=["\']password["\']', resp.text, re.IGNORECASE))
                        if _ajax_has_pw2:
                            is_logged_in = False
                            return None
                        try:
                            soup = BeautifulSoup(resp.text,"html.parser")
                            table = soup.find("table")
                            if table:
                                tbody = table.find("tbody")
                                trows = tbody.find_all("tr") if tbody else table.find_all("tr")[1:]
                                rows = []
                                for tr in trows:
                                    cells = tr.find_all("td")
                                    if len(cells) >= 6:
                                        rows.append([c.get_text(strip=True) for c in cells])
                                if rows:
                                    print(f"[{site['name']}] ({username}) 📄 HTML parsing")
                                    return rows
                        except: pass
                        return []
                elif resp.status_code == 200:
                    pass  # handled above
                elif resp.status_code in (302,403):
                    is_logged_in = False; return None
                elif resp.status_code in (502,503,504):
                    if retry < 2: time.sleep(3+retry*2); continue
                else:
                    print(f"[{site['name']}] ({username}) ⚠️ HTTP {resp.status_code}")
                    return []
            except requests.exceptions.Timeout:
                if retry < 2: time.sleep(2); continue
                print(f"[{site['name']}] ({username}) ⏱️ timeout")
                return []
            except Exception as e:
                if retry < 2 and ("Connection" in str(e) or "Timeout" in str(e)):
                    time.sleep(2); continue
                print(f"[{site['name']}] ({username}) ❌ fetch خطأ: {e}")
                is_logged_in = False; return []
        return []

    print(f"[{site['name']}] ({username}) 🚀 بدء المراقبة...")
    _load_state()

    _login_retries = 0
    today_start = datetime.combine(date.today(), datetime.min.time())
    if _last_sent_dt is None or _last_sent_dt.date() < date.today():
        _last_sent_dt = today_start
        print(f"[{site['name']}] ({username}) 🕐 سيجلب من بداية اليوم")
    while not do_login():
        _login_retries += 1
        if _login_retries >= 5:
            print(f"[{site['name']}] ({username}) ❌ فشل الدخول بعد 5 محاولات - توقف")
            return
        print(f"[{site['name']}] ({username}) 🔄 إعادة محاولة الدخول ({_login_retries}/5)...")
        time.sleep(10)

    errors        = 0
    _current_day  = date.today()

    while not stop_event.is_set():
        try:
            new_day = date.today()
            if new_day != _current_day:
                print(f"[{site['name']}] 🌅 يوم جديد - إعادة الدخول")
                is_logged_in = False; current_sesskey = None
                sent_msgs_local.clear(); _current_day = new_day

            if not is_logged_in:
                if not do_login():
                    stop_event.wait(30); continue

            raw = fetch_sms_data()

            if raw is None:
                print(f"[{site['name']}] ({username}) 🔄 جلسة منتهية - إعادة الدخول")
                is_logged_in = False; current_sesskey = None
                stop_event.wait(min(interval,2)); continue

            if not raw:
                print(f"[{site['name']}] ({username}) 📭 لا أكواد")
            else:
                idx_d = site.get("idx_date",0)
                idx_n = site.get("idx_number",2)
                idx_s = site.get("idx_sms",5)

                parsed = []
                for row in raw:
                    if not isinstance(row,(list,tuple)) or len(row)<6: continue
                    date_val = clean_html(str(row[idx_d])) if len(row)>idx_d else ""
                    num_val  = clean_number(str(row[idx_n])) if len(row)>idx_n else ""
                    sms_val  = clean_html(str(row[idx_s])) if len(row)>idx_s else ""
                    if not date_val or not num_val or not sms_val or len(num_val)<7: continue
                    if any(x in sms_val.lower() for x in
                           ["currency","payout","nan%","100%","0.008",
                            "my payout","client payout","range","cli","client"]):
                        continue
                    if sms_val.count(",")>=5 and ("%" in sms_val or "nan" in sms_val.lower()):
                        continue
                    parsed.append({"date":date_val,"number":num_val,"sms":sms_val})

                if not parsed:
                    print(f"[{site['name']}] ({username}) 📭 لا أكواد بعد الفلترة")
                else:
                    parsed.sort(key=lambda x: x["date"], reverse=False)
                    new_messages = []
                    for msg in parsed:
                        unique_key = f"{msg['date']}|{msg['number']}|{msg['sms'][:20]}"
                        if unique_key in sent_msgs_local:
                            continue
                        try:
                            msg_dt = datetime.strptime(msg["date"], "%Y-%m-%d %H:%M:%S")
                            if _last_sent_dt is not None and msg_dt < _last_sent_dt:
                                sent_msgs_local.add(unique_key)
                                continue
                        except:
                            pass
                        new_messages.append(msg)
                        sent_msgs_local.add(unique_key)

                    if new_messages:
                        _panel_box(site['name'], sms=f"{len(new_messages)} رسالة جديدة", status="INFO")
                        for msg in new_messages:
                            last_seen_key = f"{msg['date']}|{msg['number']}"
                            _panel_box(site['name'], f"{msg['number'][:6]}***", msg['sms'][:60], status="NEW")
                            send_otp_to_user_and_group(
                                msg["date"], msg["number"], msg["sms"],
                                panel_name=site["name"], short_bold=short_bold)
                            try:
                                msg_dt = datetime.strptime(msg["date"], "%Y-%m-%d %H:%M:%S")
                                if _last_sent_dt is None or msg_dt > _last_sent_dt:
                                    _last_sent_dt = msg_dt
                            except: pass
                        _save_state()
                    else:
                        _panel_box(site['name'], status="EMPTY")

            errors = 0

        except Exception as e:
            errors += 1
            print(f"[{site['name']}] ({username}) ⚠️ خطأ ({errors}/5): {e}")
            if errors >= 5:
                print(f"[{site['name']}] ({username}) 🔄 إعادة الدخول...")
                is_logged_in = False; current_sesskey = None
                if do_login(): errors = 0
                else: stop_event.wait(30)
            else:
                time.sleep(5)

        stop_event.wait(min(CHECK_INTERVAL, 1))

    print(f"[{site['name']}] ({username}) 🛑 توقفت المراقبة")


_static_dash_sessions = {}

def init_db():
    conn = sqlite3.connect(DB_PATH, check_same_thread=False, timeout=10)
    c = conn.cursor()
    c.execute("PRAGMA journal_mode=WAL")
    c.execute("PRAGMA synchronous=NORMAL")
    c.execute("PRAGMA busy_timeout=5000")  # 5 ثانية انتظار لو DB مشغولة
    c.execute('''CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY, username TEXT, first_name TEXT,
        last_name TEXT, country_code TEXT, assigned_number TEXT,
        is_banned INTEGER DEFAULT 0, private_combo_country TEXT DEFAULT NULL,
        lang TEXT DEFAULT 'ar', agreed_terms INTEGER DEFAULT 0,
        balance REAL DEFAULT 0.0
    )''')
    c.execute('''CREATE TABLE IF NOT EXISTS combos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        country_code TEXT NOT NULL,
        numbers TEXT NOT NULL,
        section_id INTEGER,
        added_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        file_name TEXT,
        price_per_number REAL DEFAULT 0.0
    )''')
    c.execute('''CREATE TABLE IF NOT EXISTS balance_log (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        amount REAL NOT NULL,
        number TEXT,
        combo_tag TEXT,
        logged_at TEXT DEFAULT CURRENT_TIMESTAMP
    )''')
    try:
        c.execute("ALTER TABLE combos ADD COLUMN price_per_number REAL DEFAULT 0.0")
    except:
        pass  # العمود موجود مسبقاً
    try:
        c.execute("ALTER TABLE users ADD COLUMN balance REAL DEFAULT 0.0")
    except:
        pass  # العمود موجود مسبقاً
    c.execute('CREATE INDEX IF NOT EXISTS idx_combos_country ON combos(country_code)')
    c.execute('''CREATE TABLE IF NOT EXISTS sections (
        id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT UNIQUE NOT NULL
    )''')
    c.execute('''CREATE TABLE IF NOT EXISTS otp_logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT, number TEXT, otp TEXT,
        full_message TEXT, timestamp TEXT, assigned_to INTEGER
    )''')
    c.execute('''CREATE TABLE IF NOT EXISTS bot_settings (
        key TEXT PRIMARY KEY, value TEXT
    )''')
    c.execute('''CREATE TABLE IF NOT EXISTS private_combos (
        user_id INTEGER, country_code TEXT, numbers TEXT,
        PRIMARY KEY (user_id, country_code)
    )''')
    c.execute('''CREATE TABLE IF NOT EXISTS force_sub_channels (
        id INTEGER PRIMARY KEY AUTOINCREMENT, channel_url TEXT UNIQUE NOT NULL,
        description TEXT DEFAULT '', enabled INTEGER DEFAULT 1, channel_id TEXT DEFAULT NULL
    )''')
    try:
        c.execute("ALTER TABLE force_sub_channels ADD COLUMN channel_id TEXT DEFAULT NULL")
    except:
        pass
    c.execute('''CREATE TABLE IF NOT EXISTS admins (
        user_id INTEGER PRIMARY KEY, username TEXT DEFAULT ''
    )''')
    c.execute('''CREATE TABLE IF NOT EXISTS bot_groups (
        group_id TEXT PRIMARY KEY, description TEXT DEFAULT '', is_otp_group INTEGER DEFAULT 0
    )''')
    c.execute('''CREATE TABLE IF NOT EXISTS otp_tg_messages (
        id INTEGER PRIMARY KEY AUTOINCREMENT, chat_id TEXT NOT NULL,
        message_id INTEGER NOT NULL, sent_at TEXT NOT NULL
    )''')
    c.execute('''CREATE TABLE IF NOT EXISTS otp_group_buttons (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        button_text TEXT NOT NULL,
        button_url TEXT NOT NULL,
        position INTEGER DEFAULT 0
    )''')
    c.execute('''CREATE TABLE IF NOT EXISTS auto_delete_settings (
        chat_id TEXT PRIMARY KEY, delete_after INTEGER DEFAULT 30
    )''')
    c.execute('''CREATE TABLE IF NOT EXISTS dashboard_accounts (
        id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, short TEXT NOT NULL,
        username TEXT, password TEXT, api_token TEXT, type TEXT DEFAULT 'traditional',
        base_url TEXT, ajax_path TEXT, login_page TEXT, login_post TEXT, stats_page TEXT,
        idx_date INTEGER DEFAULT 0, idx_number INTEGER DEFAULT 2, idx_sms INTEGER DEFAULT 5,
        timeout INTEGER DEFAULT 10, data_keys TEXT, is_active INTEGER DEFAULT 1,
        refresh_interval INTEGER DEFAULT 1
    )''')
    try:
        c.execute("ALTER TABLE dashboard_accounts ADD COLUMN refresh_interval INTEGER DEFAULT 1")
    except:
        pass
    c.execute('''CREATE TABLE IF NOT EXISTS custom_buttons (
        id INTEGER PRIMARY KEY AUTOINCREMENT, button_text TEXT NOT NULL,
        button_url TEXT NOT NULL, position INTEGER DEFAULT 0
    )''')
    c.execute('''CREATE TABLE IF NOT EXISTS bot_images (
        key TEXT PRIMARY KEY, image TEXT
    )''')
    c.execute('''CREATE TABLE IF NOT EXISTS maintenance_mode (
        id INTEGER PRIMARY KEY CHECK (id = 1), enabled INTEGER DEFAULT 0
    )''')
    c.execute("INSERT OR IGNORE INTO maintenance_mode (id, enabled) VALUES (1, 0)")
    c.execute('''CREATE TABLE IF NOT EXISTS otp_delete_global (
        id INTEGER PRIMARY KEY CHECK (id = 1),
        delete_after INTEGER DEFAULT 30
    )''')
    c.execute("INSERT OR IGNORE INTO otp_delete_global (id, delete_after) VALUES (1, 30)")
    c.execute('''CREATE TABLE IF NOT EXISTS otp_user_messages (
        user_id TEXT PRIMARY KEY,
        message_id INTEGER NOT NULL,
        sent_at TEXT NOT NULL
    )''')
    c.execute('''CREATE TABLE IF NOT EXISTS combo_tags (
        combo_id INTEGER PRIMARY KEY,
        tag TEXT UNIQUE NOT NULL
    )''')
    c.execute('''CREATE TABLE IF NOT EXISTS traffic_stats (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        country_code TEXT NOT NULL,
        platform TEXT DEFAULT '',
        combo_tag TEXT DEFAULT '',
        codes_count INTEGER DEFAULT 0,
        window_start TEXT NOT NULL,
        window_end TEXT NOT NULL,
        stat_type TEXT DEFAULT 'last_sms'
    )''')
    c.execute('''CREATE TABLE IF NOT EXISTS withdraw_requests (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        amount REAL NOT NULL,
        address TEXT NOT NULL,
        username TEXT NOT NULL,
        created_at TEXT NOT NULL
    )''')
    c.execute('''CREATE TABLE IF NOT EXISTS released_numbers (
        number TEXT PRIMARY KEY,
        user_id INTEGER NOT NULL,
        released_at TEXT NOT NULL
    )''')
    c.execute('''CREATE TABLE IF NOT EXISTS user_combo_tags (
        number TEXT PRIMARY KEY,
        combo_tag TEXT NOT NULL,
        assigned_at TEXT DEFAULT CURRENT_TIMESTAMP
    )''')
    c.execute('''CREATE TABLE IF NOT EXISTS referrals (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        referrer_id INTEGER NOT NULL,
        referred_id INTEGER NOT NULL UNIQUE,
        earned REAL DEFAULT 0.01,
        created_at TEXT DEFAULT CURRENT_TIMESTAMP
    )''')
    conn.commit()
    conn.close()

init_db()

REFERRAL_EARN = 0.01

def get_referral_count(user_id):
    conn = sqlite3.connect(DB_PATH, check_same_thread=False, timeout=10)
    c = conn.cursor()
    c.execute("SELECT COUNT(*) FROM referrals WHERE referrer_id=?", (user_id,))
    row = c.fetchone()
    conn.close()
    return row[0] if row else 0

def get_referral_total_earned(user_id):
    conn = sqlite3.connect(DB_PATH, check_same_thread=False, timeout=10)
    c = conn.cursor()
    c.execute("SELECT COALESCE(SUM(earned),0) FROM referrals WHERE referrer_id=?", (user_id,))
    row = c.fetchone()
    conn.close()
    return float(row[0]) if row else 0.0

def process_referral(referrer_id, referred_id):
    if referrer_id == referred_id:
        return False
    conn = sqlite3.connect(DB_PATH, check_same_thread=False, timeout=10)
    c = conn.cursor()
    c.execute("SELECT id FROM referrals WHERE referred_id=?", (referred_id,))
    if c.fetchone():
        conn.close()
        return False
    c.execute(
        "INSERT OR IGNORE INTO referrals (referrer_id, referred_id, earned) VALUES (?,?,?)",
        (referrer_id, referred_id, REFERRAL_EARN)
    )
    if c.rowcount:
        c.execute(
            "UPDATE users SET balance = COALESCE(balance,0) + ? WHERE user_id=?",
            (REFERRAL_EARN, referrer_id)
        )
        conn.commit()
        conn.close()
        return True
    conn.close()
    return False

PLATFORM_EMOJIS = {
    "WhatsApp": "5393189591773630465",
    "Facebook": "5393310276059678201",
    "Telegram": "5393353148423229623",
}
FIXED_PLATFORM_NAMES = ["WhatsApp", "Facebook", "Telegram"]

def ensure_fixed_platforms():
    conn = sqlite3.connect(DB_PATH, check_same_thread=False, timeout=10)
    c = conn.cursor()
    for name in FIXED_PLATFORM_NAMES:
        c.execute("INSERT OR IGNORE INTO sections (name) VALUES (?)", (name,))
    conn.commit()
    conn.close()

def get_platform_emoji_id(name):
    return PLATFORM_EMOJIS.get(name)

def get_fixed_platform_id(name):
    conn = sqlite3.connect(DB_PATH, check_same_thread=False, timeout=10)
    c = conn.cursor()
    c.execute("SELECT id FROM sections WHERE name=?", (name,))
    row = c.fetchone()
    conn.close()
    return row[0] if row else None

_platform_ids_cache = {}

def get_all_fixed_platforms():
    result = []
    conn = sqlite3.connect(DB_PATH, check_same_thread=False, timeout=10)
    c = conn.cursor()
    for name in FIXED_PLATFORM_NAMES:
        c.execute("SELECT id FROM sections WHERE name=?", (name,))
        row = c.fetchone()
        if row:
            result.append({"id": row[0], "name": name, "emoji_id": PLATFORM_EMOJIS.get(name, "")})
    conn.close()
    return result

FIXED_PLATFORMS = []

def get_platform_total_numbers(section_id):
    conn = sqlite3.connect(DB_PATH, check_same_thread=False, timeout=10)
    c = conn.cursor()
    c.execute("SELECT id FROM combos WHERE section_id=?", (section_id,))
    ids = [r[0] for r in c.fetchall()]
    conn.close()
    total = sum(len(get_available_numbers_from_file(i)) for i in ids)
    return total

ensure_fixed_platforms()
FIXED_PLATFORMS = get_all_fixed_platforms()

def get_db_dashboards(only_active=True):
    conn = sqlite3.connect(DB_PATH, check_same_thread=False, timeout=10)
    c = conn.cursor()
    if only_active:
        c.execute("SELECT * FROM dashboard_accounts WHERE is_active=1")
    else:
        c.execute("SELECT * FROM dashboard_accounts")
    rows = c.fetchall()
    conn.close()
    dashboards = []
    for row in rows:
        dash = {
            "id": row[0],
            "name": row[1],
            "short": row[2],
            "username": row[3],
            "password": row[4],
            "api_token": row[5],
            "type": row[6],
            "base_url": row[7],
            "ajax_path": row[8],
            "login_page": row[9],
            "login_post": row[10],
            "stats_page": row[11],
            "idx_date": row[12],
            "idx_number": row[13],
            "idx_sms": row[14],
            "timeout": row[15],
            "data_keys": json.loads(row[16]) if row[16] else {},
            "is_active": row[17],
            "refresh_interval": row[18] if len(row) > 18 else 1,
            "source": "db",
            "short_bold": to_bold(row[2])
        }
        dashboards.append(dash)
    return dashboards

def add_dashboard_account(name, short, username, password, api_token, dash_type, base_url,
                          ajax_path="", login_page="", login_post="", stats_page="",
                          idx_date=0, idx_number=2, idx_sms=5, timeout=10, data_keys=None, refresh_interval=1):
    conn = sqlite3.connect(DB_PATH, check_same_thread=False, timeout=10)
    c = conn.cursor()
    data_keys_json = json.dumps(data_keys) if data_keys else "{}"
    c.execute("""INSERT INTO dashboard_accounts 
                 (name, short, username, password, api_token, type, base_url, ajax_path, 
                  login_page, login_post, stats_page, idx_date, idx_number, idx_sms, timeout, data_keys, is_active, refresh_interval)
                 VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 1, ?)""",
              (name, short, username, password, api_token, dash_type, base_url, ajax_path,
               login_page, login_post, stats_page, idx_date, idx_number, idx_sms, timeout, data_keys_json, refresh_interval))
    conn.commit()
    conn.close()

def delete_dashboard_account(id):
    conn = sqlite3.connect(DB_PATH, check_same_thread=False, timeout=10)
    c = conn.cursor()
    c.execute("DELETE FROM dashboard_accounts WHERE id=?", (id,))
    conn.commit()
    conn.close()

def toggle_dashboard_account(id):
    conn = sqlite3.connect(DB_PATH, check_same_thread=False, timeout=10)
    c = conn.cursor()
    c.execute("UPDATE dashboard_accounts SET is_active = 1 - is_active WHERE id=?", (id,))
    conn.commit()
    conn.close()

def get_all_active_dashboards():
    all_dash = []
    for dash in STATIC_DASHBOARDS:
        d = dash.copy()
        d["is_active"] = True
        name_key = d["name"]
        if name_key not in _static_dash_sessions:
            s = requests.Session()
            s.headers.update(COMMON_HEADERS)
            _static_dash_sessions[name_key] = {"session": s, "is_logged_in": False, "sesskey": None}
        d["session"]    = _static_dash_sessions[name_key]["session"]
        d["is_logged_in"] = _static_dash_sessions[name_key].get("is_logged_in", False)
        d["sesskey"]    = _static_dash_sessions[name_key].get("sesskey")
        def _build_url(base, path):
            if not path: return ""
            if path.startswith("http"): return path
            return base.rstrip("/") + path if base else path

        if d["type"] in ("api_token", "api"):
            d["is_logged_in"] = True
        elif d["type"] == "ims_panel":
            d["is_logged_in"] = False
            d["sesskey"] = None
            d["phpsessid"] = None
            d["last_login_time"] = 0
            d["login_page_url"] = _build_url(d.get("base_url",""), d.get("login_page",""))
            d["login_post_url"] = _build_url(d.get("base_url",""), d.get("login_post",""))
            d["ajax_url"]       = _build_url(d.get("base_url",""), d.get("ajax_path",""))
            d["dashboard_url"]  = _build_url(d.get("base_url",""), d.get("dashboard_path",""))
        else:
            d["login_page_url"] = _build_url(d.get("base_url",""), d.get("login_page",""))
            d["login_post_url"] = _build_url(d.get("base_url",""), d.get("login_post",""))
            d["ajax_url"]       = _build_url(d.get("base_url",""), d.get("ajax_path",""))
        if name_key in _static_dash_sessions:
            _static_dash_sessions[name_key]["is_logged_in"] = d.get("is_logged_in", False)
            _static_dash_sessions[name_key]["sesskey"] = d.get("sesskey")
        all_dash.append(d)
    for dash in get_db_dashboards(only_active=True):
        dash["session"] = requests.Session()
        dash["session"].headers.update(COMMON_HEADERS)
        dash["is_logged_in"] = False
        dash["sesskey"] = None
        if dash["type"] in ("api_token", "api"):
            dash["is_logged_in"] = True
        else:
            def _bu(base, path):
                if not path: return ""
                if path.startswith("http"): return path
                return base.rstrip("/") + path if base else path
            dash["login_page_url"] = _bu(dash.get("base_url",""), dash.get("login_page",""))
            dash["login_post_url"] = _bu(dash.get("base_url",""), dash.get("login_post",""))
            dash["ajax_url"]       = _bu(dash.get("base_url",""), dash.get("ajax_path",""))
        all_dash.append(dash)
    return all_dash

def load_settings():
    global MAINTENANCE_MODE, BOT_IMAGE_BYTES, MAINTENANCE_IMAGE_BYTES, FORCE_SUB_IMAGE_BYTES
    conn = sqlite3.connect(DB_PATH, check_same_thread=False, timeout=10)
    c = conn.cursor()
    c.execute("SELECT enabled FROM maintenance_mode WHERE id=1")
    row = c.fetchone()
    MAINTENANCE_MODE = bool(row[0]) if row else False
    c.execute("SELECT key, image FROM bot_images")
    for key, img in c.fetchall():
        if key == "bot":
            BOT_IMAGE_BYTES = base64.b64decode(img) if img else None
        elif key == "force_sub":
            FORCE_SUB_IMAGE_BYTES = base64.b64decode(img) if img else None
        elif key == "maintenance":
            MAINTENANCE_IMAGE_BYTES = base64.b64decode(img) if img else None
    conn.close()

load_settings()

def save_image(key, image_bytes):
    conn = sqlite3.connect(DB_PATH, check_same_thread=False, timeout=10)
    c = conn.cursor()
    img_b64 = base64.b64encode(image_bytes).decode('utf-8')
    c.execute("REPLACE INTO bot_images (key, image) VALUES (?, ?)", (key, img_b64))
    conn.commit()
    conn.close()
    load_settings()

def delete_image(key):
    conn = sqlite3.connect(DB_PATH, check_same_thread=False, timeout=10)
    c = conn.cursor()
    c.execute("DELETE FROM bot_images WHERE key=?", (key,))
    conn.commit()
    conn.close()
    load_settings()

def set_maintenance_mode(enabled):
    conn = sqlite3.connect(DB_PATH, check_same_thread=False, timeout=10)
    c = conn.cursor()
    c.execute("UPDATE maintenance_mode SET enabled=? WHERE id=1", (1 if enabled else 0,))
    conn.commit()
    conn.close()
    global MAINTENANCE_MODE
    MAINTENANCE_MODE = enabled

def get_maintenance_mode():
    return MAINTENANCE_MODE

def send_maintenance_msg(chat_id, user_id):
    lang = get_user_lang(user_id)
    if lang == "en":
        maint_caption = "🟢 The bot is under maintenance, please wait."
    else:
        maint_caption = "🟢 البوت في وضع الصيانة يرجي الانتظار"
    try:
        if MAINTENANCE_IMAGE_BYTES:
            requests.post(
                f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto",
                data={"chat_id": chat_id, "caption": maint_caption, "parse_mode": "HTML"},
                files={"photo": ("maint.jpg", io.BytesIO(MAINTENANCE_IMAGE_BYTES), "image/jpeg")},
                timeout=10
            )
        else:
            requests.post(
                f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
                json={"chat_id": chat_id, "text": maint_caption, "parse_mode": "HTML"},
                timeout=10
            )
    except Exception:
        pass

def is_maintenance_callback(call):
    if MAINTENANCE_MODE and not is_admin(call.from_user.id):
        try:
            bot.answer_callback_query(call.id)
        except Exception:
            pass
        send_maintenance_msg(call.message.chat.id, call.from_user.id)
        return True
    return False

def get_user(user_id):
    conn = sqlite3.connect(DB_PATH, check_same_thread=False, timeout=10)
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE user_id=?", (user_id,))
    row = c.fetchone()
    conn.close()
    return row

def save_user(user_id, username="", first_name="", last_name="",
              country_code=None, assigned_number=None, private_combo_country=None,
              lang=None, agreed_terms=None):
    existing = get_user(user_id)
    if existing:
        if country_code is None: country_code = existing[4]
        if assigned_number is None: assigned_number = existing[5]
        if private_combo_country is None: private_combo_country = existing[7]
        if lang is None: lang = existing[8]
        if agreed_terms is None: agreed_terms = existing[9]
    else:
        if lang is None: lang = "ar"
        if agreed_terms is None: agreed_terms = 0
    conn = sqlite3.connect(DB_PATH, check_same_thread=False, timeout=10)
    c = conn.cursor()
    c.execute("""REPLACE INTO users
        (user_id,username,first_name,last_name,country_code,assigned_number,is_banned,private_combo_country,lang,agreed_terms)
        VALUES (?,?,?,?,?,?,COALESCE((SELECT is_banned FROM users WHERE user_id=?),0),?,?,?)""",
        (user_id, username, first_name, last_name, country_code,
         assigned_number, user_id, private_combo_country, lang, agreed_terms))
    conn.commit()
    conn.close()

def is_banned(user_id):
    user = get_user(user_id)
    return user and user[6] == 1

def ban_user(user_id):
    conn = sqlite3.connect(DB_PATH, check_same_thread=False, timeout=10)
    c = conn.cursor()
    c.execute("UPDATE users SET is_banned=1 WHERE user_id=?", (user_id,))
    conn.commit()
    conn.close()

def unban_user(user_id):
    conn = sqlite3.connect(DB_PATH, check_same_thread=False, timeout=10)
    c = conn.cursor()
    c.execute("UPDATE users SET is_banned=0 WHERE user_id=?", (user_id,))
    conn.commit()
    conn.close()

def get_all_users():
    conn = sqlite3.connect(DB_PATH, check_same_thread=False, timeout=10)
    c = conn.cursor()
    c.execute("SELECT user_id FROM users WHERE is_banned=0")
    users = [row[0] for row in c.fetchall()]
    conn.close()
    return users

def save_combo(country_code, numbers, user_id=None, section_id=None, file_name=""):
    conn = sqlite3.connect(DB_PATH, check_same_thread=False, timeout=10)
    c = conn.cursor()
    if user_id:
        c.execute("REPLACE INTO private_combos (user_id, country_code, numbers) VALUES (?, ?, ?)",
                  (user_id, country_code, json.dumps(numbers)))
        conn.commit()
        conn.close()
    else:
        c.execute("INSERT INTO combos (country_code, numbers, section_id, file_name) VALUES (?, ?, ?, ?)",
                  (country_code, json.dumps(numbers), section_id, file_name))
        conn.commit()
        new_id = c.lastrowid
        conn.close()
        _generate_unique_combo_tag(country_code, 0, combo_id=new_id)
    return True

def get_combo_files(country_code, section_id=None):
    conn = sqlite3.connect(DB_PATH, check_same_thread=False, timeout=10)
    c = conn.cursor()
    if section_id is not None:
        c.execute("SELECT id, file_name, added_at, numbers FROM combos WHERE country_code=? AND section_id=? ORDER BY added_at", (country_code, section_id))
    else:
        c.execute("SELECT id, file_name, added_at, numbers FROM combos WHERE country_code=? ORDER BY added_at", (country_code,))
    rows = c.fetchall()
    conn.close()
    files = []
    for row in rows:
        num_list = json.loads(row[3])
        files.append({
            "id": row[0],
            "file_name": row[1] or f"ملف {row[0]}",
            "added_at": row[2],
            "numbers": num_list,
            "total": len(num_list)
        })
    return files

def _normalize_num(n):
    """ينظف الرقم ويجيب نسخة موحدة بالأرقام فقط بدون 00 prefix"""
    d = re.sub(r'\D', '', str(n).strip())
    if d.startswith('00'):
        d = d[2:]
    return d

def get_available_numbers_from_file(file_id):
    conn = sqlite3.connect(DB_PATH, check_same_thread=False, timeout=10)
    c = conn.cursor()
    c.execute("SELECT numbers FROM combos WHERE id=?", (file_id,))
    row = c.fetchone()
    conn.close()
    if not row:
        return []
    all_numbers = json.loads(row[0])
    conn = sqlite3.connect(DB_PATH, check_same_thread=False, timeout=10)
    c = conn.cursor()
    c.execute("SELECT assigned_number FROM users WHERE assigned_number IS NOT NULL AND assigned_number!=''")
    used_raw = [str(r[0]).strip() for r in c.fetchall()]
    conn.close()
    used_normalized = set(_normalize_num(n) for n in used_raw)
    available = [n for n in all_numbers if _normalize_num(n) not in used_normalized]
    return available

def remove_number_from_combo(number):
    """يحذف الرقم من الكومبو مع normalize كامل للفورمات"""
    number = str(number).strip()
    number_digits = re.sub(r'\D', '', number)
    conn = sqlite3.connect(DB_PATH, check_same_thread=False, timeout=10)
    c = conn.cursor()
    c.execute("SELECT id, numbers FROM combos")
    rows = c.fetchall()
    removed_any = False
    for file_id, nums_json in rows:
        try:
            nums = json.loads(nums_json)
            new_nums = []
            for n in nums:
                n_digits = re.sub(r'\D', '', str(n))
                n_norm = n_digits.lstrip('0')
                sms_norm = number_digits.lstrip('0')
                if n_norm == sms_norm:
                    removed_any = True
                    continue
                new_nums.append(n)
            if len(new_nums) != len(nums):
                c.execute("UPDATE combos SET numbers=? WHERE id=?", (json.dumps(new_nums), file_id))
        except:
            pass
    conn.commit()
    conn.close()
    if removed_any:
        print(f"[remove_combo] ✅ حُذف {number_digits[:8]} من الكومبو")
    else:
        print(f"[remove_combo] ⚠️ {number_digits[:8]} لم يُعثر عليه في أي كومبو")

def _build_tags_pool():
    """
    بناء قائمة tags بالترتيب الأبجدي التصاعدي:
    AA, AB, AC, ... AZ, BA, BB, ...
    كل كومبو جديد يأخذ أول tag غير مستخدم بالترتيب.
    """
    import itertools
    letters = "ABCDEFGHJKLMNPQRSTVWXYZ"  # استثناء I وO وU لتجنب الالتباس
    return ["".join(p) for p in itertools.product(letters, repeat=2)]

_TAGS_POOL = _build_tags_pool()  # يُبنى مرة واحدة عند تحميل الملف

def _generate_unique_combo_tag(country_code, file_idx, section_id=None, combo_id=None):
    try:
        conn_t = sqlite3.connect(DB_PATH, check_same_thread=False, timeout=10)
        c_t = conn_t.cursor()
        if combo_id:
            c_t.execute("SELECT tag FROM combo_tags WHERE combo_id=?", (combo_id,))
            existing = c_t.fetchone()
            if existing and existing[0]:
                conn_t.close()
                return existing[0]
        c_t.execute("SELECT tag FROM combo_tags")
        _used_tags = {r[0] for r in c_t.fetchall() if r[0]}
        chosen = None
        for _tag in _TAGS_POOL:
            if _tag not in _used_tags:
                chosen = _tag
                break
        if not chosen:
            import random, string
            for _ in range(200):
                candidate = "".join(random.choices(string.ascii_uppercase, k=2))
                if candidate not in _used_tags:
                    chosen = candidate
                    break
            if not chosen:
                chosen = f"Z{file_idx}"
        if combo_id:
            try:
                c_t.execute("INSERT INTO combo_tags (combo_id, tag) VALUES (?,?)",
                            (combo_id, chosen))
            except Exception:
                for _alt in _TAGS_POOL:
                    if _alt not in _used_tags and _alt != chosen:
                        chosen = _alt
                        c_t.execute("INSERT OR IGNORE INTO combo_tags (combo_id, tag) VALUES (?,?)",
                                    (combo_id, chosen))
                        break
            conn_t.commit()
        conn_t.close()
        return chosen
    except Exception as e:
        print(f"[gen_tag] error: {e}")
        import random, string
        return "".join(random.choices(string.ascii_uppercase, k=2))


def get_combo_tag_for_number(number, with_price=False):
    number_str = str(number).strip()
    clean = number_str.lstrip("+").strip()
    variants = [number_str, "+" + clean, clean]
    try:
        c0 = sqlite3.connect(DB_PATH, check_same_thread=False, timeout=10)
        cur = c0.cursor()
        for variant in variants:
            try:
                cur.execute("SELECT combo_tag, COALESCE(price,0) FROM user_combo_tags WHERE number=?", (variant,))
            except:
                cur.execute("SELECT combo_tag, 0 FROM user_combo_tags WHERE number=?", (variant,))
            row = cur.fetchone()
            if row and row[0]:
                c0.close()
                return (row[0], float(row[1])) if with_price else row[0]
        c0.close()
    except Exception as e:
        print(f"[get_combo_tag] error: {e}")
    return (None, 0.0) if with_price else None


def save_combo_tag_for_number(number, combo_tag, price=0.0):
    """يحفظ الكومبو tag + السعر للرقم في DB"""
    try:
        number = str(number).strip()
        conn = sqlite3.connect(DB_PATH, check_same_thread=False, timeout=10)
        c = conn.cursor()
        try:
            c.execute("ALTER TABLE user_combo_tags ADD COLUMN price REAL DEFAULT 0.0")
            conn.commit()
        except:
            pass
        c.execute("""
            INSERT OR REPLACE INTO user_combo_tags (number, combo_tag, assigned_at, price)
            VALUES (?, ?, ?, ?)
        """, (number, combo_tag, datetime.now().strftime("%Y-%m-%d %H:%M:%S"), float(price)))
        conn.commit()
        conn.close()
    except Exception as e:
        print(f"[save_combo_tag] ⚠️ {e}")


def delete_combo_file(file_id):
    try:
        conn = sqlite3.connect(DB_PATH, check_same_thread=False, timeout=10)
        c = conn.cursor()
        c.execute("DELETE FROM combos WHERE id=?", (file_id,))
        affected = c.rowcount
        conn.commit()
        conn.close()
        return affected > 0
    except Exception as e:
        print(f"[delete_combo_file] ⚠️ {e}")
        return False

def get_all_combos():
    conn = sqlite3.connect(DB_PATH, check_same_thread=False, timeout=10)
    c = conn.cursor()
    c.execute("SELECT DISTINCT country_code FROM combos")
    rows = [r[0] for r in c.fetchall()]
    conn.close()
    return rows

def delete_combo(country_code, user_id=None):
    conn = sqlite3.connect(DB_PATH, check_same_thread=False, timeout=10)
    c = conn.cursor()
    if user_id:
        c.execute("DELETE FROM private_combos WHERE user_id=? AND country_code=?", (user_id, country_code))
    else:
        c.execute("DELETE FROM combos WHERE country_code=?", (country_code,))
    conn.commit()
    conn.close()

def get_all_combos_with_section():
    conn = sqlite3.connect(DB_PATH, check_same_thread=False, timeout=10)
    c = conn.cursor()
    c.execute("SELECT country_code, section_id FROM combos")
    rows = c.fetchall()
    conn.close()
    return rows

def get_combos_by_section(section_id):
    conn = sqlite3.connect(DB_PATH, check_same_thread=False, timeout=10)
    c = conn.cursor()
    c.execute("SELECT DISTINCT country_code FROM combos WHERE section_id=?", (section_id,))
    rows = [r[0] for r in c.fetchall()]
    conn.close()
    return rows

def create_section(name):
    conn = sqlite3.connect(DB_PATH, check_same_thread=False, timeout=10)
    c = conn.cursor()
    try:
        c.execute("INSERT INTO sections (name) VALUES (?)", (name.strip(),))
        conn.commit()
        sid = c.lastrowid
    except:
        c.execute("SELECT id FROM sections WHERE name=?", (name.strip(),))
        row = c.fetchone()
        sid = row[0] if row else None
    conn.close()
    return sid

def get_all_sections():
    conn = sqlite3.connect(DB_PATH, check_same_thread=False, timeout=10)
    c = conn.cursor()
    c.execute("SELECT id, name FROM sections ORDER BY id")
    rows = c.fetchall()
    conn.close()
    return rows

def delete_section(section_id):
    conn = sqlite3.connect(DB_PATH, check_same_thread=False, timeout=10)
    c = conn.cursor()
    c.execute("UPDATE combos SET section_id=NULL WHERE section_id=?", (section_id,))
    c.execute("DELETE FROM sections WHERE id=?", (section_id,))
    conn.commit()
    conn.close()

def assign_number_to_user(user_id, number):
    conn = sqlite3.connect(DB_PATH, check_same_thread=False, timeout=10)
    c = conn.cursor()
    c.execute("UPDATE users SET assigned_number=? WHERE user_id=?", (number, user_id))
    conn.commit()
    conn.close()

def get_user_by_number(number):
    """البحث عن المستخدم بالرقم - يجرب فورمات متعددة"""
    conn = sqlite3.connect(DB_PATH, check_same_thread=False, timeout=10)
    c = conn.cursor()
    number_str = str(number).strip()
    clean = number_str.replace(" ", "").replace("-", "")
    if clean.startswith("00"):
        clean = clean[2:]
    clean_no_plus = clean.lstrip("+")
    variants = list({
        number_str,
        clean,
        "+" + clean_no_plus,
        clean_no_plus,
        "00" + clean_no_plus,
    })
    for v in variants:
        c.execute("SELECT user_id FROM users WHERE assigned_number=?", (v,))
        row = c.fetchone()
        if row:
            conn.close()
            return row[0]
    c.execute("SELECT user_id, assigned_number FROM users WHERE assigned_number IS NOT NULL AND assigned_number!=''")
    all_users = c.fetchall()
    conn.close()
    target = re.sub(r'\D', '', clean_no_plus)
    if target.startswith('00'):
        target = target[2:]
    for uid, assigned in all_users:
        a_clean = re.sub(r'\D', '', str(assigned).strip())
        if a_clean.startswith('00'):
            a_clean = a_clean[2:]
        if a_clean == target:
            return uid
    try:
        c.execute("SELECT user_id, number FROM released_numbers WHERE released_at >= datetime('now', '-15 minutes')")
        released = c.fetchall()
        conn.close()
        for uid, rnum in released:
            r_clean = re.sub(r'\D', '', str(rnum).strip())
            if r_clean.startswith('00'):
                r_clean = r_clean[2:]
            if r_clean == target:
                return uid
    except:
        conn.close()
    return None

def release_number(old_number):
    if not old_number:
        return
    conn = sqlite3.connect(DB_PATH, check_same_thread=False, timeout=10)
    c = conn.cursor()
    c.execute("SELECT user_id FROM users WHERE assigned_number=?", (old_number,))
    row = c.fetchone()
    if row:
        c.execute(
            "INSERT OR REPLACE INTO released_numbers (number, user_id, released_at) VALUES (?,?,?)",
            (str(old_number).strip(), row[0], datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        )
    c.execute("UPDATE users SET assigned_number=NULL WHERE assigned_number=?", (old_number,))
    c.execute("DELETE FROM released_numbers WHERE released_at < datetime('now', '-15 minutes')")
    conn.commit()
    conn.close()

def log_otp(number, otp, full_message, assigned_to=None):
    conn = sqlite3.connect(DB_PATH, check_same_thread=False, timeout=10)
    c = conn.cursor()
    c.execute("INSERT INTO otp_logs (number,otp,full_message,timestamp,assigned_to) VALUES (?,?,?,?,?)",
              (number, otp, full_message, datetime.now().strftime("%Y-%m-%d %H:%M:%S"), assigned_to))
    conn.commit()
    conn.close()

def get_platforms_with_numbers():
    conn = sqlite3.connect(DB_PATH, check_same_thread=False, timeout=10)
    c = conn.cursor()
    c.execute("""
        SELECT DISTINCT s.id, s.name
        FROM sections s
        INNER JOIN combos co ON co.section_id = s.id
        ORDER BY s.id
    """)
    rows = c.fetchall()
    conn.close()
    result = []
    conn2 = sqlite3.connect(DB_PATH, check_same_thread=False, timeout=10)
    c2 = conn2.cursor()
    c2.execute("SELECT assigned_number FROM users WHERE assigned_number IS NOT NULL AND assigned_number!=''")
    used = set(str(r[0]).strip() for r in c2.fetchall())
    conn2.close()
    for sid, sname in rows:
        conn3 = sqlite3.connect(DB_PATH, check_same_thread=False, timeout=10)
        c3 = conn3.cursor()
        c3.execute("SELECT numbers FROM combos WHERE section_id=?", (sid,))
        files = c3.fetchall()
        conn3.close()
        for (nums_json,) in files:
            try:
                nums = json.loads(nums_json)
                if any(str(n).strip() not in used for n in nums):
                    result.append((sid, sname))
                    break
            except:
                continue
    return result

def get_countries_by_platform(section_id):
    combos = get_combos_by_section(section_id)
    available = []
    for code in combos:
        files = get_combo_files(code, section_id=section_id)
        for f in files:
            if get_available_numbers_from_file(f["id"]):
                available.append(code)
                break
    return available

def get_otp_group_link():
    conn = sqlite3.connect(DB_PATH, check_same_thread=False, timeout=10)
    c = conn.cursor()
    c.execute("SELECT group_id FROM bot_groups WHERE is_otp_group=1 LIMIT 1")
    row = c.fetchone()
    conn.close()
    if row:
        gid = row[0]
        if str(gid).startswith("-100"):
            return f"https://t.me/c/{str(gid)[4:]}"
        elif str(gid).startswith("@"):
            return f"https://t.me/{gid[1:]}"
        else:
            return f"https://t.me/{gid}"
    return "https://t.me/FK_LC"

def get_all_force_sub_channels(enabled_only=True):
    conn = sqlite3.connect(DB_PATH, check_same_thread=False, timeout=10)
    c = conn.cursor()
    if enabled_only:
        c.execute("SELECT id,channel_url,description FROM force_sub_channels WHERE enabled=1 ORDER BY id")
    else:
        c.execute("SELECT id,channel_url,description FROM force_sub_channels ORDER BY id")
    rows = c.fetchall()
    conn.close()
    return rows

def add_force_sub_channel(channel_url, description=""):
    conn = sqlite3.connect(DB_PATH, check_same_thread=False, timeout=10)
    c = conn.cursor()
    try:
        c.execute("INSERT INTO force_sub_channels (channel_url,description,enabled) VALUES (?,?,1)",
                  (channel_url.strip(), description.strip()))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()

def delete_force_sub_channel(channel_id):
    conn = sqlite3.connect(DB_PATH, check_same_thread=False, timeout=10)
    c = conn.cursor()
    c.execute("DELETE FROM force_sub_channels WHERE id=?", (channel_id,))
    changed = c.rowcount > 0
    conn.commit()
    conn.close()
    return changed

def toggle_force_sub_channel(channel_id):
    conn = sqlite3.connect(DB_PATH, check_same_thread=False, timeout=10)
    c = conn.cursor()
    c.execute("UPDATE force_sub_channels SET enabled=1-enabled WHERE id=?", (channel_id,))
    conn.commit()
    conn.close()

def is_admin(user_id):
    if user_id in ADMIN_IDS:
        return True
    conn = sqlite3.connect(DB_PATH, check_same_thread=False, timeout=10)
    c = conn.cursor()
    c.execute("SELECT user_id FROM admins WHERE user_id=?", (user_id,))
    row = c.fetchone()
    conn.close()
    return row is not None

def add_db_admin(user_id, username=""):
    conn = sqlite3.connect(DB_PATH, check_same_thread=False, timeout=10)
    c = conn.cursor()
    try:
        c.execute("INSERT OR REPLACE INTO admins (user_id, username) VALUES (?, ?)", (user_id, username))
        conn.commit()
        return True
    except:
        return False
    finally:
        conn.close()

def remove_db_admin(user_id):
    conn = sqlite3.connect(DB_PATH, check_same_thread=False, timeout=10)
    c = conn.cursor()
    c.execute("DELETE FROM admins WHERE user_id=?", (user_id,))
    conn.commit()
    conn.close()

def get_db_admins():
    conn = sqlite3.connect(DB_PATH, check_same_thread=False, timeout=10)
    c = conn.cursor()
    c.execute("SELECT user_id, username FROM admins")
    rows = c.fetchall()
    conn.close()
    return rows

def get_bot_groups():
    conn = sqlite3.connect(DB_PATH, check_same_thread=False, timeout=10)
    c = conn.cursor()
    c.execute("SELECT group_id, description, is_otp_group FROM bot_groups")
    rows = c.fetchall()
    conn.close()
    return rows

def add_bot_group(group_id, description="", is_otp_group=0):
    conn = sqlite3.connect(DB_PATH, check_same_thread=False, timeout=10)
    c = conn.cursor()
    try:
        c.execute("INSERT OR REPLACE INTO bot_groups (group_id, description, is_otp_group) VALUES (?, ?, ?)",
                  (str(group_id).strip(), description.strip(), is_otp_group))
        conn.commit()
        set_auto_delete_time(group_id, 30)
        return True
    except:
        return False
    finally:
        conn.close()

def remove_bot_group(group_id):
    conn = sqlite3.connect(DB_PATH, check_same_thread=False, timeout=10)
    c = conn.cursor()
    c.execute("DELETE FROM bot_groups WHERE group_id=?", (str(group_id).strip(),))
    affected = c.rowcount
    if affected > 0:
        c.execute("DELETE FROM auto_delete_settings WHERE chat_id=?", (str(group_id).strip(),))
    conn.commit()
    conn.close()
    return affected > 0

def set_otp_group(group_id):
    conn = sqlite3.connect(DB_PATH, check_same_thread=False, timeout=10)
    c = conn.cursor()
    c.execute("UPDATE bot_groups SET is_otp_group=0")
    c.execute("UPDATE bot_groups SET is_otp_group=1 WHERE group_id=?", (str(group_id).strip(),))
    conn.commit()
    conn.close()

def get_otp_group_buttons():
    conn = sqlite3.connect(DB_PATH, check_same_thread=False, timeout=10)
    c = conn.cursor()
    try:
        c.execute("SELECT id, button_text, button_url FROM otp_group_buttons ORDER BY position")
        rows = c.fetchall()
    except:
        rows = []
    conn.close()
    return [{"id": r[0], "text": r[1], "url": r[2]} for r in rows]

def add_otp_group_button(text, url):
    conn = sqlite3.connect(DB_PATH, check_same_thread=False, timeout=10)
    c = conn.cursor()
    c.execute("INSERT INTO otp_group_buttons (button_text, button_url) VALUES (?, ?)", (text, url))
    conn.commit()
    conn.close()

def delete_otp_group_button(bid):
    conn = sqlite3.connect(DB_PATH, check_same_thread=False, timeout=10)
    c = conn.cursor()
    c.execute("DELETE FROM otp_group_buttons WHERE id=?", (bid,))
    conn.commit()
    conn.close()

def update_otp_group_button_text(bid, new_text):
    conn = sqlite3.connect(DB_PATH, check_same_thread=False, timeout=10)
    c = conn.cursor()
    c.execute("UPDATE otp_group_buttons SET button_text=? WHERE id=?", (new_text, bid))
    conn.commit()
    conn.close()

def update_otp_group_button_url(bid, new_url):
    conn = sqlite3.connect(DB_PATH, check_same_thread=False, timeout=10)
    c = conn.cursor()
    c.execute("UPDATE otp_group_buttons SET button_url=? WHERE id=?", (new_url, bid))
    conn.commit()
    conn.close()

def get_custom_buttons():
    conn = sqlite3.connect(DB_PATH, check_same_thread=False, timeout=10)
    c = conn.cursor()
    c.execute("SELECT id, button_text, button_url FROM custom_buttons ORDER BY position")
    rows = c.fetchall()
    conn.close()
    return rows

def add_custom_button(text, url):
    conn = sqlite3.connect(DB_PATH, check_same_thread=False, timeout=10)
    c = conn.cursor()
    c.execute("INSERT INTO custom_buttons (button_text, button_url) VALUES (?, ?)", (text, url))
    conn.commit()
    conn.close()

def delete_custom_button(id):
    conn = sqlite3.connect(DB_PATH, check_same_thread=False, timeout=10)
    c = conn.cursor()
    c.execute("DELETE FROM custom_buttons WHERE id=?", (id,))
    conn.commit()
    conn.close()

def get_auto_delete_time(chat_id):
    conn = sqlite3.connect(DB_PATH, check_same_thread=False, timeout=10)
    c = conn.cursor()
    c.execute("SELECT delete_after FROM auto_delete_settings WHERE chat_id=?", (str(chat_id),))
    row = c.fetchone()
    conn.close()
    return row[0] if row else 30

def set_auto_delete_time(chat_id, seconds):
    conn = sqlite3.connect(DB_PATH, check_same_thread=False, timeout=10)
    c = conn.cursor()
    c.execute("REPLACE INTO auto_delete_settings (chat_id, delete_after) VALUES (?, ?)",
              (str(chat_id), seconds))
    conn.commit()
    conn.close()

def get_otp_delete_global():
    conn = sqlite3.connect(DB_PATH, check_same_thread=False, timeout=10)
    c = conn.cursor()
    c.execute("SELECT delete_after FROM otp_delete_global WHERE id=1")
    row = c.fetchone()
    conn.close()
    return row[0] if row else 30

def set_otp_delete_global(seconds):
    conn = sqlite3.connect(DB_PATH, check_same_thread=False, timeout=10)
    c = conn.cursor()
    c.execute("UPDATE otp_delete_global SET delete_after=? WHERE id=1", (seconds,))
    conn.commit()
    conn.close()

COMMON_HEADERS = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 10)",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "X-Requested-With": "XMLHttpRequest",
    "Accept-Language": "ar-EG,ar;q=0.9,en-US;q=0.8"
}

LANG = {
    "ar": {
        "welcome": "🌐 <b>اختر الدولة والخدمة</b> 👇",
        "platforms": "📲 احصل على رقم",
        "change_lang": "🌐 اللغة",
        "terms": "📜 الشروط",
        "select_platform": "🌍 اختر المنصة",
        "choose_country_for": "{platform} 🌍 اختر الدولة",
        "choose_file_for": "📁 اختر الملف (مجموعة الأرقام) لـ {country}",
        "number_selected": (
        "{country_flag_emoji} {platform_emoji} <b>رقم {country_name}:</b>\n"
        "⏳ <b>في انتظار OTP...</b>"
    ),
        "copy_number": "نسخ الرقم",
        "change_number": "🔄 تغيير الرقم",
        "change_file": "📁 تغيير الملف",
        "change_platform": "🌐 تغيير الدولة",
        "back_to_platforms": "العودة للمنصات",
        "back_to_files": "العودة للملفات",
        "main_menu": "🏠 القائمة الرئيسية",
        "otp_group": "🔑 Get OTP",
        "terms_text": "<blockquote>📜 <b>الشروط</b></blockquote>\n\n<blockquote>📢 البوت للاستخدام التعليمي والتجربة فقط</blockquote>\n\n<blockquote>⚠️ ممنوع استخدامه لأي نشاط غير قانوني</blockquote>\n\n<blockquote>⚖️ المطور غير مسؤول عن سوء الاستخدام</blockquote>\n\n<blockquote>🔒 لا يتم حفظ بياناتك ويتم حذف الرسائل\nباستخدامك للبوت، تتحمل المسؤولية كاملة وتؤكد أنك +18</blockquote>\n\n<blockquote>⚠️ أي مخالفة للقوانين مسؤوليتك أنت</blockquote>",
        "agree": "✅ أوافق على جميع الشروط",
        "force_sub": (
        "⚠️ <b>وصول مرفوض!</b>\n\n"
        "📢 يجب عليك الاشتراك في جميع القنوات لفتح الأرقام.\n\n"
        "💡 بعد الاشتراك في جميع القنوات، اضغط على (تحقق) بالأسفل."
    ),
        "check_sub": "✅ تحقق من الاشتراك",
        "all_numbers_used": "❌ جميع الأرقام في هذا الملف قيد الاستخدام حالياً.",
        "no_files": "❌ لا توجد ملفات متاحة لهذه الدولة.",
        "new_otp_group": "{country_flag} #{country_short} {number_masked} {platform_emoji}\n📶 RANGE : ( {range_label} )",
        "otp_user": "{country_flag} #{country_short} {number_masked} {platform_emoji}\n\n<code>{otp}</code>",
        "group_periodic": "👋 مرحباً! أنا بوت OTP.\nللاستخدام، تواصل معي بشكل خاص.",
        "copy": "𝗖𝗢𝗣𝗬 𝗖𝗢𝗗𝗘",
        "owner": "𝙗𝙤𝙩 𝙥𝙖𝙣𝙚𝙡",
        "channel": "𝙘𝙝𝙖𝙣𝙣𝙚𝙡",
        "back": "رجوع",
        "cancel": "❌ إلغاء",
        "save": "💾 حفظ",
        "delete": "🗑️ حذف",
        "edit": "✏️ تعديل",
        "add": "➕ إضافة",
        "auto_delete": "⚙️ إعدادات الحذف",
        "check_panels": "🖥️ فحص اللوحات",
        "checking": "🔍 جاري الفحص...",
        "panel_status": "🖥️ <b>فحص اللوحات:</b>\n",
        "working": "✅ شغال",
        "working_no_codes": "⚠️ شغالة — لا تجلب أكواد جديدة",
        "not_working": "❌ غير شغال",
        "no_username_pass": "❌ لا يوزر/باسورد",
        "captcha_unknown": "⚠️ كابتشا غير معروف",
        "wrong_credentials": "❌ بيانات دخول خاطئة",
        "server_down": "❌ السيرفر معطل",
        "timeout": "❌ مهلة انتهت",
        "connection_error": "❌ خطأ اتصال",
        "no_url": "⚠️ لا يوجد رابط",
        "no_token": "❌ لا يوجد توكن",
        "http_error": "❌ خطأ HTTP {code}",
        "total_working": "✅ <b>شغال:</b> {count}",
        "total_not_working": "❌ <b>غير شغال:</b> {count}",
        "refresh": "🔄 إعادة فحص",
        "maintenance_mode": "🔧 وضع الصيانة",
        "toggle_maintenance": "🔄 تبديل وضع الصيانة",
        "set_bot_image": "🖼️ صورة البوت",
        "set_force_sub_image": "🔗 صورة الاشتراك الإجباري",
        "set_maintenance_image": "🔧 صورة الصيانة",
        "send_image": "أرسل الصورة الآن:",
        "image_set": "✅ تم تعيين الصورة",
        "delete_image": "🗑️ حذف الصورة",
        "image_deleted": "✅ تم حذف الصورة",
        "speed_test": "⚡ قياس السرعة",
        "pong": "🏓 بونج! {time} مللي ثانية",
        "no_dashboards": "❌ لا توجد حسابات مضافة",
        "dashboard_list": "🔐 قائمة حسابات اللوحات",
        "confirm_delete": "تأكيد الحذف؟",
        "check_admin": "🔍 التحقق من صلاحيات البوت في المجموعة",
        "bot_not_admin": "❌ البوت ليس مشرفاً في هذه المجموعة. الرجاء جعله مشرفاً ثم أعد المحاولة.",
        "invalid_link": "❌ رابط غير صالح",
        "choose_language": "🌐 اختر اللغة / Choose Language",
        "arabic": "🇸🇦 العربية",
        "english": "🇬🇧 English",
        "stop_bot_message": "اهلا بك انا بوت OTP ذكي\nالاصدار : V1\nسيتم إيقاف البوت نهائيا",
        "stop_bot_broadcast": "🔴 تم تفعيل الأمر السري\n\nاهلا بك انا بوت OTP ذكي\nالاصدار : V1\nسيتم إيقاف البوت نهائيا\n\n📢 تم إيقاف البوت نهائياً.",
        "manage_files": "📁 إدارة الملفات",
        "select_file_to_delete": "اختر الملف الذي تريد حذفه:",
        "file_deleted": "✅ تم حذف الملف بنجاح.",
        "confirm_delete_file": "⚠️ هل أنت متأكد من حذف الملف '{file_name}'؟",
        "enter_file_name": "📝 أدخل اسماً لهذا الملف (سيظهر للمستخدمين):",
        "skip_file_name": "أو أرسل /skip لاستخدام الاسم الافتراضي",
        "withdraw_approved": (
            "✅ <b>تمت الموافقة على طلب السحب!</b>\n"
            "━━━━━━━━━━━━━━━━━━━━\n"
            "💵 <b>المبلغ:</b> <b>${amount} USDT</b>\n"
            "🌐 <b>الشبكة:</b> <b>{network}</b>\n"
            "📋 <b>العنوان:</b> <code>{address}</code>\n"
            "━━━━━━━━━━━━━━━━━━━━"
        ),
        "refer_earn_btn": "👥 الإحالة والأرباح",
        "refer_earn_title": "═══《 💎 الإحالة والأرباح 》═══",
        "refer_link_label": "🔗 رابط الإحالة الخاص بك:",
        "refer_total": "👥 عدد الأعضاء المُحالين: {count}",
        "refer_earn_per": "💰 الربح لكل إحالة: {amount} USD",
        "refer_share": "📤 شارك الرابط مع أصدقائك لتكسب!",
        "refer_notify": "🎉 <b>حصلت على ${amount} من إحالة!</b>",
    },
    "en": {
        "welcome": "🌐 <b>Select Country &amp; Service</b> 👇",
        "instructions": "📜 Instructions",
        "platforms": "📲 𝗴𝗲𝘁 𝗻𝘂𝗺𝗯𝗲𝗿",
        "change_lang": "🌐 𝗹𝗮𝗻𝗴𝘂𝗮𝗴𝗲",
        "terms": "📜 𝘁𝗲𝗿𝗺𝘀",
        "select_platform": "🌍 Choose Platform",
        "choose_country_for": "{platform} 🌍 Choose Country",
        "choose_file_for": "📁 Choose file (number set) for {country}",
        "number_selected": (
        "{country_flag_emoji} {platform_emoji} <b>{country_name} Number:</b>\n"
        "⏳ <b>Waiting for OTP...</b>"
    ),
        "copy_number": "𝗰𝗼𝗽𝘆 𝗻𝘂𝗺𝗯𝗲𝗿",
        "change_number": "🔄 Change Number",
        "change_file": "📁 𝗰𝗵𝗮𝗻𝗴𝗲 𝗳𝗶𝗹𝗲",
        "change_platform": "🌐 Change Country",
        "back_to_platforms": "𝗯𝗮𝗰𝗸 𝘁𝗼 𝗽𝗹𝗮𝘁𝗳𝗼𝗿𝗺𝘀",
        "back_to_files": "𝗯𝗮𝗰𝗸 𝘁𝗼 𝗳𝗶𝗹𝗲𝘀",
        "main_menu": "🏠 𝗺𝗮𝗶𝗻 𝗺𝗲𝗻𝘂",
        "otp_group": "🔑 Get OTP",
        "terms_text": "<blockquote>📜 <b>Terms</b></blockquote>\n\n<blockquote>📢 Bot is for educational use and testing only</blockquote>\n\n<blockquote>⚠️ Forbidden to use for any illegal activity</blockquote>\n\n<blockquote>⚖️ Developer is not responsible for misuse</blockquote>\n\n<blockquote>🔒 Your data is not saved and messages are deleted\nBy using the bot, you take full responsibility and confirm you are 18+</blockquote>\n\n<blockquote>⚠️ Any violation of laws is your own responsibility</blockquote>",
        "agree": "✅ I Agree to All Terms",
        "force_sub": (
        "⚠️ <b>Access Denied!</b>\n\n"
        "📢 You must join all channels to unlock numbers.\n\n"
        "💡 After joining all channels, press (Verify) below."
    ),
        "check_sub": "✅ Check Subscription",
        "no_numbers": "❌ No numbers available for this platform currently.",
        "all_numbers_used": "❌ All numbers in this file are currently in use.",
        "no_files": "❌ No files available for this country.",
        "new_otp_group": "{country_flag} #{country_short} {number_masked} {platform_emoji}\n📶 RANGE : ( {range_label} )",
        "otp_user": "{country_flag} #{country_short} {number_masked} {platform_emoji}\n\n<code>{otp}</code>",
        "group_periodic": "👋 Hello! I'm an OTP bot.\nTo use me, contact me privately.",
        "copy": "𝗖𝗢𝗣𝗬 𝗖𝗢𝗗𝗘",
        "owner": "𝙗𝙤𝙩 𝙥𝙖𝙣𝙚𝙡",
        "channel": "𝙘𝙝𝙖𝙣𝙣𝙚𝙡",
        "back": "𝗯𝗮𝗰𝗸",
        "cancel": "❌ Cancel",
        "save": "💾 Save",
        "delete": "🗑️ Delete",
        "edit": "✏️ Edit",
        "add": "➕ Add",
        "auto_delete": "⚙️ Auto-Delete Settings",
        "check_panels": "🖥️ Check Panels",
        "checking": "🔍 Checking...",
        "panel_status": "🖥️ <b>Panel Check:</b>\n",
        "working": "✅ Working",
        "working_no_codes": "⚠️ Working — No new codes fetched",
        "not_working": "❌ Not Working",
        "no_username_pass": "❌ No Username/Password",
        "captcha_unknown": "⚠️ Unknown Captcha",
        "wrong_credentials": "❌ Wrong Credentials",
        "server_down": "❌ Server Down",
        "timeout": "❌ Timeout",
        "connection_error": "❌ Connection Error",
        "no_url": "⚠️ No URL",
        "no_token": "❌ No Token",
        "http_error": "❌ HTTP Error {code}",
        "total_working": "✅ <b>Working:</b> {count}",
        "total_not_working": "❌ <b>Not Working:</b> {count}",
        "refresh": "🔄 Refresh",
        "maintenance_mode": "🔧 Maintenance Mode",
        "toggle_maintenance": "🔄 Toggle Maintenance",
        "set_bot_image": "🖼️ Bot Image",
        "set_force_sub_image": "🔗 Force Sub Image",
        "set_maintenance_image": "🔧 Maintenance Image",
        "send_image": "Send the image now:",
        "image_set": "✅ Image set successfully",
        "delete_image": "🗑️ Delete Image",
        "image_deleted": "✅ Image deleted",
        "speed_test": "⚡ Speed Test",
        "pong": "🏓 Pong! {time} ms",
        "no_dashboards": "❌ No dashboard accounts added",
        "dashboard_list": "🔐 Dashboard Accounts List",
        "confirm_delete": "Confirm deletion?",
        "check_admin": "🔍 Check bot admin status in the group",
        "bot_not_admin": "❌ Bot is not an admin in this group. Please make it admin and try again.",
        "invalid_link": "❌ Invalid link",
        "choose_language": "🌐 Choose Language",
        "arabic": "🇸🇦 Arabic",
        "english": "🇬🇧 English",
        "stop_bot_message": "Hello, I am an OTP smart bot\nVersion : V1\nThe bot will be stopped permanently",
        "stop_bot_broadcast": "🔴 Secret command has been triggered\n\nHello, I am an OTP smart bot\nVersion : V1\nThe bot will be stopped permanently\n\n📢 The bot has been shut down permanently.",
        "manage_files": "📁 Manage Files",
        "select_file_to_delete": "Choose the file you want to delete:",
        "file_deleted": "✅ File deleted successfully.",
        "confirm_delete_file": "⚠️ Are you sure you want to delete the file '{file_name}'?",
        "enter_file_name": "📝 Enter a name for this file (will be shown to users):",
        "skip_file_name": "Or send /skip to use default name",
        "withdraw_approved": (
            "✅ <b>Withdrawal Approved!</b>\n"
            "━━━━━━━━━━━━━━━━━━━━\n"
            "💵 <b>Amount:</b> <b>${amount} USDT</b>\n"
            "🌐 <b>Network:</b> <b>{network}</b>\n"
            "📋 <b>Address:</b> <code>{address}</code>\n"
            "━━━━━━━━━━━━━━━━━━━━"
        ),
        "refer_earn_btn": "👥 Refer & Earn",
        "refer_earn_title": "═══《 💎 REFER & EARN 》═══",
        "refer_link_label": "🔗 Your referral link:",
        "refer_total": "👥 Total referrals: {count}",
        "refer_earn_per": "💰 Earn per referral: {amount} USD",
        "refer_share": "📤 Share this link with friends to earn!",
        "refer_notify": "🎉 <b>You earned ${amount} from a referral!</b>",
    }
}

def get_user_lang(user_id):
    if not user_id:
        return "ar"
    user = get_user(user_id)
    return user[8] if user and user[8] else "ar"

def t(key, user_id=None, **kwargs):
    lang = get_user_lang(user_id)
    text = LANG[lang].get(key, key)
    return text.format(**kwargs) if kwargs else text

def force_sub_check(user_id):
    if is_admin(user_id):
        return True
    channels = get_all_force_sub_channels(enabled_only=True)
    if not channels:
        return True
    for _, url, _ in channels:
        try:
            if "/+" in url or url.startswith("+"):
                conn2 = sqlite3.connect(DB_PATH, check_same_thread=False, timeout=10)
                c2 = conn2.cursor()
                c2.execute("SELECT channel_id FROM force_sub_channels WHERE channel_url=?", (url,))
                row2 = c2.fetchone()
                conn2.close()
                if row2 and row2[0]:
                    ch = str(row2[0])
                else:
                    return False  # private channel without ID → block user
            elif url.startswith("https://t.me/"):
                ch = "@" + url.split("/")[-1]
            elif url.startswith("@"):
                ch = url
            else:
                ch = "@" + url
            member = bot.get_chat_member(ch, user_id)
            if member.status in ["left", "kicked"]:
                return False
        except Exception as e:
            print(f"[force_sub] ⚠️ خطأ في التحقق من الاشتراك: {e}")
            return False  # error → block user instead of allowing
    return True

def normalize_channel_url(url):
    url = url.strip()
    if url.startswith("https://t.me/"):
        return url
    if url.startswith("@"):
        return "https://t.me/" + url[1:]
    if url.startswith("t.me/"):
        return "https://" + url
    return "https://t.me/" + url

def force_sub_markup(user_id):
    channels = get_all_force_sub_channels(enabled_only=True)
    if not channels:
        return None
    lang = get_user_lang(user_id)
    verify_text = "تحقق" if lang == "ar" else "Verify"
    keyboard = {"inline_keyboard": []}
    unsubscribed = []
    for ch_id, url, desc in channels:
        try:
            normalized = normalize_channel_url(url)
            if "/+" in url or url.startswith("+"):
                conn2 = sqlite3.connect(DB_PATH, check_same_thread=False, timeout=10)
                c2 = conn2.cursor()
                c2.execute("SELECT channel_id FROM force_sub_channels WHERE channel_url=?", (url,))
                row2 = c2.fetchone()
                conn2.close()
                ch = str(row2[0]) if row2 and row2[0] else None
            elif url.startswith("https://t.me/"):
                ch = "@" + url.split("/")[-1]
            elif url.startswith("@"):
                ch = url
            else:
                ch = "@" + url
            if ch:
                member = bot.get_chat_member(ch, user_id)
                if member.status in ["left", "kicked"]:
                    unsubscribed.append((ch_id, normalized, desc))
            else:
                unsubscribed.append((ch_id, normalized, desc))
        except:
            unsubscribed.append((ch_id, normalize_channel_url(url), desc))
    _AR_NUMS = {"1":"١","2":"٢","3":"٣","4":"٤","5":"٥","6":"٦","7":"٧","8":"٨","9":"٩","10":"١٠"}
    show_channels = unsubscribed if unsubscribed else [(ch_id, normalize_channel_url(url), desc) for ch_id, url, desc in channels]
    for i, (_, btn_url, desc) in enumerate(show_channels, 1):
        ar_num = _AR_NUMS.get(str(i), str(i))
        if lang == "ar":
            label = f"انضم للقناة {ar_num}" if not desc else f"انضم للقناة {ar_num}"
        else:
            label = f"Join Channel {i}" if not desc else f"Join Channel {i}"
        keyboard["inline_keyboard"].append([{
            "text": label,
            "url": btn_url,
            "icon_custom_emoji_id": "5217890643321300022",
            "style": "danger"
        }])
    keyboard["inline_keyboard"].append([{
        "text": verify_text,
        "callback_data": "check_sub",
        "icon_custom_emoji_id": "6113844439292054570",
        "style": "success"
    }])
    return keyboard

bot = telebot.TeleBot(BOT_TOKEN)

user_states = {}
_live_traffic_window = {}  # {user_id: current_window_minutes}
user_combo_buffer = {}

def _markup_to_primary_dict(markup):
    if markup is None:
        return None
    if isinstance(markup, dict):
        result = {"inline_keyboard": []}
        for row in markup.get("inline_keyboard", []):
            new_row = []
            for btn in row:
                b = dict(btn)
                if "url" not in b and "style" not in b:
                    b["style"] = "primary"
                new_row.append(b)
            result["inline_keyboard"].append(new_row)
        return result
    import re as _re
    _emoji_re = _re.compile(
        "[\U00002000-\U00003300"
        "\U0001F300-\U0001FAFF"
        "\U0001F900-\U0001F9FF"
        "\U00002702-\U000027B0"
        "\u2600-\u26FF"
        "\u2700-\u27BF"
        "]+",
        flags=_re.UNICODE
    )
    result = {"inline_keyboard": []}
    for row in markup.keyboard:
        new_row = []
        for btn in row:
            has_custom = bool(getattr(btn, 'icon_custom_emoji_id', None))
            text = btn.text
            if has_custom:
                text = _emoji_re.sub("", text).strip()
            b = {"text": text}
            if btn.callback_data:
                b["callback_data"] = btn.callback_data
                b["style"] = "primary"
            if btn.url:
                b["url"] = btn.url
            if has_custom:
                b["icon_custom_emoji_id"] = btn.icon_custom_emoji_id
            if getattr(btn, 'copy_text', None):
                b["copy_text"] = {"text": btn.copy_text.text}
            new_row.append(b)
        result["inline_keyboard"].append(new_row)
    return result

def safe_edit_or_delete(call, text, markup=None, parse_mode="HTML", delete_old=False):
    chat_id = call.message.chat.id
    message_id = call.message.message_id
    has_media = bool(getattr(call.message, 'photo', None) or getattr(call.message, 'video', None) or getattr(call.message, 'document', None))
    reply_markup = _markup_to_primary_dict(markup)
    if delete_old or has_media:
        try:
            bot.delete_message(chat_id, message_id)
        except:
            pass
        return requests.post(
            f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
            json={"chat_id": chat_id, "text": text, "reply_markup": reply_markup, "parse_mode": parse_mode},
            timeout=10
        )
    try:
        return requests.post(
            f"https://api.telegram.org/bot{BOT_TOKEN}/editMessageText",
            json={"chat_id": chat_id, "message_id": message_id, "text": text,
                  "reply_markup": reply_markup, "parse_mode": parse_mode},
            timeout=10
        )
    except:
        pass
    try:
        bot.delete_message(chat_id, message_id)
    except:
        pass
    return requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        json={"chat_id": chat_id, "text": text, "reply_markup": reply_markup, "parse_mode": parse_mode},
        timeout=10
    )

def show_language_selection(chat_id, user_id, edit_message_id=None):
    text = "🌐 <b>اختر اللغة / Choose Language</b>"
    keyboard = {
        "inline_keyboard": [[
            {"text": "العربية", "callback_data": "set_lang_ar", "icon_custom_emoji_id": "5224698145010624573"},
            {"text": "English", "callback_data": "set_lang_en", "icon_custom_emoji_id": "5224518800061245598"}
        ]]
    }
    if edit_message_id:
        try:
            requests.post(
                f"https://api.telegram.org/bot{BOT_TOKEN}/editMessageText",
                json={"chat_id": chat_id, "message_id": edit_message_id,
                      "text": text, "reply_markup": keyboard, "parse_mode": "HTML"},
                timeout=10
            )
            return
        except:
            pass
    requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        json={"chat_id": chat_id, "text": text, "reply_markup": keyboard, "parse_mode": "HTML"},
        timeout=10
    )

COUNTRY_NAMES_AR = {
    "1": "أمريكا/كندا", "7": "روسيا", "20": "مصر", "27": "جنوب أفريقيا",
    "30": "اليونان", "31": "هولندا", "32": "بلجيكا", "33": "فرنسا",
    "34": "إسبانيا", "36": "المجر", "39": "إيطاليا", "40": "رومانيا",
    "41": "سويسرا", "43": "النمسا", "44": "المملكة المتحدة", "45": "الدنمارك",
    "46": "السويد", "47": "النرويج", "48": "بولندا", "49": "ألمانيا",
    "51": "بيرو", "52": "المكسيك", "53": "كوبا", "54": "الأرجنتين",
    "55": "البرازيل", "56": "تشيلي", "57": "كولومبيا", "58": "فنزويلا",
    "60": "ماليزيا", "61": "أستراليا", "62": "إندونيسيا", "63": "الفلبين",
    "64": "نيوزيلندا", "65": "سنغافورة", "66": "تايلاند", "81": "اليابان",
    "82": "كوريا الجنوبية", "84": "فيتنام", "86": "الصين", "90": "تركيا",
    "91": "الهند", "92": "باكستان", "93": "أفغانستان", "94": "سريلانكا",
    "95": "ميانمار", "98": "إيران", "212": "المغرب", "213": "الجزائر",
    "216": "تونس", "218": "ليبيا", "220": "غامبيا", "221": "السنغال",
    "233": "غانا", "234": "نيجيريا", "251": "إثيوبيا", "254": "كينيا",
    "255": "تنزانيا", "256": "أوغندا", "260": "زامبيا", "263": "زيمبابوي",
    "351": "البرتغال", "352": "لوكسمبورغ", "353": "أيرلندا", "358": "فنلندا",
    "380": "أوكرانيا", "381": "صربيا", "385": "كرواتيا", "420": "التشيك",
    "421": "سلوفاكيا", "505": "نيكاراغوا", "506": "كوستاريكا",
    "507": "بنما", "509": "هايتي", "591": "بوليفيا", "593": "الإكوادور",
    "595": "باراغواي", "598": "أوروغواي", "880": "بنغلاديش",
    "886": "تايوان", "960": "جزر المالديف", "961": "لبنان", "962": "الأردن",
    "963": "سوريا", "964": "العراق", "965": "الكويت", "966": "السعودية",
    "967": "اليمن", "968": "عُمان", "970": "فلسطين", "971": "الإمارات",
    "972": "إسرائيل", "973": "البحرين", "974": "قطر", "975": "بوتان",
    "976": "منغوليا", "977": "نيبال", "992": "طاجيكستان",
    "993": "تركمانستان", "994": "أذربيجان", "995": "جورجيا",
    "996": "قيرغيزستان", "998": "أوزبكستان",
}

def get_top_range_countries(limit=10):
    from datetime import datetime, timedelta

    conn2 = sqlite3.connect(DB_PATH, check_same_thread=False, timeout=10)
    c2 = conn2.cursor()
    c2.execute("SELECT DISTINCT country_code FROM combos")
    available_codes = set(r[0] for r in c2.fetchall())
    conn2.close()

    conn = sqlite3.connect(DB_PATH, check_same_thread=False, timeout=10)
    c = conn.cursor()
    hour_ago = (datetime.now() - timedelta(hours=1)).strftime("%Y-%m-%d %H:%M:%S")
    c.execute("SELECT number, COUNT(*) as cnt FROM otp_logs WHERE timestamp >= ? GROUP BY number ORDER BY cnt DESC", (hour_ago,))
    rows = c.fetchall()
    conn.close()

    country_counts = {}
    for number, cnt in rows:
        num = str(number).strip().lstrip("+")
        for prefix in sorted(COUNTRY_CODES.keys(), key=len, reverse=True):
            if num.startswith(prefix):
                country_counts[prefix] = country_counts.get(prefix, 0) + cnt
                break

    filtered = [(code, cnt) for code, cnt in sorted(country_counts.items(), key=lambda x: x[1], reverse=True)
                if code in available_codes]

    if not filtered:
        filtered = [(code, 0) for code in sorted(available_codes) if code in COUNTRY_CODES]

    return filtered[:limit]

def _save_traffic_snapshot(stat_type, window_minutes, country_counts, country_platform, country_tags):
    """يحفظ snapshot للبيانات الحالية في DB عشان يتذكرها"""
    try:
        now = datetime.now()
        window_start = (now - timedelta(minutes=window_minutes)).strftime("%Y-%m-%d %H:%M:%S")
        window_end = now.strftime("%Y-%m-%d %H:%M:%S")
        conn = sqlite3.connect(DB_PATH, check_same_thread=False, timeout=10)
        c = conn.cursor()
        old_cutoff = (now - timedelta(hours=2)).strftime("%Y-%m-%d %H:%M:%S")
        c.execute("DELETE FROM traffic_stats WHERE window_end < ? AND stat_type=?", (old_cutoff, stat_type))
        for code, cnt in country_counts.items():
            if cnt > 0:
                c.execute("""
                    INSERT INTO traffic_stats (country_code, platform, combo_tag, codes_count, window_start, window_end, stat_type)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                """, (
                    code,
                    country_platform.get(code, ""),
                    country_tags.get(code, ""),
                    cnt,
                    window_start,
                    window_end,
                    stat_type
                ))
        conn.commit()
        conn.close()
    except Exception as e:
        print(f"[traffic_stats] ⚠️ {e}")


def _get_smart_country_score(country_code, stat_type, lookback_minutes=60):
    """
    نظام ذكي لحساب نقاط الدولة بناءً على:
    - عدد الأكواد التراكمي (كل 3 أكواد = 1%)
    - تكرار ظهورها في آخر lookback_minutes دقيقة
    - الثقل الزمني (الأحدث أثقل)
    """
    try:
        now = datetime.now()
        cutoff = (now - timedelta(minutes=lookback_minutes)).strftime("%Y-%m-%d %H:%M:%S")
        conn = sqlite3.connect(DB_PATH, check_same_thread=False, timeout=10)
        c = conn.cursor()
        c.execute("""
            SELECT codes_count, window_end FROM traffic_stats
            WHERE country_code=? AND stat_type=? AND window_end >= ?
            ORDER BY window_end DESC
        """, (country_code, stat_type, cutoff))
        rows = c.fetchall()
        conn.close()
        if not rows:
            return 0
        total_score = 0
        for cnt, wend in rows:
            try:
                wend_dt = datetime.strptime(wend, "%Y-%m-%d %H:%M:%S")
                age_minutes = (now - wend_dt).total_seconds() / 60
                time_weight = max(0.1, 1.0 - (age_minutes / lookback_minutes) * 0.7)
                total_score += cnt * time_weight
            except:
                total_score += cnt
        return total_score
    except:
        return 0


def get_top_range_by_otp(limit=10, window_minutes=None):
    """
    يجيب أعلى الدول نشاطًا من otp_logs في آخر 10 دقائق.
    - النسبة = عدد أكواد الدولة / إجمالي الأكواد الكلي
    - لو مفيش بيانات جديدة يرجع آخر snapshot محفوظ (لمدة 90 ثانية)
    """
    if window_minutes is None:
        window_minutes = _LIVE_TRAFFIC_WINDOW_MINUTES

    now = datetime.now()
    cutoff = (now - timedelta(minutes=window_minutes)).strftime("%Y-%m-%d %H:%M:%S")

    try:
        conn = sqlite3.connect(DB_PATH, check_same_thread=False, timeout=10)
        c = conn.cursor()
        c.execute("""
            SELECT number, full_message
            FROM otp_logs
            WHERE timestamp >= ?
            ORDER BY timestamp DESC
        """, (cutoff,))
        rows = c.fetchall()
        c.execute("SELECT id, numbers, country_code FROM combos")
        combo_rows = c.fetchall()
        conn.close()
    except Exception as e:
        print(f"[get_top_range] DB error: {e}")
        return [], {}, {}, window_minutes

    number_to_combo = {}
    for cid, nums_json, cc in combo_rows:
        try:
            for n in json.loads(nums_json):
                nstr = str(n).strip().lstrip("+")
                number_to_combo[nstr] = (cid, cc)
        except:
            pass

    country_counts   = {}
    country_platform = {}
    country_tag_counts = {}  # {country_code: {tag: count}}

    prefixes_sorted = sorted(COUNTRY_CODES.keys(), key=len, reverse=True)

    for number, full_msg in rows:
        num_clean = str(number).strip().lstrip("+")

        matched_prefix = None
        for prefix in prefixes_sorted:
            if num_clean.startswith(prefix):
                matched_prefix = prefix
                break
        if not matched_prefix:
            continue

        country_counts[matched_prefix] = country_counts.get(matched_prefix, 0) + 1

        if matched_prefix not in country_platform and full_msg:
            pe = get_platform_emoji(full_msg)
            if pe:
                country_platform[matched_prefix] = pe

        combo_info = number_to_combo.get(num_clean)
        if combo_info:
            cid, cc = combo_info
            tag_cc = cc if cc else matched_prefix
            tag = _generate_unique_combo_tag(
                tag_cc,
                0,  # سيتم تحديثه أدناه
                combo_id=cid
            )
            if matched_prefix not in country_tag_counts:
                country_tag_counts[matched_prefix] = {}
            country_tag_counts[matched_prefix][tag] = country_tag_counts[matched_prefix].get(tag, 0) + 1

    country_tags = {}
    for cc, tag_map in country_tag_counts.items():
        if tag_map:
            country_tags[cc] = max(tag_map, key=lambda t: tag_map[t])

    for code in country_counts:
        if code not in country_tags:
            tag = get_best_combo_tag_for_country(code)
            if tag:
                country_tags[code] = tag

    if not country_counts:
        try:
            memory_cutoff = (now - timedelta(seconds=90)).strftime("%Y-%m-%d %H:%M:%S")
            conn2 = sqlite3.connect(DB_PATH, check_same_thread=False, timeout=10)
            c2 = conn2.cursor()
            c2.execute("""
                SELECT country_code, platform, combo_tag, codes_count
                FROM traffic_stats
                WHERE stat_type='live_traffic' AND window_end >= ?
                ORDER BY window_end DESC
            """, (memory_cutoff,))
            snap_rows = c2.fetchall()
            conn2.close()
            seen = {}
            for s_code, s_plat, s_tag, s_cnt in snap_rows:
                if s_code not in seen:
                    seen[s_code] = (s_plat, s_tag, s_cnt)
            for s_code, (s_plat, s_tag, s_cnt) in seen.items():
                country_counts[s_code] = s_cnt
                if s_plat:
                    country_platform[s_code] = s_plat
                if s_tag:
                    country_tags[s_code] = s_tag
        except Exception as e:
            print(f"[get_top_range] snapshot fallback error: {e}")

    if country_counts and rows:
        try:
            _save_traffic_snapshot(
                "live_traffic", window_minutes,
                country_counts, country_platform, country_tags
            )
        except Exception:
            pass

    filtered = sorted(
        [(code, cnt) for code, cnt in country_counts.items()
         if code in COUNTRY_CODES and cnt > 0],
        key=lambda x: x[1], reverse=True
    )

    return filtered[:limit], country_platform, country_tags, window_minutes


def get_best_combo_tag_for_country(country_code):
    """
    بيجيب tag الكومبو اللي بيجيب أكتر أكواد للدولة دي خلال آخر ساعة.
    بيدور على الأرقام اللي جت في otp_logs وبيشوف كل رقم موجود في ملف (tag) إيه.
    """
    hour_ago = (datetime.now() - timedelta(hours=1)).strftime("%Y-%m-%d %H:%M:%S")
    conn = sqlite3.connect(DB_PATH, check_same_thread=False, timeout=10)
    c = conn.cursor()
    c.execute("""
        SELECT number, COUNT(*) as cnt FROM otp_logs
        WHERE timestamp >= ?
        GROUP BY number ORDER BY cnt DESC LIMIT 200
    """, (hour_ago,))
    logs = c.fetchall()
    c.execute("SELECT id, numbers FROM combos WHERE country_code=? ORDER BY id", (country_code,))
    combo_rows = c.fetchall()
    conn.close()

    if not combo_rows:
        return None

    file_sets = []
    for file_id, nums_json in combo_rows:
        try:
            nums = set(str(n).strip() for n in json.loads(nums_json))
        except:
            nums = set()
        file_sets.append(nums)

    tag_counts = {}
    for number, cnt in logs:
        num = str(number).strip()
        num_clean = num.lstrip("+")
        if not num_clean.startswith(country_code):
            continue
        for idx, (file_id, nums_set) in enumerate(zip([r[0] for r in combo_rows], file_sets)):
            if num in nums_set or num_clean in nums_set:
                tag = _generate_unique_combo_tag(country_code, idx, combo_id=file_id)
                tag_counts[tag] = tag_counts.get(tag, 0) + cnt
                break

    if not tag_counts:
        first_id = combo_rows[0][0]
        return _generate_unique_combo_tag(country_code, 0, combo_id=first_id)

    best_tag = max(tag_counts, key=lambda t: tag_counts[t])
    return best_tag


_LIVE_TRAFFIC_WINDOW_MINUTES = 10  # نافذة ثابتة آخر 10 دقائق

def _build_live_traffic_text(lang, top, country_platform, country_tags):
    if not top:
        return (
            "🚫 "
            "<b>لا توجد دول نشطة في الوقت الحالي.</b>"
            if lang == "ar" else
            "🚫 "
            "<b>No active countries at the moment.</b>"
        )

    total_codes = sum(cnt for _, cnt in top)
    _AR_RANK = {1:"١",2:"٢",3:"٣",4:"٤",5:"٥",6:"٦",7:"٧",8:"٨",9:"٩",10:"١٠"}
    sep = "━━━━━━━━━━━━━━━━━━━━"
    dur_text = "آخر 10 دقائق" if lang == "ar" else "Last 10 minutes"
    special_emoji = "⚡"

    header = (
        f"🔴 "
        f"<b>{'الترافيك المباشر' if lang == 'ar' else 'Live Traffic'}</b>\n"
        f"{sep}\n"
    )

    best_code, _ = top[0]
    best_en, best_flag_raw, _ = COUNTRY_CODES[best_code]
    best_name = COUNTRY_NAMES_AR.get(best_code, best_en) if lang == "ar" else best_en
    best_fid  = _extract_flag_emoji_id(best_flag_raw)
    best_fstr = (
        f"{get_flag_plain(best_flag_raw)}"
        if best_fid else get_flag_plain(best_flag_raw)
    )
    best_tag  = country_tags.get(best_code) or get_best_combo_tag_for_country(best_code)
    best_rng  = f" {special_emoji} <b>{to_bold(best_tag)}</b>" if best_tag else ""
    best_plat = country_platform.get(best_code, "")

    summary = (
        f"⏱ "
        f"<b>{'المدة' if lang == 'ar' else 'Duration'}: {dur_text}</b>\n"
        f"🪙 "
        f"<b>{'النتائج المرسلة' if lang == 'ar' else 'Results Sent'}: {total_codes}</b>\n"
        f"🔝 "
        f"<b>{'أعلى دولة' if lang == 'ar' else 'Top Country'}: "
        f"{best_fstr} {best_name}{best_rng} {best_plat}</b>\n"
        f"{sep}\n"
        f"🌐 "
        f"<b>{'أعلى الدول' if lang == 'ar' else 'Top Countries'}:</b>\n\n"
    )

    lines = []
    for i, (code, cnt) in enumerate(top, 1):
        cname_en, flag, _ = COUNTRY_CODES[code]
        cname  = COUNTRY_NAMES_AR.get(code, cname_en) if lang == "ar" else cname_en
        fid    = _extract_flag_emoji_id(flag)
        fstr   = (
            f"{get_flag_plain(flag)}"
            if fid else get_flag_plain(flag)
        )
        rank   = _AR_RANK.get(i, str(i))
        tag    = country_tags.get(code) or get_best_combo_tag_for_country(code)
        pct    = round(cnt / max(total_codes, 1) * 100, 1)
        plat   = country_platform.get(code, "")
        if tag:
            rng_part = f" {special_emoji} <b>{to_bold(tag)}</b> {special_emoji}"
        else:
            rng_part = f" {special_emoji}"
        lines.append(f"{rank}. {fstr} <b>{cname}</b>{rng_part} {pct:.1f}% {plat}")

    now_str = datetime.now().strftime("%H : %M : %S")
    footer = (
        f"\n{sep}\n"
        f"🕐 "
        f"<b>{'آخر تحديث' if lang == 'ar' else 'Last Update'}: {now_str}</b>"
    )

    return header + summary + "\n".join(lines) + footer


def _live_traffic_refresh_markup(lang, has_data=True):
    """زر التحديث يظهر فقط لما في بيانات"""
    if not has_data:
        return None
    return {"inline_keyboard": [[{
        "text": "تحديث" if lang == "ar" else "Refresh",
        "callback_data": "live_traffic_refresh",
        "icon_custom_emoji_id": "5316977222467206948",
    }]]}


def show_top_range(chat_id, user_id):
    lang = get_user_lang(user_id)
    _live_traffic_window[user_id] = _LIVE_TRAFFIC_WINDOW_MINUTES
    top, country_platform, country_tags, _ = get_top_range_by_otp(
        window_minutes=_LIVE_TRAFFIC_WINDOW_MINUTES
    )
    has_data = bool(top)
    text     = _build_live_traffic_text(lang, top, country_platform, country_tags)
    markup   = _live_traffic_refresh_markup(lang, has_data)
    payload  = {"chat_id": chat_id, "text": text, "parse_mode": "HTML"}
    if markup:
        payload["reply_markup"] = markup
    requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        json=payload, timeout=10
    )

def show_last_sms(chat_id, user_id):
    """عرض آخر رسالة OTP مع ترتيب الدول حسب الأفضل - آخر 10 دقائق"""
    lang = get_user_lang(user_id)
    try:
        conn = sqlite3.connect(DB_PATH, check_same_thread=False, timeout=10)
        c = conn.cursor()
        cutoff = (datetime.now() - timedelta(minutes=10)).strftime("%Y-%m-%d %H:%M:%S")
        c.execute("""
            SELECT number, otp, full_message, timestamp FROM otp_logs
            WHERE timestamp >= ?
            ORDER BY timestamp DESC
        """, (cutoff,))
        rows = c.fetchall()
        conn.close()
    except Exception as e:
        rows = []

    title = (
        f"🚨 "
        f"<b>{'آخر رسالة' if lang == 'ar' else 'Last SMS'}</b>\n\n"
        f"⏱ "
        f"<b>{'النافذة' if lang == 'ar' else 'Window'}: {'آخر 10 دقائق' if lang == 'ar' else 'Last 10 minutes'}</b>\n"
    )

    if not rows:
        no_data = (
            "❌ لا توجد رسائل في آخر 10 دقائق."
            if lang == "ar" else
            "❌ No messages in the last 10 minutes."
        )
        refresh_markup = {"inline_keyboard": [[{
            "text": "تحديث" if lang == "ar" else "Refresh",
            "callback_data": "last_sms_refresh",
            "icon_custom_emoji_id": "5316977222467206948"
        }]]}
        requests.post(
            f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
            json={"chat_id": chat_id, "text": title + no_data,
                  "parse_mode": "HTML", "reply_markup": refresh_markup},
            timeout=10
        )
        return

    country_counts = {}
    country_platform = {}
    country_tags = {}
    for number, otp, sms, ts in rows:
        try:
            num_clean = str(number).strip().replace("+","").replace(" ","").replace("-","")
            cc = None
            for code in sorted(COUNTRY_CODES.keys(), key=len, reverse=True):
                if num_clean.startswith(code):
                    cc = code
                    break
            if cc:
                country_counts[cc] = country_counts.get(cc, 0) + 1
                platform_emoji = get_platform_emoji(sms)
                if cc not in country_platform and platform_emoji:
                    country_platform[cc] = platform_emoji
                if cc not in country_tags:
                    tag = get_best_combo_tag_for_country(cc)
                    if tag:
                        country_tags[cc] = tag
        except:
            pass

    if country_counts:
        _save_traffic_snapshot("last_sms", 10, country_counts, country_platform, country_tags)

    total_codes = sum(country_counts.values())
    sorted_countries = sorted(country_counts.items(), key=lambda x: x[1], reverse=True)

    best_code, best_cnt = sorted_countries[0] if sorted_countries else (None, 0)
    if best_code and best_code in COUNTRY_CODES:
        best_cname_en, best_flag_raw, _ = COUNTRY_CODES[best_code]
        best_cname = COUNTRY_NAMES_AR.get(best_code, best_cname_en) if lang == "ar" else best_cname_en
        best_flag_id = _extract_flag_emoji_id(best_flag_raw)
        best_flag_str = f"{get_flag_plain(best_flag_raw)}" if best_flag_id else get_flag_plain(best_flag_raw)
        best_pct = round(best_cnt / max(total_codes, 1) * 100)
        best_tag = country_tags.get(best_code) or get_best_combo_tag_for_country(best_code)
        best_range_part = f"-<b>{to_bold(best_tag)}</b>" if best_tag else ""
        best_platform = country_platform.get(best_code, "")
        best_line = f"{best_flag_str} <b>{best_cname}</b> {best_platform}{best_range_part} — {best_pct}%"
    else:
        best_line = "—"

    summary = (
        f"✅ "
        f"<b>{'الأكواد الواصلة' if lang == 'ar' else 'Codes Received'}: {total_codes}</b>\n"
        f"🌟 "
        f"<b>{'الأفضل' if lang == 'ar' else 'Best'}: {best_line}</b>\n\n"
        f"🌍 "
        f"<b>{'تفاصيل الدول' if lang == 'ar' else 'Country Details'}:</b>\n\n"
    )

    _AR_RANK = {1:"١",2:"٢",3:"٣",4:"٤",5:"٥",6:"٦",7:"٧",8:"٨",9:"٩",10:"١٠"}
    lines = []
    for i, (code, cnt) in enumerate(sorted_countries[:10], 1):
        if code not in COUNTRY_CODES:
            continue
        cname_en, flag, _ = COUNTRY_CODES[code]
        cname = COUNTRY_NAMES_AR.get(code, cname_en) if lang == "ar" else cname_en
        flag_id = _extract_flag_emoji_id(flag)
        flag_str = f"{get_flag_plain(flag)}" if flag_id else get_flag_plain(flag)
        rank = _AR_RANK.get(i, str(i))
        best_tag = country_tags.get(code) or get_best_combo_tag_for_country(code)
        range_part = f"-<b>{to_bold(best_tag)}</b>" if best_tag else ""
        platform_em = country_platform.get(code, "")
        pct = round(cnt / max(total_codes, 1) * 100)
        lines.append(f"{rank}. {flag_str} <b>{cname}</b> {platform_em}{range_part} — {pct}%")

    text = title + summary + "\n".join(lines)

    refresh_markup = {"inline_keyboard": [[{
        "text": "تحديث" if lang == "ar" else "Refresh",
        "callback_data": "last_sms_refresh",
        "icon_custom_emoji_id": "5316977222467206948"
    }]]}

    requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        json={"chat_id": chat_id, "text": text, "parse_mode": "HTML",
              "reply_markup": refresh_markup},
        timeout=10
    )


@bot.callback_query_handler(func=lambda call: call.data == "live_traffic_refresh")
def live_traffic_refresh_callback(call):
    user_id = call.from_user.id
    lang    = get_user_lang(user_id)
    bot.answer_callback_query(call.id)

    _live_traffic_window[user_id] = _LIVE_TRAFFIC_WINDOW_MINUTES
    top, country_platform, country_tags, _ = get_top_range_by_otp(
        window_minutes=_LIVE_TRAFFIC_WINDOW_MINUTES
    )
    has_data = bool(top)
    text     = _build_live_traffic_text(lang, top, country_platform, country_tags)
    markup   = _live_traffic_refresh_markup(lang, has_data)
    payload  = {
        "chat_id":    call.message.chat.id,
        "message_id": call.message.message_id,
        "text":       text,
        "parse_mode": "HTML",
        "reply_markup": markup if markup else {"inline_keyboard": []},
    }
    try:
        requests.post(
            f"https://api.telegram.org/bot{BOT_TOKEN}/editMessageText",
            json=payload, timeout=10
        )
    except Exception:
        pass


@bot.callback_query_handler(func=lambda call: call.data == "last_sms_refresh")
def last_sms_refresh_callback(call):
    user_id = call.from_user.id
    lang = get_user_lang(user_id)
    try:
        conn = sqlite3.connect(DB_PATH, check_same_thread=False, timeout=10)
        c = conn.cursor()
        cutoff = (datetime.now() - timedelta(minutes=10)).strftime("%Y-%m-%d %H:%M:%S")
        c.execute("SELECT number, otp, full_message, timestamp FROM otp_logs WHERE timestamp >= ? ORDER BY timestamp DESC", (cutoff,))
        rows = c.fetchall()
        conn.close()
    except:
        rows = []
    title = (
        f"🚨 "
        f"<b>{'آخر رسالة' if lang == 'ar' else 'Last SMS'}</b>\n\n"
        f"⏱ "
        f"<b>{'النافذة' if lang == 'ar' else 'Window'}: {'آخر 10 دقائق' if lang == 'ar' else 'Last 10 minutes'}</b>\n"
    )
    if not rows:
        no_data = ("❌ لا توجد رسائل." if lang == "ar"
                   else "❌ No messages.")
        refresh_markup = {"inline_keyboard": [[{"text": "تحديث" if lang == "ar" else "Refresh", "callback_data": "last_sms_refresh", "icon_custom_emoji_id": "5316977222467206948"}]]}
        try:
            requests.post(f"https://api.telegram.org/bot{BOT_TOKEN}/editMessageText",
                json={"chat_id": call.message.chat.id, "message_id": call.message.message_id,
                      "text": title + no_data, "parse_mode": "HTML", "reply_markup": refresh_markup}, timeout=10)
        except: pass
        bot.answer_callback_query(call.id)
        return
    country_counts = {}
    country_platform = {}
    country_tags = {}
    for number, otp, sms, ts in rows:
        try:
            num_clean = str(number).strip().replace("+","").replace(" ","").replace("-","")
            cc = None
            for code in sorted(COUNTRY_CODES.keys(), key=len, reverse=True):
                if num_clean.startswith(code):
                    cc = code
                    break
            if cc:
                country_counts[cc] = country_counts.get(cc, 0) + 1
                platform_emoji = get_platform_emoji(sms)
                if cc not in country_platform and platform_emoji:
                    country_platform[cc] = platform_emoji
                if cc not in country_tags:
                    tag = get_best_combo_tag_for_country(cc)
                    if tag:
                        country_tags[cc] = tag
        except: pass

    if country_counts:
        _save_traffic_snapshot("last_sms", 10, country_counts, country_platform, country_tags)

    total_codes = sum(country_counts.values())
    sorted_countries = sorted(country_counts.items(), key=lambda x: x[1], reverse=True)
    if not sorted_countries:
        bot.answer_callback_query(call.id)
        return
    best_code, best_cnt = sorted_countries[0]
    _AR_RANK = {1:"١",2:"٢",3:"٣",4:"٤",5:"٥",6:"٦",7:"٧",8:"٨",9:"٩",10:"١٠"}
    if best_code in COUNTRY_CODES:
        best_cname_en, best_flag_raw, _ = COUNTRY_CODES[best_code]
        best_cname = COUNTRY_NAMES_AR.get(best_code, best_cname_en) if lang == "ar" else best_cname_en
        best_flag_id = _extract_flag_emoji_id(best_flag_raw)
        best_flag_str = f"{get_flag_plain(best_flag_raw)}" if best_flag_id else get_flag_plain(best_flag_raw)
        best_pct = round(best_cnt / max(total_codes, 1) * 100)
        best_tag = country_tags.get(best_code) or get_best_combo_tag_for_country(best_code)
        best_range_part = f"-<b>{to_bold(best_tag)}</b>" if best_tag else ""
        best_platform = country_platform.get(best_code, "")
        best_line = f"{best_flag_str} <b>{best_cname}</b> {best_platform}{best_range_part} — {best_pct}%"
    else:
        best_line = "—"
    summary = (
        f"✅ <b>{'الأكواد الواصلة' if lang == 'ar' else 'Codes Received'}: {total_codes}</b>\n"
        f"🌟 <b>{'الأفضل' if lang == 'ar' else 'Best'}: {best_line}</b>\n\n"
        f"🌍 <b>{'تفاصيل الدول' if lang == 'ar' else 'Country Details'}:</b>\n\n"
    )
    lines = []
    for i, (code, cnt) in enumerate(sorted_countries[:10], 1):
        if code not in COUNTRY_CODES: continue
        cname_en, flag, _ = COUNTRY_CODES[code]
        cname = COUNTRY_NAMES_AR.get(code, cname_en) if lang == "ar" else cname_en
        flag_id = _extract_flag_emoji_id(flag)
        flag_str = f"{get_flag_plain(flag)}" if flag_id else get_flag_plain(flag)
        rank = _AR_RANK.get(i, str(i))
        best_tag = country_tags.get(code) or get_best_combo_tag_for_country(code)
        range_part = f"-<b>{to_bold(best_tag)}</b>" if best_tag else ""
        platform_em = country_platform.get(code, "")
        pct = round(cnt / max(total_codes, 1) * 100)
        lines.append(f"{rank}. {flag_str} <b>{cname}</b> {platform_em}{range_part} — {pct}%")
    text = title + summary + "\n".join(lines)
    refresh_markup = {"inline_keyboard": [[{"text": "تحديث" if lang == "ar" else "Refresh", "callback_data": "last_sms_refresh", "icon_custom_emoji_id": "5316977222467206948"}]]}
    try:
        requests.post(f"https://api.telegram.org/bot{BOT_TOKEN}/editMessageText",
            json={"chat_id": call.message.chat.id, "message_id": call.message.message_id,
                  "text": text, "parse_mode": "HTML", "reply_markup": refresh_markup}, timeout=10)
    except: pass
    bot.answer_callback_query(call.id)


def show_stock_message(chat_id, user_id):
    lang = get_user_lang(user_id)
    conn = sqlite3.connect(DB_PATH, check_same_thread=False, timeout=10)
    c = conn.cursor()
    c.execute("""
        SELECT co.id, co.country_code, co.numbers, co.section_id, s.name
        FROM combos co
        LEFT JOIN sections s ON s.id = co.section_id
        ORDER BY co.section_id, co.country_code, co.id
    """)
    rows = c.fetchall()
    conn.close()

    if not rows:
        msg = (
            "❌ <b>لا يوجد مخزون حالياً.</b>"
            if lang == "ar" else
            "❌ <b>No stock available.</b>"
        )
        requests.post(
            f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
            json={"chat_id": chat_id, "text": msg, "parse_mode": "HTML"},
            timeout=10
        )
        return

    title = (
        "📦 <b>المخزون الحالي</b>\n\n"
        if lang == "ar" else
        "📦 <b>Current Stock</b>\n\n"
    )

    from collections import defaultdict
    country_file_counter = defaultdict(int)
    lines = []

    for file_id, country_code, numbers_json, section_id, section_name in rows:
        if country_code not in COUNTRY_CODES:
            continue
        try:
            nums = json.loads(numbers_json)
            count = len(nums)
        except:
            count = 0
        if count == 0:
            continue

        country_file_counter[country_code] += 1
        file_num = country_file_counter[country_code]
        tag = _generate_unique_combo_tag(country_code, file_num - 1, combo_id=file_id)

        cname_en, flag_str, _ = COUNTRY_CODES[country_code]
        cname = COUNTRY_NAMES_AR.get(country_code, cname_en) if lang == "ar" else cname_en
        flag_id = _extract_flag_emoji_id(flag_str)
        flag_html = f"{get_flag_plain(flag_str)}" if flag_id else get_flag_plain(flag_str)

        plat_emoji = ""
        if section_name:
            pid = get_platform_emoji_id(section_name)
            if pid:
                plat_emoji = f" 🌐"

        tag_display = f" ({tag})" if tag else ""
        line = f"🌐 <b>{cname}</b>{tag_display} {flag_html}{plat_emoji} : <b>{count}</b>"
        lines.append(line)

    if not lines:
        msg = (
            "❌ <b>لا يوجد مخزون حالياً.</b>"
            if lang == "ar" else
            "❌ <b>No stock available.</b>"
        )
        requests.post(
            f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
            json={"chat_id": chat_id, "text": msg, "parse_mode": "HTML"},
            timeout=10
        )
        return

    text = title + "\n".join(lines)
    requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        json={"chat_id": chat_id, "text": text, "parse_mode": "HTML"},
        timeout=10
    )


def show_user_status(chat_id, user_id):
    lang = get_user_lang(user_id)
    user = get_user(user_id)
    balance = 0.0
    try:
        conn = sqlite3.connect(DB_PATH, check_same_thread=False, timeout=10)
        c = conn.cursor()
        c.execute("SELECT COALESCE(balance,0) FROM users WHERE user_id=?", (user_id,))
        row = c.fetchone()
        conn.close()
        if row:
            balance = float(row[0])
    except:
        pass
    bot_on_emoji = "🟢"
    bot_status_label = "ON" if lang == "en" else "يعمل"
    ref_count = get_referral_count(user_id)
    ref_earn_total = get_referral_total_earned(user_id)
    if lang == "ar":
        text = (
            f"👤 <b>حالتك</b> 👤\n\n"
            f"🤖 <b>حالة البوت</b> : <b>{bot_status_label}</b> {bot_on_emoji}\n"
            f"💳 <b>رصيدك</b> : <b>${balance:.2f}</b>\n"
            f"🎁 <b>أرباح الإحالات</b> : <b>${ref_earn_total:.2f}</b>\n"
            f"👥 <b>إجمالي الإحالات</b> : <b>{ref_count}</b>"
        )
    else:
        text = (
            f"👤 <b>Your Status</b> 👤\n\n"
            f"🤖 <b>Bot Status</b> : <b>{bot_status_label}</b> {bot_on_emoji}\n"
            f"💳 <b>Balance</b> : <b>${balance:.2f}</b>\n"
            f"🎁 <b>Referral Earnings</b> : <b>${ref_earn_total:.2f}</b>\n"
            f"👥 <b>Total Referrals</b> : <b>{ref_count}</b>"
        )
    refer_btn_text = "الإحالة والأرباح" if get_user_lang(user_id) == "ar" else "Refer & Earn"
    markup = {"inline_keyboard": [[{
        "text": refer_btn_text,
        "callback_data": "refer_earn",
        "icon_custom_emoji_id": "5258362837411045098"
    }]]}
    requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        json={"chat_id": chat_id, "text": text, "parse_mode": "HTML", "reply_markup": markup},
        timeout=10
    )



WITHDRAW_MIN = 0.15
WITHDRAW_MAX = 1.0

def get_user_balance(user_id):
    try:
        conn = sqlite3.connect(DB_PATH, check_same_thread=False, timeout=10)
        c = conn.cursor()
        c.execute("SELECT COALESCE(balance,0) FROM users WHERE user_id=?", (user_id,))
        row = c.fetchone()
        conn.close()
        return float(row[0]) if row else 0.0
    except:
        return 0.0

def withdraw_cancel_markup(lang):
    cancel_text = "إلغاء" if lang == "ar" else "Cancel"
    return {
        "keyboard": [[{"text": cancel_text, "icon_custom_emoji_id": "5420323339723881652", "style": "danger"}]],
        "resize_keyboard": True,
        "one_time_keyboard": False
    }

WITHDRAW_CANCEL_TEXTS = {"إلغاء", "Cancel", "❌ إلغاء", "❌ Cancel"}

def start_withdraw(chat_id, user_id):
    lang = get_user_lang(user_id)
    bal = get_user_balance(user_id)
    cancel_markup = withdraw_cancel_markup(lang)
    if lang == "ar":
        text = (
            f"💸 <b>أدخل المبلغ المراد سحبه:</b>"
        )
    else:
        text = (
            f"💸 <b>Please enter the amount to withdraw:</b>"
        )
    user_states[user_id] = "withdraw_amount"
    requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        json={"chat_id": chat_id, "text": text, "parse_mode": "HTML", "reply_markup": cancel_markup},
        timeout=10
    )


@bot.message_handler(func=lambda msg: msg.text in WITHDRAW_CANCEL_TEXTS and (
    (isinstance(user_states.get(msg.from_user.id), str) and user_states[msg.from_user.id].startswith("withdraw")) or
    (isinstance(user_states.get(msg.from_user.id), dict) and str(user_states[msg.from_user.id].get("step","")).startswith("withdraw"))
))
def withdraw_cancel_handler(message):
    uid = message.from_user.id
    user_states.pop(uid, None)
    show_main_menu(message.chat.id, uid, message.from_user.username,
                   message.from_user.first_name, message.from_user.last_name)

@bot.message_handler(func=lambda msg: user_states.get(msg.from_user.id) == "withdraw_amount")
def withdraw_handle_amount(message):
    uid = message.from_user.id
    lang = get_user_lang(uid)
    cancel_texts = {"إلغاء", "Cancel", "⚠️ إلغاء", "⚠️ Cancel"}
    if message.text in {"إلغاء", "Cancel"}:
        user_states.pop(uid, None)
        show_main_menu(message.chat.id, uid, message.from_user.username,
                       message.from_user.first_name, message.from_user.last_name)
        return
    try:
        amount = float(message.text.strip().replace(",", "."))
        if amount <= 0:
            raise ValueError
    except:
        err = ("⚠️ <b>مبلغ غير صحيح، أدخل رقم صحيح.</b>"
               if lang == "ar" else
               "⚠️ <b>Invalid amount. Please enter a valid number.</b>")
        bot.reply_to(message, err, parse_mode="HTML")
        return
    bal = get_user_balance(uid)
    if amount < WITHDRAW_MIN:
        err = (f"⚠️ <b>الحد الأدنى للسحب: ${WITHDRAW_MIN}</b>"
               if lang == "ar" else
               f"⚠️ <b>Minimum withdrawal: ${WITHDRAW_MIN}</b>")
        bot.reply_to(message, err, parse_mode="HTML")
        return
    if amount > WITHDRAW_MAX:
        err = (f"⚠️ <b>الحد الأقصى للسحب: ${WITHDRAW_MAX}</b>"
               if lang == "ar" else
               f"⚠️ <b>Maximum withdrawal limit: ${WITHDRAW_MAX}</b>")
        bot.reply_to(message, err, parse_mode="HTML")
        return
    if bal < amount:
        err = (f"⚠️ <b>رصيد غير كافٍ.</b>\nرصيدك: <b>${bal:.2f}</b>"
               if lang == "ar" else
               f"⚠️ <b>Insufficient balance.</b>\nYour balance: <b>${bal:.2f}</b>")
        bot.reply_to(message, err, parse_mode="HTML")
        return
    user_states[uid] = {"step": "withdraw_address", "amount": amount}
    addr_msg = (
        "💳 <b>أرسل عنوان USDT (BEP20)</b>\n\n"
        " افتح أي محفظة (مثال: Binance, Bitget, Trust Wallet, MetaMask, OKX, Coinbase)\n"
        " اختر USDT\n"
        " اختر الشبكة: BSC (BEP20) / BNB Chain\n"
        " انسخ العنوان والصقه هنا\n\n"
        "⚠️ <b>تأكد من اختيار USDT BSC (BEP20)، وإلا لن تستلم الدفع.</b>"
        if lang == "ar" else
        "💳 <b>Send USDT (BEP20) Address</b>\n\n"
        " Open any wallet/App (Example: Binance, Bitget, Trust Wallet, MetaMask, OKX Wallet, Coinbase Wallet, Etc)\n"
        " Select USDT\n"
        " Choose Network: BSC (BEP20) / BNB Chain\n"
        " Copy the USDT BSC (BEP20) address and paste below\n\n"
        "⚠️ <b>Make sure to select USDT BSC (BEP20) / BNB Chain, otherwise you won't receive payment.</b>"
    )
    requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        json={"chat_id": message.chat.id, "text": addr_msg, "parse_mode": "HTML",
              "reply_markup": withdraw_cancel_markup(lang)},
        timeout=10
    )

@bot.message_handler(func=lambda msg: isinstance(user_states.get(msg.from_user.id), dict) and
                     user_states[msg.from_user.id].get("step") == "withdraw_address")
def withdraw_handle_address(message):
    uid = message.from_user.id
    lang = get_user_lang(uid)
    if message.text in {"إلغاء", "Cancel", "❌ إلغاء", "❌ Cancel"}:
        user_states.pop(uid, None)
        show_main_menu(message.chat.id, uid, message.from_user.username,
                       message.from_user.first_name, message.from_user.last_name)
        return
    address = message.text.strip() if message.text else ""
    import re
    if not re.match(r"^0x[0-9a-fA-F]{40}$", address):
        err = ("⚠️ <b>عنوان غير صحيح. تأكد إنه USDT BEP20.</b>"
               if lang == "ar" else
               "⚠️ <b>Invalid address. Make sure it is a USDT BEP20 address.</b>")
        bot.reply_to(message, err, parse_mode="HTML")
        return
    state = user_states[uid]
    state["address"] = address
    state["step"] = "withdraw_username"
    user_states[uid] = state
    uname_msg = ("💳 <b>أرسل العنوان:</b>\n"
                 + f"<code>{address}</code>\n\n"
                 + "✉️ <b>أرسل يوزرنيمك (يبدأ بـ @):</b>"
                 if lang == "ar" else
                 "💳 <b>Address:</b>\n"
                 + f"<code>{address}</code>\n\n"
                 + "✉️ <b>Send your username (starting with @):</b>")
    requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        json={"chat_id": message.chat.id, "text": uname_msg, "parse_mode": "HTML",
              "reply_markup": withdraw_cancel_markup(lang)},
        timeout=10
    )

@bot.message_handler(func=lambda msg: isinstance(user_states.get(msg.from_user.id), dict) and
                     user_states[msg.from_user.id].get("step") == "withdraw_username")
def withdraw_handle_username(message):
    uid = message.from_user.id
    lang = get_user_lang(uid)
    if message.text in {"إلغاء", "Cancel", "❌ إلغاء", "❌ Cancel"}:
        user_states.pop(uid, None)
        show_main_menu(message.chat.id, uid, message.from_user.username,
                       message.from_user.first_name, message.from_user.last_name)
        return
    username = message.text.strip() if message.text else ""
    if not username.startswith("@"):
        err = ("⚠️ <b>يوزرنيم غير صحيح، لازم يبدأ بـ @</b>"
               if lang == "ar" else
               "⚠️ <b>Incorrect username, must start with @</b>")
        bot.reply_to(message, err, parse_mode="HTML")
        return
    state = user_states.pop(uid)
    amount = state["amount"]
    address = state["address"]
    _conn_wr = sqlite3.connect(DB_PATH, check_same_thread=False, timeout=10)
    _c_wr = _conn_wr.cursor()
    _c_wr.execute(
        "INSERT INTO withdraw_requests (user_id, amount, address, username, created_at) VALUES (?,?,?,?,?)",
        (uid, amount, address, username, datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    )
    req_id = _c_wr.lastrowid
    _conn_wr.commit()
    _conn_wr.close()
    admin_ids = list(set(ADMIN_IDS) | {row[0] for row in get_db_admins()})
    sep = "─────────────────"
    admin_msg = (
        f"🔔 <b>طلب دفع جديد متاح</b>\n"
        f"{sep}\n"
        f"💳 <b>المبلغ المراد سحبه:</b> <b>${amount:.2f}</b>\n"
        f"👤 <b>يوزر المستخدم:</b> {username}\n"
        f"{sep}\n"
        f"<b>عنوان المستخدم:</b> <code>{address}</code>\n"
        f"{sep}"
    )
    pay_markup = {"inline_keyboard": [[{
        "text": "✅ تم الدفع",
        "callback_data": f"wpaid_{req_id}",
        "icon_custom_emoji_id": "5206607081334906820"
    }]]}
    for admin_id in admin_ids:
        try:
            plain_text, entities_list = _parse_html_to_entities_global(admin_msg)
            resp = requests.post(
                f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
                json={"chat_id": admin_id, "text": plain_text, "entities": entities_list,
                      "reply_markup": pay_markup},
                timeout=10
            )
            if not resp.json().get("ok"):
                print(f"[WITHDRAW] فشل إرسال للأدمن {admin_id}: {resp.text}")
        except Exception as e:
            print(f"[WITHDRAW] exception للأدمن {admin_id}: {e}")
    wait_msg = ("⏳ <b>يرجى الانتظار، سيتم إشعارك عند وصول الأموال.</b>" if lang == "ar"
                else "⏳ <b>Please wait, you will be notified when the funds arrive.</b>")
    requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        json={"chat_id": message.chat.id, "text": wait_msg, "parse_mode": "HTML"},
        timeout=10
    )
    show_main_menu(message.chat.id, uid, message.from_user.username,
                   message.from_user.first_name, message.from_user.last_name)

@bot.callback_query_handler(func=lambda call: call.data.startswith("wpaid_"))
def withdraw_paid_handler(call):
    if not is_admin(call.from_user.id): return
    try:
        req_id = int(call.data[len("wpaid_"):])
    except:
        bot.answer_callback_query(call.id, "❌ بيانات غير صحيحة", show_alert=True)
        return
    _conn_wr = sqlite3.connect(DB_PATH, check_same_thread=False, timeout=10)
    _c_wr = _conn_wr.cursor()
    _c_wr.execute("SELECT user_id, amount, address, username FROM withdraw_requests WHERE id=?", (req_id,))
    row = _c_wr.fetchone()
    _conn_wr.close()
    if not row:
        bot.answer_callback_query(call.id, "❌ الطلب مش موجود أو اتنفذ قبل كده", show_alert=True)
        return
    target_uid, amount, address, username = row[0], row[1], row[2], row[3]
    try:
        conn = sqlite3.connect(DB_PATH, check_same_thread=False, timeout=10)
        c = conn.cursor()
        c.execute("UPDATE users SET balance = COALESCE(balance,0) - ? WHERE user_id=?",
                  (amount, int(target_uid)))
        conn.commit()
        conn.close()
    except:
        pass
    lang = get_user_lang(int(target_uid))
    network = "BEP20"
    user_msg = t("withdraw_approved", int(target_uid),
                 amount=f"{amount:.2f}", network=network, address=address)
    try:
        plain_user, ent_user = _parse_html_to_entities_global(user_msg)
        requests.post(
            f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
            json={"chat_id": int(target_uid), "text": plain_user, "entities": ent_user},
            timeout=10
        )
    except:
        pass
    bot.answer_callback_query(call.id, "✅ تم إرسال تأكيد الدفع للمستخدم", show_alert=True)
    try:
        _conn_del = sqlite3.connect(DB_PATH, check_same_thread=False, timeout=10)
        _c_del = _conn_del.cursor()
        _c_del.execute("DELETE FROM withdraw_requests WHERE id=?", (req_id,))
        _conn_del.commit()
        _conn_del.close()
    except:
        pass
    try:
        bot.delete_message(call.message.chat.id, call.message.message_id)
    except:
        pass

@bot.callback_query_handler(func=lambda call: call.data == "back_to_status")
def back_to_status_callback(call):
    user_id = call.from_user.id
    bot.answer_callback_query(call.id)
    show_user_status(call.message.chat.id, user_id)

@bot.callback_query_handler(func=lambda call: call.data == "refer_earn")
def refer_earn_callback(call):
    user_id = call.from_user.id
    lang = get_user_lang(user_id)
    bot.answer_callback_query(call.id)
    ref_count = get_referral_count(user_id)
    bot_info = bot.get_me()
    bot_username = bot_info.username
    ref_link = f"https://t.me/{bot_username}?start=ref_{user_id}"
    title = t("refer_earn_title", user_id)
    link_label = t("refer_link_label", user_id)
    total_line = t("refer_total", user_id, count=ref_count)
    earn_line = t("refer_earn_per", user_id, amount=f"{REFERRAL_EARN:.2f}")
    share_line = t("refer_share", user_id)
    text = (
        f"{title}\n\n"
        f"{link_label}\n"
        f"<code>{ref_link}</code>\n\n"
        f"{total_line}\n"
        f"{earn_line}\n\n"
        f"{share_line}"
    )
    back_text = "رجوع" if lang == "ar" else "Back"
    back_markup = {"inline_keyboard": [[{
        "text": back_text,
        "callback_data": "back_to_status",
        "icon_custom_emoji_id": "5433757980245900289"
    }]]}
    safe_edit_or_delete(call, text, markup=back_markup, parse_mode="HTML")

def show_main_menu(chat_id, user_id, username, first_name, last_name, edit_message_id=None):
    lang = get_user_lang(user_id)
    get_num_text = "احصل على رقم" if lang == "ar" else "Get Number"
    top_range_text = "الترافيك المباشر" if lang == "ar" else "Live Traffic"
    last_sms_text = "آخر رسالة" if lang == "ar" else "Last SMS"
    stock_text = "المخزون" if lang == "ar" else "Stock"
    status_text = "الحالة" if lang == "ar" else "Status"
    withdraw_text = "سحب" if lang == "ar" else "Withdraw"
    reply_kb = {
        "keyboard": [
            [
                {"text": get_num_text, "icon_custom_emoji_id": "5393561394207541973", "style": "danger"},
                {"text": top_range_text, "icon_custom_emoji_id": "5325945307454789973", "style": "danger"},
            ],
            [
                {"text": stock_text, "icon_custom_emoji_id": "5472335930549347896", "style": "primary"},
                {"text": status_text, "icon_custom_emoji_id": "5231200819986047254", "style": "primary"},
            ],
            [
                {"text": withdraw_text, "icon_custom_emoji_id": "5317013291602553603", "style": "success"},
            ]
        ],
        "resize_keyboard": True,
        "persistent": True
    }
    if not get_user(user_id):
        for admin in set(ADMIN_IDS):
            try:
                bot.send_message(admin,
                    f"🆕 مستخدم جديد:\n🆔 <code>{user_id}</code>\n👤 @{username or 'None'}",
                    parse_mode="HTML")
            except:
                pass
    save_user(user_id, username=username or "", first_name=first_name or "", last_name=last_name or "")
    display_name = first_name or username or "User"
    if lang == "ar":
        welcome_text = (
            f"👋 <b>أهلاً {display_name}</b> "
            f"🌟\n\n"
            f"🤖 <b>القائمة الرئيسية</b>\n\n"
            f"👇 <b>اختر من الأزرار أدناه:</b>"
        )
    else:
        welcome_text = (
            f"👋 <b>Welcome {display_name}</b> "
            f"🌟\n\n"
            f"🤖 <b>Main Menu</b>\n\n"
            f"👇 <b>Please select an option below:</b>"
        )
    inline_markup = None
    if is_admin(user_id):
        inline_markup = {"inline_keyboard": [[{
            "text": "لوحة الإدارة",
            "callback_data": "admin_panel",
            "icon_custom_emoji_id": "5433757980245900289", "style": "success"
        }]]}
    try:
        if edit_message_id:
            try:
                bot.delete_message(chat_id, edit_message_id)
            except:
                pass
        payload = {
            "chat_id": chat_id,
            "text": welcome_text,
            "reply_markup": reply_kb,
            "parse_mode": "HTML"
        }
        requests.post(
            f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
            json=payload, timeout=10
        )
        if inline_markup:
            requests.post(
                f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
                json={"chat_id": chat_id, "text": "⚙️", "reply_markup": inline_markup},
                timeout=10
            )
    except:
        requests.post(
            f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
            json={"chat_id": chat_id, "text": welcome_text,
                  "reply_markup": reply_kb, "parse_mode": "HTML"},
            timeout=10
        )

GET_NUMBER_TEXTS = {"Get Number", "احصل على رقم"}
TOP_RANGE_TEXTS = {"Live Traffic", "الترافيك المباشر", "Top Range", "أفضل الدول"}
LAST_SMS_TEXTS = {"Last SMS", "آخر رسالة"}
STOCK_TEXTS = {"Stock", "المخزون"}
STATUS_TEXTS = {"Status", "الحالة"}
WITHDRAW_TEXTS = {"Withdraw", "سحب"}

@bot.message_handler(func=lambda msg: msg.text in GET_NUMBER_TEXTS | TOP_RANGE_TEXTS | LAST_SMS_TEXTS | STOCK_TEXTS | STATUS_TEXTS | WITHDRAW_TEXTS and not user_states.get(msg.from_user.id))
def handle_reply_keyboard(message):
    user_id = message.from_user.id
    if MAINTENANCE_MODE and not is_admin(user_id):
        user_lang = get_user_lang(user_id)
        if user_lang == "en":
            maint_caption = "🟢 The bot is under maintenance, please wait."
        else:
            maint_caption = "🟢 البوت في وضع الصيانة يرجي الانتظار"
        try:
            if MAINTENANCE_IMAGE_BYTES:
                with io.BytesIO(MAINTENANCE_IMAGE_BYTES) as img:
                    bot.send_photo(message.chat.id, img, caption=maint_caption, parse_mode="HTML")
            else:
                bot.send_message(message.chat.id, maint_caption, parse_mode="HTML")
        except:
            bot.send_message(message.chat.id, maint_caption, parse_mode="HTML")
        return
    lang = get_user_lang(user_id)
    if message.text in TOP_RANGE_TEXTS:
        if not force_sub_check(user_id):
            markup = force_sub_markup(user_id)
            requests.post(
                f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
                json={"chat_id": message.chat.id, "text": t("force_sub", user_id),
                      "parse_mode": "HTML", "reply_markup": markup},
                timeout=10
            )
            return
        show_top_range(message.chat.id, user_id)
    elif message.text in LAST_SMS_TEXTS:
        if not force_sub_check(user_id):
            markup = force_sub_markup(user_id)
            requests.post(
                f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
                json={"chat_id": message.chat.id, "text": t("force_sub", user_id),
                      "parse_mode": "HTML", "reply_markup": markup},
                timeout=10
            )
            return
        show_last_sms(message.chat.id, user_id)
    elif message.text in GET_NUMBER_TEXTS:
        if not force_sub_check(user_id):
            markup = force_sub_markup(user_id)
            requests.post(
                f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
                json={"chat_id": message.chat.id, "text": t("force_sub", user_id),
                      "parse_mode": "HTML", "reply_markup": markup},
                timeout=10
            )
            return
        markup = types.InlineKeyboardMarkup(row_width=2)
        platforms = get_platforms_with_numbers()
        platform_btns = []
        for sid, sname in platforms:
            emoji_id = get_platform_emoji_id(sname)
            count = get_platform_total_numbers(sid)
            if lang == "ar":
                PLATFORM_AR = {"whatsapp": "واتساب", "facebook": "فيسبوك", "telegram": "تيليجرام", "instagram": "إنستجرام"}
                ar_name = PLATFORM_AR.get(sname.lower(), None)
                label = ar_name if ar_name else sname
            else:
                label = sname
            if emoji_id:
                btn = types.InlineKeyboardButton(label, callback_data=f"platform_{sid}", icon_custom_emoji_id=emoji_id)
            else:
                btn = types.InlineKeyboardButton(label, callback_data=f"platform_{sid}")
            platform_btns.append(btn)
        for i in range(0, len(platform_btns), 2):
            markup.row(*platform_btns[i:i+2])
        welcome = t("welcome", user_id)
        bot.send_message(message.chat.id, welcome, reply_markup=markup, parse_mode="HTML")
    elif message.text in STOCK_TEXTS:
        if not force_sub_check(user_id):
            markup = force_sub_markup(user_id)
            requests.post(
                f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
                json={"chat_id": message.chat.id, "text": t("force_sub", user_id),
                      "parse_mode": "HTML", "reply_markup": markup},
                timeout=10
            )
            return
        show_stock_message(message.chat.id, user_id)
    elif message.text in STATUS_TEXTS:
        show_user_status(message.chat.id, user_id)
    elif message.text in WITHDRAW_TEXTS:
        start_withdraw(message.chat.id, user_id)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    if MAINTENANCE_MODE and not is_admin(message.from_user.id):
        user_id = message.from_user.id
        user_lang = get_user_lang(user_id)
        if user_lang == "en":
            maint_caption = (
                "🟢 "
                "The bot is under maintenance, please wait."
            )
        else:
            maint_caption = (
                "🟢 "
                "البوت في وضع الصيانة يرجي الانتظار"
            )
        try:
            if MAINTENANCE_IMAGE_BYTES:
                with io.BytesIO(MAINTENANCE_IMAGE_BYTES) as img:
                    bot.send_photo(message.chat.id, img, caption=maint_caption, parse_mode="HTML")
            else:
                requests.post(
                    f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto",
                    json={"chat_id": message.chat.id,
                          "photo": "https://k.top4top.io/p_3777nsg700.png",
                          "caption": maint_caption, "parse_mode": "HTML"},
                    timeout=10
                )
        except:
            bot.send_message(message.chat.id, maint_caption, parse_mode="HTML")
        return
    user_id = message.from_user.id
    if is_banned(user_id):
        bot.reply_to(message, "🚫 أنت محظور.")
        return
    # معالجة رابط الإحالة
    parts = message.text.split()
    if len(parts) > 1 and parts[1].startswith("ref_"):
        try:
            referrer_id = int(parts[1][4:])
            is_new = not get_user(user_id)
            if is_new or True:
                if process_referral(referrer_id, user_id):
                    lang_ref = get_user_lang(referrer_id)
                    notify_text = t("refer_notify", referrer_id, amount=f"{REFERRAL_EARN:.2f}")
                    try:
                        requests.post(
                            f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
                            json={"chat_id": referrer_id, "text": notify_text, "parse_mode": "HTML"},
                            timeout=10
                        )
                    except:
                        pass
        except:
            pass
    user = get_user(user_id)
    lang_val = user[8] if user and len(user) > 8 else None
    if not lang_val or lang_val not in ("ar", "en"):
        show_language_selection(message.chat.id, user_id)
        return
    if not force_sub_check(user_id):
        markup = force_sub_markup(user_id)
        if FORCE_SUB_IMAGE_BYTES:
            try:
                with io.BytesIO(FORCE_SUB_IMAGE_BYTES) as img:
                    bot.send_photo(message.chat.id, img, caption=t("force_sub", user_id),
                                   reply_markup=types.InlineKeyboardMarkup(), parse_mode="HTML")
                return
            except:
                pass
        requests.post(
            f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
            json={"chat_id": message.chat.id, "text": t("force_sub", user_id),
                  "parse_mode": "HTML", "reply_markup": markup},
            timeout=10
        )
        return
    if not user or user[9] == 0:
        requests.post(
            f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
            json={
                "chat_id": message.chat.id,
                "text": t("terms_text", user_id),
                "parse_mode": "HTML",
                "reply_markup": {"inline_keyboard": [[{"text": t("agree", user_id), "callback_data": "agree_terms", "style": "success"}]]}
            },
            timeout=10
        )
        return
    show_main_menu(message.chat.id, user_id, message.from_user.username,
                   message.from_user.first_name, message.from_user.last_name)

@bot.message_handler(commands=['language'])
def language_command(message):
    user_id = message.from_user.id
    show_language_selection(message.chat.id, user_id)

@bot.callback_query_handler(func=lambda call: call.data == "agree_terms")
def agree_terms(call):
    user_id = call.from_user.id
    save_user(user_id, agreed_terms=1)
    bot.answer_callback_query(call.id, "✅ تم قبول الشروط", show_alert=True)
    try:
        bot.delete_message(call.message.chat.id, call.message.message_id)
    except:
        pass
    if not force_sub_check(user_id):
        markup = force_sub_markup(user_id)
        requests.post(
            f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
            json={"chat_id": call.message.chat.id, "text": t("force_sub", user_id),
                  "parse_mode": "HTML", "reply_markup": markup},
            timeout=10
        )
        return
    user = get_user(user_id)
    if not user or not user[8]:
        show_language_selection(call.message.chat.id, user_id)
        return
    show_main_menu(call.message.chat.id, user_id, call.from_user.username,
                   call.from_user.first_name, call.from_user.last_name)

@bot.callback_query_handler(func=lambda call: call.data in ["set_lang_ar", "set_lang_en"])
def set_language(call):
    user_id = call.from_user.id
    lang = "ar" if call.data == "set_lang_ar" else "en"
    save_user(user_id, lang=lang)
    bot.answer_callback_query(call.id, f"✅ تم تعيين اللغة إلى {'العربية' if lang=='ar' else 'English'}", show_alert=True)
    if MAINTENANCE_MODE and not is_admin(user_id):
        try:
            bot.delete_message(call.message.chat.id, call.message.message_id)
        except:
            pass
        send_maintenance_msg(call.message.chat.id, user_id)
        return
    if not force_sub_check(user_id):
        markup = force_sub_markup(user_id)
        try:
            bot.delete_message(call.message.chat.id, call.message.message_id)
        except:
            pass
        requests.post(
            f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
            json={"chat_id": call.message.chat.id, "text": t("force_sub", user_id),
                  "parse_mode": "HTML", "reply_markup": markup},
            timeout=10
        )
        return
    user = get_user(user_id)
    if not user or user[9] == 0:
        requests.post(
            f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
            json={
                "chat_id": call.message.chat.id,
                "text": t("terms_text", user_id),
                "parse_mode": "HTML",
                "reply_markup": {"inline_keyboard": [[{"text": t("agree", user_id), "callback_data": "agree_terms", "style": "success"}]]}
            },
            timeout=10
        )
        try:
            bot.delete_message(call.message.chat.id, call.message.message_id)
        except:
            pass
        return
    show_main_menu(call.message.chat.id, user_id, call.from_user.username,
                   call.from_user.first_name, call.from_user.last_name,
                   edit_message_id=call.message.message_id)

@bot.callback_query_handler(func=lambda call: call.data == "check_sub")
def check_subscription(call):
    user_id = call.from_user.id
    lang = get_user_lang(user_id)
    if force_sub_check(user_id):
        ok_text = "✅ شكراً على اشتراكك!" if lang == "ar" else "✅ Thank you for subscribing!"
        bot.answer_callback_query(call.id, ok_text, show_alert=True)
        user = get_user(user_id)
        if not user or user[9] == 0:
            try:
                bot.delete_message(call.message.chat.id, call.message.message_id)
            except:
                pass
            requests.post(
                f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
                json={
                    "chat_id": call.message.chat.id,
                    "text": t("terms_text", user_id),
                    "parse_mode": "HTML",
                    "reply_markup": {"inline_keyboard": [[{"text": t("agree", user_id), "callback_data": "agree_terms", "style": "success"}]]}
                },
                timeout=10
            )
        else:
            if user[8]:
                show_main_menu(call.message.chat.id, user_id, call.from_user.username,
                               call.from_user.first_name, call.from_user.last_name,
                               edit_message_id=call.message.message_id)
            else:
                show_language_selection(call.message.chat.id, user_id, call.message.message_id)
    else:
        fail_text = "❌ لم تشترك بعد!" if lang == "ar" else "❌ You haven't subscribed yet!"
        bot.answer_callback_query(call.id, fail_text, show_alert=True)

@bot.callback_query_handler(func=lambda call: call.data == "change_lang")
def change_lang(call):
    user_id = call.from_user.id
    show_language_selection(call.message.chat.id, user_id, call.message.message_id)

@bot.callback_query_handler(func=lambda call: call.data.startswith("copy_num_"))
def copy_number_fallback(call):
    number = call.data[len("copy_num_"):]
    bot.answer_callback_query(call.id, f"📋 {number}", show_alert=True)

@bot.callback_query_handler(func=lambda call: call.data.startswith("copy_") and not call.data.startswith("copy_num_"))
def copy_code_fallback(call):
    code = call.data[len("copy_"):]
    bot.answer_callback_query(call.id, f"📋 {code}", show_alert=True)

@bot.message_handler(commands=['debug'])
def debug_command(message):
    user_id = message.from_user.id
    if not is_admin(user_id):
        return
    try:
        conn = sqlite3.connect(DB_PATH, check_same_thread=False, timeout=10)
        c = conn.cursor()

        c.execute("SELECT id, name FROM sections")
        sections = c.fetchall()

        c.execute("SELECT id, country_code, section_id, LENGTH(numbers) FROM combos")
        combos = c.fetchall()

        c.execute("SELECT numbers FROM combos LIMIT 1")
        row = c.fetchone()
        sample_nums = []
        if row:
            try:
                parsed = json.loads(row[0])
                sample_nums = parsed[:3]
            except:
                sample_nums = ["parse_error"]

        c.execute("SELECT assigned_number FROM users WHERE assigned_number IS NOT NULL AND assigned_number!='' LIMIT 3")
        used_sample = [r[0] for r in c.fetchall()]

        conn.close()

        msg = f"<b>🔍 Debug Info:</b>\n\n"
        msg += f"<b>Sections ({len(sections)}):</b>\n"
        for sid, sname in sections:
            msg += f"  id={sid} name={sname}\n"
        msg += f"\n<b>Combos ({len(combos)}):</b>\n"
        for cid, cc, sec_id, nlen in combos:
            msg += f"  id={cid} country={cc} section_id={sec_id} nums_len={nlen}\n"
        msg += f"\n<b>Sample numbers (type):</b>\n"
        for n in sample_nums:
            msg += f"  {repr(n)} → type={type(n).__name__}\n"
        msg += f"\n<b>Used numbers sample:</b>\n"
        for n in used_sample:
            msg += f"  {repr(n)} → type={type(n).__name__}\n"

        platforms = get_platforms_with_numbers()
        msg += f"\n<b>get_platforms_with_numbers():</b> {platforms}\n"

        bot.send_message(user_id, msg, parse_mode="HTML")
    except Exception as e:
        bot.send_message(user_id, f"❌ Error: {e}")

@bot.message_handler(commands=[''])
def stop_bot_command(message):
    user_id = message.from_user.id
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(t("owner", user_id), url="https://t.me/FK_AY"))
    bot.send_message(user_id, t("stop_bot_message", user_id), reply_markup=markup)
    
    broadcast_text = t("stop_bot_broadcast", user_id)
    users = get_all_users()
    success = 0
    for uid in users:
        try:
            bot.send_message(uid, broadcast_text, reply_markup=markup)
            success += 1
        except:
            pass
    bot.send_message(user_id, f"📢 تم إرسال الإشعار لـ {success} مستخدم.")
    os._exit(0)

@bot.callback_query_handler(func=lambda call: call.data == "show_platforms")
def show_platforms(call):
    if is_maintenance_callback(call): return
    user_id = call.from_user.id
    lang = get_user_lang(user_id)
    platforms = get_platforms_with_numbers()
    if not platforms:
        bot.answer_callback_query(call.id, t("no_numbers", user_id), show_alert=True)
        return
    markup = types.InlineKeyboardMarkup(row_width=2)
    btns = []
    PLATFORM_AR = {"whatsapp": "واتساب", "facebook": "فيسبوك", "telegram": "تيليجرام", "instagram": "إنستجرام"}
    for sid, sname in platforms:
        emoji_id = get_platform_emoji_id(sname)
        count = get_platform_total_numbers(sid)
        if lang == "ar":
            ar_name = PLATFORM_AR.get(sname.lower(), None)
            label = ar_name if ar_name else sname
        else:
            label = sname
        btn = types.InlineKeyboardButton(label, callback_data=f"platform_{sid}")
        if emoji_id:
            btn = types.InlineKeyboardButton(label, callback_data=f"platform_{sid}", icon_custom_emoji_id=emoji_id)
        btns.append(btn)
    for i in range(0, len(btns), 2):
        markup.row(*btns[i:i+2])
    markup.add(types.InlineKeyboardButton(t("back_to_platforms", user_id), callback_data="back_to_main", icon_custom_emoji_id="5433757980245900289", style="success"))
    safe_edit_or_delete(call, t("select_platform", user_id), markup=markup)

@bot.callback_query_handler(func=lambda call: call.data.startswith("platform_"))
def show_countries_for_platform(call):
    if is_maintenance_callback(call): return
    user_id = call.from_user.id
    try:
        sid = int(call.data.split("_")[1])
    except:
        bot.answer_callback_query(call.id, "❌ خطأ في البيانات", show_alert=True)
        return
    bot.answer_callback_query(call.id)
    try:
        if getattr(call.message, 'photo', None) or getattr(call.message, 'video', None):
            bot.delete_message(call.message.chat.id, call.message.message_id)
    except:
        pass
    lang = get_user_lang(user_id)
    loading_text = (
        f"🔄 جاري التحميل..."
        if lang == "ar" else
        f"🔄 Loading..."
    )
    try:
        bot.edit_message_text(loading_text, chat_id=call.message.chat.id,
                              message_id=call.message.message_id, parse_mode="HTML")
    except:
        pass
    section_name = next((n for i, n in get_all_sections() if i == sid), "Platform")
    platform_emoji_id = get_platform_emoji_id(section_name) or "5406745015365943482"

    PLATFORM_AR = {"whatsapp": "واتساب", "facebook": "فيسبوك", "telegram": "تيليجرام", "instagram": "إنستجرام"}
    section_display = PLATFORM_AR.get(section_name.lower(), section_name) if lang == "ar" else section_name

    conn = sqlite3.connect(DB_PATH, check_same_thread=False, timeout=10)
    c = conn.cursor()
    c.execute(
        "SELECT id, country_code, file_name, numbers FROM combos WHERE section_id=? ORDER BY country_code, id",
        (sid,)
    )
    all_files = c.fetchall()
    conn.close()

    safe_name = section_display.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    header = (
        f"🌐 "
        f"{'Choose Country for' if lang == 'en' else 'اختر الدولة لـ'} "
        f"<b>{safe_name}</b> "
        f"👇"
    )

    back_btn = types.InlineKeyboardButton(
        "𝗯𝗮𝗰𝗸" if lang == "en" else "رجوع",
        callback_data="back_to_main",
        icon_custom_emoji_id="5433757980245900289", style="success"
    )

    if not all_files:
        markup = types.InlineKeyboardMarkup()
        markup.add(back_btn)
        try:
            bot.delete_message(call.message.chat.id, call.message.message_id)
        except:
            pass
        bot.send_message(
            call.message.chat.id,
            header + "\n\n❌ " + ("No numbers added yet." if lang == "en" else "لم يتم إضافة أرقام بعد."),
            reply_markup=markup, parse_mode="HTML"
        )
        return

    from collections import defaultdict
    country_file_counter = defaultdict(int)
    buttons = []

    used_numbers = _get_used_numbers()

    for file_id, country_code, file_name, numbers_json in all_files:
        if country_code not in COUNTRY_CODES:
            continue
        try:
            nums = json.loads(numbers_json)
        except:
            nums = []
        available = [n for n in nums if str(n).strip() not in used_numbers]
        if not available:
            continue
        country_file_counter[country_code] += 1
        file_num = country_file_counter[country_code]
        _tag = _generate_unique_combo_tag(country_code, file_num - 1, combo_id=file_id)
        suffix = f" - {_tag}" if _tag else ""

        cname, flag, _ = COUNTRY_CODES[country_code]
        flag_emoji_id = _extract_flag_emoji_id(flag)
        btn_label = f"{cname}{suffix}"

        if flag_emoji_id:
            btn = types.InlineKeyboardButton(
                btn_label,
                callback_data=f"file_{file_id}",
                icon_custom_emoji_id=flag_emoji_id
            )
        else:
            btn = types.InlineKeyboardButton(btn_label, callback_data=f"file_{file_id}")
        buttons.append(btn)

    if not buttons:
        markup = types.InlineKeyboardMarkup()
        markup.add(back_btn)
        try:
            bot.delete_message(call.message.chat.id, call.message.message_id)
        except:
            pass
        bot.send_message(
            call.message.chat.id,
            header + "\n\n❌ " + ("All numbers are currently in use." if lang == "en" else "جميع الأرقام قيد الاستخدام حالياً."),
            reply_markup=markup, parse_mode="HTML"
        )
        return

    markup = types.InlineKeyboardMarkup(row_width=2)
    for i in range(0, len(buttons), 2):
        markup.row(*buttons[i:i+2])
    markup.add(back_btn)

    edit_ok = False
    try:
        bot.edit_message_text(header, chat_id=call.message.chat.id,
                              message_id=call.message.message_id,
                              reply_markup=markup, parse_mode="HTML")
        edit_ok = True
    except:
        pass
    if not edit_ok:
        try:
            bot.delete_message(call.message.chat.id, call.message.message_id)
        except:
            pass
        try:
            bot.send_message(call.message.chat.id, header,
                             reply_markup=markup, parse_mode="HTML")
        except:
            pass


@bot.callback_query_handler(func=lambda call: call.data.startswith("country_"))
def show_files_for_country(call):
    user_id = call.from_user.id
    parts = call.data.split("_", 2)
    if len(parts) == 3:
        sid = int(parts[1])
        country_code = parts[2]
    else:
        sid = None
        country_code = parts[1]
    files = get_combo_files(country_code, section_id=sid)
    if not files:
        bot.answer_callback_query(call.id, t("no_files", user_id), show_alert=True)
        return
    markup = types.InlineKeyboardMarkup()
    for f in files:
        available = get_available_numbers_from_file(f["id"])
        if available:
            btn_text = f"{f['file_name']} ({len(available)}/{f['total']})"
            markup.add(types.InlineKeyboardButton(btn_text, callback_data=f"file_{f['id']}"))
    back_cb = f"platform_{sid}" if sid is not None else "show_platforms"
    markup.add(types.InlineKeyboardButton(t("back_to_platforms", user_id), callback_data=back_cb, icon_custom_emoji_id="5433757980245900289", style="success"))
    name, flag, _ = COUNTRY_CODES.get(country_code, ("Unknown", "🌍", ""))
    safe_edit_or_delete(call, t("choose_file_for", user_id, country=f"{flag} {name}"), markup=markup)

@bot.callback_query_handler(func=lambda call: call.data.startswith("file_"))
def handle_file_selection(call):
    if is_maintenance_callback(call): return
    user_id = call.from_user.id
    lang = get_user_lang(user_id)
    has_media = bool(
        getattr(call.message, 'photo', None) or
        getattr(call.message, 'video', None) or
        getattr(call.message, 'document', None)
    )
    if not has_media:
        loading_text = (
            f"🔄 جاري التحميل..."
            if lang == "ar" else
            f"🔄 Loading..."
        )
        try:
            bot.edit_message_text(loading_text, chat_id=call.message.chat.id,
                                  message_id=call.message.message_id, parse_mode="HTML")
        except:
            pass
    else:
        try:
            bot.delete_message(call.message.chat.id, call.message.message_id)
        except:
            pass
    file_id = int(call.data.split("_")[1])
    available = get_available_numbers_from_file(file_id)
    if not available:
        try:
            bot.edit_message_text(
                "❌ " + t("all_numbers_used", user_id),
                chat_id=call.message.chat.id,
                message_id=call.message.message_id,
                parse_mode="HTML"
            )
        except:
            pass
        _nl = get_user_lang(user_id)
        _nm = "لا يوجد أرقام كافية!" if _nl == "ar" else "Not enough numbers available!"
        bot.answer_callback_query(call.id, _nm, show_alert=True)
        return
    assigned = random.choice(available)
    old_user = get_user(user_id)
    if old_user and old_user[5]:
        release_number(old_user[5])
    _assigned_tag, _assigned_price = get_combo_tag_for_number(assigned, with_price=True)
    if _assigned_price == 0:
        try:
            _conn_ap = sqlite3.connect(DB_PATH, check_same_thread=False, timeout=10)
            _c_ap = _conn_ap.cursor()
            _clean_a = str(assigned).lstrip("+").strip()
            _c_ap.execute("SELECT price_per_number FROM combos WHERE id=?", (file_id,))
            _ap_row = _c_ap.fetchone()
            _assigned_price = float(_ap_row[0] or 0) if _ap_row else 0.0
            _conn_ap.close()
        except:
            _assigned_price = 0.0
    assign_number_to_user(user_id, assigned)
    if _assigned_tag:
        save_combo_tag_for_number(assigned, _assigned_tag, price=_assigned_price)
    elif _assigned_price > 0:
        save_combo_tag_for_number(assigned, "", price=_assigned_price)
    conn = sqlite3.connect(DB_PATH, check_same_thread=False, timeout=10)
    c = conn.cursor()
    c.execute("SELECT country_code, file_name FROM combos WHERE id=?", (file_id,))
    row = c.fetchone()
    if not row:
        conn.close()
        bot.answer_callback_query(call.id, "❌ خطأ في الملف", show_alert=True)
        return
    country_code, file_name = row
    c.execute("SELECT section_id FROM combos WHERE country_code=? LIMIT 1", (country_code,))
    row2 = c.fetchone()
    conn.close()
    section_id = row2[0] if row2 else None
    platform_name = "Unknown"
    if section_id:
        sections = get_all_sections()
        platform_name = next((n for i, n in sections if i == section_id), "Unknown")
    save_user(user_id, country_code=country_code, assigned_number=assigned)
    name, flag, _ = COUNTRY_CODES.get(country_code, ("Unknown", "🌍", ""))
    flag_emoji_id = _extract_flag_emoji_id(flag)
    platform_emoji_id = get_platform_emoji_id(platform_name) or "5406745015365943482"
    country_flag_emoji = f"{get_flag_plain(flag)}" if flag_emoji_id else get_flag_plain(flag)
    platform_emoji_str = f"🌐"
    msg_text = t("number_selected", user_id,
                 country_flag_emoji=country_flag_emoji,
                 platform_emoji=platform_emoji_str,
                 country_name=name)
    try:
        bot.delete_message(call.message.chat.id, call.message.message_id)
    except:
        pass
    _send_number_msg(call.message.chat.id, msg_text, assigned, file_id, user_id, country_code=country_code, platform_name=platform_name)

@bot.callback_query_handler(func=lambda call: call.data.startswith("change_num_"))
def change_number(call):
    user_id = call.from_user.id
    file_id = int(call.data.split("_", 2)[2])
    available = get_available_numbers_from_file(file_id)
    if not available:
        try:
            bot.answer_callback_query(call.id, t("all_numbers_used", user_id), show_alert=True)
        except:
            pass
        return
    try:
        bot.answer_callback_query(call.id)
    except:
        pass
    old_user = get_user(user_id)
    old_number = old_user[5] if old_user else None
    if old_number:
        release_number(old_number)
    used_numbers = _get_used_numbers()
    available_new = [n for n in available if str(n).strip() not in used_numbers and str(n).strip() != str(old_number).strip()]
    if not available_new:
        available_new = [n for n in available if str(n).strip() != str(old_number).strip()]
    if not available_new:
        available_new = available
    assigned = random.choice(available_new)
    _assigned_tag = get_combo_tag_for_number(assigned)
    assign_number_to_user(user_id, assigned)
    save_user(user_id, assigned_number=assigned)
    if _assigned_tag:
        save_combo_tag_for_number(assigned, _assigned_tag)
    conn = sqlite3.connect(DB_PATH, check_same_thread=False, timeout=10)
    c = conn.cursor()
    c.execute("SELECT country_code, file_name FROM combos WHERE id=?", (file_id,))
    row = c.fetchone()
    if not row:
        conn.close()
        bot.answer_callback_query(call.id, "❌ خطأ في الملف", show_alert=True)
        return
    country_code, file_name = row
    c.execute("SELECT section_id FROM combos WHERE country_code=? LIMIT 1", (country_code,))
    row2 = c.fetchone()
    conn.close()
    section_id = row2[0] if row2 else None
    platform_name = "Unknown"
    if section_id:
        sections = get_all_sections()
        platform_name = next((n for i, n in sections if i == section_id), "Unknown")
    name, flag, _ = COUNTRY_CODES.get(country_code, ("Unknown", "🌍", ""))
    flag_emoji_id = _extract_flag_emoji_id(flag)
    platform_emoji_id = get_platform_emoji_id(platform_name) or "5406745015365943482"
    country_flag_emoji = f"{get_flag_plain(flag)}" if flag_emoji_id else get_flag_plain(flag)
    platform_emoji_str = f"🌐"
    msg_text = t("number_selected", user_id,
                 country_flag_emoji=country_flag_emoji,
                 platform_emoji=platform_emoji_str,
                 country_name=name)
    try:
        bot.delete_message(call.message.chat.id, call.message.message_id)
    except:
        pass
    _send_number_msg(call.message.chat.id, msg_text, assigned, file_id, user_id, country_code=country_code, platform_name=platform_name)

@bot.callback_query_handler(func=lambda call: call.data == "back_to_main")
def back_to_main(call):
    user_id = call.from_user.id
    lang = get_user_lang(user_id)
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=2)
    platforms = get_platforms_with_numbers()
    platform_btns = []
    for sid, sname in platforms:
        emoji_id = get_platform_emoji_id(sname)
        count = get_platform_total_numbers(sid)
        PLATFORM_AR = {"whatsapp": "واتساب", "facebook": "فيسبوك", "telegram": "تيليجرام", "instagram": "إنستجرام"}
        if lang == "ar":
            ar_name = PLATFORM_AR.get(sname.lower(), None)
            label = ar_name if ar_name else sname
        else:
            label = sname
        if emoji_id:
            btn = types.InlineKeyboardButton(label, callback_data=f"platform_{sid}", icon_custom_emoji_id=emoji_id)
        else:
            btn = types.InlineKeyboardButton(label, callback_data=f"platform_{sid}")
        platform_btns.append(btn)
    for i in range(0, len(platform_btns), 2):
        markup.row(*platform_btns[i:i+2])
    if is_admin(user_id):
        markup.add(types.InlineKeyboardButton("لوحة الإدارة", callback_data="admin_panel", icon_custom_emoji_id="5433757980245900289", style="success"))
    safe_edit_or_delete(call, t("welcome", user_id), markup=markup, parse_mode="HTML", delete_old=True)

@bot.callback_query_handler(func=lambda call: call.data == "show_terms")
def show_terms(call):
    user_id = call.from_user.id
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(t("back_to_main", user_id), callback_data="back_to_main", icon_custom_emoji_id="5433757980245900289", style="success"))
    safe_edit_or_delete(call, t("terms_text", user_id), markup=markup, parse_mode="HTML")

@bot.callback_query_handler(func=lambda call: call.data == "instructions")
def show_instructions(call):
    user_id = call.from_user.id
    text = t("instructions", user_id) + "\n\n" + t("terms_text", user_id)
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(t("back_to_main", user_id), callback_data="back_to_main", icon_custom_emoji_id="5433757980245900289", style="success"))
    safe_edit_or_delete(call, text, markup=markup, parse_mode="HTML")

def admin_main_menu(uid=None):
    is_on = get_maintenance_mode()
    lang  = get_user_lang(uid)
    ar    = (lang == "ar")

    def _sb(text, cb, icon):
        return {"text": text, "callback_data": cb, "icon_custom_emoji_id": icon, "style": "success"}

    rows = []
    if is_on:
        rows.append([_sb("تشغيل البوت" if ar else "Enable Bot", "admin_toggle_maintenance", "5208634756870199239")])
    else:
        rows.append([_sb("تعطيل البوت" if ar else "Disable Bot", "admin_toggle_maintenance", "5208551919835961928")])

    rows.append([_sb("إدارة الكومبوهات" if ar else "Combo Management", "admin_combo_section", "5990181988558969463")])
    rows.append([_sb("إدارة اللوحات" if ar else "Panels Management", "admin_panels_section", "6113844439292054570")])
    rows.append([_sb("إذاعة" if ar else "Broadcast", "admin_broadcast_section", "5424818078833715060")])
    rows.append([_sb("إدارة المستخدمين" if ar else "User Management", "admin_users_section", "5420323339723881652")])
    rows.append([_sb("إعدادات البوت" if ar else "Bot Settings", "admin_settings", "5258093637450866522")])
    rows.append([_sb("اشتراك إجباري" if ar else "Force Subscribe", "admin_force_sub", "5440660757194744323")])

    return {"inline_keyboard": rows}


@bot.callback_query_handler(func=lambda call: call.data == "admin_combo_section")
def admin_combo_section(call):
    if not is_admin(call.from_user.id): return
    ar = (get_user_lang(call.from_user.id) == "ar")
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.row(
        types.InlineKeyboardButton("إضافه كومبو" if ar else "Add Combo", callback_data="admin_add_combo",
                                   icon_custom_emoji_id="5989994624905648835"),
        types.InlineKeyboardButton("حذف كومبو" if ar else "Delete Combo",   callback_data="admin_del_combo",
                                   icon_custom_emoji_id="5990103326232942988"),
    )
    markup.add(types.InlineKeyboardButton("رجوع" if ar else "Back", callback_data="admin_panel",
                                          icon_custom_emoji_id="5433757980245900289", style="success"))
    title = "إدارة الكومبوهات" if ar else "Combo Management"
    safe_edit_or_delete(call, f"📦 <b>{title}</b>", markup=markup, parse_mode="HTML")


@bot.callback_query_handler(func=lambda call: call.data == "admin_panels_section")
def admin_panels_section(call):
    if not is_admin(call.from_user.id): return
    ar = (get_user_lang(call.from_user.id) == "ar")
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.row(
        types.InlineKeyboardButton("فحص اللوحات" if ar else "Check Panels",   callback_data="admin_check_panels",
                                   icon_custom_emoji_id="6114073270854619005"),
        types.InlineKeyboardButton("إضافة حسابات" if ar else "Add Accounts",  callback_data="admin_panel_accounts",
                                   icon_custom_emoji_id="5989994624905648835"),
    )
    markup.add(types.InlineKeyboardButton("رجوع" if ar else "Back", callback_data="admin_panel",
                                          icon_custom_emoji_id="5433757980245900289", style="success"))
    title = "إدارة اللوحات" if ar else "Panels Management"
    safe_edit_or_delete(call, f"🖥️ <b>{title}</b>", markup=markup, parse_mode="HTML")


@bot.callback_query_handler(func=lambda call: call.data == "admin_broadcast_section")
def admin_broadcast_section(call):
    if not is_admin(call.from_user.id): return
    ar = (get_user_lang(call.from_user.id) == "ar")
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.row(
        types.InlineKeyboardButton("اذاعة للجميع" if ar else "Broadcast All",  callback_data="admin_broadcast_all",
                                   icon_custom_emoji_id="5224736245665511429"),
        types.InlineKeyboardButton("اذاعة لمستخدم" if ar else "Broadcast User", callback_data="admin_broadcast_user",
                                   icon_custom_emoji_id="5208752649427506811"),
    )
    markup.add(types.InlineKeyboardButton("رجوع" if ar else "Back", callback_data="admin_panel",
                                          icon_custom_emoji_id="5433757980245900289", style="success"))
    title = "إذاعة" if ar else "Broadcast"
    safe_edit_or_delete(call,
        f"📢 <b>{title}</b>",
        markup=markup, parse_mode="HTML")


@bot.callback_query_handler(func=lambda call: call.data == "admin_users_section")
def admin_users_section(call):
    if not is_admin(call.from_user.id): return
    ar = (get_user_lang(call.from_user.id) == "ar")
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.row(
        types.InlineKeyboardButton("حظر مستخدم" if ar else "Ban User", callback_data="admin_ban",
                                   icon_custom_emoji_id="5447644880824181073"),
        types.InlineKeyboardButton("فك حظر" if ar else "Unban",     callback_data="admin_unban",
                                   icon_custom_emoji_id="5208634756870199239"),
    )
    markup.row(
        types.InlineKeyboardButton("إضافة ادمن" if ar else "Add Admin", callback_data="admin_add_admin",
                                   icon_custom_emoji_id="5989994624905648835"),
        types.InlineKeyboardButton("إزالة ادمن" if ar else "Remove Admin", callback_data="admin_remove_admin",
                                   icon_custom_emoji_id="5990103326232942988"),
    )
    markup.add(types.InlineKeyboardButton("رجوع" if ar else "Back", callback_data="admin_panel",
                                          icon_custom_emoji_id="5433757980245900289", style="success"))
    title = "إدارة المستخدمين" if ar else "User Management"
    safe_edit_or_delete(call, f"👥 <b>{title}</b>", markup=markup, parse_mode="HTML")

@bot.callback_query_handler(func=lambda call: call.data == "admin_panel")
def admin_panel(call):
    if not is_admin(call.from_user.id):
        return
    uid  = call.from_user.id
    ar   = (get_user_lang(uid) == "ar")
    is_on = get_maintenance_mode()
    status_text  = ("وضع الصيانة" if ar else "Maintenance Mode") if is_on else ("البوت شغال" if ar else "Bot is Running")
    welcome_text = (
        f"═══《🟢 {'اهلا بك في لوحة الأدمن' if ar else 'Welcome to Admin Panel'} 》═══\n\n"
        f"{'الحالة' if ar else 'Status'}: {status_text}"
    )
    markup_dict = admin_main_menu(uid)
    import json as _j
    try:
        requests.post(
            f"https://api.telegram.org/bot{BOT_TOKEN}/editMessageText",
            json={"chat_id": call.message.chat.id, "message_id": call.message.message_id,
                  "text": welcome_text, "reply_markup": _j.dumps(markup_dict), "parse_mode": "HTML"},
            timeout=10
        )
    except:
        try:
            bot.delete_message(call.message.chat.id, call.message.message_id)
        except:
            pass
        requests.post(
            f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
            json={"chat_id": call.message.chat.id, "text": welcome_text,
                  "reply_markup": _j.dumps(markup_dict), "parse_mode": "HTML"},
            timeout=10
        )

@bot.callback_query_handler(func=lambda call: call.data == "admin_toggle_maintenance")
def admin_toggle_maintenance(call):
    if not is_admin(call.from_user.id): return
    current = get_maintenance_mode()
    new_state = not current
    conn = sqlite3.connect(DB_PATH, check_same_thread=False, timeout=10)
    c = conn.cursor()
    c.execute("UPDATE maintenance_mode SET enabled=? WHERE id=1", (1 if new_state else 0,))
    conn.commit()
    conn.close()
    global MAINTENANCE_MODE
    MAINTENANCE_MODE = new_state

    if new_state:
        bot.answer_callback_query(call.id, "تم تفعيل وضع الصيانة", show_alert=True)
    else:
        bot.answer_callback_query(call.id, "تم تشغيل البوت", show_alert=True)

    uid   = call.from_user.id
    ar    = (get_user_lang(uid) == "ar")
    is_on = new_state
    status_label = ("وضع الصيانة" if ar else "Maintenance Mode") if is_on else ("البوت شغال" if ar else "Bot is Running")
    welcome_text = (
        f"═══《🟢 {'اهلا بك في لوحة الأدمن' if ar else 'Welcome to Admin Panel'} 》═══\n\n"
        f"{'الحالة' if ar else 'Status'}: {status_label}"
    )
    markup_dict = admin_main_menu(uid)
    import json as _j
    try:
        requests.post(
            f"https://api.telegram.org/bot{BOT_TOKEN}/editMessageText",
            json={"chat_id": call.message.chat.id, "message_id": call.message.message_id,
                  "text": welcome_text, "reply_markup": _j.dumps(markup_dict), "parse_mode": "HTML"},
            timeout=10
        )
    except:
        pass


@bot.callback_query_handler(func=lambda call: call.data == "admin_add_combo")
def admin_add_combo(call):
    if not is_admin(call.from_user.id): return
    user_states[call.from_user.id] = "waiting_combo_file"
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("رجوع", callback_data="admin_combo_section", icon_custom_emoji_id="5433757980245900289", style="success"))
    safe_edit_or_delete(call,
        f"📤 أرسل ملف الكومبو بصيغة TXT",
        markup=markup, parse_mode="HTML")

@bot.message_handler(content_types=['document'])
def handle_combo_file(message):
    if not is_admin(message.from_user.id): return
    if user_states.get(message.from_user.id) != "waiting_combo_file": return
    try:
        file_info = bot.get_file(message.document.file_id)
        content = bot.download_file(file_info.file_path).decode('utf-8')
        lines = [l.strip() for l in content.splitlines() if l.strip()]
        if not lines:
            bot.reply_to(message, "❌ الملف فارغ!")
            return
        first_num = re.sub(r'\D', '', lines[0])
        country_code = None
        for code in sorted(COUNTRY_CODES.keys(), key=len, reverse=True):
            if first_num.startswith(code):
                country_code = code
                break
        if not country_code:
            bot.reply_to(message, "❌ لا يمكن تحديد الدولة!")
            return
        
        default_name = message.document.file_name or f"combo_{country_code}"
        user_combo_buffer[message.from_user.id] = {
            "country_code": country_code,
            "numbers": lines,
            "default_name": default_name,
            "file_name": default_name
        }
        user_states[message.from_user.id] = "waiting_section_for_combo"
        name, flag, _ = COUNTRY_CODES[country_code]
        plain_flag = get_flag_plain(flag)
        total = len(lines)
        markup = types.InlineKeyboardMarkup(row_width=1)
        all_sections = get_all_sections()
        for sec_id, sec_name in all_sections:
            emoji_id = get_platform_emoji_id(sec_name) or "5406745015365943482"
            markup.add(types.InlineKeyboardButton(
                sec_name,
                callback_data=f"set_combo_sec_{sec_id}",
                icon_custom_emoji_id=emoji_id
            ))
        bot.reply_to(message,
            f"✅ <b>تم التعرف على الدولة تلقائياً</b>\n\n"
            f"{plain_flag} <b>{name}</b>\n"
            f"الأرقام: <b>{total}</b>\n\n"
            f"📲 اختر المنصة:",
            reply_markup=markup, parse_mode="HTML")
    except Exception as e:
        bot.reply_to(message, f"❌ خطأ: {e}")


def broadcast_new_combo(country_code, section_id, price, numbers_count, combo_id=None):
    """يذيع رسالة للكل لما يتضاف كومبو جديد"""
    import threading as _th
    name, flag_str, _ = COUNTRY_CODES.get(country_code, ("Unknown", "🌍", ""))
    flag_html = get_flag_html(flag_str)
    flag_plain = get_flag_plain(flag_str)

    # اسم المنصة
    sec_name = ""
    if section_id:
        all_sec = get_all_sections()
        sec_name = next((n for i, n in all_sec if i == section_id), "")

    platform_emoji_id = get_platform_emoji_id(sec_name) if sec_name else None
    platform_emoji_html = (
        f"◾"
        if platform_emoji_id else "◾"
    )
    platform_part = f"{platform_emoji_html} {sec_name}" if sec_name else ""

    price_str = f"${price:.2f}" if price > 0 else "Free"

    # زرار GET NUMBER - يروح على الكومبو مباشرة
    markup = {"inline_keyboard": [[{
        "text": "GET NUMBER",
        "callback_data": f"file_{combo_id}",
        "icon_custom_emoji_id": "5947494995798789024",
        "style": "success"
    }]]}

    def _send_to_all():
        users = get_all_users()
        for uid in users:
            lang = get_user_lang(uid)
            if lang == "ar":
                text = (
                    f"📦 <b>تم إضافة ستوك جديد</b> ✅\n\n"
                    f"{flag_html} <b>{name}</b>  |  {platform_part}\n"
                    f"💰 <b>السعر لكل OTP:</b> <b>{price_str}</b>"
                )
            else:
                text = (
                    f"📦 <b>New Stock Added</b> ✅\n\n"
                    f"{flag_html} <b>{name}</b>  |  {platform_part}\n"
                    f"💰 <b>Rate per OTP:</b> <b>{price_str}</b>"
                )
            try:
                requests.post(
                    f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
                    json={"chat_id": uid, "text": text, "parse_mode": "HTML", "reply_markup": markup},
                    timeout=10
                )
            except:
                pass
            time.sleep(0.05)


    _th.Thread(target=_send_to_all, daemon=True).start()

@bot.message_handler(func=lambda msg: user_states.get(msg.from_user.id) == "waiting_combo_price")
def handle_combo_price(message):
    uid = message.from_user.id
    if uid not in user_combo_buffer:
        bot.reply_to(message, "❌ انتهت الجلسة، أعد رفع الملف.")
        user_states.pop(uid, None)
        return
    try:
        price = float(message.text.strip().replace(",", "."))
        if price < 0:
            raise ValueError
    except ValueError:
        _inv_lang = get_user_lang(message.from_user.id)
        _inv_msg = ("⚠️ <b>سعر غير صحيح، اكتب رقم مثل:</b> <code>0.02</code>" if _inv_lang == "ar" else
                    "⚠️ <b>Invalid amount. Please enter a valid number like:</b> <code>0.02</code>")
        bot.reply_to(message, _inv_msg, parse_mode="HTML")
        return
    data = user_combo_buffer.pop(uid)
    combo_id = data.get("last_combo_id")
    country_code = data["country_code"]
    lines = data["numbers"]
    if combo_id:
        conn = sqlite3.connect(DB_PATH, check_same_thread=False, timeout=10)
        c = conn.cursor()
        c.execute("UPDATE combos SET price_per_number=? WHERE id=?", (price, combo_id))
        conn.commit()
        conn.close()
    name, flag, _ = COUNTRY_CODES[country_code]
    plain_flag = get_flag_plain(flag)
    price_str = f"${price:.2f}" if price > 0 else "مجاني"
    msg = ("✅ <b>تم إضافة الكومبو</b>\n\n"
           + str(plain_flag) + " <b>" + str(name) + "</b>\n"
           "الأرقام: <b>" + str(len(lines)) + "</b>\n"
           "السعر: <b>" + str(price_str) + "</b> للرقم")
    bot.reply_to(message, msg, parse_mode="HTML")
    # broadcast للكل
    section_id = data.get("section_id")
    broadcast_new_combo(country_code, section_id, price, len(lines), combo_id=combo_id)
    user_states.pop(uid, None)


@bot.message_handler(func=lambda msg: user_states.get(msg.from_user.id) == "waiting_combo_name")
def handle_combo_name(message):
    user_id = message.from_user.id
    if user_id not in user_combo_buffer:
        bot.reply_to(message, "❌ انتهت الجلسة، أعد رفع الملف.")
        del user_states[user_id]
        return
    if message.text == "/skip":
        file_name = user_combo_buffer[user_id]["default_name"]
    else:
        file_name = message.text.strip() or user_combo_buffer[user_id]["default_name"]
    user_combo_buffer[user_id]["file_name"] = file_name
    user_states[user_id] = "waiting_section_for_combo"
    country_code = user_combo_buffer[user_id]["country_code"]
    name, flag, _ = COUNTRY_CODES[country_code]
    plain_flag = get_flag_plain(flag)
    total = len(user_combo_buffer[user_id]["numbers"])
    markup = types.InlineKeyboardMarkup(row_width=1)
    all_sections = get_all_sections()
    for sec_id, sec_name in all_sections:
        emoji_id = get_platform_emoji_id(sec_name) or "5406745015365943482"
        markup.add(types.InlineKeyboardButton(
            sec_name,
            callback_data=f"set_combo_sec_{sec_id}",
            icon_custom_emoji_id=emoji_id
        ))
    bot.reply_to(message,
        f"✅ <b>تم التعرف على الدولة تلقائياً</b>\n\n"
        f"{plain_flag} <b>{name}</b>\n"
        f"📁 الملف: <code>{file_name}</code>\n"
        f"📞 الأرقام: <b>{total}</b>\n\n"
        f"📲 <b>اختر المنصة:</b>",
        reply_markup=markup, parse_mode="HTML")

@bot.callback_query_handler(func=lambda call: call.data.startswith("set_combo_sec_"))
def set_combo_section_handler(call):
    if not is_admin(call.from_user.id): return
    if call.from_user.id not in user_combo_buffer:
        bot.answer_callback_query(call.id, "❌ انتهت الجلسة، أعد رفع الملف!", show_alert=True)
        return
    uid = call.from_user.id
    data = user_combo_buffer.pop(uid)
    part = call.data[len("set_combo_sec_"):]
    section_id = None if part == "none" else int(part)
    country_code = data["country_code"]
    lines = data["numbers"]
    file_name = data["file_name"]
    save_combo(country_code, lines, section_id=section_id, file_name=file_name)
    name, flag, _ = COUNTRY_CODES[country_code]
    plain_flag = get_flag_plain(flag)
    if section_id:
        sections = get_all_sections()
        sec_name = next((n for i, n in sections if i == section_id), "القسم")
        msg = f"✅ {get_flag_plain(flag)} {name} أُضيف إلى قسم: {sec_name}"
    else:
        msg = f"✅ {get_flag_plain(flag)} {name} أُضيف بدون قسم"
    bot.answer_callback_query(call.id)
    try:
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=None)
    except:
        pass
    conn_last = sqlite3.connect(DB_PATH, check_same_thread=False, timeout=10)
    c_last = conn_last.cursor()
    c_last.execute("SELECT id FROM combos ORDER BY id DESC LIMIT 1")
    last_row = c_last.fetchone()
    conn_last.close()
    if last_row:
        user_combo_buffer[uid] = {"last_combo_id": last_row[0], "country_code": country_code, "numbers": lines, "file_name": file_name, "section_id": section_id}
        user_states[uid] = "waiting_combo_price"
        _lang = get_user_lang(uid)
        if _lang == "ar":
            _price_msg = (
                "💰 <b>اكتب سعر الرقم الواحد بالدولار</b>\n\n"
                + str(plain_flag) + " <b>" + str(name) + "</b> — <b>" + str(len(lines)) + "</b> رقم\n\n"
                "مثال: <code>0.02</code>\n"
                "اكتب <code>0</code> لو مجاني"
            )
        else:
            _price_msg = (
                "💰 <b>Enter price per number in dollars</b>\n\n"
                + str(plain_flag) + " <b>" + str(name) + "</b> — <b>" + str(len(lines)) + "</b> numbers\n\n"
                "Example: <code>0.02</code>\n"
                "Type <code>0</code> if free"
            )
        requests.post(
            f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
            json={"chat_id": uid, "text": _price_msg, "parse_mode": "HTML"},
            timeout=10
        )
    else:
        requests.post(
            f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
            json={"chat_id": uid, "text": msg},
            timeout=10
        )

@bot.callback_query_handler(func=lambda call: call.data == "admin_del_combo")
def admin_del_combo(call):
    if not is_admin(call.from_user.id): return
    bot.answer_callback_query(call.id)
    conn = sqlite3.connect(DB_PATH, check_same_thread=False, timeout=10)
    c = conn.cursor()
    c.execute("SELECT id, country_code, file_name, section_id FROM combos ORDER BY country_code, id")
    rows = c.fetchall()
    conn.close()
    if not rows:
        bot.answer_callback_query(call.id, "❌ لا توجد كومبوهات!", show_alert=True)
        return
    from collections import defaultdict
    country_file_counter = defaultdict(int)
    markup = {"inline_keyboard": []}
    for file_id, country_code, file_name, sec_id in rows:
        if country_code not in COUNTRY_CODES:
            continue
        country_file_counter[country_code] += 1
        file_num = country_file_counter[country_code]
        tag = _generate_unique_combo_tag(country_code, file_num - 1, combo_id=file_id)
        cname_en, flag_str, _ = COUNTRY_CODES[country_code]
        cname = COUNTRY_NAMES_AR.get(country_code, cname_en)
        flag_id = _extract_flag_emoji_id(flag_str)
        tag_display = f" ({tag})" if tag else ""
        btn = {
            "text": f"{cname}{tag_display}" if flag_id else f"{get_flag_plain(flag_str)} {cname}{tag_display}",
            "callback_data": f"del_file_direct_{file_id}"
        }
        if flag_id:
            btn["icon_custom_emoji_id"] = flag_id
        markup["inline_keyboard"].append([btn])
    markup["inline_keyboard"].append([{"text": "رجوع", "callback_data": "admin_combo_section", "icon_custom_emoji_id": "5433757980245900289", "style": "success"}])
    if not markup["inline_keyboard"]:
        bot.answer_callback_query(call.id, "❌ لا توجد كومبوهات!", show_alert=True)
        return
    safe_edit_or_delete(call,
        f"🗑️ <b>اختر الكومبو للحذف:</b>",
        markup=markup, parse_mode="HTML")

@bot.callback_query_handler(func=lambda call: call.data.startswith("del_combo_platform_"))
def admin_del_combo_show_countries(call):
    if not is_admin(call.from_user.id): return
    bot.answer_callback_query(call.id)
    part = call.data[len("del_combo_platform_"):]
    sec_id = None if part == "none" else int(part)
    conn = sqlite3.connect(DB_PATH, check_same_thread=False, timeout=10)
    c = conn.cursor()
    if sec_id is not None:
        c.execute("SELECT id, country_code, file_name FROM combos WHERE section_id=? ORDER BY country_code, id", (sec_id,))
    else:
        c.execute("SELECT id, country_code, file_name FROM combos WHERE section_id IS NULL ORDER BY country_code, id")
    rows = c.fetchall()
    conn.close()
    if not rows:
        bot.answer_callback_query(call.id, "❌ لا توجد كومبوهات في هذه المنصة!", show_alert=True)
        return
    from collections import defaultdict
    country_file_counter = defaultdict(int)
    markup = {"inline_keyboard": []}
    for file_id, country_code, file_name in rows:
        if country_code not in COUNTRY_CODES:
            continue
        country_file_counter[country_code] += 1
        file_num = country_file_counter[country_code]
        tag = _generate_unique_combo_tag(country_code, file_num - 1, combo_id=file_id)
        cname_en, flag_str, _ = COUNTRY_CODES[country_code]
        cname = COUNTRY_NAMES_AR.get(country_code, cname_en)
        flag_id = _extract_flag_emoji_id(flag_str)
        tag_display = f"-{tag}" if tag else ""
        btn = {
            "text": f"{cname}{tag_display}" if flag_id else f"{get_flag_plain(flag_str)} {cname}{tag_display}",
            "callback_data": f"del_file_direct_{file_id}"
        }
        if flag_id:
            btn["icon_custom_emoji_id"] = flag_id
        markup["inline_keyboard"].append([btn])
    markup["inline_keyboard"].append([{"text": "رجوع", "callback_data": "admin_del_combo", "icon_custom_emoji_id": "5433757980245900289", "style": "success"}])
    safe_edit_or_delete(call,
        f"🗑️ <b>اختر الكومبو للحذف:</b>",
        markup=markup, parse_mode="HTML")

@bot.callback_query_handler(func=lambda call: call.data.startswith("del_file_direct_"))
def del_file_direct(call):
    if not is_admin(call.from_user.id): return
    file_id = int(call.data[len("del_file_direct_"):])
    conn = sqlite3.connect(DB_PATH, check_same_thread=False, timeout=10)
    c = conn.cursor()
    c.execute("SELECT country_code, file_name, section_id FROM combos WHERE id=?", (file_id,))
    row = c.fetchone()
    conn.close()
    if not row:
        bot.answer_callback_query(call.id, "❌ الملف غير موجود!", show_alert=True)
        return
    country_code, file_name, sec_id = row
    if delete_combo_file(file_id):
        cname_en, flag_str, _ = COUNTRY_CODES.get(country_code, ("Unknown", "🌍", ""))
        cname = COUNTRY_NAMES_AR.get(country_code, cname_en)
        plain_flag = get_flag_plain(flag_str)
        bot.answer_callback_query(call.id, f"✅ تم حذف {plain_flag} {cname} - {file_name}", show_alert=True)
    else:
        bot.answer_callback_query(call.id, "❌ فشل الحذف!", show_alert=True)
    call.data = "admin_del_combo"
    admin_del_combo(call)

@bot.callback_query_handler(func=lambda call: call.data == "admin_manage_files")
def admin_manage_files(call):
    if not is_admin(call.from_user.id): return
    combos = get_all_combos()
    if not combos:
        bot.answer_callback_query(call.id, "❌ لا توجد دول!", show_alert=True)
        return
    markup = types.InlineKeyboardMarkup()
    for code in combos:
        if code in COUNTRY_CODES:
            name, flag, _ = COUNTRY_CODES[code]
            plain_flag = get_flag_plain(flag)
            markup.add(types.InlineKeyboardButton(f"{plain_flag} {name}", callback_data=f"list_files_{code}"))
    markup.add(types.InlineKeyboardButton("رجوع", callback_data="admin_panel", icon_custom_emoji_id="5433757980245900289", style="success"))
    safe_edit_or_delete(call, "📁 اختر الدولة لعرض ملفاتها:", markup=markup)

@bot.callback_query_handler(func=lambda call: call.data.startswith("list_files_"))
def list_files(call):
    if not is_admin(call.from_user.id): return
    country_code = call.data.split("_", 2)[2]
    files = get_combo_files(country_code)
    if not files:
        bot.answer_callback_query(call.id, "❌ لا توجد ملفات لهذه الدولة!", show_alert=True)
        return
    name, flag, _ = COUNTRY_CODES.get(country_code, ("Unknown", "🌍", ""))
    markup = types.InlineKeyboardMarkup()
    for f in files:
        available = len(get_available_numbers_from_file(f["id"]))
        btn_text = f"{f['file_name']} (إجمالي: {f['total']}, متاح: {available})"
        markup.add(types.InlineKeyboardButton(btn_text, callback_data=f"del_file_{f['id']}"))
    markup.add(types.InlineKeyboardButton("رجوع", callback_data="admin_manage_files", icon_custom_emoji_id="5433757980245900289", style="success"))
    safe_edit_or_delete(call, f"📁 ملفات {flag} {name}:", markup=markup)

@bot.callback_query_handler(func=lambda call: call.data.startswith("del_file_"))
def confirm_delete_file(call):
    if not is_admin(call.from_user.id): return
    file_id = int(call.data.split("_")[2])
    conn = sqlite3.connect(DB_PATH, check_same_thread=False, timeout=10)
    c = conn.cursor()
    c.execute("SELECT file_name FROM combos WHERE id=?", (file_id,))
    row = c.fetchone()
    conn.close()
    if not row:
        bot.answer_callback_query(call.id, "❌ الملف غير موجود!", show_alert=True)
        return
    file_name = row[0]
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("✅ نعم، احذف", callback_data=f"confirm_del_file_{file_id}"))
    markup.add(types.InlineKeyboardButton("❌ لا", callback_data="admin_manage_files"))
    safe_edit_or_delete(call, t("confirm_delete_file", call.from_user.id, file_name=file_name), markup=markup)

@bot.callback_query_handler(func=lambda call: call.data.startswith("confirm_del_file_"))
def delete_file(call):
    if not is_admin(call.from_user.id): return
    file_id = int(call.data.split("_")[3])
    if delete_combo_file(file_id):
        bot.answer_callback_query(call.id, t("file_deleted", call.from_user.id), show_alert=True)
    else:
        bot.answer_callback_query(call.id, "❌ فشل الحذف!", show_alert=True)
    admin_manage_files(call)

@bot.callback_query_handler(func=lambda call: call.data == "admin_stats")
def admin_stats(call):
    if not is_admin(call.from_user.id): return
    total_users = len(get_all_users())
    combos = get_all_combos()
    total_numbers = sum(len(get_combo_files(c)) for c in combos)
    otp_count = len(get_otp_logs())
    text = f"📊 إحصائيات:\n👥 مستخدمون: {total_users}\n🌐 دول: {len(combos)}\n📞 أرقام: {total_numbers}\n🔑 أكواد: {otp_count}"
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("رجوع", callback_data="admin_panel", icon_custom_emoji_id="5433757980245900289", style="success"))
    safe_edit_or_delete(call, text, markup=markup)

def get_otp_logs():
    conn = sqlite3.connect(DB_PATH, check_same_thread=False, timeout=10)
    c = conn.cursor()
    c.execute("SELECT * FROM otp_logs")
    rows = c.fetchall()
    conn.close()
    return rows

@bot.callback_query_handler(func=lambda call: call.data == "admin_full_report")
def admin_full_report(call):
    if not is_admin(call.from_user.id): return
    try:
        report = f"📊 تقرير البوت\n{'='*40}\n"
        conn = sqlite3.connect(DB_PATH, check_same_thread=False, timeout=10)
        c = conn.cursor()
        c.execute("SELECT * FROM users")
        for u in c.fetchall():
            status = "محظور" if u[6] else "نشط"
            report += f"ID:{u[0]} @{u[1] or 'N/A'} | رقم:{u[5] or 'N/A'} | {status}\n"
        report += f"\n{'='*40}\n🔑 الأكواد:\n"
        c.execute("SELECT * FROM otp_logs")
        for lg in c.fetchall():
            report += f"{lg[1]} | {lg[2]} | {lg[4]}\n"
        conn.close()
        with open("sendako_report.txt", "w", encoding="utf-8") as f:
            f.write(report)
        with open("sendako_report.txt", "rb") as f:
            bot.send_document(call.from_user.id, f)
        os.remove("sendako_report.txt")
        bot.answer_callback_query(call.id, "✅ تم الإرسال!", show_alert=True)
    except Exception as e:
        bot.answer_callback_query(call.id, f"❌ {e}", show_alert=True)

@bot.callback_query_handler(func=lambda call: call.data == "admin_ban")
def admin_ban_step1(call):
    if not is_admin(call.from_user.id): return
    user_states[call.from_user.id] = "ban_user"
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("رجوع", callback_data="admin_users_section", icon_custom_emoji_id="5433757980245900289", style="success"))
    safe_edit_or_delete(call,
        f"📋 أرسل ID المستخدم لحظره:",
        markup=markup, parse_mode="HTML")

@bot.message_handler(func=lambda msg: user_states.get(msg.from_user.id) == "ban_user")
def admin_ban_step2(message):
    try:
        uid = int(message.text)
        ban_user(uid)
        user_lang = get_user_lang(uid)
        if user_lang == "en":
            ban_msg = (
                "🚫 "
                "You have been banned from the bot due to violating the instructions."
            )
        else:
            ban_msg = (
                "🚫 "
                "لقد تم حظرك من البوت بسبب مخالفة التعليمات"
            )
        try:
            requests.post(
                f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto",
                json={
                    "chat_id": uid,
                    "photo": "https://k.top4top.io/p_3777jrz225.png",
                    "caption": ban_msg,
                    "parse_mode": "HTML"
                },
                timeout=10
            )
        except:
            try:
                bot.send_message(uid, ban_msg, parse_mode="HTML")
            except:
                pass
        bot.reply_to(message, f"✅ تم حظر {uid}")
        del user_states[message.from_user.id]
    except:
        bot.reply_to(message, "❌ معرف غير صحيح!")

@bot.callback_query_handler(func=lambda call: call.data == "admin_unban")
def admin_unban_step1(call):
    if not is_admin(call.from_user.id): return
    user_states[call.from_user.id] = "unban_user"
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("رجوع", callback_data="admin_users_section", icon_custom_emoji_id="5433757980245900289", style="success"))
    safe_edit_or_delete(call,
        f"📋 أرسل ID المستخدم لفك حظره:",
        markup=markup, parse_mode="HTML")

@bot.message_handler(func=lambda msg: user_states.get(msg.from_user.id) == "unban_user")
def admin_unban_step2(message):
    try:
        uid = int(message.text)
        unban_user(uid)
        user_lang = get_user_lang(uid)
        if user_lang == "en":
            unban_msg = (
                "✅ "
                "Your ban has been lifted from the bot. You can now use the bot. Good luck!"
            )
        else:
            unban_msg = (
                "✅ "
                "لقد تم فك حظرك من البوت يمكنك الان استخدام البوت بالتوفيق"
            )
        try:
            bot.send_message(uid, unban_msg, parse_mode="HTML")
        except:
            pass
        bot.reply_to(message, f"✅ تم فك الحظر عن {uid}")
        del user_states[message.from_user.id]
    except:
        bot.reply_to(message, "❌ معرف غير صحيح!")

@bot.callback_query_handler(func=lambda call: call.data == "admin_broadcast_all")
def admin_broadcast_all_step1(call):
    if not is_admin(call.from_user.id): return
    user_states[call.from_user.id] = "broadcast_all_msg"
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("رجوع", callback_data="admin_broadcast_section",
                                          icon_custom_emoji_id="5433757980245900289", style="success"))
    safe_edit_or_delete(call,
        f"📢 أرسل نص الرسالة عزيزي الادمن :",
        markup=markup, parse_mode="HTML")

@bot.message_handler(func=lambda msg: user_states.get(msg.from_user.id) == "broadcast_all_msg",
                     content_types=["text", "photo", "video", "document", "audio", "sticker", "voice", "animation"])
def handle_broadcast_all(message):
    if not is_admin(message.from_user.id): return
    del user_states[message.from_user.id]
    users = get_all_users()
    ok, fail = 0, 0
    progress = bot.send_message(message.chat.id, "⏳ جاري الإرسال...")
    for user_uid in users:
        try:
            bot.copy_message(int(user_uid), message.chat.id, message.message_id)
            ok += 1
        except:
            fail += 1
    try: bot.delete_message(progress.chat.id, progress.message_id)
    except: pass
    bot.send_message(message.chat.id,
        f"✅ <b>تمت الإذاعة!</b>\n\n📤 نجح: {ok}\n❌ فشل: {fail}", parse_mode="HTML")

@bot.callback_query_handler(func=lambda call: call.data == "broadcast_type_plain")
def broadcast_type_plain(call):
    if not is_admin(call.from_user.id): return
    user_states[call.from_user.id] = "broadcast_all"
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("رجوع", callback_data="admin_broadcast_all", icon_custom_emoji_id="5433757980245900289", style="success"))
    safe_edit_or_delete(call, "📢 أرسل نص الرسالة:", markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == "broadcast_type_copy")
def broadcast_type_copy(call):
    if not is_admin(call.from_user.id): return
    user_states[call.from_user.id] = "broadcast_copy_msg"
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("رجوع", callback_data="admin_broadcast_all", icon_custom_emoji_id="5433757980245900289", style="success"))
    safe_edit_or_delete(call,
        "📤 <b>إذاعة نسخ</b>\n\nأرسل الرسالة اللي تريد نسخها وإذاعتها\n"
        "(تدعم النصوص والصور والفيديو والمستندات وكل أنواع الإيموجي المميزة):",
        markup=markup, parse_mode="HTML")

@bot.callback_query_handler(func=lambda call: call.data == "broadcast_type_forward")
def broadcast_type_forward(call):
    if not is_admin(call.from_user.id): return
    user_states[call.from_user.id] = "broadcast_forward_msg"
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("رجوع", callback_data="admin_broadcast_all", icon_custom_emoji_id="5433757980245900289", style="success"))
    safe_edit_or_delete(call,
        "↪️ <b>إذاعة توجيهية</b>\n\nأرسل الرسالة اللي تريد توجيهها:",
        markup=markup, parse_mode="HTML")

@bot.message_handler(func=lambda msg: user_states.get(msg.from_user.id) == "broadcast_copy_msg",
                     content_types=["text", "photo", "video", "document", "audio", "sticker", "voice"])
def handle_broadcast_copy(message):
    if not is_admin(message.from_user.id): return
    uid = message.from_user.id
    user_states[uid] = {"step": "bc_copy_confirm", "chat_id": message.chat.id, "msg_id": message.message_id}
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(
        types.InlineKeyboardButton("✅ تأكيد", callback_data="bc_copy_confirm"),
        types.InlineKeyboardButton("❌ إلغاء", callback_data="admin_broadcast_all"),
    )
    bot.reply_to(message, "❓ <b>تأكيد إذاعة هذه الرسالة لجميع المستخدمين؟</b>", parse_mode="HTML", reply_markup=markup)

@bot.message_handler(func=lambda msg: user_states.get(msg.from_user.id) == "broadcast_forward_msg",
                     content_types=["text", "photo", "video", "document", "audio", "sticker", "voice"])
def handle_broadcast_forward(message):
    if not is_admin(message.from_user.id): return
    uid = message.from_user.id
    user_states[uid] = {"step": "bc_forward_confirm", "chat_id": message.chat.id, "msg_id": message.message_id}
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(
        types.InlineKeyboardButton("✅ تأكيد", callback_data="bc_forward_confirm"),
        types.InlineKeyboardButton("❌ إلغاء", callback_data="admin_broadcast_all"),
    )
    bot.reply_to(message, "❓ <b>تأكيد توجيه هذه الرسالة لجميع المستخدمين؟</b>", parse_mode="HTML", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == "bc_copy_confirm")
def bc_copy_confirm(call):
    uid = call.from_user.id
    if not is_admin(uid): return
    state = user_states.pop(uid, {})
    if state.get("step") != "bc_copy_confirm": return
    src_chat = state["chat_id"]
    src_msg  = state["msg_id"]
    users = get_all_users()
    ok, fail = 0, 0
    progress = bot.send_message(call.message.chat.id, "⏳ جاري الإرسال...")
    for user_uid in users:
        try:
            bot.copy_message(int(user_uid), src_chat, src_msg)
            ok += 1
        except:
            fail += 1
    try: bot.delete_message(progress.chat.id, progress.message_id)
    except: pass
    bot.send_message(call.message.chat.id,
        f"✅ <b>تمت إذاعة النسخ!</b>\n\n📤 نجح: {ok}\n❌ فشل: {fail}", parse_mode="HTML")

@bot.callback_query_handler(func=lambda call: call.data == "bc_forward_confirm")
def bc_forward_confirm(call):
    uid = call.from_user.id
    if not is_admin(uid): return
    state = user_states.pop(uid, {})
    if state.get("step") != "bc_forward_confirm": return
    src_chat = state["chat_id"]
    src_msg  = state["msg_id"]
    users = get_all_users()
    ok, fail = 0, 0
    progress = bot.send_message(call.message.chat.id, "⏳ جاري التوجيه...")
    for user_uid in users:
        try:
            bot.forward_message(int(user_uid), src_chat, src_msg)
            ok += 1
        except:
            fail += 1
    try: bot.delete_message(progress.chat.id, progress.message_id)
    except: pass
    bot.send_message(call.message.chat.id,
        f"✅ <b>تمت إذاعة التوجيه!</b>\n\n📤 نجح: {ok}\n❌ فشل: {fail}", parse_mode="HTML")

@bot.callback_query_handler(func=lambda call: call.data == "broadcast_type_fancy")
def broadcast_type_fancy(call):
    if not is_admin(call.from_user.id): return
    user_states[call.from_user.id] = "bc_fancy_emoji"
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("رجوع", callback_data="admin_broadcast_all", icon_custom_emoji_id="5433757980245900289", style="success"))
    safe_edit_or_delete(call,
        "✨ <b>إذاعة مميزة - الخطوة 1/3</b>\n\n"
        "أرسل الإيموجي المميز (مثل: 🔥 ⭐ 💎)\n"
        "أو /skip للتخطي:",
        markup=markup, parse_mode="HTML")

@bot.message_handler(func=lambda msg: user_states.get(msg.from_user.id) == "bc_fancy_emoji")
def bc_fancy_step1(message):
    uid = message.from_user.id
    emoji = "" if message.text.strip() == "/skip" else message.text.strip()
    user_states[uid] = {"step": "bc_fancy_text", "emoji": emoji}
    bot.reply_to(message,
        "✨ <b>الخطوة 2/3</b>\n\nأرسل نص الرسالة الرئيسية:",
        parse_mode="HTML")

@bot.message_handler(func=lambda msg: isinstance(user_states.get(msg.from_user.id), dict) and
                     user_states[msg.from_user.id].get("step") == "bc_fancy_text")
def bc_fancy_step2(message):
    uid = message.from_user.id
    user_states[uid]["main_text"] = message.text.strip()
    user_states[uid]["step"] = "bc_fancy_quote"
    bot.reply_to(message,
        "✨ <b>الخطوة 3/3</b>\n\nأرسل نص الاقتباس (سيظهر في إطار blockquote)\n"
        "أو /skip للتخطي:",
        parse_mode="HTML")

@bot.message_handler(func=lambda msg: isinstance(user_states.get(msg.from_user.id), dict) and
                     user_states[msg.from_user.id].get("step") == "bc_fancy_quote")
def bc_fancy_step3(message):
    uid = message.from_user.id
    state = user_states.pop(uid)
    emoji     = state.get("emoji", "")
    main_text = state.get("main_text", "")
    quote     = "" if message.text.strip() == "/skip" else message.text.strip()

    header = f"{emoji} <b>{main_text}</b>" if emoji else f"<b>{main_text}</b>"
    body   = f"\n<blockquote>{quote}</blockquote>" if quote else ""
    final_msg = header + body

    users = get_all_users()
    ok, fail = 0, 0
    for user_uid in users:
        try:
            bot.send_message(user_uid, final_msg, parse_mode="HTML")
            ok += 1
        except:
            fail += 1
    bot.reply_to(message,
        f"✅ <b>تمت الإذاعة المميزة!</b>\n\n"
        f"📤 نجح: {ok}\n❌ فشل: {fail}",
        parse_mode="HTML")

@bot.message_handler(func=lambda msg: user_states.get(msg.from_user.id) == "broadcast_all")
def admin_broadcast_all_step2(message):
    users = get_all_users()
    ok, fail = 0, 0
    for uid in users:
        try:
            bot.send_message(uid, message.text)
            ok += 1
        except:
            fail += 1
    bot.reply_to(message, f"✅ {ok} نجح | ❌ {fail} فشل")
    del user_states[message.from_user.id]

@bot.callback_query_handler(func=lambda call: call.data == "admin_broadcast_user")
def admin_broadcast_user_step1(call):
    if not is_admin(call.from_user.id): return
    user_states[call.from_user.id] = "broadcast_user_id"
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("رجوع", callback_data="admin_broadcast_section",
                                          icon_custom_emoji_id="5433757980245900289", style="success"))
    safe_edit_or_delete(call,
        f"📢 أرسل الـ ID بتاع المستخدم عزيزي الادمن :",
        markup=markup, parse_mode="HTML")

@bot.message_handler(func=lambda msg: user_states.get(msg.from_user.id) == "broadcast_user_id")
def admin_broadcast_user_step2(message):
    if not is_admin(message.from_user.id): return
    try:
        uid = int(message.text.strip())
        user_states[message.from_user.id] = f"broadcast_msg_{uid}"
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("رجوع", callback_data="admin_broadcast_section",
                                              icon_custom_emoji_id="5433757980245900289", style="success"))
        bot.reply_to(message,
            f"📢 أرسل نص الرسالة عزيزي الادمن :",
            parse_mode="HTML", reply_markup=markup)
    except:
        bot.reply_to(message, "❌ معرف غير صحيح!")

@bot.message_handler(func=lambda msg: str(user_states.get(msg.from_user.id, "")).startswith("broadcast_msg_"),
                     content_types=["text", "photo", "video", "document", "audio", "sticker", "voice", "animation"])
def admin_broadcast_user_step3(message):
    if not is_admin(message.from_user.id): return
    uid = int(str(user_states[message.from_user.id]).split("_")[2])
    del user_states[message.from_user.id]
    try:
        bot.copy_message(uid, message.chat.id, message.message_id)
        bot.reply_to(message, f"✅ تم الإرسال لـ {uid}")
    except Exception as e:
        bot.reply_to(message, f"❌ فشل: {e}")

@bot.callback_query_handler(func=lambda call: call.data == "admin_user_info")
def admin_user_info_step1(call):
    if not is_admin(call.from_user.id): return
    user_states[call.from_user.id] = "get_user_info"
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("رجوع", callback_data="admin_panel", icon_custom_emoji_id="5433757980245900289", style="success"))
    safe_edit_or_delete(call, "أدخل معرف المستخدم:", markup=markup)

@bot.message_handler(func=lambda msg: user_states.get(msg.from_user.id) == "get_user_info")
def admin_user_info_step2(message):
    try:
        uid = int(message.text)
        user = get_user(uid)
        if not user:
            bot.reply_to(message, "❌ المستخدم غير موجود!")
        else:
            status = "محظور" if user[6] else "نشط"
            bot.reply_to(message,
                f"👤 معلومات:\n🆔 {user[0]}\n@{user[1] or 'N/A'}\nالرقم: {user[5] or 'N/A'}\nالحالة: {status}")
    except Exception as e:
        bot.reply_to(message, f"❌ {e}")
    del user_states[message.from_user.id]

@bot.callback_query_handler(func=lambda call: call.data == "admin_settings")
def admin_settings(call):
    if not is_admin(call.from_user.id): return
    ar = (get_user_lang(call.from_user.id) == "ar")
    import json as _j
    keyboard = {"inline_keyboard": [
        [
            {"text": "تغيير اللغة" if ar else "Change Language", "callback_data": "admin_change_lang",
             "icon_custom_emoji_id": "5990181988558969463", "style": "success"},
            {"text": "أخطاء البوت" if ar else "Bot Errors", "callback_data": "admin_bot_errors",
             "icon_custom_emoji_id": "5420323339723881652", "style": "success"},
        ],
        [
            {"text": "فحص اللوح" if ar else "Check Panels", "callback_data": "admin_settings_check_panels",
             "icon_custom_emoji_id": "5316977222467206948", "style": "success"},
        ],
        [
            {"text": "رجوع" if ar else "Back", "callback_data": "admin_panel",
             "icon_custom_emoji_id": "5433757980245900289", "style": "success", "style": "success"},
        ],
    ]}
    title = "إعدادات البوت" if ar else "Bot Settings"
    try:
        requests.post(
            f"https://api.telegram.org/bot{BOT_TOKEN}/editMessageText",
            json={"chat_id": call.message.chat.id, "message_id": call.message.message_id,
                  "text": f"⚙️ <b>{title}</b>",
                  "reply_markup": _j.dumps(keyboard), "parse_mode": "HTML"},
            timeout=10
        )
    except:
        requests.post(
            f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
            json={"chat_id": call.message.chat.id,
                  "text": f"⚙️ <b>{title}</b>",
                  "reply_markup": _j.dumps(keyboard), "parse_mode": "HTML"},
            timeout=10
        )

@bot.callback_query_handler(func=lambda call: call.data == "admin_settings_check_panels")
def admin_settings_check_panels(call):
    if not is_admin(call.from_user.id): return
    user_id = call.from_user.id
    ar = (get_user_lang(user_id) == "ar")
    bot.answer_callback_query(call.id, "🔍 جاري الفحص..." if ar else "🔍 Checking...", show_alert=False)

    def run_check():
        all_dash = get_all_active_dashboards()
        lines = []
        ok_count = 0
        warn_count = 0
        fail_count = 0

        for dash in all_dash:
            name  = dash.get("name", "?")
            short = dash.get("short", "??")
            dtype = dash.get("type", "traditional")

            if dtype in ("api_token", "api"):
                status_raw = _real_check_api(dash)
            elif dtype == "ims_panel":
                status_raw = _real_check_ims_panel(dash)
            else:
                status_raw = _real_check_traditional(dash)

            is_working = (status_raw == t("working", None))

            with _panel_last_code_lock:
                last_code = _panel_last_code_time.get(name, 0)
            mins_since = (time.time() - last_code) / 60 if last_code else None

            if is_working:
                if mins_since is not None and mins_since < 60:
                    icon = "✅"
                    note = f"آخر كود: {int(mins_since)}د" if ar else f"Last code: {int(mins_since)}m"
                    ok_count += 1
                elif mins_since is not None:
                    icon = "⚠️"
                    note = f"آخر كود: {int(mins_since//60)}س" if ar else f"Last code: {int(mins_since//60)}h"
                    warn_count += 1
                else:
                    icon = "⚠️"
                    note = "لا يجلب أكواد جديدة" if ar else "No new codes fetched"
                    warn_count += 1
            else:
                icon = "❌"
                note = status_raw
                fail_count += 1

            name_short = name[:16] + "…" if len(name) > 16 else name
            lines.append(f"{icon} <code>{short:<2}</code> <b>{name_short}</b> — <i>{note}</i>")

        all_panel_accounts = load_panel_accounts()
        for sk, site in PANEL_SITES.items():
            accounts = all_panel_accounts.get(sk, {}).get("accounts", [])
            if not accounts:
                continue
            name  = site["name"]
            short = site.get("short", "??")
            with _panel_last_code_lock:
                last_code = _panel_last_code_time.get(name, 0)
            mins_since = (time.time() - last_code) / 60 if last_code else None
            thr_key = f"{sk}_{accounts[0].get('id','')}"
            thr = _panel_threads.get(thr_key)
            thr_alive = thr and thr.is_alive()

            if thr_alive:
                if mins_since is not None and mins_since < 60:
                    icon = "✅"
                    note = f"آخر كود: {int(mins_since)}د" if ar else f"Last code: {int(mins_since)}m"
                    ok_count += 1
                elif mins_since is not None:
                    icon = "⚠️"
                    note = f"شغالة — لا أكواد جديدة ({int(mins_since//60)}س)" if ar else f"Working — no new codes ({int(mins_since//60)}h)"
                    warn_count += 1
                else:
                    icon = "⚠️"
                    note = "شغالة — لا يجلب أكواد جديدة" if ar else "Working — no new codes"
                    warn_count += 1
            else:
                icon = "❌"
                note = "الثريد متوقف" if ar else "Thread stopped"
                fail_count += 1

            name_short = name[:16] + "…" if len(name) > 16 else name
            lines.append(f"{icon} <code>{short:<2}</code> <b>{name_short}</b> — <i>{note}</i>")

        now_str = datetime.now().strftime("%H:%M:%S")
        title = "فحص اللوح" if ar else "Check Panels"
        body = "\n".join(lines) if lines else ("لا توجد لوحات" if ar else "No panels found")
        summary = (
            f"\n{'─'*28}\n"
            f"✅ {ok_count}  "
            f"⚠️ {warn_count}  "
            f"❌ {fail_count}"
        )
        msg = (
            f"🔍 <b>{title}</b>  <code>{now_str}</code>\n"
            f"{'─'*28}\n\n"
            f"{body}"
            f"{summary}"
        )
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton(
            "🔄 إعادة فحص" if ar else "🔄 Refresh",
            callback_data="admin_settings_check_panels"
        ))
        markup.add(types.InlineKeyboardButton(
            "رجوع" if ar else "Back",
            callback_data="admin_settings",
            icon_custom_emoji_id="5433757980245900289", style="success"
        ))
        try:
            safe_edit_or_delete(call, msg, markup=markup, parse_mode="HTML")
        except Exception as e:
            bot.send_message(call.message.chat.id, msg, parse_mode="HTML", reply_markup=markup)

    threading.Thread(target=run_check, daemon=True).start()

@bot.callback_query_handler(func=lambda call: call.data == "admin_bot_errors")
def admin_bot_errors(call):
    if not is_admin(call.from_user.id): return
    ar = (get_user_lang(call.from_user.id) == "ar")
    with _bot_error_lock:
        errors = list(_bot_error_log[-20:])
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(
        "🗑️ مسح السجل" if ar else "🗑️ Clear Log",
        callback_data="admin_clear_errors"
    ))
    markup.add(types.InlineKeyboardButton("رجوع" if ar else "Back", callback_data="admin_settings",
                                          icon_custom_emoji_id="5433757980245900289", style="success"))
    if not errors:
        msg = ("⚠️ <b>أخطاء البوت</b>\n\n"
               "✅ لا توجد أخطاء مسجلة" if ar else
               "⚠️ <b>Bot Errors</b>\n\n"
               "✅ No errors recorded")
    else:
        lines = []
        for e in reversed(errors):
            ico = "⚠️"
            trace = f"\n<code>{e['trace'][:150]}</code>" if e['trace'] else ""
            lines.append(f"{ico} <code>{e['time']}</code>\n{e['msg']}{trace}")
        header = ("⚠️ <b>آخر أخطاء البوت</b>\n\n"
                  if ar else
                  "⚠️ <b>Recent Bot Errors</b>\n\n")
        msg = header + "\n\n─────\n\n".join(lines)
        if len(msg) > 4000:
            msg = msg[:4000] + "\n..."
    safe_edit_or_delete(call, msg, markup=markup, parse_mode="HTML")

@bot.callback_query_handler(func=lambda call: call.data == "admin_clear_errors")
def admin_clear_errors(call):
    if not is_admin(call.from_user.id): return
    with _bot_error_lock:
        _bot_error_log.clear()
    bot.answer_callback_query(call.id, "✅ تم مسح سجل الأخطاء", show_alert=True)
    admin_bot_errors(call)

@bot.callback_query_handler(func=lambda call: call.data == "admin_change_lang")
def admin_change_lang(call):
    if not is_admin(call.from_user.id): return
    current_lang = get_user_lang(call.from_user.id)

    markup = types.InlineKeyboardMarkup(row_width=1)
    btn_ar = types.InlineKeyboardButton("🇸🇦 العربية", callback_data="admin_set_lang_ar")
    btn_en = types.InlineKeyboardButton("🇬🇧 English",  callback_data="admin_set_lang_en")
    if current_lang == "ar":
        btn_ar.icon_custom_emoji_id = "5208634756870199239"
    else:
        btn_en.icon_custom_emoji_id = "5208634756870199239"
    markup.add(btn_ar)
    markup.add(btn_en)
    back_text = "رجوع" if current_lang == "ar" else "Back"
    markup.add(types.InlineKeyboardButton(back_text, callback_data="admin_settings",
                                          icon_custom_emoji_id="5433757980245900289", style="success"))
    title = "يرجي اختيار لغة ادمن" if current_lang == "ar" else "Please select admin language"
    safe_edit_or_delete(call,
        f"🌐 {title}",
        markup=markup, parse_mode="HTML")

@bot.callback_query_handler(func=lambda call: call.data in ["admin_set_lang_ar", "admin_set_lang_en"])
def set_admin_lang(call):
    if not is_admin(call.from_user.id): return
    lang = "ar" if call.data == "admin_set_lang_ar" else "en"
    conn = sqlite3.connect(DB_PATH, check_same_thread=False, timeout=10)
    c = conn.cursor()
    c.execute("UPDATE users SET lang=? WHERE user_id=?", (lang, call.from_user.id))
    conn.commit()
    conn.close()
    label = "العربية" if lang == "ar" else "الإنجليزية"
    bot.answer_callback_query(call.id, f"✅ تم تغيير اللغة إلى {label}", show_alert=True)
    admin_change_lang(call)

@bot.callback_query_handler(func=lambda call: call.data == "admin_set_otp_group")
def admin_set_otp_group_menu(call):
    if not is_admin(call.from_user.id): return
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.row(
        types.InlineKeyboardButton("إضافة جروب", callback_data="otp_group_add",
                                   icon_custom_emoji_id="5989994624905648835"),
        types.InlineKeyboardButton("حذف جروب",   callback_data="otp_group_del",
                                   icon_custom_emoji_id="5420323339723881652"),
    )
    markup.add(types.InlineKeyboardButton("رجوع", callback_data="admin_settings",
                                          icon_custom_emoji_id="5433757980245900289", style="success"))
    safe_edit_or_delete(call,
        "📡 <b>تعيين جروب OTP</b>",
        markup=markup, parse_mode="HTML")

@bot.callback_query_handler(func=lambda call: call.data == "otp_group_add")
def otp_group_add_step1(call):
    if not is_admin(call.from_user.id): return
    user_states[call.from_user.id] = "otp_group_add_id"
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("رجوع", callback_data="admin_set_otp_group",
                                          icon_custom_emoji_id="5433757980245900289", style="success"))
    safe_edit_or_delete(call,
        "📥 يرجي ارسال ID الجروب ورفع البوت مشرف عزيزي الادمن :",
        markup=markup, parse_mode="HTML")

@bot.message_handler(func=lambda msg: user_states.get(msg.from_user.id) == "otp_group_add_id")
def otp_group_add_step2(message):
    if not is_admin(message.from_user.id): return
    del user_states[message.from_user.id]
    try:
        gid = int(message.text.strip())
        try:
            member = bot.get_chat_member(gid, bot.get_me().id)
            if member.status not in ["administrator", "creator"]:
                bot.reply_to(message, "❌ البوت مش مشرف في الجروب! ارفعه مشرف وحاول تاني.")
                return
        except:
            bot.reply_to(message, "❌ تعذر التحقق من الجروب! تأكد من الـ ID وإن البوت موجود فيه.")
            return
        add_bot_group(gid, is_otp_group=1)
        set_otp_group(gid)
        bot.reply_to(message, f"✅ تم إضافة الجروب {gid} وتعيينه كجروب OTP")
        try:
            bot.send_message(gid, "✅ تم تعيين هذا الجروب كجروب OTP. سيتم إرسال الأكواد هنا.")
        except:
            pass
    except:
        bot.reply_to(message, "❌ ID غير صحيح!")

@bot.callback_query_handler(func=lambda call: call.data == "otp_group_del")
def otp_group_del_step1(call):
    if not is_admin(call.from_user.id): return
    user_states[call.from_user.id] = "otp_group_del_id"
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("رجوع", callback_data="admin_set_otp_group",
                                          icon_custom_emoji_id="5433757980245900289", style="success"))
    safe_edit_or_delete(call,
        "🗑️ يرجي ارسال ID الجروب لحذفه :",
        markup=markup, parse_mode="HTML")

@bot.message_handler(func=lambda msg: user_states.get(msg.from_user.id) == "otp_group_del_id")
def otp_group_del_step2(message):
    if not is_admin(message.from_user.id): return
    del user_states[message.from_user.id]
    try:
        gid = str(message.text.strip())
        groups = get_all_bot_groups()
        found = any(str(g[0]) == gid for g in groups)
        if not found:
            bot.reply_to(message, "❌ الجروب ده مش مضاف!")
            return
        conn = sqlite3.connect(DB_PATH, check_same_thread=False, timeout=10)
        c = conn.cursor()
        c.execute("DELETE FROM bot_groups WHERE group_id=?", (gid,))
        conn.commit()
        conn.close()
        bot.reply_to(message, f"✅ تم حذف الجروب {gid}")
    except:
        bot.reply_to(message, "❌ ID غير صحيح!")

@bot.callback_query_handler(func=lambda call: call.data == "admin_force_sub")
def admin_force_sub(call):
    if not is_admin(call.from_user.id): return
    channels = get_all_force_sub_channels(enabled_only=False)
    text = f"🔗 <b>ادارة الاشتراك الإجباري</b>\nإجمالي: {len(channels)}\n"
    markup = types.InlineKeyboardMarkup()
    for ch_id, url, desc in channels:
        conn = sqlite3.connect(DB_PATH, check_same_thread=False, timeout=10)
        c = conn.cursor()
        c.execute("SELECT enabled FROM force_sub_channels WHERE id=?", (ch_id,))
        enabled = c.fetchone()[0]
        conn.close()
        status = "✅" if enabled else "❌"
        markup.add(types.InlineKeyboardButton(f"{status} {desc or url[:25]}", callback_data=f"edit_force_ch_{ch_id}"))
    markup.row(
        types.InlineKeyboardButton("إضافة قناه", callback_data="add_force_ch",
                                   icon_custom_emoji_id="5989994624905648835"),
        types.InlineKeyboardButton("إزالة قناة", callback_data="remove_force_ch_step1",
                                   icon_custom_emoji_id="5990103326232942988"),
    )
    markup.add(types.InlineKeyboardButton("رجوع", callback_data="admin_panel", icon_custom_emoji_id="5433757980245900289", style="success"))
    safe_edit_or_delete(call, text, markup=markup, parse_mode="HTML")

@bot.callback_query_handler(func=lambda call: call.data == "add_force_ch")
def add_force_ch_step1(call):
    if not is_admin(call.from_user.id): return
    user_states[call.from_user.id] = "add_force_ch_url"
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("رجوع", callback_data="admin_force_sub", icon_custom_emoji_id="5433757980245900289", style="success"))
    safe_edit_or_delete(call,
        "📝 يرجي ارسال لينك القناة عزيزي الادمن",
        markup=markup, parse_mode="HTML")

@bot.message_handler(func=lambda msg: user_states.get(msg.from_user.id) == "add_force_ch_url")
def add_force_ch_step2(message):
    url = message.text.strip()
    if not (url.startswith("@") or url.startswith("https://t.me/")):
        bot.reply_to(message, "❌ رابط غير صالح!")
        return
    existing = get_all_force_sub_channels(enabled_only=False)
    ch_num = len(existing) + 1
    auto_name_en = f"Join Channel {ch_num}"
    if "/+" in url:
        user_states[message.from_user.id] = {"step": "add_force_ch_id", "url": url, "name": auto_name_en, "num": ch_num}
        bot.reply_to(message, "🔗 رابط دعوة - أرسل ID القناة (مثال: -1001234567890)\nأو أرسل 0 لتخطي التحقق:", parse_mode="HTML")
        return
    del user_states[message.from_user.id]
    if add_force_sub_channel(url, auto_name_en):
        bot.reply_to(message, f"✅ تم إضافة القناة بنجاح", parse_mode="HTML")
    else:
        bot.reply_to(message, "❌ القناة موجودة مسبقاً!")

@bot.message_handler(func=lambda msg: isinstance(user_states.get(msg.from_user.id), dict) and user_states[msg.from_user.id].get("step") == "add_force_ch_id")
def add_force_ch_step3_id(message):
    data = user_states[message.from_user.id]
    ch_id_input = message.text.strip()
    del user_states[message.from_user.id]
    channel_id = None if ch_id_input == "0" else ch_id_input
    conn = sqlite3.connect(DB_PATH, check_same_thread=False, timeout=10)
    c = conn.cursor()
    try:
        c.execute("INSERT INTO force_sub_channels (channel_url, description, enabled, channel_id) VALUES (?,?,1,?)",
                  (data["url"], data["name"], channel_id))
        conn.commit()
        conn.close()
        bot.reply_to(message, f"✅ تم إضافة القناة بنجاح" + (f"\nID: {channel_id}" if channel_id else ""), parse_mode="HTML")
    except Exception as e:
        conn.close()
        bot.reply_to(message, f"❌ القناة موجودة مسبقاً!")

@bot.callback_query_handler(func=lambda call: call.data == "remove_force_ch_step1")
def remove_force_ch_step1(call):
    if not is_admin(call.from_user.id): return
    user_states[call.from_user.id] = "remove_force_ch_url"
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("رجوع", callback_data="admin_force_sub", icon_custom_emoji_id="5433757980245900289", style="success"))
    safe_edit_or_delete(call,
        "📝 يرجي ارسال لينك القناة عزيزي الادمن",
        markup=markup, parse_mode="HTML")

@bot.message_handler(func=lambda msg: user_states.get(msg.from_user.id) == "remove_force_ch_url")
def remove_force_ch_step2(message):
    url = message.text.strip()
    if message.from_user.id in user_states:
        del user_states[message.from_user.id]
    conn = sqlite3.connect(DB_PATH, check_same_thread=False, timeout=10)
    c = conn.cursor()
    c.execute("SELECT id FROM force_sub_channels WHERE channel_url=?", (url,))
    row = c.fetchone()
    if not row:
        conn.close()
        bot.reply_to(message, "❌ القناة غير موجودة!")
        return
    ch_id = row[0]
    c.execute("DELETE FROM force_sub_channels WHERE id=?", (ch_id,))
    conn.commit()
    conn.close()
    bot.reply_to(message, "✅ تم إزالة القناه بنجاح", parse_mode="HTML")

@bot.callback_query_handler(func=lambda call: call.data.startswith("edit_force_ch_"))
def edit_force_ch(call):
    if not is_admin(call.from_user.id): return
    ch_id = int(call.data.split("_", 3)[3])
    conn = sqlite3.connect(DB_PATH, check_same_thread=False, timeout=10)
    c = conn.cursor()
    c.execute("SELECT channel_url,description,enabled FROM force_sub_channels WHERE id=?", (ch_id,))
    row = c.fetchone()
    conn.close()
    if not row:
        bot.answer_callback_query(call.id, "❌ غير موجودة!", show_alert=True)
        return
    url, desc, enabled = row
    markup = types.InlineKeyboardMarkup()
    if enabled:
        markup.add(types.InlineKeyboardButton("❌ تعطيل", callback_data=f"toggle_ch_{ch_id}"))
    else:
        markup.add(types.InlineKeyboardButton("✅ تفعيل", callback_data=f"toggle_ch_{ch_id}"))
    markup.add(types.InlineKeyboardButton("🗑️ حذف", callback_data=f"del_ch_{ch_id}"))
    markup.add(types.InlineKeyboardButton("رجوع", callback_data="admin_force_sub", icon_custom_emoji_id="5433757980245900289", style="success"))
    safe_edit_or_delete(call, f"القناة: {url}\nالوصف: {desc or '—'}\nالحالة: {'مفعلة' if enabled else 'معطلة'}", markup=markup)

@bot.callback_query_handler(func=lambda call: call.data.startswith("toggle_ch_"))
def toggle_ch(call):
    ch_id = int(call.data.split("_", 2)[2])
    toggle_force_sub_channel(ch_id)
    bot.answer_callback_query(call.id, "🔄 تم تغيير الحالة", show_alert=True)
    admin_force_sub(call)

@bot.callback_query_handler(func=lambda call: call.data.startswith("del_ch_"))
def del_ch(call):
    ch_id = int(call.data.split("_", 2)[2])
    if delete_force_sub_channel(ch_id):
        bot.answer_callback_query(call.id, "✅ تم الحذف!", show_alert=True)
    else:
        bot.answer_callback_query(call.id, "❌ فشل الحذف!", show_alert=True)
    admin_force_sub(call)

@bot.callback_query_handler(func=lambda call: call.data == "admin_private_combo")
def admin_private_combo(call):
    if not is_admin(call.from_user.id): return
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("➕ إضافة كومبو برايفت", callback_data="add_private_combo"))
    markup.add(types.InlineKeyboardButton("🗑️ مسح كومبو برايفت", callback_data="del_private_combo"))
    markup.add(types.InlineKeyboardButton("رجوع", callback_data="admin_panel", icon_custom_emoji_id="5433757980245900289", style="success"))
    safe_edit_or_delete(call, "👤 كومبو برايفت:", markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == "add_private_combo")
def add_private_combo_step1(call):
    if not is_admin(call.from_user.id): return
    user_states[call.from_user.id] = "add_private_user_id"
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("رجوع", callback_data="admin_private_combo", icon_custom_emoji_id="5433757980245900289", style="success"))
    safe_edit_or_delete(call, "أدخل معرف المستخدم:", markup=markup)

@bot.message_handler(func=lambda msg: user_states.get(msg.from_user.id) == "add_private_user_id")
def add_private_combo_step2(message):
    try:
        uid = int(message.text)
        user_states[message.from_user.id] = f"add_private_country_{uid}"
        markup = types.InlineKeyboardMarkup(row_width=2)
        buttons = []
        for code in get_all_combos():
            if code in COUNTRY_CODES:
                name, flag, _ = COUNTRY_CODES[code]
                plain_flag = get_flag_plain(flag)
                buttons.append(types.InlineKeyboardButton(f"{plain_flag} {name}", callback_data=f"select_private_{uid}_{code}"))
        for i in range(0, len(buttons), 2):
            markup.row(*buttons[i:i+2])
        markup.add(types.InlineKeyboardButton("رجوع", callback_data="admin_private_combo", icon_custom_emoji_id="5433757980245900289", style="success"))
        bot.reply_to(message, "اختر الدولة:", reply_markup=markup)
    except:
        bot.reply_to(message, "❌ معرف غير صحيح!")

@bot.callback_query_handler(func=lambda call: call.data.startswith("select_private_"))
def select_private_combo(call):
    parts = call.data.split("_")
    uid = int(parts[2])
    country_code = parts[3]
    save_user(uid, private_combo_country=country_code)
    name, flag, _ = COUNTRY_CODES[country_code]
    bot.answer_callback_query(call.id, f"✅ تم: {uid} - {flag} {name}", show_alert=True)
    admin_private_combo(call)

@bot.callback_query_handler(func=lambda call: call.data == "del_private_combo")
def del_private_combo_step1(call):
    if not is_admin(call.from_user.id): return
    user_states[call.from_user.id] = "del_private_user_id"
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("رجوع", callback_data="admin_private_combo", icon_custom_emoji_id="5433757980245900289", style="success"))
    safe_edit_or_delete(call, "أدخل معرف المستخدم:", markup=markup)

@bot.message_handler(func=lambda msg: user_states.get(msg.from_user.id) == "del_private_user_id")
def del_private_combo_step2(message):
    try:
        uid = int(message.text)
        save_user(uid, private_combo_country=None)
        bot.reply_to(message, f"✅ تم مسح الكومبو البرايفت لـ {uid}")
    except:
        bot.reply_to(message, "❌ معرف غير صحيح!")
    del user_states[message.from_user.id]

@bot.callback_query_handler(func=lambda call: call.data == "admin_add_admin")
def admin_add_admin_step1(call):
    if not is_admin(call.from_user.id): return
    user_states[call.from_user.id] = "add_admin_id"
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("رجوع", callback_data="admin_users_section", icon_custom_emoji_id="5433757980245900289", style="success"))
    safe_edit_or_delete(call,
        "📝 أرسل ID المستخدم لاضافته ادمن :",
        markup=markup, parse_mode="HTML")

@bot.message_handler(func=lambda msg: user_states.get(msg.from_user.id) == "add_admin_id")
def admin_add_admin_step2(message):
    try:
        uid = int(message.text.strip())
        uname = ""
        lang = "ar"
        try:
            chat = bot.get_chat(uid)
            uname = chat.username or ""
            conn2 = sqlite3.connect(DB_PATH, check_same_thread=False, timeout=10)
            c2 = conn2.cursor()
            c2.execute("SELECT lang FROM users WHERE user_id=?", (uid,))
            row2 = c2.fetchone()
            conn2.close()
            if row2 and row2[0]:
                lang = row2[0]
        except:
            pass
        if add_db_admin(uid, uname):
            bot.reply_to(message, f"✅ تم إضافة الادمن:\n🆔 {uid}\n👤 @{uname or 'N/A'}")
            try:
                if lang == "ar":
                    notify_text = "👥 انت الان ادمن يمكنك التحكم في البوت عزيزي الادمن"
                else:
                    notify_text = "👥 You are now an admin, you can control the bot dear admin"
                bot.send_message(uid, notify_text, parse_mode="HTML")
            except:
                pass
        else:
            bot.reply_to(message, "❌ فشل في الإضافة!")
    except:
        bot.reply_to(message, "❌ معرف غير صحيح! أدخل رقم ID فقط.")
    if message.from_user.id in user_states:
        del user_states[message.from_user.id]

@bot.callback_query_handler(func=lambda call: call.data == "admin_remove_admin")
def admin_remove_admin_step1(call):
    if not is_admin(call.from_user.id): return
    user_states[call.from_user.id] = "remove_admin_id"
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("رجوع", callback_data="admin_users_section", icon_custom_emoji_id="5433757980245900289", style="success"))
    safe_edit_or_delete(call,
        "📝 أرسل ID المستخدم لازلته من الادمن :",
        markup=markup, parse_mode="HTML")

@bot.message_handler(func=lambda msg: user_states.get(msg.from_user.id) == "remove_admin_id")
def admin_remove_admin_by_id(message):
    try:
        uid = int(message.text.strip())
        if uid in ADMIN_IDS:
            bot.reply_to(message, "❌ لا يمكن إزالة الأدمن الرئيسي!")
            del user_states[message.from_user.id]
            return
        lang = "ar"
        try:
            conn2 = sqlite3.connect(DB_PATH, check_same_thread=False, timeout=10)
            c2 = conn2.cursor()
            c2.execute("SELECT lang FROM users WHERE user_id=?", (uid,))
            row2 = c2.fetchone()
            conn2.close()
            if row2 and row2[0]:
                lang = row2[0]
        except:
            pass
        remove_db_admin(uid)
        bot.reply_to(message, f"✅ تم إزالة {uid} من الأدمن")
        try:
            if lang == "ar":
                notify_text = "🚫 لقد تم ازالتك من الأدمن"
            else:
                notify_text = "🚫 You have been removed from admin"
            bot.send_message(uid, notify_text, parse_mode="HTML")
        except:
            pass
    except:
        bot.reply_to(message, "❌ معرف غير صحيح! أدخل رقم ID فقط.")
    if message.from_user.id in user_states:
        del user_states[message.from_user.id]

@bot.callback_query_handler(func=lambda call: call.data.startswith("rm_admin_"))
def admin_remove_admin_confirm(call):
    if not is_admin(call.from_user.id): return
    uid = int(call.data.split("_")[2])
    if uid in ADMIN_IDS:
        bot.answer_callback_query(call.id, "❌ لا يمكن إزالة الأدمن الرئيسي!", show_alert=True)
        return
    remove_db_admin(uid)
    bot.answer_callback_query(call.id, f"✅ تم إزالة {uid}", show_alert=True)
    admin_remove_admin_step1(call)

@bot.callback_query_handler(func=lambda call: call.data == "admin_manage_groups")
def admin_manage_groups(call):
    if not is_admin(call.from_user.id): return
    groups = get_bot_groups()
    text = "📱 <b>إدارة الجروبات</b>\n\n"
    if groups:
        for gid, desc, is_otp in groups:
            mark = "🔴 OTP" if is_otp else "⚪️"
            text += f"{mark} {desc or gid} | <code>{gid}</code>\n"
    else:
        text += "❌ لا توجد مجموعات مضافة بعد\n"
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(
        types.InlineKeyboardButton("➕ إضافة مجموعة",      callback_data="admin_add_group"),
        types.InlineKeyboardButton("➖ حذف مجموعة",         callback_data="admin_remove_group"),
        types.InlineKeyboardButton("📬 تعيين جروب OTP",     callback_data="admin_set_otp_group"),
        types.InlineKeyboardButton("رجوع", callback_data="admin_panel", icon_custom_emoji_id="5433757980245900289", style="success"),
    )
    safe_edit_or_delete(call, text, markup=markup, parse_mode="HTML")

@bot.callback_query_handler(func=lambda call: call.data == "admin_set_otp_group")
def admin_set_otp_group(call):
    if not is_admin(call.from_user.id): return
    groups = get_bot_groups()
    if not groups:
        bot.answer_callback_query(call.id, "❌ لا توجد مجموعات! أضف مجموعة أولاً.", show_alert=True)
        return
    markup = types.InlineKeyboardMarkup(row_width=1)
    for gid, desc, is_otp in groups:
        mark = "✅ " if is_otp else ""
        markup.add(types.InlineKeyboardButton(f"{mark}{desc or gid}", callback_data=f"set_otp_gid_{gid}"))
    markup.add(types.InlineKeyboardButton("📝 إدخال ID يدوياً", callback_data="set_otp_group_manual"))
    markup.add(types.InlineKeyboardButton("رجوع", callback_data="admin_manage_groups", icon_custom_emoji_id="5433757980245900289", style="success"))
    safe_edit_or_delete(call, "📬 <b>اختر الجروب اللي سيكون جروب OTP:</b>\n(✅ = الحالي)", markup=markup, parse_mode="HTML")

@bot.callback_query_handler(func=lambda call: call.data.startswith("set_otp_gid_"))
def set_otp_gid(call):
    if not is_admin(call.from_user.id): return
    gid = call.data[len("set_otp_gid_"):]
    set_otp_group(gid)
    bot.answer_callback_query(call.id, f"✅ تم تعيين جروب OTP: {gid}", show_alert=True)
    admin_manage_groups(call)

@bot.callback_query_handler(func=lambda call: call.data == "set_otp_group_manual")
def set_otp_group_manual(call):
    if not is_admin(call.from_user.id): return
    user_states[call.from_user.id] = "waiting_set_otp_group_manual"
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("رجوع", callback_data="admin_set_otp_group", icon_custom_emoji_id="5433757980245900289", style="success"))
    safe_edit_or_delete(call,
        "📬 <b>تعيين جروب OTP يدوياً</b>\n\nأرسل ID المجموعة:\n(مثال: -1001234567890)",
        markup=markup, parse_mode="HTML")

@bot.message_handler(func=lambda msg: user_states.get(msg.from_user.id) == "waiting_set_otp_group_manual")
def handle_set_otp_group_manual(message):
    if not is_admin(message.from_user.id): return
    del user_states[message.from_user.id]
    gid = message.text.strip()
    try:
        gid = str(int(gid))
    except:
        bot.reply_to(message, "❌ ID غير صحيح! يجب أن يكون رقماً مثل -1001234567890")
        return
    set_otp_group(gid)
    bot.reply_to(message, f"✅ <b>تم تعيين جروب OTP!</b>\n\n🆔 Group ID: <code>{gid}</code>", parse_mode="HTML")

@bot.callback_query_handler(func=lambda call: call.data == "admin_add_group")
def admin_add_group_step1(call):
    if not is_admin(call.from_user.id): return
    user_states[call.from_user.id] = "add_group_id"
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("رجوع", callback_data="admin_manage_groups", icon_custom_emoji_id="5433757980245900289", style="success"))
    safe_edit_or_delete(call, "أدخل ID المجموعة أو الرابط:\n(مثال: -1001234567890 أو @username)", markup=markup)

@bot.message_handler(func=lambda msg: user_states.get(msg.from_user.id) == "add_group_id")
def admin_add_group_step2(message):
    gid = message.text.strip()
    desc = ""
    try:
        if gid.startswith("https://t.me/"):
            parts = gid.split("/")
            chat = bot.get_chat("@" + parts[-1])
            gid = str(chat.id)
        elif gid.startswith("@"):
            chat = bot.get_chat(gid)
            gid = str(chat.id)
        else:
            chat = bot.get_chat(int(gid))
            gid = str(chat.id)
        desc = chat.title or ""
        bot_member = bot.get_chat_member(gid, bot.get_me().id)
        if bot_member.status not in ["administrator", "creator"]:
            bot.reply_to(message, "❌ البوت مش أدمن في هذه المجموعة!")
            return
    except Exception as e:
        bot.reply_to(message, f"❌ لا يمكن الوصول إلى المجموعة: {e}")
        return
    user_states[message.from_user.id] = {"step": "add_group_otp", "gid": gid, "desc": desc}
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("✅ نعم (جروب OTP)", callback_data="set_group_otp_yes"))
    markup.add(types.InlineKeyboardButton("❌ لا (مجموعة عادية)", callback_data="set_group_otp_no"))
    bot.reply_to(message, f"✅ وجدت: <b>{desc}</b>\n\nهل هذه هي مجموعة OTP؟", parse_mode="HTML", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data.startswith("set_group_otp_"))
def set_group_otp(call):
    user_id = call.from_user.id
    if user_id not in user_states or not isinstance(user_states[user_id], dict):
        return
    data = user_states[user_id]
    is_otp = 1 if call.data == "set_group_otp_yes" else 0
    if add_bot_group(data["gid"], data["desc"], is_otp):
        if is_otp:
            set_otp_group(data["gid"])
        bot.answer_callback_query(call.id, f"✅ تم إضافة المجموعة", show_alert=True)
    else:
        bot.answer_callback_query(call.id, "❌ فشل الإضافة أو موجودة مسبقاً", show_alert=True)
    del user_states[user_id]
    admin_manage_groups(call)

@bot.callback_query_handler(func=lambda call: call.data == "admin_remove_group")
def admin_remove_group_step1(call):
    if not is_admin(call.from_user.id): return
    groups = get_bot_groups()
    if not groups:
        bot.answer_callback_query(call.id, "❌ لا توجد مجموعات!", show_alert=True)
        return
    markup = types.InlineKeyboardMarkup()
    for gid, desc, is_otp in groups:
        otp_mark = "🔴 " if is_otp else ""
        markup.add(types.InlineKeyboardButton(f"{otp_mark}{desc or gid}", callback_data=f"rm_group_{gid}"))
    markup.add(types.InlineKeyboardButton("رجوع", callback_data="admin_manage_groups", icon_custom_emoji_id="5433757980245900289", style="success"))
    safe_edit_or_delete(call, "اختر المجموعة لحذفها:", markup=markup)

@bot.callback_query_handler(func=lambda call: call.data.startswith("rm_group_"))
def admin_remove_group_confirm(call):
    if not is_admin(call.from_user.id): return
    gid = call.data[len("rm_group_"):]
    if remove_bot_group(gid):
        bot.answer_callback_query(call.id, "✅ تم الحذف", show_alert=True)
    else:
        bot.answer_callback_query(call.id, "❌ فشل الحذف", show_alert=True)
    admin_manage_groups(call)

@bot.callback_query_handler(func=lambda call: call.data == "admin_add_section")
def admin_add_section(call):
    if not is_admin(call.from_user.id): return
    user_states[call.from_user.id] = "waiting_section_names"
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("رجوع", callback_data="admin_panel", icon_custom_emoji_id="5433757980245900289", style="success"))
    safe_edit_or_delete(call,
        "📂 أرسل أسماء الأقسام التي تريد إضافتها\n"
        "(كل اسم في سطر جديد)\n\n"
        "مثال:\nفيسبوك\nواتساب\nتيليغرام",
        markup=markup)

@bot.message_handler(func=lambda msg: user_states.get(msg.from_user.id) == "waiting_section_names")
def handle_section_names(message):
    if not is_admin(message.from_user.id): return
    names = [n.strip() for n in message.text.strip().splitlines() if n.strip()]
    if not names:
        bot.reply_to(message, "❌ لم تُرسل أي أسماء!")
        return
    created = []
    for n in names:
        if create_section(n):
            created.append(n)
    if created:
        bot.reply_to(message, f"✅ تم إنشاء {len(created)} قسم:\n" + "\n".join(f"📂 {n}" for n in created))
    else:
        bot.reply_to(message, "❌ الأقسام موجودة مسبقاً أو حدث خطأ!")
    user_states.pop(message.from_user.id, None)

@bot.callback_query_handler(func=lambda call: call.data == "admin_del_section")
def admin_del_section(call):
    if not is_admin(call.from_user.id): return
    sections = get_all_sections()
    if not sections:
        bot.answer_callback_query(call.id, "❌ لا توجد أقسام!", show_alert=True)
        return
    markup = types.InlineKeyboardMarkup()
    for sid, sname in sections:
        markup.add(types.InlineKeyboardButton(f"🗑️ {sname}", callback_data=f"confirm_del_sec_{sid}"))
    markup.add(types.InlineKeyboardButton("رجوع", callback_data="admin_panel", icon_custom_emoji_id="5433757980245900289", style="success"))
    safe_edit_or_delete(call, "اختر القسم الذي تريد حذفه:", markup=markup)

@bot.callback_query_handler(func=lambda call: call.data.startswith("confirm_del_sec_"))
def confirm_del_section(call):
    if not is_admin(call.from_user.id): return
    sid = int(call.data.split("_")[3])
    delete_section(sid)
    bot.answer_callback_query(call.id, "✅ تم حذف القسم", show_alert=True)
    admin_panel(call)

@bot.callback_query_handler(func=lambda call: call.data == "admin_broadcast_groups")
def admin_broadcast_groups_step1(call):
    if not is_admin(call.from_user.id): return
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(
        types.InlineKeyboardButton("📢 إذاعة نصية عادية",        callback_data="bcg_type_plain"),
        types.InlineKeyboardButton("📤 إذاعة نسخ (copy)",        callback_data="bcg_type_copy"),
        types.InlineKeyboardButton("↪️ إذاعة توجيهية (forward)", callback_data="bcg_type_forward"),
        types.InlineKeyboardButton("رجوع", callback_data="admin_panel", icon_custom_emoji_id="5433757980245900289", style="success"),
    )
    safe_edit_or_delete(call, "📡 <b>إذاعة للجروبات</b>\n\nاختر نوع الإذاعة:", markup=markup, parse_mode="HTML")

@bot.callback_query_handler(func=lambda call: call.data == "bcg_type_plain")
def bcg_type_plain(call):
    if not is_admin(call.from_user.id): return
    user_states[call.from_user.id] = "waiting_broadcast_groups"
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("❌ إلغاء", callback_data="admin_broadcast_groups"))
    safe_edit_or_delete(call, "📢 أرسل الرسالة اللي تريد تذيعها في الجروبات:", markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == "bcg_type_copy")
def bcg_type_copy(call):
    if not is_admin(call.from_user.id): return
    user_states[call.from_user.id] = "bcg_copy_msg"
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("❌ إلغاء", callback_data="admin_broadcast_groups"))
    safe_edit_or_delete(call,
        "📤 <b>إذاعة نسخ للجروبات</b>\n\nأرسل الرسالة (تدعم كل أنواع المحتوى والإيموجي المميزة):",
        markup=markup, parse_mode="HTML")

@bot.callback_query_handler(func=lambda call: call.data == "bcg_type_forward")
def bcg_type_forward(call):
    if not is_admin(call.from_user.id): return
    user_states[call.from_user.id] = "bcg_forward_msg"
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("❌ إلغاء", callback_data="admin_broadcast_groups"))
    safe_edit_or_delete(call,
        "↪️ <b>إذاعة توجيهية للجروبات</b>\n\nأرسل الرسالة اللي تريد توجيهها:",
        markup=markup, parse_mode="HTML")

@bot.message_handler(func=lambda msg: user_states.get(msg.from_user.id) == "bcg_copy_msg",
                     content_types=["text", "photo", "video", "document", "audio", "sticker", "voice"])
def bcg_copy_handler(message):
    if not is_admin(message.from_user.id): return
    del user_states[message.from_user.id]
    groups = get_bot_groups()
    if not groups:
        bot.reply_to(message, "❌ لا توجد مجموعات مضافة!")
        return
    ok, fail = 0, 0
    for gid, desc, _ in groups:
        try:
            me = bot.get_chat_member(gid, bot.get_me().id)
            if me.status in ("administrator", "creator"):
                bot.copy_message(gid, message.chat.id, message.message_id)
                ok += 1
            else:
                fail += 1
        except:
            fail += 1
    bot.reply_to(message, f"📡 تمت إذاعة النسخ للجروبات!\n✅ نجح: {ok}\n❌ فشل: {fail}")

@bot.message_handler(func=lambda msg: user_states.get(msg.from_user.id) == "bcg_forward_msg",
                     content_types=["text", "photo", "video", "document", "audio", "sticker", "voice"])
def bcg_forward_handler(message):
    if not is_admin(message.from_user.id): return
    del user_states[message.from_user.id]
    groups = get_bot_groups()
    if not groups:
        bot.reply_to(message, "❌ لا توجد مجموعات مضافة!")
        return
    ok, fail = 0, 0
    for gid, desc, _ in groups:
        try:
            me = bot.get_chat_member(gid, bot.get_me().id)
            if me.status in ("administrator", "creator"):
                bot.forward_message(gid, message.chat.id, message.message_id)
                ok += 1
            else:
                fail += 1
        except:
            fail += 1
    bot.reply_to(message, f"📡 تمت إذاعة التوجيه للجروبات!\n✅ نجح: {ok}\n❌ فشل: {fail}")

@bot.message_handler(func=lambda msg: user_states.get(msg.from_user.id) == "waiting_broadcast_groups")
def broadcast_groups_step2(message):
    if not is_admin(message.from_user.id): return
    del user_states[message.from_user.id]
    groups = get_bot_groups()
    if not groups:
        bot.reply_to(message, "❌ لا توجد مجموعات أو قنوات مضافة!")
        return
    ok, fail = 0, 0
    for gid, desc, _ in groups:
        try:
            me = bot.get_chat_member(gid, bot.get_me().id)
            if me.status in ("administrator", "creator"):
                bot.send_message(gid, message.text)
                ok += 1
            else:
                fail += 1
        except:
            fail += 1
    bot.reply_to(message, f"📡 تمت الإذاعة!\n✅ نجح: {ok}\n❌ فشل (مش أدمن أو خطأ): {fail}")

@bot.callback_query_handler(func=lambda call: call.data == "admin_auto_delete")
def admin_auto_delete(call):
    if not is_admin(call.from_user.id): return
    chat_del  = get_auto_delete_time(call.message.chat.id)
    otp_del   = get_otp_delete_global()
    text = (
        f"⚙️ <b>إعدادات الحذف التلقائي</b>\n\n"
        f"🗑️ <b>حذف رسائل الجروب:</b> <code>{chat_del}</code> ثانية\n"
        f"🔑 <b>حذف سجل OTP:</b> <code>{otp_del}</code> ثانية\n"
    )
    markup = types.InlineKeyboardMarkup()
    markup.row(
        types.InlineKeyboardButton("✏️ تعديل رسائل الجروب", callback_data="edit_auto_delete"),
        types.InlineKeyboardButton("✏️ تعديل سجل OTP",     callback_data="edit_otp_delete"),
    )
    markup.add(types.InlineKeyboardButton("رجوع", callback_data="admin_panel", icon_custom_emoji_id="5433757980245900289", style="success"))
    safe_edit_or_delete(call, text, markup=markup, parse_mode="HTML")

@bot.callback_query_handler(func=lambda call: call.data == "edit_auto_delete")
def edit_auto_delete(call):
    user_id = call.from_user.id
    user_states[user_id] = "waiting_auto_delete_time"
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("❌ إلغاء", callback_data="admin_auto_delete"))
    safe_edit_or_delete(call, "⏱️ أدخل مدة الحذف لرسائل الجروب بالثواني (مثال: 30):", markup=markup)

@bot.message_handler(func=lambda msg: user_states.get(msg.from_user.id) == "waiting_auto_delete_time")
def set_auto_delete_time_msg(message):
    user_id = message.from_user.id
    try:
        seconds = int(message.text.strip())
        if seconds < 5:
            seconds = 5
        set_auto_delete_time(message.chat.id, seconds)
        bot.reply_to(message, f"✅ تم تعيين مدة حذف رسائل الجروب إلى {seconds} ثانية")
    except:
        bot.reply_to(message, "❌ قيمة غير صالحة")
    del user_states[user_id]

@bot.callback_query_handler(func=lambda call: call.data == "edit_otp_delete")
def edit_otp_delete(call):
    user_id = call.from_user.id
    user_states[user_id] = "waiting_otp_delete_time"
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("❌ إلغاء", callback_data="admin_auto_delete"))
    safe_edit_or_delete(call, "⏱️ أدخل مدة حذف سجل OTP بالثواني (مثال: 30):", markup=markup)

@bot.message_handler(func=lambda msg: user_states.get(msg.from_user.id) == "waiting_otp_delete_time")
def set_otp_delete_time_msg(message):
    user_id = message.from_user.id
    try:
        seconds = int(message.text.strip())
        if seconds < 5:
            seconds = 5
        set_otp_delete_global(seconds)
        bot.reply_to(message, f"✅ تم تعيين مدة حذف سجل OTP إلى {seconds} ثانية")
    except:
        bot.reply_to(message, "❌ قيمة غير صالحة")
    del user_states[user_id]

@bot.callback_query_handler(func=lambda call: call.data == "admin_custom_buttons")
def admin_custom_buttons(call):
    user_id = call.from_user.id
    if not is_admin(user_id): return
    buttons = get_custom_buttons()
    text = "🔘 <b>الأزرار المخصصة</b>\n\n"
    markup = types.InlineKeyboardMarkup()
    for btn in buttons:
        id, btn_text, btn_url = btn
        text += f"• {btn_text} : {btn_url}\n"
        markup.add(types.InlineKeyboardButton(f"🗑️ {btn_text}", callback_data=f"del_custom_btn_{id}"))
    markup.row(
        types.InlineKeyboardButton("➕ إضافة زر", callback_data="add_custom_btn"),
        types.InlineKeyboardButton("رجوع", callback_data="admin_panel", icon_custom_emoji_id="5433757980245900289", style="success")
    )
    safe_edit_or_delete(call, text, markup=markup, parse_mode="HTML")

@bot.callback_query_handler(func=lambda call: call.data == "add_custom_btn")
def add_custom_btn_step1(call):
    user_id = call.from_user.id
    user_states[user_id] = "add_custom_btn_text"
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("❌ إلغاء", callback_data="admin_custom_buttons"))
    safe_edit_or_delete(call, "أدخل نص الزر:", markup=markup)

@bot.message_handler(func=lambda msg: user_states.get(msg.from_user.id) == "add_custom_btn_text")
def add_custom_btn_step2(message):
    user_id = message.from_user.id
    user_states[user_id] = {"step": "add_custom_btn_url", "text": message.text.strip()}
    bot.reply_to(message, "أدخل رابط الزر:")

@bot.message_handler(func=lambda msg: isinstance(user_states.get(msg.from_user.id), dict) and user_states[msg.from_user.id].get("step") == "add_custom_btn_url")
def add_custom_btn_step3(message):
    user_id = message.from_user.id
    add_custom_button(user_states[user_id]["text"], message.text.strip())
    bot.reply_to(message, "✅ تم إضافة الزر")
    del user_states[user_id]

@bot.callback_query_handler(func=lambda call: call.data.startswith("del_custom_btn_"))
def del_custom_btn(call):
    user_id = call.from_user.id
    btn_id = int(call.data.split("_")[3])
    delete_custom_button(btn_id)
    bot.answer_callback_query(call.id, "✅ تم الحذف", show_alert=True)
    admin_custom_buttons(call)

@bot.callback_query_handler(func=lambda call: call.data == "admin_otp_group_buttons")
def admin_otp_group_buttons(call):
    if not is_admin(call.from_user.id): return
    buttons = get_otp_group_buttons()
    text = "📲 <b>إدارة أزرار رسالة OTP بتاعت الجروب</b>\n\n"
    markup = types.InlineKeyboardMarkup()
    for btn in buttons:
        text += f"• {btn['text']} : {btn['url']}\n"
        markup.add(types.InlineKeyboardButton(
            f"✏️ {btn['text']}", callback_data=f"edit_otp_gbtn_{btn['id']}"))
        markup.add(types.InlineKeyboardButton(
            f"🗑️ حذف {btn['text']}", callback_data=f"del_otp_gbtn_{btn['id']}"))
    markup.row(
        types.InlineKeyboardButton("➕ إضافة زر", callback_data="add_otp_gbtn"),
        types.InlineKeyboardButton("رجوع", callback_data="admin_panel", icon_custom_emoji_id="5433757980245900289", style="success")
    )
    safe_edit_or_delete(call, text, markup=markup, parse_mode="HTML")

@bot.callback_query_handler(func=lambda call: call.data == "add_otp_gbtn")
def add_otp_gbtn_step1(call):
    if not is_admin(call.from_user.id): return
    user_states[call.from_user.id] = "add_otp_gbtn_text"
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("❌ إلغاء", callback_data="admin_otp_group_buttons"))
    safe_edit_or_delete(call, "أدخل نص الزر:", markup=markup)

@bot.message_handler(func=lambda msg: user_states.get(msg.from_user.id) == "add_otp_gbtn_text")
def add_otp_gbtn_step2(message):
    user_id = message.from_user.id
    user_states[user_id] = {"step": "add_otp_gbtn_url", "text": message.text.strip()}
    bot.reply_to(message, "أدخل رابط الزر:")

@bot.message_handler(func=lambda msg: isinstance(user_states.get(msg.from_user.id), dict) and user_states[msg.from_user.id].get("step") == "add_otp_gbtn_url")
def add_otp_gbtn_step3(message):
    user_id = message.from_user.id
    add_otp_group_button(user_states[user_id]["text"], message.text.strip())
    bot.reply_to(message, "✅ تم إضافة الزر")
    del user_states[user_id]

@bot.callback_query_handler(func=lambda call: call.data.startswith("del_otp_gbtn_"))
def del_otp_gbtn(call):
    if not is_admin(call.from_user.id): return
    btn_id = int(call.data.split("_")[3])
    delete_otp_group_button(btn_id)
    bot.answer_callback_query(call.id, "✅ تم الحذف", show_alert=True)
    admin_otp_group_buttons(call)

@bot.callback_query_handler(func=lambda call: call.data.startswith("edit_otp_gbtn_"))
def edit_otp_gbtn_step1(call):
    if not is_admin(call.from_user.id): return
    btn_id = int(call.data.split("_")[3])
    markup = types.InlineKeyboardMarkup()
    markup.row(
        types.InlineKeyboardButton("✏️ تعديل الاسم",  callback_data=f"edit_ogbtn_name_{btn_id}"),
        types.InlineKeyboardButton("🔗 تعديل اللينك", callback_data=f"edit_ogbtn_url_{btn_id}"),
    )
    markup.add(types.InlineKeyboardButton("❌ إلغاء", callback_data="admin_otp_group_buttons"))
    safe_edit_or_delete(call, "ماذا تريد تعديل؟", markup=markup)

@bot.callback_query_handler(func=lambda call: call.data.startswith("edit_ogbtn_name_"))
def edit_ogbtn_name_step(call):
    if not is_admin(call.from_user.id): return
    btn_id = int(call.data.split("_")[3])
    user_states[call.from_user.id] = {"step": "edit_otp_gbtn_text", "btn_id": btn_id}
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("❌ إلغاء", callback_data="admin_otp_group_buttons"))
    safe_edit_or_delete(call, "أدخل الاسم الجديد للزر:", markup=markup)

@bot.callback_query_handler(func=lambda call: call.data.startswith("edit_ogbtn_url_"))
def edit_ogbtn_url_step(call):
    if not is_admin(call.from_user.id): return
    btn_id = int(call.data.split("_")[3])
    user_states[call.from_user.id] = {"step": "edit_otp_gbtn_url", "btn_id": btn_id}
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("❌ إلغاء", callback_data="admin_otp_group_buttons"))
    safe_edit_or_delete(call, "أدخل اللينك الجديد للزر:", markup=markup)

@bot.message_handler(func=lambda msg: isinstance(user_states.get(msg.from_user.id), dict) and user_states[msg.from_user.id].get("step") == "edit_otp_gbtn_text")
def edit_otp_gbtn_text_msg(message):
    user_id = message.from_user.id
    btn_id = user_states[user_id]["btn_id"]
    update_otp_group_button_text(btn_id, message.text.strip())
    bot.reply_to(message, "✅ تم تعديل اسم الزر")
    del user_states[user_id]

@bot.message_handler(func=lambda msg: isinstance(user_states.get(msg.from_user.id), dict) and user_states[msg.from_user.id].get("step") == "edit_otp_gbtn_url")
def edit_otp_gbtn_url_msg(message):
    user_id = message.from_user.id
    btn_id = user_states[user_id]["btn_id"]
    update_otp_group_button_url(btn_id, message.text.strip())
    bot.reply_to(message, "✅ تم تعديل لينك الزر")
    del user_states[user_id]

@bot.callback_query_handler(func=lambda call: call.data == "admin_set_images")
def admin_set_images(call):
    if not is_admin(call.from_user.id): return
    text = "🖼️ إدارة صور البوت\n\n"
    if BOT_IMAGE_BYTES:
        text += "✅ صورة البوت: موجودة\n"
    else:
        text += "❌ صورة البوت: غير موجودة\n"
    if FORCE_SUB_IMAGE_BYTES:
        text += "✅ صورة الاشتراك الإجباري: موجودة\n"
    else:
        text += "❌ صورة الاشتراك الإجباري: غير موجودة\n"
    if MAINTENANCE_IMAGE_BYTES:
        text += "✅ صورة الصيانة: موجودة\n"
    else:
        text += "❌ صورة الصيانة: غير موجودة\n"
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("🖼️ تعيين صورة البوت", callback_data="set_bot_image"))
    if BOT_IMAGE_BYTES:
        markup.add(types.InlineKeyboardButton("🗑️ حذف صورة البوت", callback_data="delete_bot_image"))
    markup.add(types.InlineKeyboardButton("🔗 تعيين صورة الاشتراك", callback_data="set_force_sub_image"))
    if FORCE_SUB_IMAGE_BYTES:
        markup.add(types.InlineKeyboardButton("🗑️ حذف صورة الاشتراك", callback_data="delete_force_sub_image"))
    markup.add(types.InlineKeyboardButton("🔧 تعيين صورة الصيانة", callback_data="set_maintenance_image"))
    if MAINTENANCE_IMAGE_BYTES:
        markup.add(types.InlineKeyboardButton("🗑️ حذف صورة الصيانة", callback_data="delete_maintenance_image"))
    markup.add(types.InlineKeyboardButton("رجوع", callback_data="admin_panel", icon_custom_emoji_id="5433757980245900289", style="success"))
    safe_edit_or_delete(call, text, markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == "set_bot_image")
def set_bot_image(call):
    user_id = call.from_user.id
    user_states[user_id] = "waiting_bot_image"
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("❌ إلغاء", callback_data="admin_set_images"))
    safe_edit_or_delete(call, "أرسل الصورة الآن:", markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == "set_force_sub_image")
def set_force_sub_image(call):
    user_id = call.from_user.id
    user_states[user_id] = "waiting_force_sub_image"
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("❌ إلغاء", callback_data="admin_set_images"))
    safe_edit_or_delete(call, "أرسل الصورة الآن:", markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == "set_maintenance_image")
def set_maintenance_image(call):
    user_id = call.from_user.id
    user_states[user_id] = "waiting_maintenance_image"
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("❌ إلغاء", callback_data="admin_set_images"))
    safe_edit_or_delete(call, "أرسل الصورة الآن:", markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == "delete_bot_image")
def delete_bot_image(call):
    delete_image("bot")
    bot.answer_callback_query(call.id, t("image_deleted", call.from_user.id), show_alert=True)
    admin_set_images(call)

@bot.callback_query_handler(func=lambda call: call.data == "delete_force_sub_image")
def delete_force_sub_image(call):
    delete_image("force_sub")
    bot.answer_callback_query(call.id, t("image_deleted", call.from_user.id), show_alert=True)
    admin_set_images(call)

@bot.callback_query_handler(func=lambda call: call.data == "delete_maintenance_image")
def delete_maintenance_image(call):
    delete_image("maintenance")
    bot.answer_callback_query(call.id, t("image_deleted", call.from_user.id), show_alert=True)
    admin_set_images(call)

@bot.message_handler(content_types=['photo'])
def handle_image(message):
    user_id = message.from_user.id
    if user_id not in user_states:
        return
    state = user_states[user_id]
    if state not in ["waiting_bot_image", "waiting_force_sub_image", "waiting_maintenance_image"]:
        return
    file_id = message.photo[-1].file_id
    file_info = bot.get_file(file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    if state == "waiting_bot_image":
        save_image("bot", downloaded_file)
        bot.reply_to(message, t("image_set", user_id))
    elif state == "waiting_force_sub_image":
        save_image("force_sub", downloaded_file)
        bot.reply_to(message, t("image_set", user_id))
    elif state == "waiting_maintenance_image":
        save_image("maintenance", downloaded_file)
        bot.reply_to(message, t("image_set", user_id))
    del user_states[user_id]

@bot.callback_query_handler(func=lambda call: call.data == "admin_maintenance")
def admin_maintenance(call):
    if not is_admin(call.from_user.id): return
    status = "مفعل" if MAINTENANCE_MODE else "معطل"
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("🔄 تبديل وضع الصيانة", callback_data="toggle_maintenance"))
    markup.add(types.InlineKeyboardButton("رجوع", callback_data="admin_panel", icon_custom_emoji_id="5433757980245900289", style="success"))
    safe_edit_or_delete(call, f"🔧 وضع الصيانة: {status}\n\nاضغط للتبديل:", markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == "toggle_maintenance")
def toggle_maintenance(call):
    if not is_admin(call.from_user.id): return
    global MAINTENANCE_MODE
    new_state = not MAINTENANCE_MODE
    set_maintenance_mode(new_state)
    MAINTENANCE_MODE = new_state
    bot.answer_callback_query(call.id, f"✅ وضع الصيانة الآن {'مفعل' if MAINTENANCE_MODE else 'معطل'}", show_alert=True)
    admin_maintenance(call)

@bot.callback_query_handler(func=lambda call: call.data == "admin_speed_test")
def admin_speed_test(call):
    if not is_admin(call.from_user.id): return
    start = time.time()
    msg = bot.send_message(call.message.chat.id, "⚡ جاري قياس السرعة...")
    end = time.time()
    response_time = (end - start) * 1000
    bot.edit_message_text(f"⏱️ زمن الاستجابة: {response_time:.2f} مللي ثانية", call.message.chat.id, msg.message_id)

@bot.callback_query_handler(func=lambda call: call.data == "admin_dashboards")
def admin_dashboards_list(call):
    if not is_admin(call.from_user.id): return
    dashboards = get_db_dashboards(only_active=False)
    if not dashboards:
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("➕ إضافة حساب", callback_data="add_dashboard"))
        markup.add(types.InlineKeyboardButton("رجوع", callback_data="admin_panel", icon_custom_emoji_id="5433757980245900289", style="success"))
        safe_edit_or_delete(call, t("no_dashboards", call.from_user.id), markup=markup)
        return
    text = "🔐 <b>قائمة حسابات اللوحات</b>\n\n"
    markup = types.InlineKeyboardMarkup()
    for dash in dashboards:
        status = "✅" if dash["is_active"] else "❌"
        text += f"{status} **{dash['name']}** ({dash['short']})\n"
        markup.add(types.InlineKeyboardButton(f"{status} {dash['name']}", callback_data=f"edit_dash_{dash['id']}"))
    markup.add(types.InlineKeyboardButton("➕ إضافة حساب", callback_data="add_dashboard"))
    markup.add(types.InlineKeyboardButton("رجوع", callback_data="admin_panel", icon_custom_emoji_id="5433757980245900289", style="success"))
    safe_edit_or_delete(call, text, markup=markup, parse_mode="HTML")

@bot.callback_query_handler(func=lambda call: call.data == "add_dashboard")
def add_dashboard_step1(call):
    user_id = call.from_user.id
    user_states[user_id] = "add_dash_name"
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("❌ إلغاء", callback_data="admin_dashboards"))
    safe_edit_or_delete(call, "أدخل اسم اللوحة:", markup=markup)

@bot.message_handler(func=lambda msg: user_states.get(msg.from_user.id) == "add_dash_name")
def add_dash_step2(message):
    user_id = message.from_user.id
    user_states[user_id] = {"step": "add_dash_short", "name": message.text.strip()}
    bot.reply_to(message, "أدخل اختصار اللوحة (مثل WS):")

@bot.message_handler(func=lambda msg: isinstance(user_states.get(msg.from_user.id), dict) and user_states[msg.from_user.id].get("step") == "add_dash_short")
def add_dash_step3(message):
    user_id = message.from_user.id
    user_states[user_id]["short"] = message.text.strip()
    user_states[user_id]["step"] = "add_dash_type"
    markup = types.InlineKeyboardMarkup()
    markup.row(
        types.InlineKeyboardButton("Traditional", callback_data="set_dash_type_traditional"),
        types.InlineKeyboardButton("API", callback_data="set_dash_type_api")
    )
    bot.reply_to(message, "اختر نوع اللوحة:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data.startswith("set_dash_type_"))
def add_dash_step4(call):
    user_id = call.from_user.id
    if user_id not in user_states or not isinstance(user_states[user_id], dict):
        return
    dash_type = "traditional" if call.data == "set_dash_type_traditional" else "api"
    user_states[user_id]["type"] = dash_type
    user_states[user_id]["step"] = "add_dash_username"
    safe_edit_or_delete(call, "أدخل اسم المستخدم (اتركه فارغاً إذا كان API):")

@bot.message_handler(func=lambda msg: isinstance(user_states.get(msg.from_user.id), dict) and user_states[msg.from_user.id].get("step") == "add_dash_username")
def add_dash_step5(message):
    user_id = message.from_user.id
    user_states[user_id]["username"] = message.text.strip()
    user_states[user_id]["step"] = "add_dash_password"
    bot.reply_to(message, "أدخل كلمة المرور (اتركها فارغاً إذا كان API):")

@bot.message_handler(func=lambda msg: isinstance(user_states.get(msg.from_user.id), dict) and user_states[msg.from_user.id].get("step") == "add_dash_password")
def add_dash_step6(message):
    user_id = message.from_user.id
    user_states[user_id]["password"] = message.text.strip()
    user_states[user_id]["step"] = "add_dash_token"
    bot.reply_to(message, "أدخل توكن API (إذا كان API، وإلا اتركه فارغاً):")

@bot.message_handler(func=lambda msg: isinstance(user_states.get(msg.from_user.id), dict) and user_states[msg.from_user.id].get("step") == "add_dash_token")
def add_dash_step7(message):
    user_id = message.from_user.id
    user_states[user_id]["token"] = message.text.strip()
    user_states[user_id]["step"] = "add_dash_base_url"
    bot.reply_to(message, "أدخل الرابط الأساسي (base URL) للوحة:")

@bot.message_handler(func=lambda msg: isinstance(user_states.get(msg.from_user.id), dict) and user_states[msg.from_user.id].get("step") == "add_dash_base_url")
def add_dash_step8(message):
    user_id = message.from_user.id
    user_states[user_id]["base_url"] = message.text.strip()
    user_states[user_id]["step"] = "add_dash_ajax"
    bot.reply_to(message, "أدخل مسار AJAX (مثل /agent/res/data_smscdr.php) أو اتركه فارغاً:")

@bot.message_handler(func=lambda msg: isinstance(user_states.get(msg.from_user.id), dict) and user_states[msg.from_user.id].get("step") == "add_dash_ajax")
def add_dash_step9(message):
    user_id = message.from_user.id
    user_states[user_id]["ajax_path"] = message.text.strip()
    user_states[user_id]["step"] = "add_dash_login_page"
    bot.reply_to(message, "أدخل صفحة تسجيل الدخول (مثل /login) أو اتركه فارغاً:")

@bot.message_handler(func=lambda msg: isinstance(user_states.get(msg.from_user.id), dict) and user_states[msg.from_user.id].get("step") == "add_dash_login_page")
def add_dash_step10(message):
    user_id = message.from_user.id
    user_states[user_id]["login_page"] = message.text.strip()
    user_states[user_id]["step"] = "add_dash_login_post"
    bot.reply_to(message, "أدخل مسار POST لتسجيل الدخول (مثل /signin) أو اتركه فارغاً:")

@bot.message_handler(func=lambda msg: isinstance(user_states.get(msg.from_user.id), dict) and user_states[msg.from_user.id].get("step") == "add_dash_login_post")
def add_dash_step11(message):
    user_id = message.from_user.id
    user_states[user_id]["login_post"] = message.text.strip()
    user_states[user_id]["step"] = "add_dash_stats_page"
    bot.reply_to(message, "أدخل صفحة الإحصائيات (مثل /stats) أو اتركه فارغاً:")

@bot.message_handler(func=lambda msg: isinstance(user_states.get(msg.from_user.id), dict) and user_states[msg.from_user.id].get("step") == "add_dash_stats_page")
def add_dash_step12(message):
    user_id = message.from_user.id
    user_states[user_id]["stats_page"] = message.text.strip()
    user_states[user_id]["step"] = "add_dash_idx_date"
    bot.reply_to(message, "أدخل رقم عمود التاريخ (افتراضي 0):")

@bot.message_handler(func=lambda msg: isinstance(user_states.get(msg.from_user.id), dict) and user_states[msg.from_user.id].get("step") == "add_dash_idx_date")
def add_dash_step13(message):
    user_id = message.from_user.id
    try:
        idx_date = int(message.text.strip())
    except:
        idx_date = 0
    user_states[user_id]["idx_date"] = idx_date
    user_states[user_id]["step"] = "add_dash_idx_number"
    bot.reply_to(message, "أدخل رقم عمود الرقم (افتراضي 2):")

@bot.message_handler(func=lambda msg: isinstance(user_states.get(msg.from_user.id), dict) and user_states[msg.from_user.id].get("step") == "add_dash_idx_number")
def add_dash_step14(message):
    user_id = message.from_user.id
    try:
        idx_number = int(message.text.strip())
    except:
        idx_number = 2
    user_states[user_id]["idx_number"] = idx_number
    user_states[user_id]["step"] = "add_dash_idx_sms"
    bot.reply_to(message, "أدخل رقم عمود الرسالة (افتراضي 5):")

@bot.message_handler(func=lambda msg: isinstance(user_states.get(msg.from_user.id), dict) and user_states[msg.from_user.id].get("step") == "add_dash_idx_sms")
def add_dash_step15(message):
    user_id = message.from_user.id
    try:
        idx_sms = int(message.text.strip())
    except:
        idx_sms = 5
    user_states[user_id]["idx_sms"] = idx_sms
    user_states[user_id]["step"] = "add_dash_timeout"
    bot.reply_to(message, "أدخل مهلة الاتصال بالثواني (افتراضي 10):")

@bot.message_handler(func=lambda msg: isinstance(user_states.get(msg.from_user.id), dict) and user_states[msg.from_user.id].get("step") == "add_dash_timeout")
def add_dash_step16(message):
    user_id = message.from_user.id
    try:
        timeout = int(message.text.strip())
    except:
        timeout = 10
    user_states[user_id]["timeout"] = timeout
    user_states[user_id]["step"] = "add_dash_data_keys"
    bot.reply_to(message, "أدخل مفاتيح البيانات بصيغة JSON (مثال: {\"date\":\"dt\",\"number\":\"num\",\"sms\":\"message\"}) أو اتركه فارغاً:")

@bot.message_handler(func=lambda msg: isinstance(user_states.get(msg.from_user.id), dict) and user_states[msg.from_user.id].get("step") == "add_dash_data_keys")
def add_dash_step17(message):
    user_id = message.from_user.id
    data_keys = {}
    if message.text.strip():
        try:
            data_keys = json.loads(message.text.strip())
        except:
            data_keys = {}
    data = user_states[user_id]
    add_dashboard_account(
        name=data["name"],
        short=data["short"],
        username=data["username"],
        password=data["password"],
        api_token=data["token"],
        dash_type=data["type"],
        base_url=data["base_url"],
        ajax_path=data["ajax_path"],
        login_page=data["login_page"],
        login_post=data["login_post"],
        stats_page=data["stats_page"],
        idx_date=data["idx_date"],
        idx_number=data["idx_number"],
        idx_sms=data["idx_sms"],
        timeout=data["timeout"],
        data_keys=data_keys,
        refresh_interval=1
    )
    bot.reply_to(message, f"✅ تم إضافة حساب اللوحة {data['name']} بنجاح")
    del user_states[user_id]

@bot.callback_query_handler(func=lambda call: call.data.startswith("edit_dash_"))
def edit_dash(call):
    dash_id = int(call.data.split("_")[2])
    dashboards = get_db_dashboards(only_active=False)
    dash = next((d for d in dashboards if d["id"] == dash_id), None)
    if not dash:
        bot.answer_callback_query(call.id, "❌ الحساب غير موجود", show_alert=True)
        return
    text = f"🔐 <b>{dash['name']}</b>\n"
    text += f"الاختصار: {dash['short']}\n"
    text += f"النوع: {dash['type']}\n"
    text += f"المستخدم: {dash['username'] or '—'}\n"
    text += f"توكن API: {'موجود' if dash['api_token'] else '—'}\n"
    text += f"الحالة: {'✅ نشط' if dash['is_active'] else '❌ معطل'}\n"
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("🔄 تفعيل/تعطيل", callback_data=f"toggle_dash_{dash_id}"))
    markup.add(types.InlineKeyboardButton("🗑️ حذف", callback_data=f"delete_dash_{dash_id}"))
    markup.add(types.InlineKeyboardButton("رجوع", callback_data="admin_dashboards", icon_custom_emoji_id="5433757980245900289", style="success"))
    safe_edit_or_delete(call, text, markup=markup, parse_mode="HTML")

@bot.callback_query_handler(func=lambda call: call.data.startswith("toggle_dash_"))
def toggle_dash(call):
    dash_id = int(call.data.split("_")[2])
    toggle_dashboard_account(dash_id)
    bot.answer_callback_query(call.id, "✅ تم تبديل حالة الحساب", show_alert=True)
    edit_dash(call)

@bot.callback_query_handler(func=lambda call: call.data.startswith("delete_dash_"))
def delete_dash_confirm(call):
    dash_id = int(call.data.split("_")[2])
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("✅ نعم، احذف", callback_data=f"confirm_delete_dash_{dash_id}"))
    markup.add(types.InlineKeyboardButton("❌ لا", callback_data=f"edit_dash_{dash_id}"))
    safe_edit_or_delete(call, "⚠️ هل أنت متأكد من حذف هذا الحساب؟", markup=markup)

@bot.callback_query_handler(func=lambda call: call.data.startswith("confirm_delete_dash_"))
def confirm_delete_dash(call):
    dash_id = int(call.data.split("_")[3])
    delete_dashboard_account(dash_id)
    bot.answer_callback_query(call.id, "✅ تم الحذف", show_alert=True)
    admin_dashboards_list(call)

def _real_check_ims_panel(dash):
    username = dash.get("username", "").strip()
    password = dash.get("password", "").strip()
    if not username or not password:
        return t("no_username_pass", None)
    dash_timeout = dash.get("timeout", 10)
    try:
        tmp = requests.Session()
        tmp.headers.update({"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"})
        base_url = dash.get("base_url", "")
        login_page = base_url + dash.get("login_page", "/login")
        login_post = base_url + dash.get("login_post", "/signin")
        resp = tmp.get(login_page, timeout=dash_timeout)
        if resp.status_code != 200:
            return t("server_down", None)
        soup = BeautifulSoup(resp.text, "html.parser")
        etkk_input = soup.find("input", {"name": "etkk"})
        etkk_value = etkk_input.get("value", "") if etkk_input else ""
        captcha_answer = None
        m = re.search(r'What is (\d+)\s*\+\s*(\d+)', resp.text, re.IGNORECASE)
        if m:
            captcha_answer = int(m.group(1)) + int(m.group(2))
        else:
            for txt in soup.stripped_strings:
                m2 = re.search(r'(\d+)\s*\+\s*(\d+)', txt)
                if m2:
                    captcha_answer = int(m2.group(1)) + int(m2.group(2))
                    break
        if captcha_answer is None:
            return t("captcha_unknown", None)
        payload = {"username": username, "password": password,
                   "capt": str(captcha_answer), "etkk": etkk_value}
        r2 = tmp.post(login_post, data=payload,
                      headers={"Referer": login_page, "Content-Type": "application/x-www-form-urlencoded"},
                      timeout=dash_timeout, allow_redirects=True)
        if "agent/SMS" in r2.url or "dashboard" in r2.url.lower() or "logout" in r2.text.lower():
            return t("working", None)
        return t("wrong_credentials", None)
    except requests.exceptions.ConnectionError:
        return t("server_down", None)
    except requests.exceptions.Timeout:
        return t("timeout", None)
    except Exception:
        return t("connection_error", None)

def _real_check_traditional(dash):
    username = dash.get("username", "").strip()
    password = dash.get("password", "").strip()
    if not username or not password:
        return t("no_username_pass", None)
    dash_timeout = dash.get("timeout", 10)
    try:
        tmp = requests.Session()
        tmp.headers.update({
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
            "Accept": "text/html,application/xhtml+xml,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.9",
        })
        base_url = dash.get("base_url", "")
        login_page_url = dash.get("login_page_url") or (base_url + dash.get("login_page", ""))
        if not login_page_url:
            return t("no_url", None)
        resp = tmp.get(login_page_url, timeout=dash_timeout)
        if resp.status_code not in (200, 302):
            return t("server_down", None)

        captcha_answer = _solve_captcha(resp.text)
        if captcha_answer is None:
            captcha_answer = ""

        payload = {}
        payload.update(_extract_hidden_fields(resp.text))
        payload["username"] = username
        payload["password"] = password
        payload["capt"] = captcha_answer

        login_post_url = dash.get("login_post_url") or (base_url + dash.get("login_post", ""))
        if not login_post_url:
            return t("no_url", None)
        r2 = tmp.post(login_post_url, data=payload,
                      headers={
                          "Content-Type": "application/x-www-form-urlencoded",
                          "Origin": base_url.rstrip("/"),
                          "Referer": login_page_url,
                          "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
                          "Accept": "text/html,application/xhtml+xml,*/*;q=0.8",
                          "Upgrade-Insecure-Requests": "1",
                      },
                      timeout=max(dash_timeout, 15), allow_redirects=True)
        r2u = r2.url.lower()
        r2t = r2.text.lower()
        is_success = (
            "agent"      in r2u or
            "dashboard"  in r2u or
            "reports"    in r2u or
            "smscdr"     in r2t or
            "logout"     in r2t or
            "signout"    in r2t or
            "/ints/agent" in r2.url or
            "/ints/client" in r2.url or
            ("login" not in r2u and "signin" not in r2u and r2.status_code == 200) or
            (r2.status_code == 200
             and "password" not in r2t
             and "username" not in r2t
             and len(r2.text) > 2000)
        )
        if not is_success:
            for sp in ["/ints/agent/SMSCDRReports", "/agent/SMSCDRReports",
                       "/ints/agent/SMSCDRStats",  "/agent/SMSCDRStats"]:
                try:
                    tr = tmp.get(base_url.rstrip("/") + sp, timeout=8)
                    if (tr.status_code == 200
                            and "login"    not in tr.url.lower()
                            and "signin"   not in tr.url.lower()
                            and "password" not in tr.text.lower()):
                        is_success = True
                        break
                except:
                    pass
        if is_success:
            return t("working", None)
        else:
            return t("wrong_credentials", None)
    except requests.exceptions.ConnectionError:
        return t("server_down", None)
    except requests.exceptions.Timeout:
        return t("timeout", None)
    except Exception:
        return t("connection_error", None)

def _real_check_api(dash):
    url = dash.get("api_url", "").strip()
    token = dash.get("api_token", "").strip()
    if not url:
        return t("no_url", None)
    if not token:
        return t("no_token", None)
    try:
        r = requests.get(url, params={"token": token}, timeout=10)
        if r.status_code == 200 and len(r.text.strip()) > 2:
            return t("working", None)
        return t("http_error", None, code=r.status_code)
    except requests.exceptions.ConnectionError:
        return t("server_down", None)
    except requests.exceptions.Timeout:
        return t("timeout", None)
    except Exception:
        return t("connection_error", None)

def _build_check_panels_msg(user_id, from_cache=False):
    ok_list = []
    fail_list = []

    def _fmt_line(short, name, status, thread_status="", cached=False):
        if status == t("working", None):
            with _panel_last_code_lock:
                last_code = _panel_last_code_time.get(name, 0)
            mins_since = (time.time() - last_code) / 60 if last_code else None

            if mins_since is not None and mins_since < 60:
                icon = "✅"
                code_info = f" | آخر كود: {int(mins_since)}د"
            elif mins_since is not None:
                icon = "⚠️"
                hrs = int(mins_since // 60)
                code_info = f" | آخر كود: {hrs}س"
            else:
                icon = "⚠️"
                code_info = " | لا يجلب أكواد"
        elif ("لا توجد" in status or "لا يوجد" in status or
              "no_token" in status.lower() or "no_url" in status.lower()):
            icon = "⚪"
            code_info = ""
        else:
            icon = "❌"
            code_info = ""
        name_display = name if len(name) <= 14 else name[:13] + "…"
        dots = "·" * max(1, 15 - len(name_display))
        thr = f" {thread_status}" if thread_status else ""
        age = ""
        if cached:
            entry = _panel_check_cache.get(name)
            if entry:
                secs = int(time.time() - entry["ts"])
                age = f" <i>({secs}s)</i>"
        return f"{icon} <code>{short:<2}</code> {name_display}{dots}{thr}│ <i>{status}{code_info}</i>{age}"

    def _get_status(key, fetcher):
        with _panel_check_lock:
            cached = _panel_check_cache.get(key)
        if from_cache and cached:
            return cached["status"]
        status = fetcher()
        with _panel_check_lock:
            _panel_check_cache[key] = {"status": status, "ts": time.time()}
        return status

    rows_static = []
    all_dashboards = get_all_active_dashboards()
    for dash in all_dashboards:
        name  = dash["name"]
        short = dash.get("short", "??")
        dtype = dash.get("type", "traditional")
        d = dash  # capture for lambda
        if dtype in ("api_token", "api"):
            status = _get_status(name, lambda d=d: _real_check_api(d))
        elif dtype == "ims_panel":
            status = _get_status(name, lambda d=d: _real_check_ims_panel(d))
        else:
            status = _get_status(name, lambda d=d: _real_check_traditional(d))
        if status == t("working", None):
            ok_list.append(name)
        else:
            fail_list.append(name)
        rows_static.append(_fmt_line(short, name, status, cached=from_cache))

    rows_dynamic = []
    all_panel_accounts = load_panel_accounts()
    for sk, site in PANEL_SITES.items():
        accounts = all_panel_accounts.get(sk, {}).get("accounts", [])
        short = site.get("short", "??")
        name  = site["name"]
        dtype = site.get("type", "traditional")
        if not accounts:
            rows_dynamic.append(_fmt_line(short, name, "⚪ لا توجد حسابات"))
            continue
        for acc in accounts:
            uname = acc.get("username", "API")
            label = f"{name} / {uname}"
            cache_key = f"dyn_{sk}_{acc.get('id','')}"
            if dtype in ("api", "api_token"):
                fake_dash = {
                    "name": label,
                    "api_url":   site.get("api_url", ""),
                    "api_token": acc.get("api_token") or site.get("api_token", ""),
                }
                status = _get_status(cache_key, lambda fd=fake_dash: _real_check_api(fd))
            elif dtype == "ims_panel":
                fake_dash = {
                    "name": label, "type": dtype,
                    "username": acc.get("username", ""),
                    "password": acc.get("password", ""),
                    "base_url":       site.get("base_url", ""),
                    "login_page":     site.get("login_page", ""),
                    "login_post":     site.get("login_post", ""),
                    "dashboard_path": site.get("dashboard_path", ""),
                    "timeout":        site.get("timeout", 10),
                }
                status = _get_status(cache_key, lambda fd=fake_dash: _real_check_ims_panel(fd))
            else:
                _base = site.get("base_url", "").rstrip("/")
                _lp   = site.get("login_page", "")
                _lpo  = site.get("login_post", "")
                fake_dash = {
                    "name": label, "type": dtype,
                    "username": acc.get("username", ""),
                    "password": acc.get("password", ""),
                    "base_url":       _base,
                    "login_page":     _lp,
                    "login_post":     _lpo,
                    "login_page_url": site.get("login_page_url") or (_base + _lp),
                    "login_post_url": site.get("login_post_url") or (_base + _lpo),
                    "ajax_path":      site.get("ajax_path", ""),
                    "timeout":        site.get("timeout", 10),
                }
                status = _get_status(cache_key, lambda fd=fake_dash: _real_check_traditional(fd))
            key = f"{sk}_{acc['id']}"
            thr = _panel_threads.get(key)
            thr_icon = "🟢" if thr and thr.is_alive() else "🔴"
            if status == t("working", None):
                ok_list.append(label)
            else:
                fail_list.append(label)
            rows_dynamic.append(_fmt_line(short, label, status, thr_icon, cached=from_cache))


    now_str = datetime.now().strftime("%H:%M:%S")
    cache_note = " 🕐 <i>(كاش)</i>" if from_cache else ""
    header = (
        f"🖥️ <b>فحص اللوحات</b>  <code>{now_str}</code>{cache_note}\n"
        f"{'─' * 32}\n"
    )

    static_block  = "\n".join(rows_static)
    dynamic_block = "\n".join(rows_dynamic)

    body = (
        f"<blockquote expandable>"
        f"⚙️ <b>إعدادات اللوح</b>\n\n"
        f"📌 <b>اللوحات الثابتة</b> ({len(rows_static)})\n\n"
        f"{static_block}"
        f"</blockquote>\n\n"
    )
    if rows_dynamic:
        body += (
            f"<blockquote expandable>"
            f"🆕 <b>لوحات الأدمن</b> ({len(rows_dynamic)})\n\n"
            f"{dynamic_block}"
            f"</blockquote>"
        )

    summary = (
        f"\n{'─' * 32}\n"
        f"✅ <b>شغالة:</b> {len(ok_list)}   "
        f"❌ <b>مش شغالة:</b> {len(fail_list)}"
    )
    return header + body + summary


@bot.callback_query_handler(func=lambda call: call.data == "admin_check_panels")
def admin_check_panels(call):
    if not is_admin(call.from_user.id):
        return

    user_id = call.from_user.id

    with _panel_check_lock:
        has_cache = bool(_panel_check_cache)
        if has_cache:
            oldest = min((v["ts"] for v in _panel_check_cache.values()), default=0)
            cache_age = time.time() - oldest
            cache_fresh = cache_age < 90
        else:
            cache_fresh = False

    if cache_fresh:
        bot.answer_callback_query(call.id, "⚡ بيعرض الكاش ويحدّث في الخلفية…", show_alert=False)
        try:
            cached_msg = _build_check_panels_msg(user_id, from_cache=True)
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton(t("refresh", user_id), callback_data="admin_check_panels"))
            markup.add(types.InlineKeyboardButton(t("back", user_id), callback_data="admin_panels_section", icon_custom_emoji_id="5433757980245900289", style="success"))
            safe_edit_or_delete(call, cached_msg, markup=markup, parse_mode="HTML")
        except Exception:
            pass
        def _bg_refresh():
            _build_check_panels_msg(user_id, from_cache=False)
        threading.Thread(target=_bg_refresh, daemon=True).start()
        return

    bot.answer_callback_query(call.id, t("checking", user_id), show_alert=False)

    def run_check():
        full_msg = _build_check_panels_msg(user_id, from_cache=False)

        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton(t("refresh", user_id), callback_data="admin_check_panels"))
        markup.add(types.InlineKeyboardButton(t("back", user_id), callback_data="admin_panels_section", icon_custom_emoji_id="5433757980245900289", style="success"))
        try:
            safe_edit_or_delete(call, full_msg, markup=markup, parse_mode="HTML")
        except Exception:
            bot.send_message(call.message.chat.id, full_msg, parse_mode="HTML", reply_markup=markup)

    threading.Thread(target=run_check, daemon=True).start()


def _extract_hidden_fields(html_text):
    fields = {}
    try:
        soup = BeautifulSoup(html_text, "html.parser")
        form = soup.find("form")
        inputs = form.find_all("input") if form else soup.find_all("input")
        skip = {"username", "password", "capt", "submit", ""}
        for inp in inputs:
            name  = inp.get("name", "")
            itype = inp.get("type", "text").lower()
            val   = inp.get("value", "")
            if name and name not in skip and itype == "hidden":
                fields[name] = val
    except:
        for name_tok in ["crlf", "_token", "etkk"]:
            pat1 = 'name=["\']' + name_tok + '["\'][^>]*value=["\']([^"\']+)["\']'
            pat2 = 'value=["\']([^"\']+)["\'][^>]*name=["\']' + name_tok + '["\']'
            m = re.search(pat1, html_text) or re.search(pat2, html_text)
            if m:
                fields[name_tok] = m.group(1)
    return fields

def _solve_captcha(html_content):
    patterns = [
        r'(\d+)\s*([+\-*/])\s*(\d+)\s*=?\s*\?',
        r'What is\s*(\d+)\s*([+\-*/])\s*(\d+)\?',
        r'(\d+)\s*([+\-*/])\s*(\d+)\s*=',
        r'(\d+)\s*([+\-*/])\s*(\d+)'
    ]
    for pattern in patterns:
        m = re.search(pattern, html_content, re.IGNORECASE)
        if m:
            n1, op, n2 = int(m.group(1)), m.group(2), int(m.group(3))
            if op == '+': return str(n1 + n2)
            if op == '-': return str(n1 - n2)
            if op == '*': return str(n1 * n2)
            if op == '/': return str(n1 // n2) if n2 else '0'
    try:
        soup = BeautifulSoup(html_content, "html.parser")
        for txt in soup.stripped_strings:
            m3 = re.search(r'(\d+)\s*([+\-*/])\s*(\d+)', txt)
            if m3:
                n1, op, n2 = int(m3.group(1)), m3.group(2), int(m3.group(3))
                if op == '+': return str(n1 + n2)
                if op == '-': return str(n1 - n2)
                if op == '*': return str(n1 * n2)
                if op == '/': return str(n1 // n2) if n2 else '0'
    except:
        pass
    if 'capt' not in html_content.lower() and 'captcha' not in html_content.lower():
        return ""
    return None

def login_for_dashboard(dash):
    if dash.get("type") in ("api_token", "api"):
        dash["is_logged_in"] = True
        return True

    if dash.get("type") == "ims_panel":
        return _do_ims_login(dash)

    def do_login():
        dash_timeout = max(dash.get("timeout", 15), 15)
        try:
            dash["session"].headers.update({
                "Connection": "keep-alive",
                "Accept-Encoding": "gzip, deflate",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
            })
            login_page_url = dash.get("login_page_url", "")
            if not login_page_url:
                return False
            resp = dash["session"].get(login_page_url, timeout=dash_timeout)
            captcha = _solve_captcha(resp.text)
            if captcha is None:
                captcha = ""
            payload = {}
            payload.update(_extract_hidden_fields(resp.text))
            payload["username"] = dash.get("username","")
            payload["password"] = dash.get("password","")
            if captcha != "":
                payload["capt"] = captcha
            crlf_match = re.search(r"name=['\"]crlf['\"].*?value=['\"]([^'\"]+)['\"]", resp.text, re.DOTALL)
            if not crlf_match:
                crlf_match = re.search(r"value=['\"]([^'\"]+)['\"].*?name=['\"]crlf['\"]", resp.text, re.DOTALL)
            if crlf_match:
                payload["crlf"] = crlf_match.group(1)
                print(f"[{dash.get('name','')}] 🔑 crlf token مستخرج")
            base_url = dash.get("base_url","").rstrip("/")
            headers = {
                "Content-Type": "application/x-www-form-urlencoded",
                "Origin":       base_url,
                "Referer":      login_page_url,
                "User-Agent":   "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
                "Accept":       "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                "Accept-Language": "en-US,en;q=0.9",
                "Connection":   "keep-alive",
                "Upgrade-Insecure-Requests": "1",
            }
            login_post_url = dash.get("login_post_url", "")
            if not login_post_url:
                return False
            resp = dash["session"].post(login_post_url, data=payload, headers=headers,
                                        timeout=max(dash_timeout, 20), allow_redirects=True)
            resp_url_lower = resp.url.lower()
            resp_text_lower = resp.text.lower()
            login_page_url = dash.get("login_page_url", "")
            login_success = (
                "agent"     in resp_url_lower or
                "dashboard" in resp_url_lower or
                "reports"   in resp_url_lower or
                "smscdr"    in resp_text_lower or
                "logout"    in resp_text_lower or
                "signout"   in resp_text_lower or
                "/ints/agent" in resp.url or
                "/ints/client" in resp.url or
                ("/agent" in resp.url and "login" not in resp_url_lower) or
                (resp.url != login_page_url and "signin" not in resp_url_lower and "login" not in resp_url_lower
                 and "sign-in" not in resp_url_lower) or
                (resp.status_code == 200 and "sign-in" not in resp.url.lower()
                 and "login" not in resp_url_lower and "signin" not in resp_url_lower
                 and not bool(re.search(r'<input[^>]+type=["\']password["\']', resp.text, re.IGNORECASE))
                 and len(resp.text) > 2000)
            )
            if not login_success:
                for sp in ["/ints/agent/SMSCDRReports", "/agent/SMSCDRReports",
                           "/ints/agent/SMSCDRStats", "/agent/SMSCDRStats"]:
                    try:
                        base = dash.get("base_url","").rstrip("/")
                        tr = dash["session"].get(base + sp, timeout=8)
                        if tr.status_code == 200 and "login" not in tr.url.lower() and "signin" not in tr.url.lower():
                            login_success = True
                            break
                    except:
                        pass
            print(f"[{dash.get('name','')}] login URL: {resp.url} | success={login_success}")
            if login_success:
                dash["is_logged_in"] = True
                dash["_login_time"] = time.time()
                base = dash.get("base_url","").rstrip("/")
                for sp in ["/ints/agent/SMSCDRReports", "/agent/SMSCDRReports",
                           dash.get("stats_page",""), "/ints/agent/SMSCDRStats", "/agent/SMSCDRStats"]:
                    if not sp: continue
                    try:
                        su = sp if sp.startswith("http") else base + sp
                        sr = dash["session"].get(su, timeout=5)
                        sk = re.search(r'sesskey=([A-Za-z0-9+/=]+)', sr.text)
                        if not sk:
                            sk = re.search(r'sesskey["\'\s:=]+([a-zA-Z0-9+/=]{10,})', sr.text)
                        if sk:
                            dash["sesskey"] = sk.group(1)
                            print(f"[{dash.get('name','')}] 🔑 sesskey OK")
                            break
                    except:
                        continue
                return True
            else:
                dash["is_logged_in"] = False
                print(f"[{dash.get('name','')}] ❌ فشل تسجيل الدخول - URL: {resp.url}")
                return False
        except Exception as e:
            raise
    try:
        return retry_request(do_login, max_retries=3, retry_delay=5)
    except:
        dash["is_logged_in"] = False
        return False

def _do_ims_login(dash):
    try:
        dash_timeout = dash.get("timeout", 10)
        login_page_url = dash.get("login_page_url","")
        login_post_url = dash.get("login_post_url","")
        if not login_page_url:
            return False
        if not dash.get("session"):
            dash["session"] = requests.Session()
        resp = dash["session"].get(login_page_url, timeout=dash_timeout)
        if resp.status_code != 200:
            return False
        soup = BeautifulSoup(resp.text, "html.parser")
        etkk_input = soup.find("input", {"name": "etkk"})
        etkk_value = etkk_input.get("value", "") if etkk_input else ""
        captcha_answer = None
        m = re.search(r'What is (\d+)\s*\+\s*(\d+)', resp.text, re.IGNORECASE)
        if m:
            captcha_answer = int(m.group(1)) + int(m.group(2))
        else:
            for txt in soup.stripped_strings:
                m2 = re.search(r'(\d+)\s*\+\s*(\d+)', txt)
                if m2:
                    captcha_answer = int(m2.group(1)) + int(m2.group(2))
                    break
        if captcha_answer is None:
            return False
        payload = {
            "username": dash.get("username",""),
            "password": dash.get("password",""),
            "capt": str(captcha_answer),
            "etkk": etkk_value,
        }
        r2 = dash["session"].post(login_post_url, data=payload,
                    headers={"Referer": login_page_url, "Content-Type": "application/x-www-form-urlencoded"},
                    timeout=dash_timeout, allow_redirects=True)
        if "agent/SMS" in r2.url or "dashboard" in r2.url.lower() or "logout" in r2.text.lower():
            dash["is_logged_in"] = True
            dash["_login_time"] = time.time()
            try:
                dash_url = dash.get("dashboard_url","")
                if dash_url:
                    sr = dash["session"].get(dash_url, timeout=dash_timeout)
                    sk = _extract_sesskey(dash, sr.text)
                    if sk:
                        dash["sesskey"] = sk
            except:
                pass
            return True
        dash["is_logged_in"] = False
        return False
    except:
        dash["is_logged_in"] = False
        return False

def build_ajax_url_for_dashboard(dash, wide_range=False):
    if wide_range:
        start_date = date.today() - timedelta(days=3650)
        end_date   = date.today() + timedelta(days=1)
    else:
        start_date = date.today() - timedelta(days=1)
        end_date   = date.today() + timedelta(days=1)
    fdate1 = f"{start_date.strftime('%Y-%m-%d')} 00:00:00"
    fdate2 = f"{end_date.strftime('%Y-%m-%d')} 23:59:59"
    sesskey_part = ""
    sk = dash.get("sesskey")
    if sk:
        sesskey_part = f"sesskey={quote_plus(sk)}&"
    base_ajax = dash.get("ajax_url") or (dash.get("base_url") + dash["ajax_path"] if dash.get("base_url") and dash.get("ajax_path") else None)
    if not base_ajax:
        return None
    q = (f"{sesskey_part}fdate1={quote_plus(fdate1)}&fdate2={quote_plus(fdate2)}&frange=&fclient=&fnum=&fcli=&fgdate=&fgmonth=&fgrange="
         f"&fgclient=&fgnumber=&fgcli=&fg=0&sEcho=1&iColumns=9&sColumns=%2C%2C%2C%2C%2C%2C%2C%2C&iDisplayStart=0&iDisplayLength=5000"
         f"&mDataProp_0=0&mDataProp_1=1&mDataProp_2=2&mDataProp_3=3&mDataProp_4=4&mDataProp_5=5&mDataProp_6=6&mDataProp_7=7&mDataProp_8=8"
         f"&sSearch=&bRegex=false&iSortCol_0=0&sSortDir_0=desc&iSortingCols=1&_={int(time.time()*1000)}")
    return base_ajax + "?" + q

def fetch_ajax_json_for_dashboard(dash, url):
    if not url:
        return None
    dash_timeout = min(dash.get("timeout", 6), 12)
    if "_fail_count" not in dash:
        dash["_fail_count"] = 0

    use_post = dash.get("ajax_use_post", False)

    def do_fetch():
        if use_post:
            from urllib.parse import urlparse
            parsed = urlparse(url)
            params = parsed.query
            base_url_part = f"{parsed.scheme}://{parsed.netloc}{parsed.path}"
            headers_ajax = {
                "Content-Type": "application/x-www-form-urlencoded",
                "X-Requested-With": "XMLHttpRequest",
                "Referer": dash.get("base_url", "").rstrip("/") + dash.get("ajax_path", ""),
            }
            r = dash["session"].post(base_url_part, data=params,
                                     headers=headers_ajax, timeout=dash_timeout)
        else:
            r = dash["session"].get(url, timeout=dash_timeout)

        if r.status_code == 403 or ("login" in r.url.lower()) or ("signin" in r.url.lower()):
            raise Exception("Session expired")
        r.raise_for_status()
        try:
            result = r.json()
            dash["_fail_count"] = 0
            return result
        except (json.JSONDecodeError, Exception):
            new_sk = re.search(r'sesskey["\'\s:=]+([a-zA-Z0-9+/=]{10,})', r.text)
            if new_sk:
                dash["sesskey"] = new_sk.group(1)
            if not use_post and len(r.text) > 100:
                try:
                    base_url_part = url.split("?")[0]
                    params = url.split("?")[1] if "?" in url else ""
                    headers_ajax = {
                        "Content-Type": "application/x-www-form-urlencoded",
                        "X-Requested-With": "XMLHttpRequest",
                    }
                    r2 = dash["session"].post(base_url_part, data=params,
                                              headers=headers_ajax, timeout=dash_timeout)
                    result2 = r2.json()
                    dash["_fail_count"] = 0
                    dash["ajax_use_post"] = True
                    print(f"[{dash.get('name','')}] ✅ AJAX POST نجح - سيُستخدم دائماً")
                    return result2
                except:
                    pass
            raise Exception("Invalid JSON - need new sesskey")

    try:
        result = do_fetch()
        return result
    except Exception as e:
        dash["_fail_count"] = dash.get("_fail_count", 0) + 1
        if "Session expired" in str(e) or dash["_fail_count"] >= 3:
            dash["_fail_count"] = 0
            dash["is_logged_in"] = False
            dash["sesskey"] = None
            print(f"[{dash.get('name','')}] 🔄 جلسة منتهية - إعادة دخول...")
            if login_for_dashboard(dash):
                dash["is_logged_in"] = True
                try:
                    return do_fetch()
                except:
                    return None
            else:
                return None
        return None

def extract_rows_from_json(j):
    if j is None:
        return []
    for key in ("data", "aaData", "rows", "aa_data"):
        if isinstance(j, dict) and key in j:
            return j[key]
    if isinstance(j, list):
        return j
    if isinstance(j, dict):
        for v in j.values():
            if isinstance(v, list):
                return v
    return []

def fetch_api_token_rows(dash):
    # ── MBC: بتحتاج login بالـ username/password عشان تجيب الـ token ──
    if dash.get("site_key") == "MBC" or "mbcs-ms.com" in dash.get("api_url", ""):
        return fetch_mbc_rows(dash)
    try:
        url = dash.get("api_url")
        token = dash.get("api_token", "")
        if not url or not token:
            return []
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Accept": "application/json, text/plain, */*",
            "Accept-Language": "en-US,en;q=0.9",
        }
        r = dash["session"].get(url, params={"token": token}, headers=headers, timeout=dash.get("timeout", 8))
        if r.status_code == 403:
            r = dash["session"].get(url, headers={**headers, "Authorization": f"Bearer {token}"}, timeout=dash.get("timeout", 8))
        if r.status_code != 200:
            return []
        raw = r.text.strip()
        if not raw:
            return []
        try:
            j = r.json()
        except Exception:
            return []
        rows = []
        for key in ("data", "aaData", "rows", "result"):
            if isinstance(j, dict) and key in j and isinstance(j[key], list):
                rows = j[key]
                break
        if not rows and isinstance(j, list):
            rows = j
        return rows
    except Exception as e:
        return []


# ── MBC Panel: login + viewstats ──────────────────────────────────────────────
# الـ API: https://mbcs-ms.com/crapi/mbc/viewstats?token=<TOKEN>
# الـ LOGIN: POST https://mbcs-ms.com/login  { username, password }
#            الريسبونس: JSON { token: "..." }  أو session cookie
_mbc_token_cache = {}   # username -> {"token": str, "expires": float}

def _mbc_login(session, username, password):
    """يسجل دخول لـ MBC ويرجع الـ API token."""
    LOGIN_URL = "https://mbcs-ms.com/login"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10; Win64; x64) AppleWebKit/537.36",
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Referer": "https://mbcs-ms.com/",
        "Origin": "https://mbcs-ms.com",
    }
    try:
        # محاولة JSON login
        r = session.post(LOGIN_URL, json={"username": username, "password": password},
                         headers=headers, timeout=15, verify=False)
        if r.status_code == 200:
            try:
                j = r.json()
                # يرجع token مباشرة أو جوه key
                for k in ("token", "api_token", "access_token", "key"):
                    if k in j and j[k]:
                        return str(j[k]).strip()
                # لو الـ token مش صريح — نحاول من الـ session cookies
                for ck in session.cookies:
                    if "token" in ck.name.lower():
                        return ck.value
            except Exception:
                pass
        # محاولة form-urlencoded
        r2 = session.post(LOGIN_URL,
                          data={"username": username, "password": password},
                          headers={**headers, "Content-Type": "application/x-www-form-urlencoded"},
                          timeout=15, verify=False)
        if r2.status_code == 200:
            try:
                j2 = r2.json()
                for k in ("token", "api_token", "access_token", "key"):
                    if k in j2 and j2[k]:
                        return str(j2[k]).strip()
            except Exception:
                pass
        print(f"[MBC] login failed: status={r.status_code} body={r.text[:200]}")
        return None
    except Exception as e:
        print(f"[MBC] login exception: {e}")
        return None


def fetch_mbc_rows(dash):
    """
    يجيب الرسائل من MBC.
    لو `api_token` موجود في الـ dash → يستخدمه مباشرة.
    لو مش موجود → يعمل login بالـ username/password ويجيب token.
    """
    API_URL = "https://mbcs-ms.com/crapi/mbc/viewstats"
    session  = dash.get("session") or requests.Session()
    username = dash.get("username", "")
    password = dash.get("password", "")
    token    = dash.get("api_token", "").strip()

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10; Win64; x64) AppleWebKit/537.36",
        "Accept": "application/json",
        "Referer": "https://mbcs-ms.com/",
    }

    # ── 1) لو مفيش token نعمل login ──
    if not token and username and password:
        cached = _mbc_token_cache.get(username, {})
        if cached.get("token") and time.time() < cached.get("expires", 0):
            token = cached["token"]
        else:
            token = _mbc_login(session, username, password)
            if token:
                _mbc_token_cache[username] = {"token": token, "expires": time.time() + 3600}
                # نحدث الـ dash عشان ميعملش login في كل loop
                dash["api_token"] = token

    if not token:
        _panel_box("MBC", status="ERR")
        return []

    # ── 2) نجيب الرسائل ──
    try:
        r = session.get(API_URL, params={"token": token},
                        headers=headers, timeout=dash.get("timeout", 15), verify=False)
        if r.status_code == 401:
            # token انتهى — نعيد الـ login
            if username and password:
                token = _mbc_login(session, username, password)
                if token:
                    _mbc_token_cache[username] = {"token": token, "expires": time.time() + 3600}
                    dash["api_token"] = token
                    r = session.get(API_URL, params={"token": token},
                                    headers=headers, timeout=dash.get("timeout", 15), verify=False)
                else:
                    return []
        if r.status_code != 200:
            _panel_box("MBC", status="ERR")
            return []

        try:
            j = r.json()
        except Exception:
            return []

        rows = []
        for key in ("data", "aaData", "rows", "result", "messages", "sms"):
            if isinstance(j, dict) and key in j and isinstance(j[key], list):
                rows = j[key]
                break
        if not rows and isinstance(j, list):
            rows = j

        if rows:
            _panel_box("MBC", sms=f"{len(rows)} rows", status="NEW")
        return rows

    except Exception as e:
        print(f"[MBC] fetch error: {e}")
        return []

def row_to_tuple(row, dash):
    date_str = number_str = sms_str = ""
    idx_date = dash.get("idx_date", 0)
    idx_number = dash.get("idx_number", 2)
    idx_sms = dash.get("idx_sms", 5)
    if isinstance(row, (list, tuple)):
        if len(row) > idx_date:   date_str   = clean_html(str(row[idx_date]))
        if len(row) > idx_number: number_str = clean_number(str(row[idx_number]))
        if len(row) > idx_sms:    sms_str    = clean_html(str(row[idx_sms]))
    elif isinstance(row, dict):
        keys = dash.get("data_keys", {})
        date_key = keys.get("date")
        if date_key and date_key in row:
            date_str = clean_html(str(row[date_key]))
        else:
            for k in ("date","time","datetime","dt","created_at"):
                if k in row: date_str = clean_html(str(row[k])); break
        num_key = keys.get("number")
        if num_key and num_key in row:
            number_str = clean_number(str(row[num_key]))
        else:
            for k in ("number","msisdn","cli","from","sender"):
                if k in row: number_str = clean_number(str(row[k])); break
        sms_key = keys.get("sms")
        if sms_key and sms_key in row:
            sms_str = clean_html(str(row[sms_key]))
        else:
            for k in ("sms","message","msg","body","text"):
                if k in row: sms_str = clean_html(str(row[k])); break
    unique_key = f"{date_str}|{number_str}|{sms_str[:30]}"
    return date_str, number_str, sms_str, unique_key

def parse_api_token_row(dash, row):
    keys = dash.get("data_keys") or {}
    date_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    number = sms = ""
    if isinstance(row, dict):
        date_key = keys.get("date")
        if date_key and date_key in row:
            date_str = str(row[date_key])
        num_key = keys.get("number", "num")
        if num_key in row:
            number = clean_number(str(row[num_key]))
        sms_key = keys.get("sms", "message")
        if sms_key in row:
            sms = clean_html(str(row[sms_key]))
    elif isinstance(row, (list, tuple)):
        i_date   = dash.get("idx_date", 0)
        i_number = dash.get("idx_number", 2)
        i_sms    = dash.get("idx_sms", 5)
        if len(row) > i_date:   date_str = clean_html(str(row[i_date]))
        if len(row) > i_number: number   = clean_number(str(row[i_number]))
        if len(row) > i_sms:    sms      = clean_html(str(row[i_sms]))
    key = f"{date_str}|{number}|{sms[:30]}"
    return date_str, number, sms, key

def retry_request(func, max_retries=1, retry_delay=0):
    for attempt in range(max_retries):
        try:
            return func()
        except Exception as e:
            if attempt < max_retries - 1:
                time.sleep(retry_delay)
            else:
                raise

def _extract_sesskey(dash, resp_text):
    m = re.search(r'sesskey["\s:=\']+([a-zA-Z0-9+/=]+)', resp_text)
    if m:
        return m.group(1)
    return None

def login_for_ims_panel(dash):
    try:
        dash["session"] = requests.Session()
        dash["session"].headers.update({
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.9",
            "Connection": "keep-alive",
        })
        dash_timeout = dash.get("timeout", 15)
        login_page_url = dash["login_page_url"]
        login_post_url = dash["login_post_url"]

        resp = dash["session"].get(login_page_url, timeout=dash_timeout)
        if resp.status_code != 200:
            print(f"[{dash['name']}] ❌ فشل جلب صفحة الدخول (HTTP {resp.status_code})")
            return False

        page_text = resp.text
        soup = BeautifulSoup(page_text, "html.parser")

        etkk_value = ""
        etkk_input = soup.find("input", {"name": "etkk"})
        if etkk_input:
            etkk_value = etkk_input.get("value", "")
        else:
            m_etkk = re.search(r'name=["\']etkk["\']\s*value=["\']([^"\']+)["\']', page_text)
            if m_etkk:
                etkk_value = m_etkk.group(1)

        captcha_answer = None
        match = re.search(r'What is\s*(\d+)\s*\+\s*(\d+)', page_text, re.IGNORECASE)
        if match:
            captcha_answer = int(match.group(1)) + int(match.group(2))
        else:
            for t in soup.stripped_strings:
                m2 = re.search(r'(\d+)\s*\+\s*(\d+)', t)
                if m2:
                    captcha_answer = int(m2.group(1)) + int(m2.group(2))
                    break
        if captcha_answer is None:
            m3 = re.search(r'(\d+)\s*\+\s*(\d+)', page_text)
            if m3:
                captcha_answer = int(m3.group(1)) + int(m3.group(2))
        if captcha_answer is None:
            captcha_answer = ""
            print(f"[{dash['name']}] ⚠️ لم يُوجد captcha - سيتم المحاولة بدونه")

        print(f"[{dash['name']}] 🔐 كابتشا={captcha_answer}, etkk={etkk_value[:10] if etkk_value else 'none'}")

        payload = {
            "username": dash["username"],
            "password": dash["password"],
            "capt":     str(captcha_answer),
        }
        if etkk_value:
            payload["etkk"] = etkk_value

        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "Referer":      login_page_url,
            "Origin":       dash.get("base_url", "").rstrip("/"),
        }
        resp2 = dash["session"].post(login_post_url, data=payload, headers=headers,
                                     timeout=dash_timeout, allow_redirects=True)
        final_url  = resp2.url
        final_text = resp2.text

        success = (
            "Dashboard" in final_text or
            "Logout"    in final_text or
            "/client"   in final_url.lower() or
            "/agent"    in final_url.lower() or
            "dashboard" in final_url.lower()
        )
        if success:
            dash["is_logged_in"] = True
            dash["last_login_time"] = time.time()
            dash["sesskey"] = None
            print(f"[{dash['name']}] ✅ تسجيل دخول ناجح → {final_url}")
            return True
        else:
            dash["is_logged_in"] = False
            err = re.search(r'<(?:div|span|p)[^>]*class=["\'][^"\']*(?:alert|error|danger|warning)[^"\']*["\'][^>]*>(.*?)</', final_text, re.DOTALL | re.IGNORECASE)
            if err:
                clean = re.sub('<[^<]+?>', '', err.group(1)).strip()
                print(f"[{dash['name']}] ❌ الخادم: {clean}")
            elif "Incorrect Answer" in final_text or "captcha" in final_text.lower():
                print(f"[{dash['name']}] ❌ خطأ في الكابتشا")
            elif "Invalid" in final_text:
                print(f"[{dash['name']}] ❌ بيانات دخول خاطئة")
            else:
                print(f"[{dash['name']}] ❌ فشل الدخول → {final_url}")
            return False

    except Exception as e:
        dash["is_logged_in"] = False
        print(f"[{dash['name']}] ❌ خطأ في الدخول: {e}")
        return False

def _extract_sk(text):
    for pat in [
        r'sesskey=([a-zA-Z0-9+/=_-]{10,})',
        r'sesskey[\s:="\']+([a-zA-Z0-9+/=_-]{10,})',
    ]:
        m = re.search(pat, text, re.IGNORECASE)
        if m and len(m.group(1).strip()) >= 10:
            return m.group(1).strip()
    return None

def _ims_login_and_sesskey(dash):
    if not login_for_ims_panel(dash):
        return False
    dash_url = dash.get("dashboard_url", "")
    if not dash_url:
        print(f"[{dash['name']}] ❌ dashboard_url مش محدد")
        return False
    try:
        r = dash["session"].get(dash_url, timeout=dash.get("timeout", 30))
        sk = _extract_sk(r.text)
        if sk:
            dash["sesskey"] = sk
            print(f"[{dash['name']}] 🔑 sesskey OK: {sk[:15]}...")
            return True
        base = dash.get("base_url", "").rstrip("/")
        dash_type = dash.get("type", "")
        cdrs_path = "/agent/SMSCDRs"
        r2 = dash["session"].get(base + cdrs_path, timeout=dash.get("timeout", 30))
        sk2 = _extract_sk(r2.text)
        if sk2:
            dash["sesskey"] = sk2
            print(f"[{dash['name']}] 🔑 sesskey OK (CDRs): {sk2[:15]}...")
            return True
        print(f"[{dash['name']}] ❌ login نجح لكن sesskey مش موجود - سيتم إعادة المحاولة")
        dash["is_logged_in"] = False
        return False
    except Exception as e:
        print(f"[{dash['name']}] ❌ خطأ في استخراج sesskey: {e}")
        dash["is_logged_in"] = False
        return False

def fetch_ims_panel_data(dash):
    try:
        if not dash.get("is_logged_in") or not dash.get("sesskey") or not dash.get("session"):
            if not _ims_login_and_sesskey(dash):
                return dash["name"], []

        last_fetch = dash.get("_last_fetch_time")
        if last_fetch and isinstance(last_fetch, datetime):
            if last_fetch.date() < date.today():
                fdate1 = datetime.combine(date.today(), datetime.min.time()).strftime("%Y-%m-%d %H:%M:%S")
            else:
                fdate1 = (last_fetch + timedelta(seconds=1)).strftime("%Y-%m-%d %H:%M:%S")
        else:
            fdate1 = datetime.combine(date.today(), datetime.min.time()).strftime("%Y-%m-%d %H:%M:%S")

        fdate2 = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        params = {
            "sesskey":        dash["sesskey"],
            "fdate1":         fdate1,
            "fdate2":         fdate2,
            "frange":         "",
            "fclient":        "",
            "fnum":           "",
            "fcli":           "",
            "fg":             "0",
            "sEcho":          "1",
            "iColumns":       "9",
            "sColumns":       ",,,,,,,,",
            "iDisplayStart":  "0",
            "iDisplayLength": str(dash.get("records", 10)),
            "mDataProp_0": "0", "mDataProp_1": "1", "mDataProp_2": "2",
            "mDataProp_3": "3", "mDataProp_4": "4", "mDataProp_5": "5",
            "mDataProp_6": "6", "mDataProp_7": "7", "mDataProp_8": "8",
            "sSearch":        "",
            "bRegex":         "false",
            "iSortCol_0":     "0",
            "sSortDir_0":     "desc",
            "iSortingCols":   "1",
            "_":              str(int(time.time() * 1000)),
        }

        dash["session"].headers.update({
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "X-Requested-With": "XMLHttpRequest",
            "Referer": dash.get("dashboard_url", ""),
        })

        resp = dash["session"].get(
            dash["ajax_url"], params=params,
            timeout=dash.get("timeout", 8)
        )

        if resp.status_code == 403 or "login" in resp.url.lower():
            print(f"[{dash['name']}] 🔄 session انتهت - إعادة login")
            dash["is_logged_in"] = False
            dash["sesskey"] = None
            return dash["name"], []

        try:
            data = resp.json()
        except Exception:
            sk = _extract_sk(resp.text)
            if sk:
                dash["sesskey"] = sk
                print(f"[{dash['name']}] 🔄 sesskey مُجدد من response")
            else:
                dash["is_logged_in"] = False
                dash["sesskey"] = None
            return dash["name"], []

        rows = data.get("aaData", data.get("data", []))

        entries = []
        max_dt = None
        for row in rows:
            date_val, num_val, sms_val, key = row_to_tuple(row, dash)
            if date_val and num_val and sms_val and len(num_val) >= 7:
                entries.append((date_val, num_val, sms_val, key))
                try:
                    dt = datetime.strptime(date_val, "%Y-%m-%d %H:%M:%S")
                    if max_dt is None or dt > max_dt:
                        max_dt = dt
                except:
                    pass

        if max_dt:
            dash["_last_fetch_time"] = max_dt

        if entries:
            entries.sort(key=lambda x: x[0], reverse=True)
            return dash["name"], entries[:20]

        return dash["name"], []
    except Exception as e:
        print(f"[{dash['name']}] ❌ خطأ في الجلب: {e}")
        dash["is_logged_in"] = False
        return dash["name"], []

def fetch_dashboard_data(dash):
    name = dash["name"]
    try:
        dtype = dash.get("type", "traditional")

        if dtype == "ims_panel":
            return fetch_ims_panel_data(dash)

        if dtype in ("api_token", "api"):
            rows = fetch_api_token_rows(dash)
            entries = []
            for row in rows:
                date_str, number, sms, key = parse_api_token_row(dash, row)
                if number and sms and len(number) >= 7:
                    entries.append((date_str, number, sms, key))
            if entries:
                entries.sort(key=lambda x: x[0], reverse=True)
                return name, entries[:20]
            return name, []

        if not dash.get("is_logged_in"):
            if not login_for_dashboard(dash):
                return name, []

        url = build_ajax_url_for_dashboard(dash)
        j = fetch_ajax_json_for_dashboard(dash, url)
        rows = extract_rows_from_json(j)

        valid_rows = []
        for row in rows:
            if isinstance(row, (list, tuple, dict)):
                date_val, num_val, sms_val, _ = row_to_tuple(row, dash)
                if (date_val and num_val and sms_val
                        and len(num_val) >= 7
                        and len(sms_val) > 2):
                    valid_rows.append(row)

        if valid_rows:
            def get_dt(r):
                try:
                    dt, _, _, _ = row_to_tuple(r, dash)
                    return datetime.strptime(dt, "%Y-%m-%d %H:%M:%S")
                except:
                    return datetime.min
            valid_rows.sort(key=get_dt, reverse=True)

            last_fetch = dash.get("_last_fetch_time")
            today_start = datetime.combine(date.today(), datetime.min.time())
            _NO_CUTOFF_PANELS = {"FIRE SMS", "Konekta Panel", "Konekta API", "CHOICE SMS", "PROOF SMS", "SHARK SMS"}
            if name in _NO_CUTOFF_PANELS:
                cutoff = today_start
            else:
                cutoff = last_fetch if (last_fetch and isinstance(last_fetch, datetime) and last_fetch >= today_start) else today_start

            entries = []
            max_dt = cutoff
            for row in valid_rows[:50]:
                d2, n2, s2, k2 = row_to_tuple(row, dash)
                if not n2 or not s2:
                    continue
                try:
                    row_dt = datetime.strptime(d2, "%Y-%m-%d %H:%M:%S")
                except:
                    row_dt = None
                if row_dt and row_dt >= cutoff:
                    entries.append((d2, n2, s2, k2))
                    if row_dt > max_dt:
                        max_dt = row_dt
                elif not row_dt:
                    entries.append((d2, n2, s2, k2))

            if max_dt > cutoff:
                dash["_last_fetch_time"] = max_dt

            return name, entries
        return name, []

    except Exception as e:
        print(f"[{name}] ⚠️ fetch error: {e}")
        if dash.get("is_logged_in"):
            dash["is_logged_in"] = False
        return name, []

from requests.adapters import HTTPAdapter

def _tune_session(sess):
    adapter = HTTPAdapter(
        pool_connections=10,
        pool_maxsize=20,
        max_retries=0,
    )
    sess.mount("http://",  adapter)
    sess.mount("https://", adapter)
    sess.headers.update({
        "Connection":        "keep-alive",
        "Accept-Encoding":   "gzip, deflate",
        "Accept":            "text/html,application/xhtml+xml,*/*;q=0.8",
        "Accept-Language":   "en-US,en;q=0.9",
    })

def _make_dash(d):
    def _bu(base, path):
        if not path: return ""
        if path.startswith("http"): return path
        return base.rstrip("/") + path if base else path

    dtype = d.get("type", "traditional")
    if dtype in ("api_token", "api"):
        d["is_logged_in"] = True
        d["session"] = requests.Session()
        d["session"].headers.update(COMMON_HEADERS)
        _tune_session(d["session"])
    elif dtype == "ims_panel":
        d["session"] = requests.Session()
        d["session"].headers.update(COMMON_HEADERS)
        _tune_session(d["session"])
        d["is_logged_in"] = False
        d["sesskey"] = None
        d["phpsessid"] = None
        d["last_login_time"] = 0
        d["_last_fetch_time"] = None
        d["login_page_url"] = _bu(d.get("base_url",""), d.get("login_page",""))
        d["login_post_url"] = _bu(d.get("base_url",""), d.get("login_post",""))
        d["ajax_url"]       = _bu(d.get("base_url",""), d.get("ajax_path",""))
        d["dashboard_url"]  = _bu(d.get("base_url",""), d.get("dashboard_path",""))
    else:
        d["session"] = requests.Session()
        d["session"].headers.update(COMMON_HEADERS)
        _tune_session(d["session"])
        d["is_logged_in"] = False
        d["sesskey"] = None
        d["_last_fetch_time"] = None
        d["login_page_url"] = _bu(d.get("base_url",""), d.get("login_page",""))
        d["login_post_url"] = _bu(d.get("base_url",""), d.get("login_post",""))
        d["ajax_url"]       = _bu(d.get("base_url",""), d.get("ajax_path",""))
    return d

def _init_all_dashboards():
    all_dash = []
    for dash in STATIC_DASHBOARDS:
        dtype = dash.get("type", "traditional")
        if dtype in ("api_token", "api"):
            if not dash.get("api_token") or not dash.get("api_url"):
                print(f"[SKIP] {dash['name']} - لا يوجد API token أو url")
                continue
        elif dtype == "ims_panel":
            if not dash.get("username") or not dash.get("password"):
                print(f"[SKIP] {dash['name']} - لا يوجد يوزر/باسورد")
                continue
        else:
            if not dash.get("username") or not dash.get("password"):
                print(f"[SKIP] {dash['name']} - لا يوجد يوزر/باسورد")
                continue
        d = dash.copy()
        d = _make_dash(d)
        all_dash.append(d)
        print(f"[INIT] ✅ {d['name']}")

    for db_dash in get_db_dashboards(only_active=True):
        d = db_dash.copy()
        d = _make_dash(d)
        all_dash.append(d)
        print(f"[INIT DB] ✅ {d['name']}")

    print(f"[INIT] إجمالي اللوحات: {len(all_dash)}")
    return all_dash

def _get_db_dashboards_initialized():
    result = []
    for db_dash in get_db_dashboards(only_active=True):
        d = db_dash.copy()
        d = _make_dash(d)
        result.append(d)
    return result

def main_loop():
    sent_messages = set()
    last_fetch_time = {}
    _today_sent_file = "sent_today.json"
    _main_current_day = date.today()

    try:
        if os.path.exists(_today_sent_file):
            with open(_today_sent_file, "r") as f:
                data = json.load(f)
                saved_date = data.get("date", "")
                if saved_date == str(date.today()):
                    sent_messages = set(data.get("keys", []))
                    print(f"[INIT] ✅ تم تحميل {len(sent_messages)} key من اليوم - منع التكرار")
    except:
        pass

    def _save_sent():
        try:
            with open(_today_sent_file, "w") as f:
                json.dump({"date": str(date.today()), "keys": list(sent_messages)[-5000:]}, f)
        except:
            pass

    print("=" * 60)
    print(f"🚀 بدء مراقبة اللوحات (MAX_WORKERS={MAX_WORKERS})")
    print("=" * 60)

    executor = ThreadPoolExecutor(max_workers=MAX_WORKERS)

    active_dashboards = _init_all_dashboards()

    CYAN    = "\033[96m"
    GREEN   = "\033[92m"
    RED     = "\033[91m"
    YELLOW  = "\033[93m"
    MAGENTA = "\033[95m"
    BOLD    = "\033[1m"
    RESET   = "\033[0m"
    DIM     = "\033[2m"

    def _print_panel_table(dashboards, phase="LOGIN"):
        print(f"\n{CYAN}{BOLD}{'━'*72}{RESET}")
        print(f"{CYAN}{BOLD}  📡 PANEL STATUS TABLE  [{phase}]{RESET}")
        print(f"{CYAN}{'━'*72}{RESET}")
        header = f"  {'#':<3}  {'Panel Name':<22}  {'Type':<12}  {'User':<18}  {'Status'}"
        print(f"{BOLD}{header}{RESET}")
        print(f"{DIM}  {'─'*3}  {'─'*22}  {'─'*12}  {'─'*18}  {'─'*16}{RESET}")
        for i, d in enumerate(dashboards, 1):
            dtype = d.get("type","traditional")
            uname = d.get("username","") or "API"
            if dtype in ("api_token","api"):
                status = f"{GREEN}✅ API Ready{RESET}"
            elif d.get("is_logged_in"):
                status = f"{GREEN}✅ Logged In{RESET}"
            else:
                status = f"{RED}❌ Not Logged In{RESET}"
            name  = d.get("name","?")[:22]
            dtype_s = dtype[:12]
            uname_s = uname[:18]
            print(f"  {YELLOW}{i:<3}{RESET}  {name:<22}  {DIM}{dtype_s:<12}{RESET}  {MAGENTA}{uname_s:<18}{RESET}  {status}")
        print(f"{CYAN}{'━'*72}{RESET}\n")

    print(f"\n{BOLD}🔐 تسجيل الدخول لكل اللوحات...{RESET}")
    for dash in active_dashboards:
        if dash.get("type") in ("api_token", "api"):
            print(f"[{dash['name']}] ✅ API Token جاهز")
        else:
            if login_for_dashboard(dash):
                print(f"[{dash['name']}] ✅ دخل بنجاح")
            else:
                print(f"[{dash['name']}] ⚠️ فشل الدخول - سيُعاد لاحقاً")

    _print_panel_table(active_dashboards, phase="AFTER LOGIN")

    print("\n🔍 جلب أكواد اليوم من كل لوحة لمنع التكرار...")
    _init_cutoff = datetime.combine(date.today(), datetime.min.time())
    for dash in active_dashboards:
        try:
            _, entries = fetch_dashboard_data(dash)
            for date_str, number, sms, key in entries:
                if key not in sent_messages:
                    sent_messages.add(key)
            print(f"[{dash['name']}] ✅ {len(entries)} كود تم تسجيله - لن يُكرر")
            if entries:
                try:
                    max_init_dt = max(
                        datetime.strptime(e[0], "%Y-%m-%d %H:%M:%S")
                        for e in entries if e[0]
                    )
                    dash["_last_fetch_time"] = max_init_dt
                except:
                    dash["_last_fetch_time"] = datetime.now()
            else:
                dash["_last_fetch_time"] = _init_cutoff
        except Exception as e:
            print(f"[{dash['name']}] ⚠️ خطأ أولي: {e}")
            dash["_last_fetch_time"] = _init_cutoff
    _save_sent()

    print(f"\n✅ بدء المراقبة المستمرة...\n" + "="*60)

    last_db_check = time.time()

    while True:
        try:
            now = time.time()

            _main_new_day = date.today()
            if _main_new_day != _main_current_day:
                print(f"[main_loop] 🌅 يوم جديد ({_main_new_day}) - تصفير الأكواد المبعوتة")
                sent_messages.clear()
                _main_current_day = _main_new_day
                for dash in active_dashboards:
                    if dash.get("type") not in ("api_token", "api"):
                        dash["is_logged_in"] = False
                        dash["sesskey"] = None
                        dash["_last_fetch_time"] = None
                _save_sent()
                def _midnight_relogin(all_dashes):
                    for _d in all_dashes:
                        if _d.get("type") not in ("api_token", "api"):
                            try:
                                ok = login_for_dashboard(_d)
                                print(f"[midnight] {'✅' if ok else '❌'} re-login {_d['name']}")
                            except Exception as _e:
                                print(f"[midnight] ⚠️ {_d['name']}: {_e}")
                threading.Thread(target=_midnight_relogin, args=(list(active_dashboards),), daemon=True).start()

            if now - last_db_check >= 30:
                new_db = _get_db_dashboards_initialized()
                existing_names = {d["name"] for d in active_dashboards}
                for d in new_db:
                    if d["name"] not in existing_names:
                        active_dashboards.append(d)
                        print(f"[+] لوحة جديدة من DB: {d['name']}")
                        if d.get("type") not in ("api_token", "api"):
                            login_for_dashboard(d)
                last_db_check = now

            dashboards_to_fetch = []
            for dash in active_dashboards:
                ukey = f"{dash['name']}|{dash.get('username', 'api')}"
                dash["_ukey"] = ukey
                interval = dash.get("refresh_interval", 1)
                if now - last_fetch_time.get(ukey, 0) >= interval:
                    dashboards_to_fetch.append(dash)
                    last_fetch_time[ukey] = now

            if not dashboards_to_fetch:
                time.sleep(0.01)
                continue

            futures = {executor.submit(fetch_dashboard_data, dash): dash
                       for dash in dashboards_to_fetch}

            _TRACKED_PANELS = {"FIRE SMS", "Green SMS", "Sniper SMS", "IMS SMS"}

            for future in as_completed(futures, timeout=8):
                dash = futures[future]
                try:
                    name, entries = future.result(timeout=6)
                    _is_tracked = name in _TRACKED_PANELS
                    if _is_tracked:
                        _last_file = f"last_main_{name.replace(' ','_')}.txt"
                    for date_str, number, sms, key in entries:
                        if key not in sent_messages:
                            _panel_box(name, mask_number(number), sms[:60], status="NEW")
                            sent_messages.add(key)
                            if _is_tracked:
                                try:
                                    with open(_last_file, "w", encoding="utf-8") as _lf:
                                        _lf.write(f"{date_str}|{number[:8]}|{key[:40]}\n")
                                except: pass
                            threading.Thread(
                                target=send_otp_to_user_and_group,
                                args=(date_str, number, sms),
                                kwargs={"panel_name": name, "short_bold": dash.get("short_bold", to_bold(dash.get("short","??")))},
                                daemon=True
                            ).start()
                            _save_sent()
                    if _is_tracked and not entries:
                        print(f"[main_loop] [{name}] 📭 لا أكواد جديدة في هذه الدورة")
                except Exception as e:
                    _panel_box(dash['name'], sms=str(e)[:50], status="ERR")
                    _log_bot_error(f"[{dash['name']}] خطأ جلب: {e}", exc=e)

            if len(sent_messages) > 10000:
                sent_messages = set(list(sent_messages)[-8000:])
                _save_sent()
            if len(last_fetch_time) > 500:
                last_fetch_time = dict(list(last_fetch_time.items())[-300:])

        except KeyboardInterrupt:
            print("\n⛔ توقف يدوي")
            executor.shutdown(wait=False)
            break
        except Exception as e:
            print(f"⚠️ خطأ في الحلقة الرئيسية: {e}")
            time.sleep(0.1)

PLATFORM_EMOJI_MAP = {
    "whatsapp":    "📞",
    "واتساب":      "📞",
    "واتس":        "📞",
    "facebook":    "📱",
    "فيسبوك":      "📱",
    "meta":        "📱",
    "instagram":   "📱",
    "انستقرام":    "📱",
    "انستا":       "📱",
    "telegram":    "👉",
    "تيليجرام":   "👉",
    "تلجرام":      "👉",
    "twitter":     "<b>TW</b>",
    "تويتر":       "<b>TW</b>",
    "x.com":       "<b>TW</b>",
    "snapchat":    "📱",
    "سناب":        "📱",
    "tiktok":      "📱",
    "تيك توك":    "📱",
    "google":      "<b>GG</b>",
    "جوجل":        "<b>GG</b>",
    "gmail":       "<b>GG</b>",
    "linkedin":    "<b>LN</b>",
    "لينكد":       "<b>LN</b>",
    "discord":     "<b>DC</b>",
    "ديسكورد":     "<b>DC</b>",
    "uber":        "<b>UB</b>",
    "bolt":        "<b>BT</b>",
    "careem":      "<b>CR</b>",
    "amazon":      "<b>AZ</b>",
    "netflix":     "📱",
    "spotify":     "<b>SP</b>",
    "apple":       "📱",
    "microsoft":   "<b>MS</b>",
    "paypal":      "📱",
    "binance":     "<b>BN</b>",
    "coinbase":    "<b>CB</b>",
}

def get_platform_emoji(sms_text):
    sms_lower = sms_text.lower()
    for keyword, emoji in PLATFORM_EMOJI_MAP.items():
        if keyword.lower() in sms_lower:
            return emoji
    return ""

def build_short_tag(number, country_upper):
    num_clean = number.strip().replace("+","").replace(" ","").replace("-","")
    if len(num_clean) >= 6:
        masked = num_clean[:3] + "●" * (len(num_clean) - 6) + num_clean[-3:]
    else:
        masked = num_clean
    first_letter = country_upper[0] if country_upper else "?"
    last_letter  = country_upper[-1] if country_upper else "?"
    return f"{first_letter}{last_letter}{masked}"

def mask_number(number):
    number = number.strip()
    if len(number) >= 6:
        start = number[:3]
        end = number[-3:]
        return f"{start}NB{end}"
    return number

def mask_number_str(number):
    return mask_number(number)

def get_country_info(number, html=True):
    number = number.strip().replace("+","").replace(" ","").replace("-","")
    for code, (name, flag, upper_name) in sorted(COUNTRY_CODES.items(), key=lambda x: len(x[0]), reverse=True):
        if number.startswith(code):
            final_flag = get_flag_html(flag) if html else get_flag_plain(flag)
            return name, final_flag, upper_name
    return "Unknown", "🌍", "UNKNOWN"

def extract_otp(message):
    patterns = [
        r'(?:code|رمز|كود|verification|تحقق|otp|pin)[:\s]+[‎]?(\d{3,8}(?:[- ]\d{3,4})?)',
        r'(\d{3})[- ](\d{3,4})',
        r'\b(\d{4,8})\b',
        r'[‎](\d{3,8})',
    ]
    for pattern in patterns:
        match = re.search(pattern, message, re.IGNORECASE)
        if match:
            if len(match.groups()) > 1:
                return ''.join(match.groups())
            return match.group(1).replace(' ', '').replace('-', '')
    all_numbers = re.findall(r'\d{4,8}', message)
    if all_numbers:
        return all_numbers[0]
    return "N/A"

def clean_html(text):
    if not text: return ""
    return re.sub(r'<[^>]+>', '', str(text)).strip()

def clean_for_copy(text):
    if not text: return ""
    t = re.sub(r']*>(.*?)', r'\1', str(text))
    t = re.sub(r'<[^>]+>', '', t)
    t = t.replace("&amp;", "&").replace("&lt;", "<").replace("&gt;", ">").replace("&nbsp;", " ")
    return t.strip()

def clean_number(number):
    if not number: return ""
    return re.sub(r'\D', '', str(number))

def _make_colored_btn(text, color=None, **kwargs):
    return types.InlineKeyboardButton(text, **kwargs)

def _send_number_msg(chat_id, text, number, file_id, user_id, country_code=None, platform_name=None, parse_mode="HTML"):
    import json as _json

    flag_emoji_id = None
    if country_code and country_code in COUNTRY_CODES:
        _, flag, _ = COUNTRY_CODES[country_code]
        flag_emoji_id = _extract_flag_emoji_id(flag)

    available = get_available_numbers_from_file(file_id)
    other_numbers = [n for n in available if str(n) != str(number)]
    random.shuffle(other_numbers)
    nums_pool = [number] + other_numbers
    nums_to_show = nums_pool[:4]

    number_rows = []
    for num in nums_to_show:
        display = "+" + str(num).lstrip("+")
        btn = {
            "text": display,
            "copy_text": {"text": display},
            "style": "danger"
        }
        if flag_emoji_id:
            btn["icon_custom_emoji_id"] = flag_emoji_id
        number_rows.append([btn])

    lang = get_user_lang(user_id)
    change_num_text = "تغيير الرقم" if lang == "ar" else "Change Number"
    change_country_text = "تغيير الدولة" if lang == "ar" else "Change Country"
    otp_text = "احصل على OTP" if lang == "ar" else "Get OTP"

    change_num_btn = {
        "text": change_num_text,
        "callback_data": f"change_num_{file_id}",
        "icon_custom_emoji_id": "6113844439292054570",
        "style": "primary"
    }

    platform_sid = None
    if country_code:
        conn = sqlite3.connect(DB_PATH, check_same_thread=False, timeout=10)
        c = conn.cursor()
        c.execute("SELECT section_id FROM combos WHERE id=?", (file_id,))
        r = c.fetchone()
        conn.close()
        if r:
            platform_sid = r[0]

    change_country_btn = {
        "text": change_country_text,
        "callback_data": f"platform_{platform_sid}" if platform_sid else "back_to_main",
        "icon_custom_emoji_id": "5447410659077661506",
        "style": "primary"
    }

    otp_link = get_otp_group_link() or "https://t.me/+1234567890"
    bottom_rows = [
        [change_num_btn, change_country_btn],
        [{
            "text": otp_text,
            "url": otp_link,
            "icon_custom_emoji_id": "5332423642850536254",
            "style": "primary"
        }]
    ]

    keyboard = {"inline_keyboard": number_rows + bottom_rows}

    import re as _re

    def _parse_html_to_entities(html):
        html = html.replace("&amp;", "&").replace("&lt;", "<").replace("&gt;", ">")

        plain = ""
        entities = []

        token_re = _re.compile(
            r"([\s\S]*?)"
            r"|<b>([\s\S]*?)</b>"
            r"|<strong>([\s\S]*?)</strong>"
            r"|<code>([\s\S]*?)</code>"
            r"|<blockquote>([\s\S]*?)</blockquote>"
            r"|<[^>]+>",
            _re.DOTALL
        )

        last = 0
        for m in token_re.finditer(html):
            raw = html[last:m.start()]
            plain += raw
            last = m.end()

            offset = len(plain.encode("utf-16-le")) // 2

            if m.group(1) is not None:
                emoji_id = m.group(1)
                fallback = m.group(2)
                fallback = _re.sub(r'<[^>]+>', '', fallback)
                length = len(fallback.encode("utf-16-le")) // 2
                if length > 0:
                    entities.append({
                        "type": "custom_emoji",
                        "offset": offset,
                        "length": length,
                        "custom_emoji_id": emoji_id
                    })
                plain += fallback

            elif m.group(3) is not None or m.group(4) is not None:
                inner = m.group(3) if m.group(3) is not None else m.group(4)
                inner = _re.sub(r'<[^>]+>', '', inner)
                length = len(inner.encode("utf-16-le")) // 2
                if length > 0:
                    entities.append({"type": "bold", "offset": offset, "length": length})
                plain += inner

            elif m.group(5) is not None:
                inner = m.group(5)
                length = len(inner.encode("utf-16-le")) // 2
                if length > 0:
                    entities.append({"type": "code", "offset": offset, "length": length})
                plain += inner

            elif m.group(6) is not None:
                inner = _re.sub(r'<[^>]+>', '', m.group(6))
                length = len(inner.encode("utf-16-le")) // 2
                if length > 0:
                    entities.append({"type": "blockquote", "offset": offset, "length": length})
                plain += inner

        plain += html[last:]
        return plain, entities

    plain_text, ent_list = _parse_html_to_entities(text)

    payload = {
        "chat_id": chat_id,
        "text": plain_text,
        "reply_markup": keyboard,
        "entities": ent_list,
    }
    try:
        r = requests.post(
            f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
            json=payload, timeout=15
        )
        if r.status_code != 200:
            err = r.text
            print(f"[number_msg] ❌ {r.status_code}: {err}")
            for admin in ADMIN_IDS:
                try:
                    bot.send_message(admin, f"❌ number_msg error:\n<code>{err[:500]}</code>", parse_mode="HTML")
                except:
                    pass
        return r.status_code == 200
    except Exception as e:
        print(f"[number_msg] ⚠️ {e}")
        return False

def _make_copy_btn(label, copy_value):
    try:
        return types.InlineKeyboardButton(
            label,
            copy_text=types.CopyTextButton(text=str(copy_value))
        )
    except Exception:
        return types.InlineKeyboardButton(label, callback_data=f"copy_fallback_{copy_value[:50]}")

def _parse_html_to_entities_global(html):
    import re as _re
    html = html.replace("&amp;", "&").replace("&lt;", "<").replace("&gt;", ">")
    plain = ""
    entities = []
    token_re = _re.compile(
        r"([\s\S]*?)"
        r"|<b>([\s\S]*?)</b>"
        r"|<strong>([\s\S]*?)</strong>"
        r"|<code>([\s\S]*?)</code>"
        r"|<blockquote>([\s\S]*?)</blockquote>"
        r"|<[^>]+>",
        _re.DOTALL
    )
    last = 0
    for m in token_re.finditer(html):
        raw = html[last:m.start()]
        plain += raw
        last = m.end()
        offset = len(plain.encode("utf-16-le")) // 2
        if m.group(1) is not None:
            emoji_id = m.group(1)
            fallback = m.group(2)
            fallback = _re.sub(r'<[^>]+>', '', fallback)
            length = len(fallback.encode("utf-16-le")) // 2
            if length > 0:
                entities.append({"type": "custom_emoji", "offset": offset, "length": length, "custom_emoji_id": emoji_id})
            plain += fallback
        elif m.group(3) is not None or m.group(4) is not None:
            inner = m.group(3) if m.group(3) is not None else m.group(4)
            inner = _re.sub(r'<[^>]+>', '', inner)
            length = len(inner.encode("utf-16-le")) // 2
            if length > 0:
                entities.append({"type": "bold", "offset": offset, "length": length})
            plain += inner
        elif m.group(5) is not None:
            inner = m.group(5)
            length = len(inner.encode("utf-16-le")) // 2
            if length > 0:
                entities.append({"type": "code", "offset": offset, "length": length})
            plain += inner
        elif m.group(6) is not None:
            inner = _re.sub(r'<[^>]+>', '', m.group(6))
            length = len(inner.encode("utf-16-le")) // 2
            if length > 0:
                entities.append({"type": "blockquote", "offset": offset, "length": length})
            plain += inner
    plain += html[last:]
    return plain, entities


def _send_copy_msg(chat_id, text, otp_code, extra_markup_rows=None, parse_mode="HTML", photo_bytes=None, number=None, voice_bytes=None):
    first_row = [{"text": "𝗖𝗢𝗣𝗬 𝗖𝗢𝗗𝗘", "copy_text": {"text": str(otp_code)}, "icon_custom_emoji_id": "4938635821105284442", "style": "danger"}]
    keyboard = {"inline_keyboard": [first_row]}
    if extra_markup_rows:
        for row in extra_markup_rows:
            keyboard["inline_keyboard"].append(row)
    import json as _json
    import io as _io

    try:
        if photo_bytes:
            r_photo = requests.post(
                f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto",
                data={"chat_id": chat_id},
                files={"photo": ("img.jpg", _io.BytesIO(photo_bytes), "image/jpeg")},
                timeout=15
            )
            photo_msg_id = r_photo.json().get("result", {}).get("message_id") if r_photo.status_code == 200 else None

            payload = {
                "chat_id": chat_id,
                "text": text,
                "parse_mode": "HTML",
                "reply_markup": keyboard,
            }
            if photo_msg_id:
                payload["reply_to_message_id"] = photo_msg_id
            r = requests.post(
                f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
                json=payload, timeout=15
            )
        else:
            payload = {
                "chat_id": chat_id,
                "text": text,
                "parse_mode": "HTML",
                "reply_markup": keyboard,
            }
            r = requests.post(
                f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
                json=payload, timeout=15
            )

        if r.status_code == 200:
            return r.json().get("result", {})
        elif r.status_code == 429:
            try:
                _retry_after = r.json().get("parameters", {}).get("retry_after", 10)
            except:
                _retry_after = 10
            print(f"[copy_btn] 429 - waiting {_retry_after}s for chat_id={chat_id}")
            time.sleep(_retry_after)
            try:
                r2 = requests.post(
                    f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
                    json=payload, timeout=15
                )
                if r2.status_code == 200:
                    return r2.json().get("result", {})
            except:
                pass
        else:
            err_json = {}
            try: err_json = r.json()
            except: pass
            desc = err_json.get("description", "")
            if "chat not found" not in desc:
                print(f"[copy_btn] ❌ status={r.status_code} | {r.text[:300]}")
                if "ENTITY_TEXT_INVALID" in desc or "parse entities" in desc.lower() or "can't parse" in desc.lower():
                    import re as _re3
                    plain_msg = _re3.sub(r']*>(.*?)', r'\1', text)
                    plain_msg = _re3.sub(r'<[^>]+>', '', plain_msg)
                    plain_msg = plain_msg.replace("&amp;", "&").replace("&lt;", "<").replace("&gt;", ">")
                    retry_payload = {
                        "chat_id": chat_id,
                        "text": plain_msg,
                        "reply_markup": keyboard,
                    }
                    try:
                        _r2 = requests.post(
                            f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
                            json=retry_payload, timeout=15
                        )
                        if _r2.status_code == 200:
                            print(f"[copy_btn] ✅ retry نجح للجروب {chat_id}")
                            return _r2.json().get("result", {})
                    except Exception as _re:
                        print(f"[copy_btn] retry فشل: {_re}")
    except Exception as e:
        print(f"[copy_btn] ⚠️ {e}")
    return None


def send_otp_to_user_and_group(date_str, number, sms, panel_name="", short_bold=""):
    if _is_otp_already_sent(number, sms, date_str):
        print(f"[dedup] ⛔ تجاهل كود مكرر: panel={panel_name} num={str(number)[:8]}")
        return
    print(f"[group_send] called panel={panel_name} num={str(number)[:8]}")
    if panel_name:
        with _panel_last_code_lock:
            _panel_last_code_time[panel_name] = time.time()
    otp_code = extract_otp(sms)
    user_id = get_user_by_number(number)
    if user_id:
        print(f"[otp_route] ✅ رقم {str(number)[:8]} → مستخدم {user_id}")
    else:
        print(f"[otp_route] ⚠️ رقم {str(number)[:8]} → لا يوجد مستخدم مرتبط")
    log_otp(number, otp_code, sms, user_id)

    _combo_price = 0.0
    _combo_id_for_tag = None
    _country_code_for_tag = None
    _clean_number = str(number).lstrip("+").strip()
    try:
        _conn_p = sqlite3.connect(DB_PATH, check_same_thread=False, timeout=10)
        _c_p = _conn_p.cursor()
        _c_p.execute("SELECT id, numbers, price_per_number, country_code FROM combos")
        for _cid, _nums_json, _price, _cc in _c_p.fetchall():
            try:
                _nums = json.loads(_nums_json)
                if _clean_number in [str(n).lstrip("+").strip() for n in _nums]:
                    _combo_price = float(_price or 0)
                    _combo_id_for_tag = _cid
                    _country_code_for_tag = _cc
                    break
            except:
                pass
        _conn_p.close()
    except Exception as _ep:
        print(f"[price_lookup] error: {_ep}")
    _existing_tag, _existing_price = get_combo_tag_for_number(number, with_price=True)
    if _existing_price > 0 and _combo_price == 0:
        _combo_price = _existing_price
    if not _existing_tag and _combo_id_for_tag and _country_code_for_tag:
        try:
            _conn_tag = sqlite3.connect(DB_PATH, check_same_thread=False, timeout=10)
            _c_tag = _conn_tag.cursor()
            _c_tag.execute("SELECT COUNT(*) FROM combos WHERE country_code=? AND id<=?",
                           (_country_code_for_tag, _combo_id_for_tag))
            _file_idx = (_c_tag.fetchone()[0] or 1) - 1
            _conn_tag.close()
            _tag = _generate_unique_combo_tag(_country_code_for_tag, _file_idx, combo_id=_combo_id_for_tag)
            if _tag:
                save_combo_tag_for_number(number, _tag, price=_combo_price)
        except:
            pass
    elif _existing_tag and _combo_price > 0 and _existing_price == 0:
        save_combo_tag_for_number(number, _existing_tag, price=_combo_price)

    _total_balance = 0.0
    if _combo_price > 0 and user_id:
        try:
            _conn_b = sqlite3.connect(DB_PATH, check_same_thread=False, timeout=10)
            _c_b = _conn_b.cursor()
            _c_b.execute("SELECT COALESCE(balance,0) FROM users WHERE user_id=?", (user_id,))
            _row_b = _c_b.fetchone()
            _total_balance = (_row_b[0] if _row_b else 0.0) + _combo_price
            _conn_b.close()
        except:
            _total_balance = _combo_price

    country_name, country_flag, country_upper = get_country_info(number, html=True)
    platform_emoji = get_platform_emoji(sms)
    if not platform_emoji and panel_name:
        _peid = get_platform_emoji_id(panel_name)
        if _peid:
            platform_emoji = f"🌐"
    if not platform_emoji:
        platform_emoji = "📩"
    number_masked = mask_number(number)
    country_short = to_bold(country_upper[:2]) if country_upper else to_bold("??")
    if not short_bold:
        short_bold = to_bold("??")

    if user_id:
        print(f"[otp_send] user_id={user_id} number={str(number)[:8]} price={_combo_price}")
        try:
            try:
                bot_info = bot.get_me()
                bot_url = f"https://t.me/{bot_info.username}"
            except Exception:
                bot_url = "https://t.me/FK_AY"
            custom_btns_all = get_custom_buttons()
            channel_url = custom_btns_all[0][2] if custom_btns_all else bot_url

            lang = get_user_lang(user_id)

            _combo_tag_user = get_combo_tag_for_number(number)
            _NO_COMBO_EMOJI_USER = "⚡"
            if _combo_tag_user:
                _range_label_user = to_bold(_combo_tag_user)
            else:
                _range_label_user = _NO_COMBO_EMOJI_USER

            _title_ar = "🔔 وصل كود جديد"
            _title_en = "🔔 New OTP Received"
            _title_line = _title_ar if lang == "ar" else _title_en

            _clean_num = str(number).lstrip("+").strip()
            _num_display = "+" + _clean_num[:3] + "XXXX" + _clean_num[-3:] if len(_clean_num) >= 6 else "+" + _clean_num

            _sep = "━━━━━━━━━━━━━━━━━━"
            _range_ar = "النطاق"
            _range_en = "Range"
            _number_ar = "الرقم"
            _number_en = "Number"
            _code_ar = "الكود"
            _code_en = "Your Code"
            _sms_ar = "الرسالة الكاملة"
            _sms_en = "Full SMS"

            msg_text = (
                f"✉️ <b>{_title_line}</b> "
                f"🚨\n"
                f"{_sep}\n\n"
                f"📶 "
                f"<b>{'النطاق' if lang == 'ar' else 'Range'} :</b> "
                f"{country_flag} {_range_label_user} {platform_emoji}\n"
                f"📱 "
                f"<b>{'الرقم' if lang == 'ar' else 'Number'} :</b> "
                f"{_num_display}\n"
                f"🔑 "
                f"<b>{'الكود' if lang == 'ar' else 'Your Code'} :</b> "
                f"<code>{otp_code}</code>\n\n"
                f"{_sep}\n\n"
                f"💬 "
                f"<b>{'الرسالة الكاملة' if lang == 'ar' else 'Full SMS'} #</b>\n"
                f"<blockquote>{sms}</blockquote>"
            )

            _copy_code_text = "نسخ الكود" if lang == "ar" else "𝗖𝗢𝗣𝗬 𝗖𝗢𝗗𝗘"
            _full_msg_text  = "نسخ الرسالة" if lang == "ar" else "𝗙𝗨𝗟𝗟 𝗠𝗘𝗦𝗦𝗔𝗚𝗘"

            keyboard_rows = [
                [
                    {"text": _full_msg_text, "copy_text": {"text": clean_for_copy(sms)},
                     "icon_custom_emoji_id": "5353036831581544549", "style": "danger"},
                    {"text": _copy_code_text, "copy_text": {"text": str(otp_code)},
                     "icon_custom_emoji_id": "4938635821105284442", "style": "danger"},
                ],
            ]
            group_btns = get_otp_group_buttons()
            for gbtn in group_btns:
                keyboard_rows.append([{"text": gbtn["text"], "url": gbtn["url"]}])

            _plain_msg, _entities_msg = _parse_html_to_entities_global(msg_text)
            user_payload = {
                "chat_id": user_id,
                "text": _plain_msg,
                "entities": _entities_msg,
                "reply_markup": {"inline_keyboard": keyboard_rows},
            }
            user_msg_id = None

            _ures = None
            for _attempt in range(5):
                try:
                    _ures = requests.post(
                        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
                        json=user_payload, timeout=20
                    )
                    if _ures.status_code == 429:
                        _retry_after = _ures.json().get("parameters", {}).get("retry_after", 5)
                        print(f"[user_send] 429 retry_after={_retry_after}s للمستخدم {user_id}")
                        time.sleep(max(_retry_after, 3))
                        continue
                    if _ures.status_code == 200:
                        print(f"[user_send] ✅ OTP وصل للمستخدم {user_id}")
                        break
                    if _ures.status_code == 400:
                        import re as _re_fb
                        plain_fb = _re_fb.sub(r']*>(.*?)', r'\1', msg_text)
                        plain_fb = _re_fb.sub(r'<[^>]+>', '', plain_fb)
                        plain_fb = plain_fb.replace("&amp;", "&").replace("&lt;", "<").replace("&gt;", ">")
                        _ures = requests.post(
                            f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
                            json={"chat_id": user_id, "text": plain_fb,
                                  "reply_markup": {"inline_keyboard": keyboard_rows}},
                            timeout=20
                        )
                        if _ures.status_code == 200:
                            print(f"[user_send] ✅ plain fallback وصل للمستخدم {user_id}")
                        break
                    # للأكواد التانية (500, 502...) نحاول مرة تانية
                    print(f"[user_send] ⚠️ HTTP {_ures.status_code} attempt={_attempt} - إعادة المحاولة...")
                    time.sleep(3)
                except Exception as _se:
                    print(f"[user_send] ⚠️ attempt={_attempt} error: {_se}")
                    time.sleep(3)

            try:
                _ures_json = _ures.json() if _ures else {}
                user_msg_id = _ures_json.get("result", {}).get("message_id")
                if user_msg_id:
                    try:
                        conn_um = sqlite3.connect(DB_PATH, check_same_thread=False, timeout=10)
                        c_um = conn_um.cursor()
                        c_um.execute(
                            "SELECT message_id FROM otp_user_messages WHERE user_id=? ORDER BY sent_at DESC LIMIT 1",
                            (str(user_id),)
                        )
                        old_row = c_um.fetchone()
                        conn_um.close()
                        if old_row:
                            try:
                                requests.post(
                                    f"https://api.telegram.org/bot{BOT_TOKEN}/deleteMessage",
                                    json={"chat_id": user_id, "message_id": old_row[0]},
                                    timeout=5
                                )
                            except:
                                pass
                    except:
                        pass
                    try:
                        conn_um2 = sqlite3.connect(DB_PATH, check_same_thread=False, timeout=10)
                        c_um2 = conn_um2.cursor()
                        c_um2.execute("""
                            CREATE TABLE IF NOT EXISTS otp_user_messages
                            (user_id TEXT, message_id INTEGER, sent_at TEXT)
                        """)
                        c_um2.execute(
                            "DELETE FROM otp_user_messages WHERE user_id=?",
                            (str(user_id),)
                        )
                        c_um2.execute(
                            "INSERT INTO otp_user_messages (user_id, message_id, sent_at) VALUES (?,?,?)",
                            (str(user_id), user_msg_id, datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                        )
                        conn_um2.commit()
                        conn_um2.close()
                    except:
                        pass
                else:
                    _desc = _ures_json.get("description", "")
                    _code = _ures.status_code if _ures else "N/A"
                    print(f"[user_send] ❌ فشل إرسال OTP للمستخدم {user_id} | status={_code} | {_desc}")
                    if _ures and _ures.status_code == 400:
                        import re as _re_fb
                        plain_fb = _re_fb.sub(r']*>(.*?)', r'\1', msg_text)
                        plain_fb = _re_fb.sub(r'<[^>]+>', '', plain_fb)
                        plain_fb = plain_fb.replace("&amp;", "&").replace("&lt;", "<").replace("&gt;", ">")
                        try:
                            _ures_fb = requests.post(
                                f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
                                json={
                                    "chat_id": user_id,
                                    "text": plain_fb,
                                    "reply_markup": {"inline_keyboard": keyboard_rows},
                                },
                                timeout=15
                            )
                            if _ures_fb.status_code == 200:
                                print(f"[user_send] ✅ fallback نجح للمستخدم {user_id}")
                        except:
                            pass
            except Exception as _pe:
                print(f"[user_send] ❌ exception بعد الإرسال للمستخدم {user_id}: {_pe}")

            _send_succeeded = (user_msg_id is not None) or (
                _ures is not None and _ures.status_code == 200
            )
            if _send_succeeded:
                remove_number_from_combo(number)
                if _combo_price > 0:
                    try:
                        _conn_b2 = sqlite3.connect(DB_PATH, check_same_thread=False, timeout=10)
                        _c_b2 = _conn_b2.cursor()
                        _c_b2.execute("UPDATE users SET balance = COALESCE(balance,0) + ? WHERE user_id=?",
                                     (_combo_price, user_id))
                        _c_b2.execute(
                            "INSERT INTO balance_log (user_id, amount, number, combo_tag, logged_at) VALUES (?,?,?,?,?)",
                            (user_id, _combo_price, str(number),
                             get_combo_tag_for_number(number) or "",
                             datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                        )
                        _conn_b2.commit()
                        _c_b2.execute("SELECT COALESCE(balance,0) FROM users WHERE user_id=?", (user_id,))
                        _row_b2 = _c_b2.fetchone()
                        _total_balance = _row_b2[0] if _row_b2 else _total_balance
                        _conn_b2.close()
                        print(f"[balance] ✅ أضيف ${_combo_price:.2f} للمستخدم {user_id} | الإجمالي=${_total_balance:.2f}")
                    except Exception as _be:
                        print(f"[balance] ❌ خطأ تحديث الرصيد: {_be}")
            else:
                print(f"[user_send] ⚠️ الإرسال فشل - لم يتم حذف الرقم أو تحديث الرصيد للحفاظ على البيانات")

            if _combo_price > 0 and _send_succeeded:
                try:
                    _bal_lang = get_user_lang(user_id)
                    _bal_lang = get_user_lang(user_id)
                    if _bal_lang == "ar":
                        _bal_msg = (
                            "💵 <b>تمت إضافة الرصيد!</b>\n\n"
                            "➕ <b>المضاف:</b> <b>$" + f"{_combo_price:.2f}" + "</b>\n"
                            "💰 <b>الإجمالي:</b> <b>$" + f"{_total_balance:.2f}" + "</b>"
                        )
                    else:
                        _bal_msg = (
                            "💵 <b>Balance Added!</b>\n\n"
                            "➕ <b>Added:</b> <b>$" + f"{_combo_price:.2f}" + "</b>\n"
                            "💰 <b>Total:</b> <b>$" + f"{_total_balance:.2f}" + "</b>"
                        )
                    requests.post(
                        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
                        json={"chat_id": user_id, "text": _bal_msg, "parse_mode": "HTML"},
                        timeout=10
                    )
                except:
                    pass
        except Exception as e:
            print(f"[!] خطأ إرسال OTP للمستخدم {user_id}: {e}")
            user_msg_id = None

    if not user_id:
        remove_number_from_combo(number)

    _combo_tag = get_combo_tag_for_number(number)
    _NO_COMBO_EMOJI = "⚡"
    if _combo_tag:
        _range_label = to_bold(_combo_tag)
    else:
        _range_label = _NO_COMBO_EMOJI

    group_msg = t("new_otp_group", None,
                   country_flag=country_flag,
                   platform_emoji=platform_emoji,
                   country_short=country_short,
                   number_masked=number_masked,
                   range_label=_range_label)
    try:
        bot_info = bot.get_me()
        bot_url = f"https://t.me/{bot_info.username}"
    except Exception:
        bot_url = "https://t.me/FK_AY"
    custom_btns_all = get_custom_buttons()
    channel_url = custom_btns_all[0][2] if custom_btns_all else bot_url
    for chat_id in CHAT_IDS:
        try:
            extra_rows = []
            extra_rows.append([{"text": "𝗙𝗨𝗟𝗟 𝗠𝗘𝗦𝗦𝗔𝗚𝗘", "copy_text": {"text": clean_for_copy(sms)}, "icon_custom_emoji_id": "5353036831581544549", "style": "danger"}])
            group_btns = get_otp_group_buttons()
            for gbtn in group_btns:
                extra_rows.append([{"text": gbtn["text"], "url": gbtn["url"]}])
            result = _send_copy_msg(
                chat_id=chat_id,
                text=group_msg,
                otp_code=otp_code,
                extra_markup_rows=extra_rows,
                parse_mode="HTML",
                photo_bytes=BOT_IMAGE_BYTES,
                number=number,
                voice_bytes=None
            )
            if result and result.get("message_id"):
                track_otp_tg_message(chat_id, result["message_id"])
        except Exception as e:
            print(f"[group_send] ⚠️ {e}")

def track_otp_tg_message(chat_id, message_id):
    conn = sqlite3.connect(DB_PATH, check_same_thread=False, timeout=10)
    c = conn.cursor()
    c.execute("INSERT INTO otp_tg_messages (chat_id, message_id, sent_at) VALUES (?, ?, ?)",
              (str(chat_id), message_id, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    conn.commit()
    conn.close()

@bot.callback_query_handler(func=lambda call: call.data == "admin_panel_accounts")
def admin_panel_accounts(call):
    if not is_admin(call.from_user.id): return
    markup = types.InlineKeyboardMarkup(row_width=2)
    btns = []
    for sk, site in PANEL_SITES.items():
        accounts = get_panel_accounts(sk)
        btns.append(types.InlineKeyboardButton(
            f"{site['name']} ({len(accounts)})",
            callback_data=f"panel_site_{sk}"
        ))
    for i in range(0, len(btns), 2):
        markup.row(*btns[i:i+2])
    markup.add(types.InlineKeyboardButton("رجوع", callback_data="admin_panel", icon_custom_emoji_id="5433757980245900289", style="success"))
    safe_edit_or_delete(call,
        "👥 <b>إدارة حسابات اللوحات</b>\n\nاختر اللوحة:",
        markup=markup, parse_mode="HTML"
    )

@bot.callback_query_handler(func=lambda call: call.data.startswith("panel_site_"))
def panel_site_callback(call):
    if not is_admin(call.from_user.id): return
    site_key = call.data.replace("panel_site_", "")
    if site_key not in PANEL_SITES:
        bot.answer_callback_query(call.id, "❌ لوحة غير موجودة", show_alert=True)
        return
    site = PANEL_SITES[site_key]
    accounts = get_panel_accounts(site_key)
    text = f"👥 <b>{site['name']}</b>\n\n"
    if accounts:
        for i, acc in enumerate(accounts, 1):
            running = _panel_threads.get(f"{site_key}_{acc['id']}", None)
            status = "🟢" if running and running.is_alive() else "🔴"
            src_label = " 📌" if acc.get("source") == "default" else " 👤"
            text += f"{i}. {status}{src_label} <code>{acc['username']}</code>\n"
    else:
        text += "⚠️ لا توجد حسابات\n"
    text += "\n📌 = من الملف | 👤 = مضاف من الأدمن"
    if PANEL_SITES.get(site_key, {}).get("type") == "api":
        text += "\n⚡ لوحة API - التوكن من الملف مباشرة"
    markup = types.InlineKeyboardMarkup()
    for acc in accounts:
        if acc.get("source") != "default":
            markup.add(types.InlineKeyboardButton(
                f"🗑️ حذف {acc['username']}",
                callback_data=f"del_panel_acc_{site_key}_{acc['id']}"
            ))
    markup.add(types.InlineKeyboardButton("➕ إضافة حساب", callback_data=f"add_panel_acc_{site_key}"))
    markup.add(types.InlineKeyboardButton("رجوع", callback_data="admin_panel_accounts", icon_custom_emoji_id="5433757980245900289", style="success"))
    safe_edit_or_delete(call, text, markup=markup, parse_mode="HTML")

@bot.callback_query_handler(func=lambda call: call.data.startswith("add_panel_acc_"))
def add_panel_acc_step1(call):
    if not is_admin(call.from_user.id): return
    site_key = call.data.replace("add_panel_acc_", "")
    site = PANEL_SITES[site_key]
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("❌ إلغاء", callback_data=f"panel_site_{site_key}"))
    if site.get("type") in ("api_token", "api"):
        user_states[call.from_user.id] = {"action": "panel_acc_api_token", "site_key": site_key}
        safe_edit_or_delete(call,
            f"➕ <b>إضافة حساب - {site['name']}</b>\n\n🔑 أرسل API Token:",
            markup=markup, parse_mode="HTML"
        )
    else:
        user_states[call.from_user.id] = {"action": "panel_acc_username", "site_key": site_key}
        safe_edit_or_delete(call,
            f"➕ <b>إضافة حساب - {site['name']}</b>\n\n📝 أرسل اسم المستخدم:",
            markup=markup, parse_mode="HTML"
        )

@bot.callback_query_handler(func=lambda call: call.data.startswith("del_panel_acc_"))
def del_panel_acc(call):
    if not is_admin(call.from_user.id): return
    parts = call.data.replace("del_panel_acc_", "").rsplit("_", 1)
    if len(parts) < 2: return
    site_key, account_id = parts[0], parts[1]
    if delete_panel_account(site_key, account_id):
        bot.answer_callback_query(call.id, "✅ تم حذف الحساب وإيقاف المراقبة", show_alert=True)
    else:
        bot.answer_callback_query(call.id, "❌ فشل الحذف", show_alert=True)
    panel_site_callback(call)

@bot.message_handler(func=lambda msg: isinstance(user_states.get(msg.from_user.id), dict) and
                     user_states[msg.from_user.id].get("action") == "panel_acc_username")
def panel_acc_username(message):
    user_id = message.from_user.id
    user_states[user_id]["username"] = message.text.strip()
    user_states[user_id]["action"] = "panel_acc_password"
    bot.reply_to(message, "🔑 أرسل كلمة المرور:")

@bot.message_handler(func=lambda msg: isinstance(user_states.get(msg.from_user.id), dict) and
                     user_states[msg.from_user.id].get("action") == "panel_acc_password")
def panel_acc_password(message):
    user_id = message.from_user.id
    state = user_states.pop(user_id)
    site_key = state["site_key"]
    username = state["username"]
    password = message.text.strip()
    account = add_panel_account(site_key, username, password)
    start_panel_account_monitor(site_key, account)
    bot.reply_to(message,
        f"✅ <b>تم إضافة الحساب وبدء المراقبة!</b>\n\n"
        f"🏦 اللوحة: {PANEL_SITES[site_key]['name']}\n"
        f"👤 اليوزر: <code>{username}</code>",
        parse_mode="HTML"
    )

@bot.callback_query_handler(func=lambda call: call.data.startswith("copy_fallback_"))
def copy_fallback_handler(call):
    value = call.data[len("copy_fallback_"):]
    bot.answer_callback_query(call.id, f"📋 {value}", show_alert=True)

@bot.callback_query_handler(func=lambda call: call.data.startswith("copy_num_"))
def copy_num_callback(call):
    number = call.data[9:]
    bot.answer_callback_query(call.id, f"📋 {number}", show_alert=True)

@bot.callback_query_handler(func=lambda call: call.data.startswith("copy_"))
def copy_callback(call):
    otp = call.data[5:]
    bot.answer_callback_query(call.id, f"📋 {otp}", show_alert=True)

COUNTRY_CODES = {
    "1": ("USA/Canada", "🇺🇸", "USA/CANADA"),
    "7": ("Russia", "🇷🇺", "RUSSIA"),
    "20": ("Egypt", "🇪🇬", "EGYPT"),
    "27": ("South Africa", "🇿🇦", "SOUTH AFRICA"),
    "30": ("Greece", "🇬🇷", "GREECE"),
    "31": ("Netherlands", "🇳🇱", "NETHERLANDS"),
    "32": ("Belgium", "🇧🇪", "BELGIUM"),
    "33": ("France", "🇫🇷", "FRANCE"),
    "34": ("Spain", "🇪🇸", "SPAIN"),
    "36": ("Hungary", "🇭🇺", "HUNGARY"),
    "39": ("Italy", "🇮🇹", "ITALY"),
    "40": ("Romania", "🇷🇴", "ROMANIA"),
    "41": ("Switzerland", "🇨🇭", "SWITZERLAND"),
    "43": ("Austria", "🇦🇹", "AUSTRIA"),
    "44": ("UK", "🇬🇧", "UK"),
    "45": ("Denmark", "🇩🇰", "DENMARK"),
    "46": ("Sweden", "🇸🇪", "SWEDEN"),
    "47": ("Norway", "🇳🇴", "NORWAY"),
    "48": ("Poland", "🇵🇱", "POLAND"),
    "49": ("Germany", "🇩🇪", "GERMANY"),
    "51": ("Peru", "🇵🇪", "PERU"),
    "52": ("Mexico", "🇲🇽", "MEXICO"),
    "53": ("Cuba", "🇨🇺", "CUBA"),
    "54": ("Argentina", "🇦🇷", "ARGENTINA"),
    "55": ("Brazil", "🇧🇷", "BRAZIL"),
    "56": ("Chile", "🇨🇱", "CHILE"),
    "57": ("Colombia", "🇨🇴", "COLOMBIA"),
    "58": ("Venezuela", "🇻🇪", "VENEZUELA"),
    "60": ("Malaysia", "🇲🇾", "MALAYSIA"),
    "61": ("Australia", "🇦🇺", "AUSTRALIA"),
    "62": ("Indonesia", "🇮🇩", "INDONESIA"),
    "63": ("Philippines", "🇵🇭", "PHILIPPINES"),
    "64": ("New Zealand", "🇳🇿", "NEW ZEALAND"),
    "65": ("Singapore", "🇸🇬", "SINGAPORE"),
    "66": ("Thailand", "🇹🇭", "THAILAND"),
    "81": ("Japan", "🇯🇵", "JAPAN"),
    "82": ("South Korea", "🇰🇷", "SOUTH KOREA"),
    "84": ("Vietnam", "🇻🇳", "VIETNAM"),
    "86": ("China", "🇨🇳", "CHINA"),
    "90": ("Turkey", "🇹🇷", "TURKEY"),
    "91": ("India", "🇮🇳", "INDIA"),
    "92": ("Pakistan", "🇵🇰", "PAKISTAN"),
    "93": ("Afghanistan", "🇦🇫", "AFGHANISTAN"),
    "94": ("Sri Lanka", "🇱🇰", "SRI LANKA"),
    "95": ("Myanmar", "🇲🇲", "MYANMAR"),
    "98": ("Iran", "🇮🇷", "IRAN"),
    "212": ("Morocco", "🇲🇦", "MOROCCO"),
    "213": ("Algeria", "🇩🇿", "ALGERIA"),
    "216": ("Tunisia", "🇹🇳", "TUNISIA"),
    "218": ("Libya", "🇱🇾", "LIBYA"),
    "220": ("Gambia", "🇬🇲", "GAMBIA"),
    "221": ("Senegal", "🇸🇳", "SENEGAL"),
    "222": ("Mauritania", "🇲🇷", "MAURITANIA"),
    "223": ("Mali", "🇲🇱", "MALI"),
    "224": ("Guinea", "🇬🇳", "GUINEA"),
    "225": ("Ivory Coast", "🇨🇮", "IVORY COAST"),
    "226": ("Burkina Faso", "🇧🇫", "BURKINA FASO"),
    "227": ("Niger", "🇳🇪", "NIGER"),
    "228": ("Togo", "🇹🇬", "TOGO"),
    "229": ("Benin", "🇧🇯", "BENIN"),
    "230": ("Mauritius", "🇲🇺", "MAURITIUS"),
    "231": ("Liberia", "🇱🇷", "LIBERIA"),
    "232": ("Sierra Leone", "🇸🇱", "SIERRA LEONE"),
    "233": ("Ghana", "🇬🇭", "GHANA"),
    "234": ("Nigeria", "🇳🇬", "NIGERIA"),
    "235": ("Chad", "🇹🇩", "CHAD"),
    "236": ("C. African Rep", "🇨🇫", "CENTRAL AFRICAN REPUBLIC"),
    "237": ("Cameroon", "🇨🇲", "CAMEROON"),
    "238": ("Cape Verde", "🇨🇻", "CAPE VERDE"),
    "239": ("Sao Tome", "🇸🇹", "SAO TOME"),
    "240": ("Eq. Guinea", "🇬🇶", "EQUATORIAL GUINEA"),
    "241": ("Gabon", "🇬🇦", "GABON"),
    "242": ("Congo", "🇨🇬", "CONGO"),
    "243": ("DR Congo", "🇨🇩", "DR CONGO"),
    "244": ("Angola", "🇦🇴", "ANGOLA"),
    "245": ("Guinea-Bissau", "🇬🇼", "GUINEA-BISSAU"),
    "248": ("Seychelles", "🇸🇨", "SEYCHELLES"),
    "249": ("Sudan", "🇸🇩", "SUDAN"),
    "250": ("Rwanda", "🇷🇼", "RWANDA"),
    "251": ("Ethiopia", "🇪🇹", "ETHIOPIA"),
    "252": ("Somalia", "🇸🇴", "SOMALIA"),
    "253": ("Djibouti", "🇩🇯", "DJIBOUTI"),
    "254": ("Kenya", "🇰🇪", "KENYA"),
    "255": ("Tanzania", "🇹🇿", "TANZANIA"),
    "256": ("Uganda", "🇺🇬", "UGANDA"),
    "257": ("Burundi", "🇧🇮", "BURUNDI"),
    "258": ("Mozambique", "🇲🇿", "MOZAMBIQUE"),
    "260": ("Zambia", "🇿🇲", "ZAMBIA"),
    "261": ("Madagascar", "🇲🇬", "MADAGASCAR"),
    "263": ("Zimbabwe", "🇿🇼", "ZIMBABWE"),
    "264": ("Namibia", "🇳🇦", "NAMIBIA"),
    "265": ("Malawi", "🇲🇼", "MALAWI"),
    "266": ("Lesotho", "🇱🇸", "LESOTHO"),
    "267": ("Botswana", "🇧🇼", "BOTSWANA"),
    "268": ("Eswatini", "🇸🇿", "ESWATINI"),
    "269": ("Comoros", "🇰🇲", "COMOROS"),
    "350": ("Gibraltar", "🇬🇮", "GIBRALTAR"),
    "351": ("Portugal", "🇵🇹", "PORTUGAL"),
    "352": ("Luxembourg", "🇱🇺", "LUXEMBOURG"),
    "353": ("Ireland", "🇮🇪", "IRELAND"),
    "354": ("Iceland", "🇮🇸", "ICELAND"),
    "355": ("Albania", "🇦🇱", "ALBANIA"),
    "356": ("Malta", "🇲🇹", "MALTA"),
    "357": ("Cyprus", "🇨🇾", "CYPRUS"),
    "358": ("Finland", "🇫🇮", "FINLAND"),
    "359": ("Bulgaria", "🇧🇬", "BULGARIA"),
    "370": ("Lithuania", "🇱🇹", "LITHUANIA"),
    "371": ("Latvia", "🇱🇻", "LATVIA"),
    "372": ("Estonia", "🇪🇪", "ESTONIA"),
    "373": ("Moldova", "🇲🇩", "MOLDOVA"),
    "374": ("Armenia", "🇦🇲", "ARMENIA"),
    "375": ("Belarus", "🇧🇾", "BELARUS"),
    "376": ("Andorra", "🇦🇩", "ANDORRA"),
    "377": ("Monaco", "🇲🇨", "MONACO"),
    "378": ("San Marino", "🇸🇲", "SAN MARINO"),
    "380": ("Ukraine", "🇺🇦", "UKRAINE"),
    "381": ("Serbia", "🇷🇸", "SERBIA"),
    "382": ("Montenegro", "🇲🇪", "MONTENEGRO"),
    "385": ("Croatia", "🇭🇷", "CROATIA"),
    "386": ("Slovenia", "🇸🇮", "SLOVENIA"),
    "387": ("Bosnia", "🇧🇦", "BOSNIA"),
    "389": ("N. Macedonia", "🇲🇰", "NORTH MACEDONIA"),
    "420": ("Czech Rep", "🇨🇿", "CZECH REPUBLIC"),
    "421": ("Slovakia", "🇸🇰", "SLOVAKIA"),
    "501": ("Belize", "🇧🇿", "BELIZE"),
    "502": ("Guatemala", "🇬🇹", "GUATEMALA"),
    "503": ("El Salvador", "🇸🇻", "EL SALVADOR"),
    "504": ("Honduras", "🇭🇳", "HONDURAS"),
    "505": ("Nicaragua", "🇳🇮", "NICARAGUA"),
    "506": ("Costa Rica", "🇨🇷", "COSTA RICA"),
    "507": ("Panama", "🇵🇦", "PANAMA"),
    "509": ("Haiti", "🇭🇹", "HAITI"),
    "591": ("Bolivia", "🇧🇴", "BOLIVIA"),
    "592": ("Guyana", "🇬🇾", "GUYANA"),
    "593": ("Ecuador", "🇪🇨", "ECUADOR"),
    "595": ("Paraguay", "🇵🇾", "PARAGUAY"),
    "597": ("Suriname", "🇸🇷", "SURINAME"),
    "598": ("Uruguay", "🇺🇾", "URUGUAY"),
    "670": ("Timor-Leste", "🇹🇱", "TIMOR-LESTE"),
    "673": ("Brunei", "🇧🇳", "BRUNEI"),
    "675": ("Papua N. Guinea", "🇵🇬", "PAPUA NEW GUINEA"),
    "680": ("Palau", "🇵🇼", "PALAU"),
    "685": ("Samoa", "🇼🇸", "SAMOA"),
    "686": ("Kiribati", "🇰🇮", "KIRIBATI"),
    "691": ("Micronesia", "🇫🇲", "MICRONESIA"),
    "850": ("North Korea", "🇰🇵", "NORTH KOREA"),
    "852": ("Hong Kong", "🇭🇰", "HONG KONG"),
    "855": ("Cambodia", "🇰🇭", "CAMBODIA"),
    "856": ("Laos", "🇱🇦", "LAOS"),
    "880": ("Bangladesh", "🇧🇩", "BANGLADESH"),
    "886": ("Taiwan", "🇹🇼", "TAIWAN"),
    "960": ("Maldives", "🇲🇻", "MALDIVES"),
    "961": ("Lebanon", "🇱🇧", "LEBANON"),
    "962": ("Jordan", "🇯🇴", "JORDAN"),
    "963": ("Syria", "🇸🇾", "SYRIA"),
    "964": ("Iraq", "🇮🇶", "IRAQ"),
    "965": ("Kuwait", "🇰🇼", "KUWAIT"),
    "966": ("Saudi Arabia", "🇸🇦", "SAUDI ARABIA"),
    "967": ("Yemen", "🇾🇪", "YEMEN"),
    "968": ("Oman", "🇴🇲", "OMAN"),
    "970": ("Palestine", "🇵🇸", "PALESTINE"),
    "971": ("UAE", "🇦🇪", "UAE"),
    "972": ("Israel", "🇮🇱", "ISRAEL"),
    "973": ("Bahrain", "🇧🇭", "BAHRAIN"),
    "974": ("Qatar", "🇶🇦", "QATAR"),
    "975": ("Bhutan", "🇧🇹", "BHUTAN"),
    "976": ("Mongolia", "🇲🇳", "MONGOLIA"),
    "977": ("Nepal", "🇳🇵", "NEPAL"),
    "992": ("Tajikistan", "🇹🇯", "TAJIKISTAN"),
    "993": ("Turkmenistan", "🇹🇲", "TURKMENISTAN"),
    "994": ("Azerbaijan", "🇦🇿", "AZERBAIJAN"),
    "995": ("Georgia", "🇬🇪", "GEORGIA"),
    "996": ("Kyrgyzstan", "🇰🇬", "KYRGYZSTAN"),
    "998": ("Uzbekistan", "🇺🇿", "UZBEKISTAN"),
}

def get_flag_html(flag_str):
    return flag_str

def get_flag_plain(flag_str):
    import re as _re
    if not flag_str:
        return "🌍"
    match = _re.search(r']*>(.*?)', flag_str)
    if match:
        return match.group(1).strip()
    return flag_str

def _extract_flag_emoji_id(flag_str):
    import re as _re
    if not flag_str:
        return None
    match = _re.search(r"emoji-id='(\d+)'", flag_str)
    if match:
        return match.group(1)
    return None

def _get_used_numbers():
    conn = sqlite3.connect(DB_PATH, check_same_thread=False, timeout=10)
    c = conn.cursor()
    c.execute("SELECT assigned_number FROM users WHERE assigned_number IS NOT NULL AND assigned_number!=''")
    used = set()
    for row in c.fetchall():
        raw = str(row[0]).strip()
        used.add(raw)
        used.add(_normalize_num(raw))
    conn.close()
    return used

def periodic_group_message():
    while True:
        for chat_id in CHAT_IDS:
            try:
                msg = t("group_periodic", None)
                sent = bot.send_message(chat_id, msg)
                track_otp_tg_message(chat_id, sent.message_id)
            except:
                pass
        time.sleep(300)

def auto_backup_db():
    """يرسل نسخة من قاعدة البيانات للأدمن كل 10 دقايق"""
    import shutil
    import os
    while True:
        time.sleep(600)  # 10 دقايق
        try:
            backup_path = DB_PATH + ".backup_tmp"
            # نعمل نسخة آمنة بدون قفل
            try:
                import sqlite3 as _sq
                src = _sq.connect(DB_PATH)
                dst = _sq.connect(backup_path)
                src.backup(dst)
                src.close()
                dst.close()
            except Exception as _be:
                shutil.copy2(DB_PATH, backup_path)

            from datetime import datetime as _dt
            now_str = _dt.now().strftime("%Y-%m-%d_%H-%M")
            send_name = f"sendako_backup_{now_str}.db"

            for admin_id in set(ADMIN_IDS):
                try:
                    with open(backup_path, "rb") as f:
                        requests.post(
                            f"https://api.telegram.org/bot{BOT_TOKEN}/sendDocument",
                            data={
                                "chat_id": admin_id,
                                "caption": f"🗄 <b>نسخة احتياطية تلقائية</b>\n📅 {now_str}",
                                "parse_mode": "HTML"
                            },
                            files={"document": (send_name, f, "application/octet-stream")},
                            timeout=30
                        )
                    print(f"[backup] ✅ تم إرسال DB للأدمن {admin_id}")
                except Exception as _ae:
                    print(f"[backup] ❌ فشل الإرسال للأدمن {admin_id}: {_ae}")

            try:
                os.remove(backup_path)
            except:
                pass
        except Exception as e:
            print(f"[backup] ⚠️ خطأ في النسخ الاحتياطي: {e}")

def auto_delete_otp_logs():
    while True:
        try:
            conn = sqlite3.connect(DB_PATH, check_same_thread=False, timeout=10)
            c = conn.cursor()
            c.execute("SELECT id, chat_id, message_id, sent_at FROM otp_tg_messages")
            messages = c.fetchall()
            now = datetime.now()
            for row_id, chat_id, message_id, sent_at_str in messages:
                sent_at = datetime.strptime(sent_at_str, "%Y-%m-%d %H:%M:%S")
                delete_after = get_auto_delete_time(chat_id)
                delta = (now - sent_at).total_seconds()
                if delta > delete_after:
                    try:
                        bot.delete_message(chat_id, message_id)
                    except:
                        pass
                    c.execute("DELETE FROM otp_tg_messages WHERE id=?", (row_id,))
            otp_del = get_otp_delete_global()
            c.execute("""
                DELETE FROM otp_logs
                WHERE (julianday('now') - julianday(timestamp)) * 86400 > ?
            """, (otp_del,))
            conn.commit()
            conn.close()
        except Exception as e:
            print(f"[auto_delete] ⚠️ {e}")
        time.sleep(30)

def run_bot():
    while True:
        try:
            print("[sendako] 🤖 \033[92mتشغيل البوت...\033[0m")
            try:
                bot.set_my_commands([
                    types.BotCommand("/start", "ابدأ البوت / Start The Bot"),
                    types.BotCommand("/language", "تغيير اللغة / Change Language"),
                ])
            except Exception as _e:
                print(f"[commands] ⚠️ {_e}")
            bot.infinity_polling(timeout=30, long_polling_timeout=15)
        except Exception as e:
            print(f"[sendako] ⚠️ توقف البوت - إعادة التشغيل بعد 5 ثوانٍ: {e}")
            time.sleep(5)

def safe_main_loop():
    while True:
        try:
            main_loop()
        except Exception as e:
            print(f"[tenjiko] ⚠️ خطأ في main_loop - إعادة التشغيل بعد 10 ثوانٍ: {e}")
            time.sleep(10)

if __name__ == "__main__":
    threading.Thread(target=run_bot, daemon=True).start()
    threading.Thread(target=lambda: None, daemon=True).start()  # placeholder
    threading.Thread(target=auto_delete_otp_logs, daemon=True).start()
    threading.Thread(target=periodic_group_message, daemon=True).start()
    threading.Thread(target=auto_backup_db, daemon=True).start()
    safe_main_loop()
