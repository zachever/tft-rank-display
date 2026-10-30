import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

DEFAULT_LOCKFILE = r"C:\Riot Games\League of Legends\lockfile"

def from_lockfile(path=None):
    try:
        with open(DEFAULT_LOCKFILE) as f:
            # LeagueClient:<pid>:<port>:<password>:<protocol>
            _, _, port, password, _ = f.read().strip().split(":")
            return port, password
    except (OSError, ValueError):
        return None
    return None

def get_lcu_session():
    port, password = from_lockfile()
    if not port or not password:
        return None
    session = requests.Session()
    session.verify = False
    session.auth = ("riot", password)
    base_url = f"https://127.0.0.1:{port}"
    return session, base_url

session, base_url = get_lcu_session()

def get(endpoint):
    return session.get(f"{base_url}{endpoint}").json()

def post(endpoint, body=None):
    return session.post(f"{base_url}{endpoint}", json=body).json()