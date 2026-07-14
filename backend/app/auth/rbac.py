from fastapi import Depends, HTTPException, status

from app.auth.dependencies import get_current_user

ROLE_PERMISSIONS = {
    "admin": {"*"},
    "lawyer": {
        "cases",
        "clients",
        "documents",
        "research",
        "drafting",
        "reasoning",
        "workspace",
        "dashboard",
    },
    "associate": {
        "cases",
        "documents",
        "research",
        "reasoning",
        "workspace",
    },
    "paralegal": {
        "documents",
        "workspace",
        "research",
    },
    "client": {
        "profile",
    },
}


def require_role(*roles):
    def dependency(current_user=Depends(get_current_user)):
        if current_user.role not in roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Insufficient role",
            )
        return current_user

    return dependency


def require_permission(permission: str):
    def dependency(current_user=Depends(get_current_user)):
        permissions = ROLE_PERMISSIONS.get(current_user.role, set())

        if "*" not in permissions and permission not in permissions:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Permission denied",
            )

        return current_user

    return dependency
