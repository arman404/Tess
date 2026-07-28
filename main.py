import asyncio
import io
import re
import json
import html
import os
import httpx
import random
import string
import time
import unicodedata
from datetime import datetime, timedelta
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters, CallbackQueryHandler
from telegram.request import HTTPXRequest

try:
    from telegram import CopyTextButton
    HAS_COPY_BTN = True
except ImportError:
    HAS_COPY_BTN = False

# ==================== EMOJI CONFIGURATION ENGINE ====================

EMOJI_ID_MAP = {
    "telegram": "5271801931814165886",
    "instagram": "5269682734820777950",
    "facebook": "5269427536453984598",
    "tiktok": "5271527792641595125",
    "x": "5269500885905468781",
    "whatsapp": "5271536803482981220",
    "discord": "5807892405306791778",
    "uber": "5298715455316303708",
    "up": "5244837092042750681",
    "down": "5246762912428603768",
    "add": "5397916757333654639",
    "setting": "5341715473882955310",
    "1st": "5440539497383087970",
    "2st": "5447203607294265305",
    "3rd": "5453902265922376865",
    "free": "5406756500108501710",
    "msg": "5253742260054409879",
    "link": "5271604874419647061",
    "status": "5231200819986047254",
    "home": "5416041192905265756",
    "gift_box": "5970074171449808121",
    "delete": "5422557736330106570",
    "refer_btn": "5420396762189831222",
    "get_number_btn": "5382357040008021292",
    "cross": "5420130255174145507",
    "stop": "5956074558044770726",
    "ban": "5420323339723881652",
    "done": "6298670698948724690",
    "nagad": "5352985330628730418",
    "bkash": "5348469219761626211",
    "rocket": "5346042941196507141",
    "binance": "5348212415077064131",
    "live": "5355102594886833928",
    "channel": "6215074610845585917",
    "admin": "5350396951407895212",
    "waiting": "6217721388736712699",
    "back": "5267490665117275176",
    "leader_board": "5280769763398671636",
    "money": "6233367447789899509",
    "change_number": "5402186569006210455"
}

PREMIUM_FLAGS = {
    "🇺🇸": "5913463998522592692", "🇺🇦": "5911406692007941050", "🇵🇱": "5913550391789752571",
    "🇰🇿": "5913724621433082323", "🇨🇳": "5913779335021466780", "🇦🇿": "5911197578640233518",
    "🇪🇺": "5911106310585193018", "🇦🇲": "5913272455866093666", "🇷🇺": "5913274246867456342",
    "🇺🇿": "5911051846104912282", "🇩🇪": "5911096835887337583", "🇯🇵": "5913293711659241040",
    "🇹🇷": "5910995113881901195", "🇧🇾": "5911011185649521599", "🇬🇧": "5913443365499703513",
    "🇮🇳": "5913754823643107921", "🇧🇷": "5911148568768418614", "🇿🇲": "5913564754160389778",
    "🇾🇪": "5913346492512341993", "🇻🇳": "5913428887164949581", "🇨🇲": "5911172109484167745",
    "🇨🇮": "5222233374948602940", "🇲🇬": "5913766918271012920", "🇷🇴": "5913460373570195273",
    "🇨🇫": "5913443245240619222", "🇹🇬": "5913423260757790970", "🇧🇯": "5913735869952430547",
    "🇸🇱": "5911210450657218661", "🇧🇩": "5911365056594973179", "🇰🇷": "5913371673905598425",
    "🇬🇶": "5911306279967529251", "🇬🇱": "5292014752283774878", "🇫🇴": "5296469342039327674",
    "🇧🇳": "5911336409163109113", "🇧🇬": "5294329219965272288", "🇧🇫": "5913407764515786948",
    "🇪🇷": "5433723401464198287", "🇲🇼": "5433968339154122439", "🇲🇷": "5433859405898594234",
    "🇳🇷": "5434131139889478358", "🇸🇦": "4985897134424328239", "🇹🇴": "5433640100573491806",
    "🇹🇻": "5433684690923961019", "🇹🇼": "5366187256937726720", "🇭🇰": "5292166459118606932",
    "🇲🇴": "6323557758096377611", "🇨🇺": "5431551436502611633", "🇰🇵": "5434142701941437163",
    "🇻🇪": "5434009132753499322", "🇸🇾": "5433910876786670092", "🇲🇲": "5433666360003540231",
    "🇳🇮": "5334807849418003620", "🇬🇳": "5913471858312744319", "🇰🇪": "5222279743415531561",
    "🏴󠁧󠁢󠁷󠁬󠁳󠁿": "5911297801702084799", "🇻🇦": "5911211932420938860", "🇻🇺": "5913511535220625585",
    "🇺🇾": "5913623088406204470", "🇦🇪": "5913726554168365343", "🇺🇬": "5913488939397681980",
    "🇹🇲": "5913315521503170180", "🇹🇳": "5911332947419468671", "🇹🇹": "5911228635548750294",
    "🇹🇭": "5913617968805187987", "🇹🇿": "5911418949844603556", "🇹🇯": "5911287639809463107",
    "🇨🇭": "5913271227505448072", "🇸🇪": "5911156510162949403", "🇸🇿": "5913374525763883286",
    "🇸🇷": "5913275539652611719", "🇸🇩": "5911387497799094470", "🇪🇸": "5911193287967904547",
    "🇱🇰": "5911293163137406640", "🇸🇸": "5911406262511211744", "🇿🇦": "5911203119148044594",
    "🇸🇴": "5911397852965244436", "🇸🇧": "5911482712929080608", "🇸🇮": "5913431983836368644",
    "🇸🇰": "5913751666842145020", "🇸🇬": "5911531460808051849", "🇸🇨": "5911185183364616913",
    "🇷🇸": "5913592598433369871", "🇸🇳": "5910995302860461643", "🏴󠁧󠁢󠁳󠁣󠁴󠁿": "5911460091336331851",
    "🇸🇹": "5913574331937462345", "🇸🇲": "5913587968458625465", "🇼🇸": "5913325971158602854",
    "🇰🇳": "5913691898077253637", "🇻🇨": "5911318941531116255", "🇱🇨": "5911243659344351824",
    "🇵🇸": "5913684768431541668", "🇷🇼": "5911455229433352234", "🇶🇦": "5911260864983339619",
    "🇵🇷": "5911504350974317480", "🇵🇹": "5911023653939581472", "🇵🇭": "5911268638874145162",
    "🇵🇪": "5911207993935925780", "🇵🇾": "5911014265141072316", "🇵🇬": "5911107251183030903",
    "🇵🇦": "5913428968769327174", "🇵🇼": "5911283903187915549", "🇵🇰": "5913705895375672082",
    "🇴🇲": "5913570801474343473", "🇳🇴": "5913617397574537046", "🇳🇬": "5911143844304393105",
    "🇳🇪": "5911270086278124251", "🇳🇿": "5913640044937089340", "🇳🇱": "5913367645226275100",
    "🇳🇵": "5913496520014958723", "🇳🇦": "5911108535378252443", "🇲🇿": "5911333419865871464",
    "🇲🇦": "5911482111633658301", "🇲🇪": "5913239436157522151", "🇲🇳": "5911041383564580038",
    "🇲🇨": "5911245347266500057", "🇲🇩": "5913456847402045950", "🇲🇻": "5913501399097806832",
    "🇲🇱": "5911305266355245916", "🇲🇹": "5911023714069123567", "🇧🇲": "5913680005312811090",
    "🇲🇶": "5911378005921370347", "🇲🇭": "5913235935759175692", "🇲🇺": "5913291113204027321",
    "🇲🇽": "5913687302462246518", "🇫🇲": "5911271104185373336", "🇲🇾": "5913654360063087453",
    "🇲🇰": "5913394029210374721", "🇱🇺": "5913390842344640293", "🇱🇹": "5911172315642597775",
    "🇱🇮": "5911166650580734660", "🇱🇾": "5911236989260140996", "🇱🇷": "5913324167272337727",
    "🇰🇮": "5911294443037660118", "🇽🇰": "5911433681582429010", "🇰🇼": "5913290705182134003",
    "🇰🇬": "5911202161370337549", "🇱🇦": "5913718526874489279", "🇱🇻": "5913738489882480243",
    "🇱🇧": "5911504273664905447", "🇱🇸": "5911059881988723711", "🇮🇩": "5913479361620611038",
    "🇮🇷": "5911308891307643032", "🇮🇶": "5911382442622587735", "🇮🇪": "5913440715504881532",
    "🇮🇱": "5911471936856134692", "🇮🇹": "5913688444923547525", "🇯🇲": "5913232280742006526",
    "🇯🇴": "5913234136167878475", "🇮🇸": "5911047899029967246", "🇭🇺": "5913767635530551104",
    "🇭🇳": "5911406889576436289", "🇭🇹": "5913459789454643194", "🇬🇾": "5913579412883771480",
    "🇬🇼": "5911398694778836149", "🇬🇹": "5913324858762072330", "🇬🇩": "5913228063084121946",
    "🇬🇷": "5911210399117611448", "🇬🇭": "5913391155877252952", "🇬🇪": "5913434771270144023",
    "🇬🇲": "5913657267755945883", "🇬🇦": "5911037896051137264", "🇫🇷": "5913605586414473124",
    "🇫🇮": "5911041344909873378", "🇫🇯": "5911393832875856716", "🇪🇹": "5911078333168227043",
    "🇩🇴": "5911152099231536123", "🇩🇲": "5911377121158107430", "🇩🇯": "5911407709915190157",
    "🇩🇰": "5911206009661034712", "🇨🇾": "5911023550860366409", "🇨🇷": "5911261745451635030",
    "🇨🇬": "5911338788574990168", "🇨🇩": "5913770362834783827", "🇰🇲": "5911338582416560604",
    "🇰🇭": "5913699998385573485", "🇨🇦": "5913623736946265914", "🇨🇻": "5913571501554012193",
    "🇹🇩": "5913299849167507310", "🇨🇿": "5911198691036764307", "🇨🇱": "5911470957603592832",
    "🇨🇴": "5913773060074246009", "🇧🇮": "5913766441529642752", "🇧🇼": "5911513782722499475",
    "🇧🇦": "5913700002680541032", "🇧🇴": "5913638795101606133", "🇧🇹": "5913236734623093021",
    "🇦🇷": "5913573356979884082", "🇦🇺": "5913632326880858455", "🇦🇹": "5911338831524664592",
    "🇧🇸": "5911451643135660214", "🇧🇭": "5913581663446634403", "🇧🇧": "5911016996740272263",
    "🇧🇪": "5913529642802745141", "🇧🇿": "5913355005137522807", "🇦🇬": "5913389025573475085",
    "🇦🇴": "5913753316109586411", "🇦🇩": "5911314702398396902", "🇩🇿": "5913782968563800236",
    "🇦🇱": "5911357458797826163", "🇦🇫": "5913492040364068694", "🇿🇼": "5911092502265336396"
}

def p_em(key: str, fallback: str = "⭐") -> str:
    key_clean = str(key).strip().lower()
    if key_clean in EMOJI_ID_MAP:
        return f'<tg-emoji emoji-id="{EMOJI_ID_MAP[key_clean]}">{fallback}</tg-emoji>'
    if key in PREMIUM_FLAGS:
        return f'<tg-emoji emoji-id="{PREMIUM_FLAGS[key]}">{fallback}</tg-emoji>'
    return fallback

def strip_html_tags(text: str) -> str:
    return re.sub(r'<[^>]*>', '', str(text))

# ==================== CONFIG SECTION ====================

BOT_TOKEN = "8757538163:" 8971982488:AAGaWPQ7JT3BudfNXqt66K9_7pdKsXWWEU8"
API_KEY = "mino_live_09cb5b0c2bc3c238ceedc02380c0a85f"  
BASE_URL = "https://mino-sms-panel.xyz"      

# --- SYSTEM IDS & ADMINS ---
ADMINS = [1574411746]
OTP_GROUP_ID = -1004358664557

# --- SYSTEM LINKS & USERNAME SETTINGS ---
DEFAULT_WELCOME_MESSAGE = f"{p_em('live')} <b>OTP BOOSTER V2</b> {p_em('live')}\n━━━━━━━━━━━━━━━━━━━━━━━━\n{p_em('status')} <b>START INSTANT OTP RECEPTION NOW!</b> {p_em('status')}\n━━━━━━━━━━━━━━━━━━━━━━━━"
DEFAULT_OTP_GROUP_URL = "https://t.me/maxgunsotp"
DEFAULT_CHANNEL_URL = "https://t.me/Mypwni"
DEFAULT_SUPPORT_USERNAME = "@maxgunsotp"
FORCE_JOIN_CHANNELS = ["@Mypwni"]

# --- WITHDRAWAL & STATS LIMITS ---
DEFAULT_MIN_WITHDRAW = 0.5
DEFAULT_MAX_WITHDRAW = 100.0
DEFAULT_COOLDOWN_TIME = 1.0
DEFAULT_OTP_REWARD = 0.0020
DEFAULT_REFER_BONUS = 0.050
DEFAULT_NUMBERS_PER_REQUEST = 5
MAX_NUMBERS_PER_USER = 10000

# --- DATA FILES ---
USER_DATA_FILE = "users.json"
PAID_SMS_FILE = "paid_sms.json"
STATS_FILE = "user_stats.json"
BANNED_USERS_FILE = "banned_users.json"
WITHDRAW_DATA_FILE = "withdraw_requests.json"
ACTIVITY_LOGS_FILE = "activity_logs.json"
DATA_RANGE_FILE = "datarange.json"
SETTINGS_FILE = "settings.json"
ACTIVE_NUMBERS_FILE = "active_numbers.json"
MANUAL_RANGES_FILE = "manual_ranges.json"

# ========================================================

def load_active_numbers():
    if not os.path.exists(ACTIVE_NUMBERS_FILE):
        return {}
    try:
        with open(ACTIVE_NUMBERS_FILE, "r") as f:
            return json.load(f)
    except:
        return {}

def save_active_numbers(data):
    try:
        with open(ACTIVE_NUMBERS_FILE, "w") as f:
            json.dump(data, f, indent=4)
    except Exception as e:
        print(f"Error saving active numbers: {e}")

# ==================== MANUAL RANGE STORAGE ====================

def load_manual_ranges():
    if not os.path.exists(MANUAL_RANGES_FILE):
        with open(MANUAL_RANGES_FILE, "w") as f:
            json.dump({}, f)
        return {}
    try:
        with open(MANUAL_RANGES_FILE, "r") as f:
            return json.load(f)
    except:
        return {}

def save_manual_ranges(data):
    try:
        with open(MANUAL_RANGES_FILE, "w") as f:
            json.dump(data, f, indent=4)
    except Exception as e:
        print(f"Error saving manual ranges: {e}")

# ==================== BUTTON COLOR PATCH ENGINE ====================

def rbtn(text: str, style: str = None, callback_data: str = None, url: str = None, icon_custom_emoji_id: str = None):
    clean_text = strip_html_tags(text)
    kwargs = {"text": clean_text}
    if callback_data:
        kwargs["callback_data"] = callback_data
    if url:
        kwargs["url"] = url
    
    if style:
        kwargs["style"] = style
    if icon_custom_emoji_id:
        kwargs["icon_custom_emoji_id"] = icon_custom_emoji_id
        
    try:
        return InlineKeyboardButton(**kwargs)
    except TypeError:
        kwargs.pop("style", None)
        kwargs.pop("icon_custom_emoji_id", None)
        
        api_kwargs = {}
        if style:
            api_kwargs["style"] = style
        if icon_custom_emoji_id:
            api_kwargs["icon_custom_emoji_id"] = icon_custom_emoji_id
            
        if api_kwargs:
            kwargs["api_kwargs"] = api_kwargs
            
        return InlineKeyboardButton(**kwargs)

def rkbtn(text: str, icon_custom_emoji_id: str = None, style: str = None):
    kwargs = {"text": text}
    if icon_custom_emoji_id:
        kwargs["icon_custom_emoji_id"] = icon_custom_emoji_id
    if style:
        kwargs["style"] = style
        
    try:
        return KeyboardButton(**kwargs)
    except TypeError:
        kwargs.pop("icon_custom_emoji_id", None)
        kwargs.pop("style", None)
        api_kwargs = {}
        if icon_custom_emoji_id:
            api_kwargs["icon_custom_emoji_id"] = icon_custom_emoji_id
        if style:
            api_kwargs["style"] = style
        if api_kwargs:
            kwargs["api_kwargs"] = api_kwargs
        return KeyboardButton(**kwargs)

# ==================== SYSTEM DYNAMIC SETTINGS ====================

def load_settings():
    default_settings = {
        "max_numbers_per_user": MAX_NUMBERS_PER_USER,
        "welcome_message": DEFAULT_WELCOME_MESSAGE,
        "otp_group_url": DEFAULT_OTP_GROUP_URL,
        "channel_url": DEFAULT_CHANNEL_URL,
        "support_username": DEFAULT_SUPPORT_USERNAME,
        "maintenance_mode": False,
        "min_withdraw": DEFAULT_MIN_WITHDRAW,
        "max_withdraw": DEFAULT_MAX_WITHDRAW,
        "api_key": API_KEY,
        "base_url": BASE_URL,
        "cooldown_time": DEFAULT_COOLDOWN_TIME,          
        "force_join_enabled": False,   
        "force_join_channels": FORCE_JOIN_CHANNELS, 
        "join_alert_enabled": True,     
        "otp_reward": DEFAULT_OTP_REWARD,          
        "refer_bonus": DEFAULT_REFER_BONUS,          
        "numbers_per_request": DEFAULT_NUMBERS_PER_REQUEST,
        "auto_range": True      
    }

    if not os.path.exists(SETTINGS_FILE):
        with open(SETTINGS_FILE, "w") as f:
            json.dump(default_settings, f, indent=1)
        return default_settings
    try:
        with open(SETTINGS_FILE, "r") as f:
            data = json.load(f)
            
        updated = False
        
        for k, v in default_settings.items():
            if k not in data:
                data[k] = v
                updated = True
                
        if updated:
            with open(SETTINGS_FILE, "w") as f:
                json.dump(data, f, indent=1)
        return data
    except:
        return default_settings

def save_settings(settings):
    with open(SETTINGS_FILE, "w") as f:
        json.dump(settings, f, indent=1)

def get_api_credentials():
    settings = load_settings()
    raw_key = settings.get("api_key", API_KEY)
    raw_url = settings.get("base_url", BASE_URL)
    raw_url = str(raw_url).strip().rstrip('/')
    return raw_key, raw_url

def get_withdraw_limits():
    settings = load_settings()
    return float(settings.get("min_withdraw", DEFAULT_MIN_WITHDRAW)), float(settings.get("max_withdraw", DEFAULT_MAX_WITHDRAW))

def is_under_maintenance(uid):
    settings = load_settings()
    return settings.get("maintenance_mode", False) and not is_admin(uid)

request_queue = asyncio.Queue() 
MAX_WORKERS = 50000 

client_async = httpx.AsyncClient(
    timeout=10.0,
    verify=False,
    limits=httpx.Limits(max_connections=1000, max_keepalive_connections=200)
)

active_numbers = load_active_numbers()
last_range = {}
last_request_time = {} 
CHECK_INTERVAL = 0.1

# ==================== GLOBAL RANGES CACHE ====================
_ranges_cache = {"data": None, "updated_at": 0.0, "fetching": False}

def get_platform_icon(platform_name: str) -> str:
    name_lower = platform_name.lower().strip()
    if name_lower in EMOJI_ID_MAP:
        return p_em(name_lower)
    return ""

def make_bold_text(text: str) -> str:
    out = []
    for char in str(text):
        o = ord(char)
        if 65 <= o <= 90: 
            out.append(chr(o - 65 + 0x1D5D4))
        elif 97 <= o <= 122: 
            out.append(chr(o - 97 + 0x1D5EE))
        elif 48 <= o <= 57: 
            out.append(chr(o - 48 + 0x1D7EC))
        else:
            out.append(char)
    return "".join(out)

def unstyle_text(text: str) -> str:
    if not text:
        return ""
    normalized = unicodedata.normalize('NFKC', str(text))
    return normalized

async def _bg_refresh_ranges():
    global _ranges_cache
    while True:
        try:
            settings = load_settings()
            if settings.get("auto_range", True) and not _ranges_cache["fetching"]:
                _ranges_cache["fetching"] = True
                try:
                    data, err = await fetch_top55_ranges_by_app()
                    if data:
                        _ranges_cache["data"] = data
                        _ranges_cache["updated_at"] = time.monotonic()
                except Exception:
                    pass
                finally:
                    _ranges_cache["fetching"] = False
        except Exception:
            pass
        await asyncio.sleep(200)

# ==================== CHECK IF USER IS ADMIN ====================

def is_admin(user_id):
    return user_id in ADMINS

# ==================== WITHDRAW DATA FUNCTIONS ====================

def load_withdraw_requests():
    if not os.path.exists(WITHDRAW_DATA_FILE):
        with open(WITHDRAW_DATA_FILE, "w") as f:
            json.dump({}, f)
        return {}
    try:
        with open(WITHDRAW_DATA_FILE, "r") as f:
            return json.load(f)
    except:
        return {}

def save_withdraw_requests(data):
    with open(WITHDRAW_DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

def generate_payment_id():
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=20))

# ==================== BANNED USERS FUNCTIONS ====================

def load_banned_users():
    if not os.path.exists(BANNED_USERS_FILE):
        with open(BANNED_USERS_FILE, "w") as f:
            json.dump([], f)
        return []
    try:
        with open(BANNED_USERS_FILE, "r") as f:
            return json.load(f)
    except:
        return []

def save_banned_users(banned_list):
    with open(BANNED_USERS_FILE, "w") as f:
        json.dump(banned_list, f, indent=4)

def is_user_banned(uid):
    banned_list = load_banned_users()
    return str(uid) in banned_list

def ban_user(uid):
    banned_list = load_banned_users()
    uid_str = str(uid)
    if uid_str not in banned_list:
        banned_list.append(uid_str)
        save_banned_users(banned_list)
        return True
    return False

def unban_user(uid):
    banned_list = load_banned_users()
    uid_str = str(uid)
    if uid_str in banned_list:
        banned_list.remove(uid_str)
        save_banned_users(banned_list)
        return True
    return False

# ==================== DATA RANGE FILE ====================

def load_range_db():
    if not os.path.exists(DATA_RANGE_FILE):
        return {}
    try:
        with open(DATA_RANGE_FILE, "r") as f:
            return json.load(f)
    except:
        return {}

def save_range_db(data):
    with open(DATA_RANGE_FILE, "w") as f:
        json.dump(data, f, indent=4)

def save_number_range_info(uid, number, range_text):
    db = load_range_db()
    flag_html, name = get_country_info(number)
    db[normalize_number(number)] = {
        "user_id": str(uid),
        "number": f"+{normalize_number(number)}",
        "range": range_text,
        "country": f"{flag_html} {name}"
    }
    save_range_db(db)

# ==================== COUNTRY MAPPING SECTION ====================

def get_country_info(number):
    number_str = str(number).strip()
    if '|' in number_str:
        number_str = number_str.split('|')[-1].strip()
        
    clean_num = re.sub(r'[^\w]', '', number_str).replace('_', '').replace(" ", "").strip()
    
    country_map = {
        "2376": ("🇨🇲", "Cameroon"), "2250": ("🇨🇮", "Ivory Coast"), "2613": ("🇲🇬", "Madagascar"),
        "4077": ("🇷🇴", "Romania"), "447": ("🇬🇧", "UK (Virtual)"), "1201": ("🇺🇸", "USA (Virtual)"),
        "1302": ("🇺🇸", "USA (Virtual)"), "1415": ("🇺🇸", "USA (Virtual)"), "1212": ("🇺🇸", "USA (Virtual)"),
        "1917": ("🇺🇸", "USA (Virtual)"), "1646": ("🇺🇸", "USA (Virtual)"), "1347": ("🇺🇸", "USA (Virtual)"),
        "237": ("🇨🇲", "Cameroon"), "225": ("🇨🇮", "Ivory Coast"), "261": ("🇲🇬", "Madagascar"),
        "20": ("🇪🇬", "Egypt"), "27": ("🇿🇦", "South Africa"), "234": ("🇳🇬", "Nigeria"),
        "254": ("🇰🇪", "Kenya"), "233": ("🇬🇭", "Ghana"), "212": ("🇲🇦", "Morocco"),
        "213": ("🇩🇿", "Algeria"), "216": ("🇹🇳", "Tunisia"), "218": ("🇱🇾", "Libya"),
        "249": ("🇸🇩", "Sudan"), "251": ("🇪🇹", "Ethiopia"), "252": ("🇸🇴", "Somalia"),
        "253": ("🇩🇿", "Djibouti"), "255": ("🇹ℤ", "Tanzania"), "256": ("🇺🇬", "Uganda"),
        "257": ("🇧🇮", "Burundi"), "258": ("🇲🇿", "Mozambique"), "260": ("🇿🇲", "Zambia"),
        "263": ("🇿🇼", "Zimbabwe"), "264": ("🇳🇦", "Namibia"), "265": ("🇲🇼", "Malawi"),
        "266": ("🇱🇸", "Lesotho"), "267": ("🇧🇼", "Botswana"), "268": ("🇸🇿", "Eswatini"),
        "269": ("🇰🇲", "Comoros"), "220": ("🇬🇲", "Gambia"), "221": ("🇸🇳", "Senegal"),
        "222": ("🇲🇷", "Mauritania"), "223": ("🇲🇱", "Mali"), "224": ("🇬🇳", "Guinea"),
        "226": ("🇧🇫", "Burkina Faso"), "227": ("🇳🇪", "Niger"), "228": ("🇹🇬", "Togo"),
        "229": ("🇧🇯", "Benin"), "230": ("🇲🇺", "Mauritius"), "231": ("🇱🇷", "Liberia"),
        "232": ("🇸🇱", "Sierra Leone"), "235": ("🇹🇩", "Chad"), "236": ("🇨🇫", "Central African Republic"),
        "238": ("🇨🇻", "Cape Verde"), "239": ("🇸🇹", "Sao Tome and Principe"), "240": ("🇬🇶", "Equatorial Guinea"),
        "241": ("🇬🇦", "Gabon"), "242": ("🇨🇬", "Congo"), "243": ("🇨🇩", "DR Congo"),
        "244": ("🇦🇴", "Angola"), "245": ("🇬🇼", "Guinea-Bissau"), "248": ("🇸🇨", "Seychelles"),
        "250": ("🇷🇼", "Rwanda"), "291": ("🇪🇷", "Eritrea"), "40": ("🇷🇴", "Romania"),
        "44": ("🇬🇧", "United Kingdom"), "33": ("🇫🇷", "France"), "49": ("🇩🇪", "Germany"),
        "39": ("🇮🇹", "Italy"), "34": ("🇪🇸", "Spain"), "31": ("🇳🇱", "Netherlands"),
        "32": ("🇧🇪", "Belgium"), "41": ("🇨🇭", "Switzerland"), "43": ("🇦🇹", "Austria"),
        "46": ("🇸🇪", "Sweden"), "47": ("🇳🇴", "Norway"), "45": ("🇩🇰", "Denmark"),
        "358": ("🇫🇮", "Finland"), "351": ("🇵🇹", "Portugal"), "353": ("🇮🇪", "Ireland"),
        "36": ("🇭🇺", "Hungary"), "48": ("🇵🇱", "Poland"), "380": ("🇺🇦", "Ukraine"),
        "370": ("🇱🇹", "Lithuania"), "371": ("🇱🇻", "Latvia"), "372": ("🇪🇪", "Estonia"),
        "373": ("🇲🇩", "Moldova"), "374": ("🇦🇲", "Armenia"), "375": ("🇧🇾", "Belarus"),
        "376": ("🇦🇩", "Andorra"), "377": ("🇲🇨", "Monaco"), "378": ("🇸🇲", "San Marino"),
        "381": ("🇷🇸", "Serbia"), "382": ("🇲🇪", "Montenegro"), "383": ("🇽🇰", "Kosovo"),
        "385": ("🇭🇷", "Croatia"), "386": ("🇸🇮", "Slovenia"), "387": ("🇧🇦", "Bosnia and Herzegovina"),
        "389": ("🇲🇰", "North Macedonia"), "350": ("🇬🇮", "Gibraltar"), "352": ("🇱🇺", "Luxembourg"),
        "354": ("🇮🇸", "Iceland"), "355": ("🇦🇱", "Albania"), "356": ("🇲🇹", "Malta"),
        "357": ("🇨🇾", "Cyprus"), "359": ("🇧🇬", "Bulgaria"), "421": ("🇸🇰", "Slovakia"),
        "420": ("🇨🇿", "Czech Republic"), "298": ("🇫🇴", "Faroe Islands"), "299": ("🇬🇱", "Greenland"),
        "1": ("🇺🇸", "United States / Canada"), "7": ("🇷🇺", "Russia / Kazakhstan"), "880": ("🇧🇩", "Bangladesh"),
        "86": ("🇨🇳", "China"), "81": ("🇯🇵", "Japan"), "82": ("🇰🇷", "South Korea"),
        "84": ("🇻🇳", "Vietnam"), "66": ("🇹🇭", "Thailand"), "62": ("🇮🇩", "Indonesia"),
        "60": ("🇲🇾", "Malaysia"), "65": ("🇸🇬", "Singapore"), "63": ("🇵🇭", "Philippines"),
        "95": ("🇲🇲", "Myanmar"), "94": ("🇱🇰", "Sri Lanka"), "977": ("🇳🇵", "Nepal"),
        "93": ("🇦🇫", "Afghanistan"), "98": ("🇮🇷", "Iran"), "90": ("🇹🇷", "Turkey"),
        "964": ("🇮🇶", "Iraq"), "963": ("🇸🇾", "Syria"), "961": ("🇱🇧", "Lebanon"),
        "962": ("🇯🇴", "Jordan"), "965": ("🇰🇼", "Kuwait"), "966": ("🇸🇦", "Saudi Arabia"),
        "967": ("🇾🇪", "Yemen"), "968": ("🇴🇲", "Oman"), "971": ("🇦🇪", "United Arab Emirates"),
        "972": ("🇮🇱", "Israel"), "973": ("🇧🇭", "Bahrain"), "974": ("🇶🇦", "Qatar"),
        "994": ("🇦🇿", "Azerbaijan"), "995": ("🇬🇪", "Georgia"), "996": ("🇰🇬", "Kyrgyzstan"),
        "992": ("🇹🇯", "Tajikistan"), "993": ("🇹🇲", "Turkmenistan"), "998": ("🇺🇿", "Uzbekistan"),
        "855": ("🇰🇭", "Cambodia"), "856": ("🇱🇦", "Laos"), "976": ("🇲🇳", "Mongolia"),
        "850": ("🇰🇵", "North Korea"), "55": ("🇧🇷", "Brazil"), "52": ("🇲🇽", "Mexico"),
        "54": ("🇦🇷", "Argentina"), "57": ("🇨🇴", "Colombia"), "51": ("🇵🇪", "Peru"),
        "58": ("🇻🇪", "Venezuela"), "56": ("🇨🇱", "Chile"), "593": ("🇪🇨", "Ecuador"),
        "591": ("🇧🇴", "Bolivia"), "595": ("🇵🇾", "Paraguay"), "598": ("🇺🇾", "Uruguay"),
        "502": ("🇬🇹", "Guatemala"), "503": ("🇸🇻", "El Salvador"), "504": ("🇭🇳", "Honduras"),
        "505": ("🇳🇮", "Nicaragua"), "506": ("🇨🇷", "Costa Rica"), "507": ("🇵🇦", "Panama"),
        "509": ("🇭🇹", "Haiti"), "501": ("🇧ℤ", "Belize"), "61": ("🇦🇺", "Australia"),
        "64": ("🇳ℤ", "New Zealand"), "675": ("🇵🇬", "Papua New Guinea"), "679": ("🇫🇯", "Fiji"),
        "685": ("🇼🇸", "Samoa"), "686": ("🇰🇮", "Kiribati"), "691": ("🇫🇲", "Micronesia"),
        "692": ("🇲🇭", "Marshall Islands"), "297": ("🇦🇼", "Aruba"), "1246": ("🇧🇧", "Barbados"),
        "1441": ("🇧🇲", "Bermuda"), "1345": ("🇰🇾", "Cayman Islands"), "53": ("🇨🇺", "Cuba"),
        "1473": ("🇬🇩", "Grenada"), "592": ("🇬🇾", "Guyana"), "1876": ("🇯🇲", "Jamaica"),
        "1758": ("🇱🇨", "Saint Lucia"), "1784": ("🇻🇨", "Saint Vincent"), "1868": ("🇹🇹", "Trinidad and Tobago")
    }
    
    sorted_prefixes = sorted(country_map.keys(), key=len, reverse=True)
    for prefix in sorted_prefixes:
        if clean_num.startswith(prefix):
            raw_flag, c_name = country_map[prefix]
            return p_em(raw_flag, raw_flag), c_name
    
    return p_em("🇨🇮", "🇨🇮"), "IVORY COAST"

# ==================== SERVICE DETECTION & CLEANING ====================

def get_clean_app_name(app_name: str) -> str:
    name_lower = app_name.lower().strip()
    
    if "facebook" in name_lower or name_lower == "fb":
        return "Facebook"
    if "instagram" in name_lower or "instragram" in name_lower or name_lower == "insta":
        return "Instagram"
    if "whatsapp" in name_lower or "whats app" in name_lower:
        return "WhatsApp"
    if "tiktok" in name_lower:
        return "TikTok"
    if "telegram" in name_lower or name_lower == "tg":
        return "Telegram"
    if "uber" in name_lower or "ubar" in name_lower:
        return "Uber"
    if "daraz" in name_lower:
        return "Daraz"
    if "imo" in name_lower:
        return "Imo"
    if "discord" in name_lower:
        return "Discord"
    if "linkedin" in name_lower:
        return "Linkedin"
    if "bumble" in name_lower:
        return "Bumble"
        
    return app_name.strip().title()

def detect_service(full_sms):
    if not full_sms:
        return "SMS SERVICE"
    
    sms_lower = full_sms.lower()
    
    service_keywords = {
        "facebook": "FACEBOOK", "fb": "FACEBOOK", "instagram": "INSTAGRAM", "insta": "INSTAGRAM",
        "tiktok": "TIKTOK", "whatsapp": "WHATSAPP", "whats app": "WHATSAPP", "telegram": "TELEGRAM",
        "tg": "TELEGRAM", "discord": "DISCORD", "imo": "IMO", "uber": "UBER", "daraz": "DARAZ",
        "linkedin": "LINKEDIN", "bumble": "BUMBLE"
    }
    
    for keyword, service_name in sorted(service_keywords.items(), key=lambda x: len(x[0]), reverse=True):
        if keyword in sms_lower:
            return service_name
    
    return "SMS SERVICE"

# ==================== KEYBOARDS SECTION ====================

def main_keyboard(user_id):
    keyboard = [
        [rkbtn(make_bold_text("GET NUMBER"), icon_custom_emoji_id=EMOJI_ID_MAP.get("get_number_btn"), style="danger")],
        [
            rkbtn(make_bold_text("TRAFFIC"), icon_custom_emoji_id=EMOJI_ID_MAP.get("live"), style="primary"),
            rkbtn(make_bold_text("LEADERBOARD"), icon_custom_emoji_id=EMOJI_ID_MAP.get("leader_board"), style="primary")
        ],
        [
            rkbtn(make_bold_text("BALANCE"), icon_custom_emoji_id=EMOJI_ID_MAP.get("money"), style="success"), 
            rkbtn(make_bold_text("REFER & EARN"), icon_custom_emoji_id=EMOJI_ID_MAP.get("refer_btn"), style="success")
        ],
        [
            rkbtn(make_bold_text("SUPPORT"), icon_custom_emoji_id=EMOJI_ID_MAP.get("msg"), style="primary")
        ]
    ]
    if is_admin(user_id):
        keyboard.append([rkbtn(make_bold_text("ADMIN PANEL"), icon_custom_emoji_id=EMOJI_ID_MAP.get("admin"), style="primary")])
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

def cancel_keyboard():
    keyboard = [[rkbtn("CANCEL", icon_custom_emoji_id=EMOJI_ID_MAP.get("cross"), style="danger")]]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

# ==================== ADMIN PANEL KEYBOARDS ====================

def admin_main_keyboard():
    keyboard = [
        [
            rkbtn("SYSTEM CONFIG", icon_custom_emoji_id=EMOJI_ID_MAP.get("setting"), style="primary"), 
            rkbtn("USER & BALANCE", icon_custom_emoji_id=EMOJI_ID_MAP.get("money"), style="success")
        ],
        [
            rkbtn("SECURITY & JOIN", icon_custom_emoji_id=EMOJI_ID_MAP.get("link"), style="primary"), 
            rkbtn("NOTICE & B-CAST", icon_custom_emoji_id=EMOJI_ID_MAP.get("live"), style="primary")
        ],
        [
            rkbtn("BACK TO MAIN", icon_custom_emoji_id=EMOJI_ID_MAP.get("back"), style="danger")
        ]
    ]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

def admin_system_config_keyboard():
    keyboard = [
        [
            rkbtn("SET MAX NUMBERS LIMIT", icon_custom_emoji_id=EMOJI_ID_MAP.get("setting"), style="primary"), 
            rkbtn("SET WITHDRAW LIMITS", icon_custom_emoji_id=EMOJI_ID_MAP.get("money"), style="success")
        ],
        [
            rkbtn("SET OTP BONUS", icon_custom_emoji_id=EMOJI_ID_MAP.get("add"), style="success"), 
            rkbtn("SET REFER BONUS", icon_custom_emoji_id=EMOJI_ID_MAP.get("gift_box"), style="success")
        ],
        [
            rkbtn("SET NUMBERS PER REQUEST", icon_custom_emoji_id=EMOJI_ID_MAP.get("get_number_btn"), style="primary"), 
            rkbtn("SET COOLDOWN", icon_custom_emoji_id=EMOJI_ID_MAP.get("waiting"), style="primary")
        ],
        [
            rkbtn("TOGGLE AUTO RANGE", icon_custom_emoji_id=EMOJI_ID_MAP.get("status"), style="primary"),
            rkbtn("MANAGE MANUAL RANGES", icon_custom_emoji_id=EMOJI_ID_MAP.get("setting"), style="primary")
        ],
        [
            rkbtn("TOGGLE MAINTENANCE", icon_custom_emoji_id=EMOJI_ID_MAP.get("stop"), style="danger"), 
            rkbtn("BACK TO ADMIN", icon_custom_emoji_id=EMOJI_ID_MAP.get("back"), style="danger")
        ]
    ]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

def admin_user_balance_keyboard():
    keyboard = [
        [
            rkbtn("ADD BALANCE", icon_custom_emoji_id=EMOJI_ID_MAP.get("add"), style="success"), 
            rkbtn("REMOVE BALANCE", icon_custom_emoji_id=EMOJI_ID_MAP.get("delete"), style="danger")
        ],
        [
            rkbtn("DIRECT MSG USER", icon_custom_emoji_id=EMOJI_ID_MAP.get("msg"), style="primary"), 
            rkbtn("SEARCH BY USERNAME", icon_custom_emoji_id=EMOJI_ID_MAP.get("status"), style="primary")
        ],
        [
            rkbtn("USER STATUS CHECK", icon_custom_emoji_id=EMOJI_ID_MAP.get("status"), style="primary"), 
            rkbtn("ALL USER ID", icon_custom_emoji_id=EMOJI_ID_MAP.get("link"), style="primary")
        ],
        [
            rkbtn("ALL USER BALANCE", icon_custom_emoji_id=EMOJI_ID_MAP.get("money"), style="success"), 
            rkbtn("BACK TO ADMIN", icon_custom_emoji_id=EMOJI_ID_MAP.get("back"), style="danger")
        ]
    ]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

def admin_security_join_keyboard():
    keyboard = [
        [
            rkbtn("SET FORCE JOIN", icon_custom_emoji_id=EMOJI_ID_MAP.get("link"), style="primary"), 
            rkbtn("TOGGLE FORCE JOIN", icon_custom_emoji_id=EMOJI_ID_MAP.get("status"), style="primary")
        ],
        [
            rkbtn("BAN USER", icon_custom_emoji_id=EMOJI_ID_MAP.get("ban"), style="danger"), 
            rkbtn("UNBAN USER", icon_custom_emoji_id=EMOJI_ID_MAP.get("done"), style="success")
        ],
        [
            rkbtn("BAN USER LIST", icon_custom_emoji_id=EMOJI_ID_MAP.get("status"), style="primary"), 
            rkbtn("TOGGLE JOIN ALERT", icon_custom_emoji_id=EMOJI_ID_MAP.get("live"), style="primary")
        ],
        [
            rkbtn("BACK TO ADMIN", icon_custom_emoji_id=EMOJI_ID_MAP.get("back"), style="danger")
        ]
    ]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

def admin_notice_bcast_keyboard():
    keyboard = [
        [
            rkbtn("BROADCAST NOTICE", icon_custom_emoji_id=EMOJI_ID_MAP.get("live"), style="primary"), 
            rkbtn("B-CAST WITH BUTTON", icon_custom_emoji_id=EMOJI_ID_MAP.get("link"), style="primary")
        ],
        [
            rkbtn("EDIT LINKS & TEXTS", icon_custom_emoji_id=EMOJI_ID_MAP.get("setting"), style="primary"), 
            rkbtn("BACK TO ADMIN", icon_custom_emoji_id=EMOJI_ID_MAP.get("back"), style="danger")
        ]
    ]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

MENU_BUTTONS = {
    "GET NUMBER", "TRAFFIC", "LEADERBOARD", "SUPPORT", "ADMIN PANEL", "BALANCE", "REFER & EARN",
    "BACK TO MAIN", "BACK TO ADMIN", "CANCEL", "ADD BALANCE", "REMOVE BALANCE", 
    "SET MAX NUMBERS LIMIT", "EDIT LINKS & TEXTS", "BAN USER", "UNBAN USER",
    "BAN USER LIST", "SEND MESSAGE TO ALL USERS", "ALL USER ID", "ALL USER BALANCE",
    "SET WITHDRAW LIMITS", "TOGGLE MAINTENANCE", "RESET DAILY LIMITS",
    "DIRECT MSG USER", "SEARCH BY USERNAME", "SET FORCE JOIN", 
    "TOGGLE FORCE JOIN", "SET COOLDOWN", "BROADCAST NOTICE", "RESET LEADERBOARD",
    "SET OTP BONUS", "SET REFER BONUS", "SET NUMBERS PER REQUEST",
    "SYSTEM CONFIG", "USER & BALANCE", "SECURITY & JOIN", "NOTICE & B-CAST", "TOGGLE JOIN ALERT",
    "TOGGLE AUTO RANGE", "MANAGE MANUAL RANGES"
}

# ==================== HELPER FUNCTIONS SECTION ====================

def clean_range_id(range_str: str) -> str:
    if not range_str:
        return ""
    number_str = str(range_str).strip()
    if '|' in number_str:
        number_str = number_str.split('|')[-1].strip()
    return re.sub(r'[^\w]', '', number_str).replace('_', '').replace(" ", "").strip()

def format_balance(balance):
    return f"{balance:.4f}"

# ==================== OPTIMIZED OTP DETECTOR ====================

def extract_otp(text):
    if not text or text == "No Content": 
        return "N/A"
    
    text_clean = str(text).strip()
    
    label_match = re.search(
        r'(?:code|otp|verify|verification|pin|gd|confirmation|kod|passcode|pass|identifier)[\s:-]+([a-zA-Z0-9]{3,10}(?:[\s-][a-zA-Z0-9]{3,10})?)\b', 
        text_clean, 
        re.IGNORECASE
    )
    if label_match:
        candidate = label_match.group(1).strip()
        if 3 <= len(candidate) <= 12 and not candidate.isalpha():
            return candidate
        elif candidate.isdigit():
            return candidate
            
    spaced_otp = re.search(r'\b(\d{3}[\s-]\d{3})\b', text_clean)
    if spaced_otp:
        return spaced_otp.group(1)
        
    digit_match = re.search(r'\b(\d{4,8})\b', text_clean)
    if digit_match:
        return digit_match.group(1)
        
    alphanum_match = re.search(r'\b([A-Z0-9]{4,8})\b', text_clean)
    if alphanum_match:
        return alphanum_match.group(1)
        
    url_match = re.search(r'https?://[^\s]+', text_clean)
    if url_match:
        url = url_match.group(0).strip()
        parsed_url = url.split('?')[0]  
        path_parts = [p for p in parsed_url.rstrip('/').split('/') if p]
        if len(path_parts) > 2:  
            last_part = path_parts[-1]
            if len(last_part) >= 4 and any(c.isalnum() for c in last_part):
                return last_part
        return url  
        
    numbers_only = re.sub(r'\D', '', text_clean)
    if 4 <= len(numbers_only) <= 8:
        return numbers_only
        
    return "N/A"

def normalize_number(num):
    return re.sub(r'\D', '', str(num))

def mask_number(num):
    num_str = str(num).replace('+', '').replace(' ', '').strip()
    if len(num_str) >= 8:
        return f"{num_str[:4]}✦✦✦{num_str[-4:]}"
    elif len(num_str) > 4:
        half = len(num_str) // 2
        return f"{num_str[:half]}✦✦✦{num_str[half:]}"
    return num_str

def format_otp_display(otp):
    otp = str(otp).strip()
    if otp.isdigit() and len(otp) == 6:
        return f"{otp[:3]}-{otp[3:]}"
    return otp

def get_date_reset_time():
    now = datetime.now()
    today_midnight = datetime(now.year, now.month, now.day, 0, 0, 0)
    return today_midnight

def is_valid_bangladesh_number(number):
    number = re.sub(r'\D', '', str(number))
    return len(number) == 11 and number.startswith('01')

def is_range_request(param):
    if not param:
        return False
    param_upper = str(param).upper().strip()
    
    if 'X' in param_upper:
        return True
        
    if param_upper.isdigit():
        if len(param_upper) <= 8:
            return True
            
    if any(char in param_upper for char in ['?', '*', '#', '-']):
        return True
        
    return False

def numbers_match(num1, num2):
    n1 = normalize_number(num1)
    n2 = normalize_number(num2)
    if not n1 or not n2:
        return False
    if n1 == n2:
        return True
    if len(n1) >= 7 and len(n2) >= 7:
        return n1.endswith(n2) or n2.endswith(n1)
    return False

# ==================== DATABASE FUNCTIONS SECTION ====================

def load_data(filename=USER_DATA_FILE):
    if not os.path.exists(filename):
        with open(filename, "w") as f:
            json.dump({}, f)
        return {}
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except:
        return {}

def save_data(data, filename=USER_DATA_FILE):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

def get_user(uid, username=None, full_name=None):
    uid = str(uid)
    data = load_data()
    if uid not in data:
        data[uid] = {
            "user_id": uid, 
            "balance": 0.0, 
            "total_numbers": 0, 
            "username": username, 
            "full_name": full_name,
            "referrals": 0,
            "referral_earnings": 0.0,
            "referred_by": None,
            "withdrawal_method": None
        }
        save_data(data)
    else:
        updated = False
        if "referrals" not in data[uid]:
            data[uid]["referrals"] = 0
            updated = True
        if "referral_earnings" not in data[uid]:
            data[uid]["referral_earnings"] = 0.0
            updated = True
        if "referred_by" not in data[uid]:
            data[uid]["referred_by"] = None
            updated = True
        if "withdrawal_method" not in data[uid]:
            data[uid]["withdrawal_method"] = None
            updated = True
        if username: 
            data[uid]["username"] = username
            updated = True
        if full_name: 
            data[uid]["full_name"] = full_name
            updated = True
        if updated:
            save_data(data)
    return data[uid]

async def update_db_balance(uid, amount):
    uid = str(uid)
    data = load_data()
    if uid in data:
        data[uid]["balance"] = round(data[uid].get("balance", 0.0) + amount, 4)
        save_data(data)
        return data[uid]["balance"]
    return 0.0

def get_all_users():
    data = load_data(USER_DATA_FILE)
    return list(data.keys()) if data else []

def user_exists(uid):
    data = load_data(USER_DATA_FILE)
    return str(uid) in data

# ==================== STATS FUNCTIONS SECTION ====================

def load_stats():
    if not os.path.exists(STATS_FILE):
        with open(STATS_FILE, "w") as f:
            json.dump({}, f)
        return {}
    try:
        with open(STATS_FILE, "r") as f:
            return json.load(f)
    except:
        return {}

def save_stats(stats):
    with open(STATS_FILE, "w") as f:
        json.dump(stats, f, indent=4)

def add_number_taken(uid, count=1):
    uid = str(uid)
    stats = load_stats()
    if uid not in stats:
        stats[uid] = {"numbers_taken": [], "otps_received": []}
    now = datetime.now().isoformat()
    for _ in range(count):
        stats[uid]["numbers_taken"].append(now)
    log_global_activity(uid, "NUMBER_TAKEN", {"count": count})
    save_stats(stats)

def add_otp_received(uid):
    uid = str(uid)
    stats = load_stats()
    if uid not in stats:
        stats[uid] = {"numbers_taken": [], "otps_received": []}
    now = datetime.now().isoformat()
    stats[uid]["otps_received"].append(now)
    save_stats(stats)

def get_user_stats(uid):
    uid = str(uid)
    stats = load_stats()
    user_stats = stats.get(uid, {"numbers_taken": [], "otps_received": []})
    
    now = datetime.now()
    today_midnight = get_date_reset_time()
    
    last_24h = now - timedelta(hours=24)
    last_7d = now - timedelta(days=7)
    
    numbers_taken = user_stats.get("numbers_taken", [])
    otps_received = user_stats.get("otps_received", [])
    
    today_numbers = sum(1 for t in numbers_taken if datetime.fromisoformat(t) >= today_midnight)
    today_otps = sum(1 for t in otps_received if datetime.fromisoformat(t) >= today_midnight)
    
    last24h_numbers = sum(1 for t in numbers_taken if datetime.fromisoformat(t) > last_24h)
    last24h_otps = sum(1 for t in otps_received if datetime.fromisoformat(t) > last_24h)
    
    last7d_numbers = sum(1 for t in numbers_taken if datetime.fromisoformat(t) > last_7d)
    last7d_otps = sum(1 for t in otps_received if datetime.fromisoformat(t) > last_7d)
    
    total_numbers = len(numbers_taken)
    total_otps = len(otps_received)
    
    return {
        "total_numbers": total_numbers,
        "total_otps": total_otps,
        "today_numbers": today_numbers,
        "today_otps": today_otps,
        "last24h_numbers": last24h_numbers,
        "last24h_otps": last24h_otps,
        "last7d_numbers": last7d_numbers,
        "last7d_otps": last7d_otps
    }

def log_global_activity(uid, action, details):
    if not os.path.exists(ACTIVITY_LOGS_FILE):
        with open(ACTIVITY_LOGS_FILE, "w") as f:
            json.dump([], f)
    try:
        with open(ACTIVITY_LOGS_FILE, "r") as f:
            logs = json.load(f)
    except:
        logs = []
    now = datetime.now()
    log_entry = {
        "uid": str(uid),
        "action": action,
        "details": details,
        "timestamp": now.isoformat(),
        "date": now.strftime("%d/%m/%Y"),
        "time": now.strftime("%H:%M:%S")
    }
    logs.append(log_entry)
    with open(ACTIVITY_LOGS_FILE, "w") as f:
        json.dump(logs, f, indent=4)

# ==================== MINO API - ACTIVE RANGES FLOW ====================

async def fetch_top55_ranges_by_app():
    settings = load_settings()
    auto_range_enabled = settings.get("auto_range", True)
    
    if not auto_range_enabled:
        manual_data = load_manual_ranges()
        top_ranges_by_app = {}
        for app_raw, rng_list in manual_data.items():
            primary_app = get_clean_app_name(app_raw)
            icon = get_platform_icon(primary_app)
            top_ranges_by_app[primary_app] = {
                "icon": icon,
                "ranges": list(rng_list),
                "total_otps": len(rng_list)
            }
        top_ranges_by_app = dict(
            sorted(top_ranges_by_app.items(),
                   key=lambda x: len(x[1]["ranges"]), reverse=True)
        )
        return top_ranges_by_app, None

    api_key, base_url = get_api_credentials()
    
    for attempt in range(2):
        try:
            url = f"{base_url}/liveaccess?api_key={api_key}"
            r = await client_async.get(
                url,
                timeout=httpx.Timeout(connect=4.0, read=10.0, write=4.0, pool=4.0)
            )
            
            try:
                data = r.json()
            except Exception as json_err:
                return None, f"JSONDecodeError: Expecting valid JSON, got HTML or bad response."

            top_ranges_by_app = {}
            ranges_dict = None

            if isinstance(data, dict):
                if "ranges" in data and isinstance(data["ranges"], dict):
                    ranges_dict = data["ranges"]
                elif "data" in data and isinstance(data["data"], dict) and "ranges" in data["data"] and isinstance(data["data"]["ranges"], dict):
                    ranges_dict = data["data"]["ranges"]
            
            if ranges_dict:
                for app_raw, rng_list in ranges_dict.items():
                    if not isinstance(rng_list, list):
                        continue
                    primary_app = get_clean_app_name(app_raw)
                    icon = get_platform_icon(primary_app)
                    if primary_app not in top_ranges_by_app:
                        top_ranges_by_app[primary_app] = {"icon": icon, "ranges": [], "total_otps": 0}
                    for rng in rng_list:
                        if rng and rng not in top_ranges_by_app[primary_app]["ranges"]:
                            top_ranges_by_app[primary_app]["ranges"].append(rng)
                    top_ranges_by_app[primary_app]["total_otps"] = len(top_ranges_by_app[primary_app]["ranges"])

            top_ranges_by_app = dict(
                sorted(top_ranges_by_app.items(), key=lambda x: len(x[1]["ranges"]), reverse=True)
            )
            return top_ranges_by_app, None
            
        except Exception as e:
            if attempt == 0:
                await asyncio.sleep(0.3)

    return None, "Server unreachable or invalid API key."

def build_app_buttons_from_cache(top_ranges_by_app):
    buttons = []
    for app_name in top_ranges_by_app.keys():
        bold_name = make_bold_text(app_name)
        emoji_key = app_name.lower().strip()
        emoji_id = EMOJI_ID_MAP.get(emoji_key)
        buttons.append([rbtn(bold_name, "primary", callback_data=f"sel_app_{app_name}", icon_custom_emoji_id=emoji_id)])
    return buttons

async def show_app_selection(update, context):
    uid = update.effective_user.id
    if is_user_banned(uid):
        settings = load_settings()
        support = settings.get("support_username", DEFAULT_SUPPORT_USERNAME)
        await update.message.reply_text(
            f"{p_em('ban')} <b>YOU ARE BANNED</b> {p_em('ban')}\n\n"
            f"<blockquote>{p_em('msg')} Contact Support: {support}</blockquote>",
            parse_mode="HTML",
            reply_markup=main_keyboard(uid)
        )
        return

    if is_under_maintenance(uid):
        await update.message.reply_text(f"{p_em('stop')} <b>SYSTEM UNDER MAINTENANCE</b> {p_em('stop')}", parse_mode="HTML")
        return

    is_joined = await is_user_joined_force_channels(uid, context)
    if not is_joined:
        await update.message.reply_text(
            f"{p_em('channel')} <b>আপনাকে অবশ্যই আমাদের চ্যানেলে জয়েন করতে হবে!</b>",
            parse_mode="HTML",
            reply_markup=build_force_join_keyboard()
        )
        return

    context.user_data.pop("top_ranges_by_app", None)

    settings = load_settings()
    auto_range_enabled = settings.get("auto_range", True)

    cache_age = time.monotonic() - _ranges_cache["updated_at"]
    if auto_range_enabled and _ranges_cache["data"] and cache_age < 300:
        top_ranges_by_app = _ranges_cache["data"]
        context.user_data["top_ranges_by_app"] = top_ranges_by_app
        buttons = build_app_buttons_from_cache(top_ranges_by_app)
        keyboard = InlineKeyboardMarkup(buttons)
        msg = f"{p_em('get_number_btn')} <b>SELECT APP TO GET</b>"
        await update.message.reply_text(msg, parse_mode="HTML", reply_markup=keyboard)
        return

    status = await update.message.reply_text(f"{p_em('waiting')} Loading ranges...")

    top_ranges_by_app, err = await fetch_top55_ranges_by_app()
    if err:
        await status.edit_text(f"{p_em('cross')} <b>Could not load ranges.</b>\n\n<code>{err}</code>", parse_mode="HTML")
        return

    if not top_ranges_by_app:
        await status.edit_text(f"{p_em('cross')} No active ranges returned.")
        return

    if auto_range_enabled:
        _ranges_cache["data"] = top_ranges_by_app
        _ranges_cache["updated_at"] = time.monotonic()
        
    context.user_data["top_ranges_by_app"] = top_ranges_by_app

    buttons = build_app_buttons_from_cache(top_ranges_by_app)
    keyboard = InlineKeyboardMarkup(buttons)
    msg = f"{p_em('get_number_btn')} <b>SELECT APP TO GET</b>"
    await status.edit_text(msg, parse_mode="HTML", reply_markup=keyboard)

# ==================== TRAFFIC CONTROLLER ====================

async def show_traffic(update: Update, context: ContextTypes.DEFAULT_TYPE):
    uid = update.effective_user.id
    if is_user_banned(uid) or is_under_maintenance(uid):
        return

    if not os.path.exists(ACTIVITY_LOGS_FILE):
        await update.message.reply_text(f"{p_em('live')} <b>Live Traffic (Last 1 Hours)</b>\n\n<i>No logs recorded.</i>", parse_mode="HTML")
        return

    try:
        with open(ACTIVITY_LOGS_FILE, "r") as f:
            logs = json.load(f)
    except:
        logs = []

    one_hour_ago = datetime.now() - timedelta(hours=1)
    otp_logs = [log for log in logs if log.get("action") == "OTP_RECEIVED" and datetime.fromisoformat(log.get("timestamp", "")) >= one_hour_ago]

    if not otp_logs:
        await update.message.reply_text(f"{p_em('live')} <b>Live Traffic (Last 1 Hours)</b>\n\n<i>No OTPs in last hour.</i>", parse_mode="HTML")
        return

    counts = {}
    total_otps = 0
    for log in otp_logs:
        details = log.get("details", {})
        num = details.get("number")
        sms = details.get("sms")
        if num and sms:
            service = detect_service(sms).upper()
            flag_html, country_name = get_country_info(num)
            key = (service, flag_html, country_name)
            counts[key] = counts.get(key, 0) + 1
            total_otps += 1

    lines = [f"{p_em('live')} <b>Live Traffic (Last 1 Hours)</b>\n"]
    for (service, flag_html, country_name), count in sorted(counts.items(), key=lambda x: x[1], reverse=True):
        percentage = (count / total_otps) * 100
        app_icon = get_platform_icon(service) or p_em("status")
        lines.append(f"{app_icon} <b>{service}</b> | {flag_html} {country_name} | {percentage:.1f}%")

    await update.message.reply_text("\n".join(lines), parse_mode="HTML")

# ==================== LEADERBOARD & SUPPORT ====================

async def show_leaderboard_command(update, context):
    stats = load_stats()
    sorted_users = sorted([(u_id, len(u.get("otps_received", []))) for u_id, u in stats.items() if u.get("otps_received")], key=lambda x: x[1], reverse=True)[:10]
    
    lines = [f"{p_em('leader_board')} <b>OTP LEADERBOARD</b>\n━━━━━━━━━━━━━━━━━━━━━━━\n"]
    if sorted_users:
        users_db = load_data(USER_DATA_FILE)
        for idx, (user_id, count) in enumerate(sorted_users, 1):
            u_info = users_db.get(str(user_id), {})
            name = u_info.get("full_name") or f"User ({user_id[-4:]})"
            lines.append(f"<blockquote><b>#{idx}</b> {html.escape(name)} | <code>{count} OTPs</code></blockquote>")
    else:
        lines.append("<i>No OTPs recorded yet.</i>")
    
    await update.message.reply_text("\n".join(lines), parse_mode="HTML")

async def support_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    support_text = f"{p_em('msg')} <b>SUPPORT HELP CENTER</b>"
    keyboard = InlineKeyboardMarkup([
        [rbtn("SUPPORT TEAM", "success", url="https://t.me/maxgunsotp")],
        [rbtn("DEVELOPER", "primary", url="https://t.me/Pwkuni")]
    ])
    await update.message.reply_text(support_text, reply_markup=keyboard, parse_mode="HTML")

# ==================== AUTO OTP MONITOR SECTION ====================

async def monitor_loop(app):
    while True:
        try:
            api_key, base_url = get_api_credentials()
            if not api_key:
                await asyncio.sleep(2.0)
                continue
                
            r = await client_async.get(f"{base_url}/success_otp?api_key={api_key}")
            try:
                res = r.json()
            except Exception:
                await asyncio.sleep(CHECK_INTERVAL)
                continue
            
            otps = res.get("data") if isinstance(res, dict) else []
            if isinstance(otps, list) and otps:
                paid_data = load_data(PAID_SMS_FILE)
                for otp in otps:
                    if not isinstance(otp, dict): continue
                    num = normalize_number(otp.get("number") or "")
                    full_sms = otp.get('message') or otp.get('otp') or "No Content"
                    otp_code = extract_otp(full_sms)
                    sms_key = f"{num}_{otp_code}"

                    matched_key = next((k for k in active_numbers.keys() if numbers_match(num, k)), None)
                    if matched_key and sms_key not in paid_data:
                        details = active_numbers[matched_key]
                        paid_data[sms_key] = {"uid": details["uid"], "otp": otp_code}

                        settings = load_settings()
                        otp_reward = settings.get("otp_reward", DEFAULT_OTP_REWARD)

                        await update_db_balance(details["uid"], otp_reward)
                        add_otp_received(details["uid"])
                        log_global_activity(details["uid"], "OTP_RECEIVED", {"number": matched_key, "otp": otp_code, "sms": full_sms})

                        safe_sms = html.escape(str(full_sms))
                        safe_otp = html.escape(str(otp_code))

                        user_msg = f"<b>OTP RECEIVED!</b>\nNumber: <code>+{matched_key}</code>\nOTP: <code>{safe_otp}</code>\n\nSMS: <code>{safe_sms}</code>"
                        
                        try:
                            await app.bot.send_message(details["uid"], user_msg, parse_mode="HTML")
                        except Exception as e:
                            print(f"User Msg Send Fail: {e}")

                        save_data(paid_data, PAID_SMS_FILE)

        except Exception as e:
            print(f"Monitor Error: {e}")
        await asyncio.sleep(CHECK_INTERVAL)

# ==================== WORKER & API ====================

async def fetch_number_async(range_str):
    try:
        api_key, base_url = get_api_credentials()
        clean_rid = clean_range_id(range_str)
        r = await client_async.post(
            f"{base_url}/getnumber",
            json={"api_key": api_key, "rid": clean_rid, "national": 1, "remove_plus": 1}
        )
        data = r.json()
        if data.get("status") == "success":
            return data.get("number")
    except Exception as e: 
        print(f"Fetch number error: {e}")
    return None

async def worker():
    while True:
        task = await request_queue.get()
        try:
            if task['type'] == 'process_numbers':
                await process_numbers(task['update'], task['context'], task['range_text'], task['count'], task.get('edit_message'))
        except Exception as e:
            print(f"Worker Error: {e}")
        finally:
            request_queue.task_done()

async def process_numbers(update, context, range_text, count, edit_message=None):
    uid = update.effective_user.id
    chat_id = update.effective_chat.id

    if is_user_banned(uid) or is_under_maintenance(uid):
        return

    is_joined = await is_user_joined_force_channels(uid, context)
    if not is_joined:
        await context.bot.send_message(chat_id=chat_id, text="Please join force channel first.", reply_markup=build_force_join_keyboard())
        return

    status_msg = edit_message or await context.bot.send_message(chat_id=chat_id, text=f"{p_em('waiting')} SEARCHING...")

    try:
        add_number_taken(uid, count)
        last_range[uid] = range_text   

        tasks = [fetch_number_async(range_text) for _ in range(count)]  
        results = await asyncio.gather(*tasks)  
        generated_nums = [normalize_number(n) for n in results if n]  

        if not generated_nums:  
            await status_msg.edit_text(f"{p_em('cross')} NO NUMBERS FOUND.", parse_mode="HTML")
            return  

        for clean_num in generated_nums:  
            active_numbers[clean_num] = {"uid": uid, "range": range_text, "timestamp": datetime.now().isoformat()}
            save_number_range_info(uid, clean_num, range_text)
        save_active_numbers(active_numbers)

        country_flag, country_name = get_country_info(generated_nums[0])
        num_lines = [f"<blockquote>Number {i}: <code>+{g}</code></blockquote>" for i, g in enumerate(generated_nums, 1)]

        final_text = f"<b>ACTIVE NUMBERS RECEIVED</b>\n" + "\n".join(num_lines)
        await status_msg.edit_text(final_text, parse_mode="HTML")
            
    except Exception as e:
        await status_msg.edit_text(f"{p_em('cross')} Error: {str(e)}", parse_mode="HTML")

# ==================== FORCE JOIN ENGINE ====================

async def is_user_joined_force_channels(user_id, context):
    settings = load_settings()
    if not settings.get("force_join_enabled", False) or user_id in ADMINS:
        return True
    for ch in settings.get("force_join_channels", []):
        try:
            member = await context.bot.get_chat_member(chat_id=ch, user_id=user_id)
            if member.status not in ["member", "administrator", "creator"]:
                return False
        except Exception:
            return False
    return True

def build_force_join_keyboard():
    settings = load_settings()
    buttons = [[rbtn(f"Join Channel {i+1}", "primary", url=f"https://t.me/{ch.replace('@','')}") ] for i, ch in enumerate(settings.get("force_join_channels", []))]
    buttons.append([rbtn("Check Joined", "success", callback_data="check_force_join")])
    return InlineKeyboardMarkup(buttons)

# ==================== MESSAGE HANDLER SECTION ====================

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message: return
    uid = update.effective_user.id
    raw_text = update.message.text.strip()
    text = unstyle_text(raw_text)

    if text == "GET NUMBER":
        await show_app_selection(update, context)
        return
    elif text == "TRAFFIC":
        await show_traffic(update, context)
        return
    elif text == "LEADERBOARD":
        await show_leaderboard_command(update, context)
        return
    elif text == "SUPPORT":
        await support_command(update, context)
        return
    elif text == "ADMIN PANEL" and is_admin(uid):
        await update.message.reply_text("Admin Panel Menu", reply_markup=admin_main_keyboard())
        return
    elif text == "BACK TO MAIN":
        await update.message.reply_text("Main Menu", reply_markup=main_keyboard(uid))
        return
    else:
        await update.message.reply_text("Please use available buttons:", reply_markup=main_keyboard(uid))

# ==================== START & CALLBACK ENGINE ====================

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    uid = update.effective_user.id
    get_user(uid, update.effective_user.username, update.effective_user.full_name)
    await update.message.reply_text("Welcome!", reply_markup=main_keyboard(uid))

async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    data = query.data
    if data == "check_force_join":
        if await is_user_joined_force_channels(query.from_user.id, context):
            await query.message.delete()
            await context.bot.send_message(query.from_user.id, "Successfully joined!", reply_markup=main_keyboard(query.from_user.id))
        else:
            await query.answer("You have not joined all channels yet!", show_alert=True)

# ==================== MAIN INIT & ENTRY POINT ====================

async def post_init(application): 
    for _ in range(10):
        asyncio.create_task(worker())
    asyncio.create_task(monitor_loop(application))
    asyncio.create_task(_bg_refresh_ranges())

def main():
    request_config = HTTPXRequest(connect_timeout=20.0, read_timeout=20.0)
    
    app = (
        ApplicationBuilder()
        .token(BOT_TOKEN)
        .request(request_config)
        .concurrent_updates(True)
        .post_init(post_init)
        .build()
    )
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_callback))
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))
    
    print("🚀 BOT RUNNING SUCCESSFULLY...")  
    app.run_polling(allowed_updates=Update.ALL_TYPES, drop_pending_updates=True)

if __name__ == '__main__':
    main()
