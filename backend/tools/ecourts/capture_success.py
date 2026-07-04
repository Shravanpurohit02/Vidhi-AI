import asyncio
import json
from pathlib import Path

from app.integrations.courts.ecourts import ECourtsProvider

CNR = "MHCC010142422024"

async def main():
    provider = ECourtsProvider()

    sid = await provider.create_session()

    image = await provider.fetch_captcha(sid)

    Path("captcha_live.png").write_bytes(image)

    print("=" * 70)
    print("Session ID :", sid)
    print("CNR        :", CNR)
    print("CAPTCHA    : captcha_live.png")
    print("=" * 70)

    captcha = input("Enter CAPTCHA: ").strip()

    result = await provider.search_by_cnr(
        session_id=sid,
        cnr=CNR,
        captcha=captcha,
    )

    Path("last_search.json").write_text(
        json.dumps(result, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )

    if result.get("success") and result.get("history_html"):
        Path("last_success.html").write_text(
            result["history_html"],
            encoding="utf-8",
        )
        print("\n✓ Saved last_success.html")

    print("\n===== RESULT =====")
    print(json.dumps(result, indent=2, ensure_ascii=False))
    print("\nSaved last_search.json")

asyncio.run(main())
