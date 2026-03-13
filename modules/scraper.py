import requests
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

def extract_profile_info(url):

    profile = {
        "name": None,
        "bio": None
    }

    try:

        r = requests.get(url, headers=HEADERS, timeout=8)

        soup = BeautifulSoup(r.text, "html.parser")

        title = soup.find("title")

        if title:
            profile["name"] = title.text.strip()

        description = soup.find("meta", attrs={"name": "description"})

        if description:
            profile["bio"] = description.get("content")

    except:
        pass

    return profile
