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
