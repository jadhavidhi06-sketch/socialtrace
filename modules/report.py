import os
import json
from datetime import datetime


def save_report(username, results):

    folder = f"output/{username}"

    os.makedirs(folder, exist_ok=True)

    txt_path = f"{folder}/report.txt"
    json_path = f"{folder}/report.json"

    found = [r for r in results if r["status"] == "FOUND"]

    with open(txt_path, "w") as f:

        f.write("SOCIALTRACE OSINT REPORT\n")
        f.write("=========================\n\n")

        f.write(f"Target Username : {username}\n")
        f.write(f"Profiles Found  : {len(found)}\n")
        f.write(f"Scan Date       : {datetime.now()}\n\n")

        for r in found:

            f.write(f"Platform : {r['site']}\n")
            f.write(f"URL      : {r['url']}\n")

            data = r.get("data", {})

            if data.get("name"):
                f.write(f"Name     : {data['name']}\n")

            if data.get("bio"):
                f.write(f"Bio      : {data['bio']}\n")

            if data.get("image"):
                f.write(f"Image    : {data['image']}\n")

            f.write("\n")

    with open(json_path, "w") as jf:
        json.dump(results, jf, indent=4)

    print(f"\nReport saved in: {folder}")
