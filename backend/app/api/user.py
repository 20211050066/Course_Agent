from fastapi import APIRouter, Depends, HTTPException, status
from app.schemas.user import UserResponse
from app.models.user import User
from app.dependencies.auth import get_current_user

router = APIRouter(tags=["用户信息"], prefix="/user")


@router.get("/info")
def get_user_info(current_user: User = Depends(get_current_user)):
    """
    获取当前用户信息
    """
    return {
        "code": 200,
        "message": "获取用户信息成功",
        "data": UserResponse.model_validate(current_user),
    }
