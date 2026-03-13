import requests
from tqdm import tqdm
from modules.scraper import extract_profile_info

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

def scan_username(username, sites):

    results = []

    for site in tqdm(sites, desc="Scanning Platforms"):

        url = site["url"].format(username)

        try:

            r = requests.get(url, headers=HEADERS, timeout=8)

            if r.status_code == 200:

                profile_data = extract_profile_info(url)

                results.append({
                    "site": site["name"],
                    "url": url,
                    "status": "FOUND",
                    "data": profile_data
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
