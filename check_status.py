import csv
import requests

with open('Intern.csv', 'r', encoding='utf-8-sig') as file:
    reader = csv.DictReader(file)

    for row in reader:
        url = row['urls']

        try:
            response = requests.get(url,timeout=5)
            print(f"({response.status_code}) {url}")
        except:
            pass