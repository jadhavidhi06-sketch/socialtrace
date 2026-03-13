import requests
from bs4 import BeautifulSoup

def extract_metadata(url):

    data = {}

    try:

        r = requests.get(url, timeout=6)

        soup = BeautifulSoup(r.text,"html.parser")

        title = soup.find("title")

        if title:
            data["title"] = title.text.strip()

        meta = soup.find("meta",{"property":"og:updated_time"})

        if meta:
            data["last_update"] = meta.get("content")

    except:
        pass

    return data