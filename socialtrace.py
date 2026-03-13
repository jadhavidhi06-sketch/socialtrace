#!/usr/bin/env python3

import argparse
import json
from colorama import Fore, init
from modules.scanner import scan_username
from modules.report import save_report

init(autoreset=True)

BANNER = f"""{Fore.CYAN}

███████╗ ██████╗  ██████╗██╗ █████╗ ██╗     ████████╗██████╗  █████╗  ██████╗███████╗
██╔════╝██╔═══██╗██╔════╝██║██╔══██╗██║     ╚══██╔══╝██╔══██╗██╔══██╗██╔════╝██╔════╝
███████╗██║   ██║██║     ██║███████║██║        ██║   ██████╔╝███████║██║     █████╗
╚════██║██║   ██║██║     ██║██╔══██║██║        ██║   ██╔══██╗██╔══██║██║     ██╔══╝
███████║╚██████╔╝╚██████╗██║██║  ██║███████╗   ██║   ██║  ██║██║  ██║╚██████╗███████╗
╚══════╝ ╚═════╝  ╚═════╝╚═╝╚═╝  ╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚══════╝

SocialTrace OSINT Username Footprinting Tool
"""


def main():

    parser = argparse.ArgumentParser(
        description="SocialTrace OSINT Username Investigation Tool"
    )

    parser.add_argument("-u", "--username", help="Target username")
    parser.add_argument("-s", "--save", action="store_true", help="Save report")

    args = parser.parse_args()

    print(BANNER)

    if not args.username:
        print(Fore.RED + "Use -u to specify username")
        return

    username = args.username

    # Load site database
    with open("sites.json") as f:
        sites = json.load(f)

    # Scan usernames
    results = scan_username(username, sites)

    # Filter found profiles
    found = [r for r in results if r["status"] == "FOUND"]

    print("\n" + "=" * 40)
    print("INVESTIGATION SUMMARY")
    print("=" * 40)

    print("Username:", username)
    print("Profiles Found:", len(found))

    # Show found profile links
    for p in found:
        print(Fore.GREEN + f"{p['site']} → {p['url']}")

    # Display profile metadata
    print("\n" + "=" * 40)
    print("PROFILE DETAILS")
    print("=" * 40)

    for r in found:

        print("\nPlatform:", r["site"])
        print("Profile:", r["url"])

        data = r.get("data", {})

        if data:

            if data.get("name"):
                print("Name:", data["name"])

            if data.get("bio"):
                print("Bio:", data["bio"])

            if data.get("image"):
                print("Profile Image:", data["image"])

    # Save report option
    if args.save:

        save_report(username, results)

    else:

        choice = input("\nSave report to output folder? (y/n): ")

        if choice.lower() == "y":
            save_report(username, results)


if __name__ == "__main__":
    main()