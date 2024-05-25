#                   _      _             _        
#                  | |    (_)           (_)       
#  ___   __ _  ___ | |__   _  _ __ ___   _ __   __
# / __| / _` |/ __|| '_ \ | || '_ ` _ \ | |\ \ / /
# \__ \| (_| |\__ \| | | || || | | | | || | \ V / 
# |___/ \__,_||___/|_| |_||_||_| |_| |_||_|  \_/  
# 
# Created from russia with <3
# Code is licensed under " MIT " unless otherwise specified.
# https://opensource.org/license/mit/
# (c) t.me/sashimiv (https://github.com/sashimiv)



import webbrowser
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QRadioButton, QPushButton, QVBoxLayout, QHBoxLayout 

bing = "https://www.bing.com/search?q="
duckduckgo = "https://duckduckgo.com/?q="
yahoo = "https://search.yahoo.com/search?p="
google = "https://www.google.com/search?q="
baidu = "https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd="
yandex = "https://ya.ru/search/?text="
def open_browser(url):
    webbrowser.open(url, new=2, autoraise=True)

def search_query():
    urlgets = query_entry.text()
    global service_var
    if service_var == "google":
        url = google + urlgets
    elif service_var == "yahoo":
        url = yahoo + urlgets
    elif service_var == "duckduckgo":
        url = duckduckgo + urlgets
    elif service_var == "baidu":
        url = baidu + urlgets
    elif service_var == "yandex":
        url = yandex + urlgets
    else:
        url = bing + urlgets

    open_browser(url)

app = QApplication([])

window = QWidget()
window.setWindowTitle("search by sashimiv")

query_label = QLabel("Введите запрос:")
query_entry = QLineEdit()
service_label = QLabel("Выберите сервис:")
google_rb = QRadioButton("Google")
yahoo_rb = QRadioButton("Yahoo")
duckduckgo_rb = QRadioButton("DuckDuckGo")
bing_rb = QRadioButton("Bing")
baidu_rb = QRadioButton("Baidu")
yandex_rb = QRadioButton("Yandex")
search_button = QPushButton("Поиск в internet")

layout = QVBoxLayout()
layout.addWidget(query_label)
layout.addWidget(query_entry)
layout.addWidget(service_label)
layout.addWidget(google_rb)
layout.addWidget(yahoo_rb)
layout.addWidget(duckduckgo_rb)
layout.addWidget(bing_rb)
layout.addWidget(baidu_rb)
layout.addWidget(yandex_rb)

button_layout = QHBoxLayout()
button_layout.addWidget(search_button)
layout.addLayout(button_layout)

window.setLayout(layout)

google_rb.setChecked(True)
service_var = "google"

def service_radio_button(rb):
    global service_var
    if rb.text() == "Google":
        service_var = "google"
    elif rb.text() == "Yahoo":
        service_var = "yahoo"
    elif rb.text() == "DuckDuckGo":
        service_var = "duckduckgo"
    elif rb.text() == "Baidu":
        service_var = "baidu"
    elif rb.text() == "Yandex":
        service_var = "yandex"
    else:
        service_var = ""

google_rb.toggled.connect(lambda: service_radio_button(google_rb))
yahoo_rb.toggled.connect(lambda: service_radio_button(yahoo_rb))
duckduckgo_rb.toggled.connect(lambda: service_radio_button(duckduckgo_rb))
bing_rb.toggled.connect(lambda: service_radio_button(bing_rb))
baidu_rb.toggled.connect(lambda: service_radio_button(baidu_rb))
yandex_rb.toggled.connect(lambda: service_radio_button(yandex_rb))
search_button.clicked.connect(search_query)

window.show()

app.exec_()
