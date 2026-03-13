import os
from datetime import datetime

def save_report(username, results):

    os.makedirs("output", exist_ok=True)

    filename = f"output/{username}_report.txt"

    with open(filename,"w") as f:

        f.write("SocialTrace OSINT Report\n")
        f.write("="*40+"\n")
        f.write(f"Username: {username}\n")
        f.write(f"Scan Date: {datetime.now()}\n\n")

        for r in results:
                
            if r["status"]=="FOUND":

                f.write(f"Platform: {r['site']}\n")
                f.write(f"Profile: {r['url']}\n")

                data = r.get("data",{})

                if data.get("name"):
                    f.write(f"Name: {data['name']}\n")

                if data.get("bio"):
                    f.write(f"Bio: {data['bio']}\n")

                if data.get("image"):
                    f.write(f"Profile Image: {data['image']}\n")

                f.write("\n")    

    print(f"\nReport saved: {filename}")