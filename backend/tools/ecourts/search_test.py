import json
import re
import requests

BASE = "https://services.ecourts.gov.in/ecourtindia_v6"

session = requests.Session()

headers = {
    "User-Agent": "Mozilla/5.0",
    "X-Requested-With": "XMLHttpRequest",
}

print("=" * 80)
print("Opening homepage...")

r = session.get(BASE + "/", headers=headers)

print("Status:", r.status_code)
print("Cookies:", session.cookies.get_dict())

print("\nFetching CAPTCHA image...")

captcha = session.get(
    BASE + "/vendor/securimage/securimage_show.php",
    headers=headers,
)

with open("captcha.jpg", "wb") as f:
    f.write(captcha.content)

print("CAPTCHA saved as captcha.jpg")

captcha_text = input("Enter CAPTCHA: ").strip()

print("\nSubmitting search...")

r = session.post(
    BASE + "/cnr_status/searchByCNR/",
    headers=headers,
    data={
        "cino": "MHCC010142422024",
        "fcaptcha_code": captcha_text,
    },
)

print("=" * 80)
print("HTTP", r.status_code)

text = r.text

m = re.search(r'(\{.*\})', text, re.S)

if m:
    obj = json.loads(m.group(1))
    print(json.dumps(obj, indent=2))
else:
    print(text)
