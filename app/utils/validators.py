from app.config import settings


def is_admin(user_id: str) -> bool:
    return user_id in settings.ADMINS
