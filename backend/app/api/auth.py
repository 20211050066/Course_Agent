from fastapi import APIRouter, Depends, HTTPException, status
from app.schemas.auth import LoginRequest
from app.schemas.user import UserResponse
from app.database import get_db
from sqlalchemy.orm import Session
from app.models.user import User
from app.utils.password import verify_password
from app.utils.jwt import create_access_token, decode_access_token

router = APIRouter(tags=["权限验证"], prefix="/auth")


@router.post("/login")
async def login(data: LoginRequest, db: Session = Depends(get_db)):
    # 根据用户名查询用户
    user = db.query(User).filter(User.username == data.username).first()
    # 如果用户不存在或者密码不正确，返回401错误
    if not user or verify_password(data.password, user.password) is False:
        return {"code": 401, "message": "用户名或密码错误"}
    # 如果用户被禁用，返回403错误
    if user.status != 1:
        return {"code": 403, "message": "用户已被禁用，请联系管理员"}
    # 生成token
    token = create_access_token(user.id)
    # 返回用户信息和token
    return {
        "code": 200,
        "message": "登录成功",
        "data": {
            "token": token,
            "user": UserResponse.model_validate(user),
        },
    }
