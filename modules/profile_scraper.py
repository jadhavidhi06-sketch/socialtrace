import requests
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}


def scrape_profile(url):

    data = {
        "name": None,
        "bio": None,
        "image": None
    }

    try:

        r = requests.get(url, headers=HEADERS, timeout=8)

        soup = BeautifulSoup(r.text, "html.parser")

        title = soup.find("title")

        if title:
            data["name"] = title.text.strip()

        desc = soup.find("meta", attrs={"name": "description"})

        if desc:
            data["bio"] = desc.get("content")

        img = soup.find("img")

        if img:
            data["image"] = img.get("src")

    except:
        pass

    return data
