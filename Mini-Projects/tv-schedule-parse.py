from bs4 import BeautifulSoup
import requests

url = 'https://segodnya.tv'

headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36"}


def addChannels() -> list:
    answ = input("Введите каналы, которые хотите посмотреть\nКогда Ваш список закончится, напишите 'Конец':\n\n")
    tmp = []
    while answ != 'Конец':
        tmp.append(answ)
        answ = input()
    return tmp

channels = ["Первый", "Россия 1", "МАТЧ!", "Россия 24"] if input("Введите 'Да', если хотите воспользоваться предустановленным набором каналов, либо любое другое слово, если хотите ввести каналы самостоятельно:\n")=='Да' else add_channels()

def parse(url : str) -> str:
    session = requests.Session()
    r = session.get(url=url, headers=headers)
    soup = BeautifulSoup(r.content, "html.parser")
    cases = soup.find_all("div", class_="schedule-unit")

    events = "\nПрограмма на сегодня: \n\n"
    for case in cases:
        head = case.find("a", class_="schedule-header")
        if head and head.text in channels:
            fnc = case.find_all("li")
            events += f"{head.text}\n"
            for index in range(len(channels)):
                base = fnc[index]
                time = base.find("div", class_="b-time").text
                anons = base.find("span", class_="anons-pop").text
                events += f"{time} - {anons}\n"
        else:
            continue
        events += '\n'
    return events

print(parse(url))