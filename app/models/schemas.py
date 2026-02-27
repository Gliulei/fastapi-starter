"""数据模型定义"""
from datetime import datetime
from pydantic import BaseModel
from typing import Optional


class HealthCheckResponse(BaseModel):
    """健康检查响应模型"""
    status: str
    timestamp: datetime
    service: str


class InfoResponse(BaseModel):
    """应用信息响应模型"""
    app_name: str
    version: str
    description: str
    environment: str


class ErrorResponse(BaseModel):
    """错误响应模型"""
    detail: str
    error_code: Optional[str] = None
    timestamp: datetime = None

    def __init__(self, **data):
        if 'timestamp' not in data:
            data['timestamp'] = datetime.now()
        super().__init__(**data)