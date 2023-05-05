#Консольный интерфейс устарел
import webbrowser
import time
konsoleversion = "0.0.6"
guiversion = "1.0.5"

if konsoleversion == guiversion:
    #Пожалуйста, не запускайте программу если версии не совпадают
    def open_browser(url):
        webbrowser.open(url, new=2, autoraise=True)
        time.sleep(4)
    print("t.me/sashimiv\n")
    urlgets = input("Введите запрос: ")
    service = input("Выберите сервис(google/yandex/yahoo): ")
    if service == "google":
        url = "https://www.google.com/search?q=" + urlgets
        open_browser(url)
    elif service == "yahoo":
        url = "https://search.yahoo.com/search?p=" + urlgets
        open_browser(url)
    else:
        url = "https://yandex.ru/search/?lr=10735&text=" + urlgets
        open_browser(url)
else:
    print("Текущая версия программы не функционирует")
