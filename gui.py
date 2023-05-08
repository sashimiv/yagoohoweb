import webbrowser
from searchpro import servicesall, duckduckgo, bing, yahoo, google # Обязательно в одной директории с этим файлом должен быть файл searchpro.py (скачивайте отсюда)
import time
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QRadioButton, QPushButton, QVBoxLayout, QHBoxLayout
def open_browser(url):
    webbrowser.open(url, new=2, autoraise=True)
    time.sleep(5)
def search_query():
    urlgets = query_entry.text()
    service = service_var
    if service == "google":
        url = google + urlgets
        open_browser(url)
    elif service == "yahoo":
        url = yahoo + urlgets
        open_browser(url)
    elif service == "duckduckgo":
        url = duckduckgo + urlgets
        open_browser(url)
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
search_button = QPushButton("Поиск в ❤️internet❤️")
layout = QVBoxLayout()
layout.addWidget(query_label)
layout.addWidget(query_entry)
layout.addWidget(service_label)
layout.addWidget(google_rb)
layout.addWidget(yahoo_rb)
layout.addWidget(duckduckgo_rb)
layout.addWidget(bing_rb)
button_layout = QHBoxLayout()
button_layout.addWidget(search_button)
layout.addLayout(button_layout)
window.setLayout(layout)
google_rb.setChecked(True)
service_var = "google"
google_rb.toggled.connect(lambda: service_radio_button(google_rb))
yahoo_rb.toggled.connect(lambda: service_radio_button(yahoo_rb))
duckduckgo_rb.toggled.connect(lambda: service_radio_button(duckduckgo_rb))
bing_rb.toggled.connect(lambda: service_radio_button(bing_rb))
def service_radio_button(rb):
    global service_var
    if rb.text() == "Google":
        service_var = "google"
    elif rb.text() == "Yahoo":
        service_var = "yahoo"
    elif rb.text() == "DuckDuckGo":
        service_var = "duckduckgo"
    else:
        service_var = ""
search_button.clicked.connect(search_query)
window.show()
app.exec_()
