"""通用API路由"""
from fastapi import APIRouter
from datetime import datetime
from app.models.schemas import HealthCheckResponse, InfoResponse

router = APIRouter()


@router.get("/health", response_model=HealthCheckResponse)
async def health_check():
    """健康检查端点"""
    return HealthCheckResponse(
        status="healthy",
        timestamp=datetime.now(),
        service="fastapi-starter"
    )


@router.get("/info", response_model=InfoResponse)
async def get_info():
    """获取应用信息"""
    return InfoResponse(
        app_name="FastAPI Starter",
        version="1.0.0",
        description="现代化的FastAPI项目骨架",
        environment="development"
    )