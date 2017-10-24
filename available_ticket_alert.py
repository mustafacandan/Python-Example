import requests, time, vlc, webbrowser
from bs4 import BeautifulSoup

url = 'https://www.eventbrite.com/e/uygulamal-teknik-siber-guvenlik-egitimi-tickets-39004117365'

alert = vlc.MediaPlayer("alert.mp3")

while(True):
    res = requests.get(url)
    soup = BeautifulSoup(res.content, 'html.parser')
    panel_sold = soup.find_all("div", { "class" : "listing-panel-info__status hide-small hide-medium l-mar-left-2" })
    text_at_div = panel_sold[0].get_text().strip()
    print(text_at_div)
    if text_at_div != "Sold Out":
        alert.play()
        webbrowser.open(url)
    time.sleep(3)
    alert.stop()
