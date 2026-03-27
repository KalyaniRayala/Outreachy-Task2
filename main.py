import requests

with open("data/Intern.csv", "r", encoding="utf-8") as f:
    next(f)

    for url in f:
        url = url.strip()

        try:
            res = requests.get(url, timeout=5)
            print(f"({res.status_code}) {url}")

        except :
            pass
