import random
import requests,fake_useragent,time,os,threading
from threading import Thread
from rich.console import Console
from rich.progress import *
payload = {"JoinForm[gamecode]": "9627399", "JoinForm[name]": "tester"}

console = Console()

os.system('cls' if os.name == 'nt' else 'clear')

console.print('''взломщик тестов
''')
with requests.session() as s:
    p=s.post('https://naurok.ua/test/join', data=payload)
