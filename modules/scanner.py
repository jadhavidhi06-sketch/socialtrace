import requests
from tqdm import tqdm
from modules.profile_scraper import scrape_profile

# Common patterns that indicate a profile DOES NOT exist
INVALID_PATTERNS = [
    "user not found",
    "page not found",
    "profile not found",
    "this account doesn’t exist",
    "this page isn't available",
    "sorry, that page doesn’t exist",
    "404",
    "not available"
]


def is_valid_profile(response, username):
    """
    Checks if a page actually belongs to a valid profile.
    """

    html = response.text.lower()

    # Check known error patterns
    for pattern in INVALID_PATTERNS:
        if pattern in html:
            return False

    # Check if username appears in page content
    if username.lower() not in html:
        return False

    return True


def scan_username(username, sites):
    """
    Scans username across multiple websites
    """

    results = []

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }

    for site in tqdm(sites, desc="Scanning Platforms"):

        url = site["url"].format(username)

        try:

            r = requests.get(url, headers=headers, timeout=8)

            # Check if profile likely exists
            if r.status_code == 200 and is_valid_profile(r, username):

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

        except requests.exceptions.RequestException:

            results.append({
                "site": site["name"],
                "url": url,
                "status": "ERROR"
            })

    return results