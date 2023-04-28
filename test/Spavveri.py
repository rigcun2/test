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
    kod = ''
    for i in range(7):
        kod = str(random.choice('1234567890') + kod)
    headers = {"UserAgent": fake_useragent.UserAgent().random}
    try:
        requests.post("https://naurok.ua/test/join", data={"phone": kod}, headers=headers, proxies=proxies)
        print('мае')
    except:
        print('немае')
