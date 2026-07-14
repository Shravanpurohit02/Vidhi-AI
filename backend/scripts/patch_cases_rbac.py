from pathlib import Path

path = Path("app/api/v1/cases.py")
text = path.read_text()

if "from app.auth.rbac import require_permission" not in text:
    text = text.replace(
        "from app.auth.dependencies import get_current_user",
        "from app.auth.dependencies import get_current_user\nfrom app.auth.rbac import require_permission",
    )

if 'Depends(require_permission("cases"))' not in text:
    text = text.replace(
        "current_user: User = Depends(get_current_user),",
        'current_user: User = Depends(get_current_user),\n    _: User = Depends(require_permission("cases")),',
    )

path.write_text(text)

print("Done")
