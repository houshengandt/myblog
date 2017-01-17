from Cryptodome.Cipher import PKCS1_v1_5
from Cryptodome.PublicKey import RSA

import requests
import random
import re
import time
import base64


class LoginBaidu(object):

    token_url = 'https://passport.baidu.com/v2/api/?getapi&tpl=mn&apiver=v3&tt={tt}&class=login&gid={gid}&logintype=dialogLogin&callback={callback}'
    rsa_url = 'https://passport.baidu.com/v2/getpublickey?token={token}&tpl=mn&apiver=v3&tt={tt}&gid={gid}&callback={callback}'
    verifycode_url = 'https://passport.baidu.com/cgi-bin/genimage?{code_string}'
    login_check_url = 'https://passport.baidu.com/v2/api/?logincheck&token={token}&tpl=mn&apiver=v3&tt={tt}&sub_source=leadsetpwd&username={username}&isphone=false&callback={callback}'
    login_url = 'https://passport.baidu.com/v2/api/?login'

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.gid = self.get_gid()
        self.session = requests.Session()
        self.session.get('http://yun.baidu.com')
        self.token = self.get_token()
        self.code_string = self.get_code_string()
        self.key, self.pubkey = self.get_keys()
        self.encrypted_password = self.encrypt_password(self.password, self.pubkey)
        # self.download_verifycode()

    def get_token(self):
        tt = self.get_tt()
        callback = self.get_callback()
        token_response = self.session.get(self.token_url.format(tt=tt, gid=self.gid, callback=callback))
        pattern = re.compile(r'"token"\s*:\s*"(\w+)"')
        match = pattern.search(token_response.text)
        if match:
            token = match.group(1)
        else:
            raise TokenError("can not find token in response")
        return token

    def get_code_string(self):
        tt = self.get_tt()
        callback = self.get_callback()
        code_string_response = self.session.get(self.login_check_url.format(token=self.token, tt=tt, username=self.username, callback=callback))
        pattern = re.compile(r'"codeString"\s*:\s*"(\w+)"')
        match = pattern.search(code_string_response.text)
        if match:
            code_string = match.group(1)
        else:
            raise CodeStringError("can not find codestring in response")
        return code_string

    def get_keys(self):
        tt = self.get_tt()
        callback = self.get_callback()
        keys_response = self.session.get(self.rsa_url.format(token=self.token, tt=tt, gid=self.gid, callback=callback))
        pattern = re.compile("\"key\"\s*:\s*'(\w+)'")
        match = pattern.search(keys_response.text)
        if match:
            key = match.group(1)
        else:
            raise Exception
        pattern = re.compile("\"pubkey\":'(.+?)'")
        match = pattern.search(keys_response.text)
        if match:
            pubkey = match.group(1)
            pubkey = pubkey.replace('\\n','\n').replace('\\','')
        else:
            raise Exception
        return key, pubkey

    def get_verifycode(self, verifycode):
        self.verifycode = verifycode

    def download_verifycode(self, path="verifycode.png"):
        verifycode_response = self.session.get(self.verifycode_url.format(code_string=self.code_string))
        with open(path, 'wb') as codeWriter:
            codeWriter.write(verifycode_response.content)
            codeWriter.close()

    def encrypt_password(self, pre_pw, pubkey):
        rsakey = RSA.importKey(pubkey)
        cipher = PKCS1_v1_5.new(rsakey)
        password = base64.b64encode(cipher.encrypt(pre_pw.encode())).decode()
        return password

    @staticmethod
    def get_tt():
        return str(int(time.time()*1000))

    @staticmethod
    def base36(q):
        if q < 0: raise ValueError("must supply a positive integer")
        letters = "0123456789abcdefghijklmnopqrstuvwxyz"
        converted = []
        while q != 0:
            q, r = divmod(q, 36)
            converted.insert(0, letters[r])
        return "".join(converted) or '0'
        
    def get_callback(self):
        return 'bd__cbs__' + self.base36(int(2147483648 * random.random()))

    @staticmethod
    def get_gid():
        gid = 'xxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'
        l = list(gid)
        for i in range(0, len(gid)):
            if l[i] == '-' or l[i] == '4':
                continue
            t = int(16 * random.random()) | 0
            n = t if gid[i] == 'x' else 3 & t | 8
            l[i] = str(hex(n))[2:]
        gid = ''.join(l)
        return gid.upper()

    def login(self):
        tt = self.get_tt()
        callback = self.get_callback()
        data = {
            'staticpage': 'https://www.baidu.com/cache/user/html/v3Jump.html',
            'charset': 'UTF-8',
            'token': self.token,
            'tpl': 'mn',
            'subpro': '',
            'apiver': 'v3',
            'tt': tt,
            'codestring': self.code_string,
            'safeflg': '0',
            'u': 'https://www.baidu.com/',
            'isPhone': 'false',
            'detect': '1',
            'gid': self.gid,
            'quick_user': '0',
            'logintype': 'dialogLogin',
            'logLoginType': 'pc_loginDialog',
            'idc': '',
            'loginmerge': 'true',
            'splogin': 'rate',
            'username': self.username,
            'password': self.encrypted_password,
            'verifycode': self.verifycode,
            'mem_pass':'on',
            'rsakey': self.key,
            'crypttype':'12',
            'ppui_logintime':'10842',
            'countrycode':'',
            'callback': 'parent.' + callback,
            }

        login_response = self.session.post(self.login_url, data=data)
        if login_response.text.find('err_no=0') == -1:
            raise Exception


class LoginBaiduWenku(LoginBaidu):
    check_in_url = "http://wenku.baidu.com/task/submit/signin"

    def check_in(self):
        self.session.get(self.check_in_url)
