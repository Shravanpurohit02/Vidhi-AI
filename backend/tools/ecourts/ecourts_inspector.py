import re
import requests
from bs4 import BeautifulSoup

URL = "https://services.ecourts.gov.in/ecourtindia_v6/"

session = requests.Session()

headers = {
    "User-Agent": (
        "Mozilla/5.0 (X11; Linux x86_64) " "AppleWebKit/537.36 Chrome/137 Safari/537.36"
    )
}

print("=" * 80)
print("GET", URL)

response = session.get(URL, headers=headers, timeout=30)

print("=" * 80)
print("STATUS:", response.status_code)
print("FINAL URL:", response.url)

print("=" * 80)
print("COOKIES")
for k, v in session.cookies.items():
    print(f"{k} = {v}")

print("=" * 80)
print("FORMS")

soup = BeautifulSoup(response.text, "html.parser")

forms = soup.find_all("form")

print("Found", len(forms), "form(s)\n")

for i, form in enumerate(forms, start=1):
    print("-" * 60)
    print("FORM", i)
    print("ACTION :", form.get("action"))
    print("METHOD :", form.get("method"))

    for inp in form.find_all("input"):
        print(
            "INPUT:",
            inp.get("type"),
            inp.get("name"),
            "=",
            inp.get("value"),
        )

print("=" * 80)
print("HIDDEN INPUTS")

for hidden in soup.find_all("input", {"type": "hidden"}):
    print(hidden.get("name"), "=", hidden.get("value"))

print("=" * 80)
print("JAVASCRIPT FILES")

for script in soup.find_all("script", src=True):
    print(script["src"])

print("=" * 80)
print("INLINE FUNCTIONS")

matches = re.findall(r"function\s+([A-Za-z0-9_]+)", response.text)

for fn in sorted(set(matches)):
    print(fn)

print("=" * 80)
