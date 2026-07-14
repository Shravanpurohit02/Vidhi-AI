import json
from pathlib import Path

from app.integrations.courts.ecourts import ECourtsProvider

provider = ECourtsProvider()


async def main():
    sid = await provider.create_session()

    img = await provider.fetch_captcha(sid)

    Path("captcha_live.png").write_bytes(img)

    print("=" * 70)
    print("Session ID:", sid)
    print("CAPTCHA saved as captcha_live.png")
    print("=" * 70)

    captcha = input("Enter CAPTCHA: ").strip()

    result = await provider.search_by_cnr(
        session_id=sid,
        cnr="MHCC010142422024",
        captcha=captcha,
    )

    Path("last_search.json").write_text(
        json.dumps(result, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )

    print("=" * 70)
    print(json.dumps(result, indent=2, ensure_ascii=False))
    print("=" * 70)
    print("Saved: last_search.json")


import asyncio

asyncio.run(main())
