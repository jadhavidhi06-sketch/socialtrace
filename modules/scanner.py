import requests
from tqdm import tqdm
from modules.profile_scraper import scrape_profile

def scan_username(username, sites):

    results = []

    for site in tqdm(sites,desc="Scanning Platforms"):

        url = site["url"].format(username)

        try:

            r = requests.get(url,timeout=6)

            if r.status_code == 200:

                profile_info = scrape_profile(url)

                results.append({
                    "site":site["name"],
                    "url":url,
                    "status":"FOUND",
                    "data":profile_info
                })

            else:

                results.append({
                    "site":site["name"],
                    "url":url,
                    "status":"NOT FOUND"
                })

        except:

            results.append({
                "site":site["name"],
                "url":url,
                "status":"ERROR"
            })

    return results