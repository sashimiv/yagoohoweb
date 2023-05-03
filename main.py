import webbrowser
from googlesearch import search
import time
print("t.me/sashimiv")
print()
urlgets = input("Введите запрос: ")
service = input("Выберите сервис(google/yandex/yahoo) ")
if service == "google":
    url = "https://www.google.com/search?q=" + urlgets
    webbrowser.open(url, new=2, autoraise=True) 
    time.sleep(5)   
else:
    if service == "yahoo":
        url = "https://search.yahoo.com/search?p=" + urlgets
        webbrowser.open(url, new=2, autoraise=True)
        time.sleep(5)
    else:
        url = "https://yandex.ru/search/?lr=10735&text=" + urlgets
        webbrowser.open(url, new=2, autoraise=True)
        time.sleep(5)
