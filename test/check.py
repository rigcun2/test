import random
import requests,fake_useragent,time,os,threading
from threading import Thread
from rich.console import Console
from rich.progress import *
login="https://naurok.ua/test/join"
kod='9627399'
data={'action': 'test', "password": "9627399", "name": "testing"}

console = Console()

os.system('cls' if os.name == 'nt' else 'clear')

console.print('''взломщик тестов
''')
with requests.session() as s:
    s.post(login, data)
