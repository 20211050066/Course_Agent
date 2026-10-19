from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.user import User
from app.utils.jwt import decode_access_token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/login")


def get_current_user(
    token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)
) -> User:
    """
    JWT token验证，获取当前用户信息
    """
    try:
        payload = decode_access_token(token)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(e))

    # 获取用户信息
    user_id = payload.get("user_id")
    if not user_id:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Token无效"
        )
    # 查询用户信息
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user.status != 1:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="用户已被禁用，请联系管理员"
        )
    return db_user
