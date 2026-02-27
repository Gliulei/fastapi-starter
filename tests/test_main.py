"""FastAPI应用测试"""
import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.config.settings import settings

client = TestClient(app)


def test_root_endpoint():
    """测试根路径端点"""
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert "version" in data
    assert data["version"] == settings.APP_VERSION


def test_health_check():
    """测试健康检查端点"""
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert data["app_name"] == settings.APP_NAME


def test_api_health_check():
    """测试API健康检查端点"""
    response = client.get("/api/v1/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert data["service"] == "fastapi-starter"


def test_api_info():
    """测试API信息端点"""
    response = client.get("/api/v1/info")
    assert response.status_code == 200
    data = response.json()
    assert data["app_name"] == "FastAPI Starter"
    assert data["version"] == "1.0.0"


def test_docs_endpoint():
    """测试文档端点"""
    response = client.get("/docs")
    assert response.status_code == 200


def test_redoc_endpoint():
    """测试Redoc端点"""
    response = client.get("/redoc")
    assert response.status_code == 200


def test_404_not_found():
    """测试404错误处理"""
    response = client.get("/non-existent-endpoint")
    assert response.status_code == 404