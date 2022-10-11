import requests
from bs4 import BeautifulSoup

types_busyness = ["Полный рабочий день", "Неполный рабочий день"]
types_remote = ["Можно удалённо", "Можно удаленно"]


def finding_city(meta) -> str:
    temp = [i for i in meta if i not in types_busyness and i not in types_remote]
    if len(temp) != 0:
        return temp


def finding_busynes_info(meta) -> str:
    for i in meta:
        if i in types_busyness:
            return i


def finding_remote_info(meta) -> bool:
    for i in meta:
        if i in types_remote:
            return True


def pick_qualification_info(meta):
    if "(" in meta[0]:
        return meta[0][meta[0].index("(") + 1 : meta[0].index(")")]


def find_exhange_rate() -> float:
    answer = requests.get(
        "https://www.xe.com/currencyconverter/convert/?Amount=1&From=USD&To=RUB"
    )
    soup = BeautifulSoup(answer.content, "html.parser")
    exhange_rate = float(
        soup.find("p", {"class": "result__BigRate-sc-1bsijpp-1 iGrAod"}).text.split()[0]
    )
    return exhange_rate


def pick_salary_bottom_info(meta) -> str:

    if "от" in meta:
        if "$" in meta or "€" in meta:
            exhange_rate = find_exhange_rate()
            return int(float(meta[1]) * exhange_rate)
        return int(meta[1] + meta[2])


def pick_salary_top_info(meta) -> str:
    if "до" in meta:
        if meta[meta.index("до") + 2] == "$" or meta[meta.index("до") + 2] == "€":
            exhange_rate = find_exhange_rate()
            return int(float(meta[meta.index("до") + 1]) * exhange_rate)
        return int(meta[meta.index("до") + 1] + meta[meta.index("до") + 2])
