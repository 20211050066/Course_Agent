from datetime import datetime, timedelta, timezone
import jwt

from app.config import settings


def create_access_token(user_id: int) -> str:
    """
    创建 JWT token.
    """
    now = datetime.now(timezone.utc)
    payload = {
        "user_id": str(user_id),
        "iat": int(now.timestamp()),
        "exp": int((now + timedelta(hours=settings.JWT_EXPIRE_HOURS)).timestamp()),
    }
    jwt.encode(payload, settings.JWT_SECRET, algorithm=settings.JWT_ALGORITHM)

    return jwt.encode(payload, settings.JWT_SECRET, algorithm=settings.JWT_ALGORITHM)


def decode_access_token(token: str) -> dict:
    """
    解码 JWT token.
    """
    try:
        payload = jwt.decode(
            token, settings.JWT_SECRET, algorithms=[settings.JWT_ALGORITHM]
        )
        return payload
    except jwt.ExpiredSignatureError:
        raise Exception("Token has expired")
    except jwt.InvalidTokenError:
        raise Exception("Invalid token")
