'''Dieser Code ist von Quelle: xxx. Er generiert die SID-Authenfizierungsdaten um die Fritzbox über einen HTTP-Request anzusprechen.'''


import sys
import hashlib
import time
import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET
import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    # Legacy Python that doesn't verify HTTPS certificates by default
    pass
else:
    # Handle target environment that doesn't support HTTPS verification
    ssl._create_default_https_context = _create_unverified_https_context

LOGIN_SID_ROUTE = "/login_sid.lua?version=2"


class LoginState:
    def __init__(self, challenge: str, blocktime: int):
        self.challenge = challenge
        self.blocktime = blocktime
        self.is_pbkdf2 = challenge.startswith("2$")


def get_sid(box_url: str, username: str, password: str) -> str:
    try:
        state = get_login_state(box_url)
    except Exception as ex:
        raise Exception("failed to get challenge") from ex
    if state.is_pbkdf2:
        print("PBKDF2 supported")
        challenge_response = calculate_pbkdf2_response(
            state.challenge, password)
        print(challenge_response)
    else:
        print("Falling back to MD5")
        challenge_response = calculate_md5_response(state.challenge, password)
    if state.blocktime > 0:
        print(f"Waiting for {state.blocktime} seconds...")
        time.sleep(state.blocktime)
    try:
        sid = send_response(box_url, username, challenge_response)
        print('This is the SID:', sid)
    except Exception as ex:
        raise Exception("failed to login") from ex
    if sid == "0000000000000000":
        raise Exception("wrong username or password")
    return sid


def get_login_state(box_url: str) -> LoginState:
    """ Get login state from FRITZ!Box using login_sid.lua?version=2 """
    url = box_url + LOGIN_SID_ROUTE
    http_response = urllib.request.urlopen(url)
    xml = ET.fromstring(http_response.read())
    # print(f"xml: {xml}")
    challenge = xml.find("Challenge").text
    blocktime = int(xml.find("BlockTime").text)
    return LoginState(challenge, blocktime)


def calculate_pbkdf2_response(challenge: str, password: str) -> str:
    """ Calculate the response for a given challenge via PBKDF2 """
    challenge_parts = challenge.split("$")
    # Extract all necessary values encoded into the challenge
    iter1 = int(challenge_parts[1])
    salt1 = bytes.fromhex(challenge_parts[2])
    iter2 = int(challenge_parts[3])
    salt2 = bytes.fromhex(challenge_parts[4])
    # Hash twice, once with static salt...
    hash1 = hashlib.pbkdf2_hmac("sha256", password.encode(), salt1, iter1)
    # Once with dynamic salt.
    hash2 = hashlib.pbkdf2_hmac("sha256", hash1, salt2, iter2)
    return f"{challenge_parts[4]}${hash2.hex()}"


def calculate_md5_response(challenge: str, password: str) -> str:
    """ Calculate the response for a challenge using legacy MD5 """
    response = challenge + "-" + password
    # the legacy response needs utf_16_le encoding
    response = response.encode("utf_16_le")
    md5_sum = hashlib.md5()
    md5_sum.update(response)
    response = challenge + "-" + md5_sum.hexdigest()
    return response


def send_response(box_url: str, username: str, challenge_response: str) -> str:
    # Build response params
    post_data_dict = {"username": username, "response": challenge_response}
    post_data = urllib.parse.urlencode(post_data_dict).encode()
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    url = box_url + LOGIN_SID_ROUTE
    # Send response
    http_request = urllib.request.Request(url, post_data, headers)
    http_response = urllib.request.urlopen(http_request)
    # Parse SID from resulting XML.
    xml = ET.fromstring(http_response.read())
    return xml.find("SID").text


get_sid('https://gmhn0evflkdlpmbw.myfritz.net:8254',
        'admin', 'QUANTO_Solutions')
