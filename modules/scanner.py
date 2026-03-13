import requests
from tqdm import tqdm
from modules.profile_scraper import scrape_profile


# Common error messages used by websites
INVALID_PATTERNS = [
    "user not found",
    "page not found",
    "profile not found",
    "this page isn't available",
    "account suspended",
    "doesn't exist",
    "not available",
    "404",
    "error",
]


def is_valid_profile(response, username):
    """
    Verify if the profile is real
    """

    html = response.text.lower()

    # Detect error pages
    for pattern in INVALID_PATTERNS:
        if pattern in html:
            return False

    # Username should appear somewhere
    if username.lower() not in html:
        return False

    return True


def scan_username(username, sites):

    results = []

    headers = {
        "User-Agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }

    for site in tqdm(sites, desc="Scanning Platforms"):

        url = site["url"].format(username)

        try:

            r = requests.get(
                url,
                headers=headers,
                timeout=10,
                allow_redirects=True
            )

            # Only continue if page loads
            if r.status_code == 200:

                if is_valid_profile(r, username):

                    profile_info = scrape_profile(url)

                    results.append({
                        "site": site["name"],
                        "url": url,
                        "status": "FOUND",
                        "data": profile_info
                    })

                else:

                    results.append({
                        "site": site["name"],
                        "url": url,
                        "status": "NOT FOUND"
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
