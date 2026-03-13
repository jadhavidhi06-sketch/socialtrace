import os

def save_report(username, results):

    os.makedirs("output", exist_ok=True)

    filename = f"output/{username}_report.txt"

    found = [r for r in results if r["status"] == "FOUND"]

    with open(filename, "w") as f:

        f.write("SOCIALTRACE USERNAME REPORT\n")
        f.write("============================\n\n")

        f.write(f"Target Username: {username}\n")
        f.write(f"Profiles Found: {len(found)}\n\n")

        for r in found:

            f.write(f"Platform: {r['site']}\n")
            f.write(f"URL: {r['url']}\n")

            data = r.get("data", {})

            if data.get("name"):
                f.write(f"Name: {data['name']}\n")

            if data.get("bio"):
                f.write(f"Bio: {data['bio']}\n")

            f.write("\n")

    print(f"\nReport saved to {filename}")
