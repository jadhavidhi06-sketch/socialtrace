import requests
from bs4 import BeautifulSoup

def scrape_profile(url):

    profile_data = {
        "name": None,
        "bio": None,
        "image": None,
        "title": None
    }

    try:

        r = requests.get(url,timeout=8)

        soup = BeautifulSoup(r.text,"html.parser")

        # Page Title
        title = soup.find("title")
        if title:
            profile_data["title"] = title.text.strip()

        # Meta Description
        desc = soup.find("meta",{"name":"description"})
        if desc:
            profile_data["bio"] = desc.get("content")

        # OpenGraph Title
        og_title = soup.find("meta",{"property":"og:title"})
        if og_title:
            profile_data["name"] = og_title.get("content")

        # Profile Image
        img = soup.find("meta",{"property":"og:image"})
        if img:
            profile_data["image"] = img.get("content")

    except:
        pass

    return profile_data