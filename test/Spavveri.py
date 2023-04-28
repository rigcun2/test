
import requests,fake_useragent,time,os,threading
from threading import Thread
from rich.console import Console
from rich.progress import *

console = Console()

os.system('cls' if os.name == 'nt' else 'clear')

console.print('''взломщик тестов
''')

os.system('termuxopenurl https://t.me/Bomberukr')

for _ in track(range(999)):
    kod = 0
    for i in range(6):
         kod = string(random.randint(0, 9) + kod) 
         headers = {"UserAgent": fake_useragent.UserAgent().random}
         try:
            requests.post("https://naurok.ua/student/tests", json={"login": "+" + number}, headers=headers, proxies=proxies)
            print('мае')
         except:
            print('немае')
