import requests
from tqdm import tqdm
from modules.profile_scraper import scrape_profile

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

ERROR_KEYWORDS = [
    "not found",
    "page doesn't exist",
    "doesn't exist",
    "user not found",
    "sorry, this page",
    "404",
    "error"
]


def valid_profile(response, username):

    html = response.text.lower()

    for word in ERROR_KEYWORDS:
        if word in html:
            return False

    if username.lower() not in html:
        return False

    return True


def scan_username(username, sites):

    results = []

    for site in tqdm(sites, desc="Scanning Platforms"):

        url = site["url"].format(username)

        try:

            r = requests.get(url, headers=HEADERS, timeout=8)

            if r.status_code == 200 and valid_profile(r, username):

                data = scrape_profile(url)

                results.append({
                    "site": site["name"],
                    "url": url,
                    "status": "FOUND",
                    "data": data
                })

            else:

                results.append({
                    "site": site["name"],
                    "url": url,
                    "status": "NOT FOUND"
                })

        except requests.exceptions.RequestException:

            results.append({
                "site": site["name"],
                "url": url,
                "status": "ERROR"
            })

    return results
