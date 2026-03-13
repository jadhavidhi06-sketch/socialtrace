# socialtrace
A CEH social OSINT Footprinting tool.

# SocialTrace 🔎

### OSINT Username Footprinting Tool

SocialTrace is a **professional OSINT (Open-Source Intelligence) username investigation tool** designed for cybersecurity researchers, ethical hackers, and investigators.

The tool searches **100+ popular platforms** including:

* Social Media
* Developer Platforms
* Forums
* Design Communities
* Tech Websites

Using only a **username**, the tool attempts to find **public profiles and metadata** such as:

* Profile URL
* Display name
* Bio / description
* Profile image link
* Platform name

All results can optionally be **saved into a structured investigation folder**.

---

# Features

✔ Scan **100+ popular websites**
✔ Detect **public profiles using username**
✔ Extract **public metadata** from profile pages
✔ Show **direct clickable profile links**
✔ Clean **investigation summary output**
✔ Optional **report saving in output folder**
✔ Colorized terminal output
✔ Beginner-friendly CLI usage
✔ Lightweight and fast

---

# Screenshot (Example Output)

```
INVESTIGATION SUMMARY
================================

Username: johndoe
Profiles Found: 3

GitHub → https://github.com/johndoe
Reddit → https://reddit.com/user/johndoe
Dev.to → https://dev.to/johndoe


PROFILE DETAILS
================================

Platform: GitHub
Profile: https://github.com/johndoe
Name: John Doe
Bio: Python Developer | Security Researcher
Profile Image: https://avatars.githubusercontent.com/u/12345
```

---

# Project Structure

```
SocialTrace/
│
├── socialtrace.py
├── sites.json
├── README.md
│
├── modules/
│   ├── scanner.py
│   ├── profile_scraper.py
│   └── report.py
│
└── output/
```

Explanation:

| File               | Description                        |
| ------------------ | ---------------------------------- |
| socialtrace.py     | Main program                       |
| sites.json         | Database of websites to scan       |
| scanner.py         | Username scanning engine           |
| profile_scraper.py | Extracts metadata from profiles    |
| report.py          | Saves investigation reports        |
| output/            | Stores saved investigation reports |

---

# Requirements

Before running the tool install:

* Python 3.8+
* pip

Python packages required:

```
requests
beautifulsoup4
colorama
tqdm
```

---

# Installation Guide

## Step 1 — Clone the Repository

```
git clone https://github.com/yourusername/SocialTrace.git
```

```
cd SocialTrace
```

---

## Step 2 — Install Python Dependencies

```
pip install requests beautifulsoup4 colorama tqdm
```

---

## Step 3 — Make Script Executable (Optional)

On Linux systems:

```
chmod +x socialtrace.py
```

---

# Usage

Basic syntax:

```
python3 socialtrace.py -u USERNAME
```

Example:

```
python3 socialtrace.py -u johndoe
```

The tool will:

1. Load the website database
2. Search each site for the username
3. Extract public metadata
4. Display investigation results

---

# Command Line Flags

| Flag | Description               |
| ---- | ------------------------- |
| `-u` | Target username           |
| `-s` | Automatically save report |

---

# Command Examples

### Scan Username

```
python3 socialtrace.py -u johndoe
```

---

### Scan and Save Report Automatically

```
python3 socialtrace.py -u johndoe -s
```

---

### Interactive Save Option

If `-s` is not used, the tool will ask:

```
Save report to output folder? (y/n)
```

---

# Output Reports

When a report is saved, a file will be created inside the **output folder**.

Example:

```
output/johndoe_report.txt
```

Example content:

```
Platform: GitHub
Profile: https://github.com/johndoe
Name: John Doe
Bio: Python Developer | Security Researcher
Profile Image: https://avatars.githubusercontent.com/u/12345
```

---

# Websites Database

The tool uses:

```
sites.json
```

This file contains **100+ platforms**.

Example entry:

```
{
"name":"GitHub",
"url":"https://github.com/{}"
}
```

The `{}` placeholder is replaced with the username.

Example:

```
https://github.com/johndoe
```

---

# Adding More Websites

You can easily extend the tool by adding new entries in **sites.json**.

Example:

```
{
"name":"ExampleSite",
"url":"https://examplesite.com/{}"
}
```

---

# Use Cases

SocialTrace can be used for:

* OSINT investigations
* Cybersecurity research
* Ethical hacking practice
* Digital footprint analysis
* Username correlation

---

# Important Notice

This tool is intended **only for ethical and legal use**.

Do not use this tool to:

* Harass individuals
* Stalk people
* Violate privacy laws

Always follow:

* Ethical hacking guidelines
* Local cybersecurity laws

---

# Troubleshooting

### Python not found

Install Python:

```
sudo apt install python3
```

---

### pip not installed

```
sudo apt install python3-pip
```

---

### Module error

Install dependencies again:

```
pip install -r requirements.txt
```

---

# Future Improvements

Planned upgrades:

* Parallel scanning (faster scanning)
* Profile image downloader
* Reverse image search
* Identity correlation graphs
* Interactive OSINT dashboard
* PDF investigation reports
* Timeline analysis

---

# Contributing

Pull requests are welcome.

If you want to improve the tool:

1. Fork the repository
2. Create a new branch
3. Submit a pull request

---

# Author

Created for cybersecurity learning and OSINT investigation research.

---

# License

MIT License

---
