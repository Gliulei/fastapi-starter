# FastAPI Starter

##简介

一个现代化、开箱即用的 FastAPI 项目骨架，旨在帮你快速搭建高性能的 Python Web 服务或 API接口。告别繁琐的初始化配置，专注于业务逻辑的开发。

##特性

-🚀基于 FastAPI构建，支持异步和高性能
- 📦标化的项目结构，易于维护和扩展
-🔧完整的配置管理系统
-🛡️内置 CORS支持和安全配置
-📝 自动生成 API 文档 (Swagger UI & ReDoc)
-🧪完整的测试套件和覆盖率报告
-🐳 Docker容器化支持
- 📊 请求日志记录和性能监控
-⚡ uv进高速依赖管理

##技术栈

- **FastAPI** - 现代、快速的 Python Web框架
- **Pydantic** - 数据验证和设置管理
- **Uvicorn** - ASGI 服务器
- **uv** -极的Python包管理器
- **pytest** -测试框架
- **Docker** -容器化部署

## 项目结构

```
fastapi-starter/
├── app/                    #应用核心代码
│   ├── __init__.py
│   ├── main.py            # FastAPI应用入口
│   ├── config/            #配置管理
│   │   └── settings.py
│   ├── api/               # API路由
│   │   └── routes/
│   │       └── general.py
│   ├── models/            # 数据模型
│   │  └── schemas.py
│   └── middleware/        # 中间件
│       └── logging.py
├── tests/                 #测试代码
│   └── test_main.py
├── docs/                  # 文档
├── Dockerfile
└── docker-compose.yml
```

##快速开始

### 1.安装依赖

```bash
# 使用 uv安项目项目依赖（推荐）
uv pip install -e .

#安装开发依赖（包括测试工具）
uv pip install -e ".[test]"

# 或者使用传统的 pip（不推荐）
pip install -e .
pip install -e ".[test]"
```

### 2.运行应用

```bash
# 开发模式（带热重载）
uvicorn app.main:app --reload

# 或者直接运行
python -m app.main
```

### 3.访问应用

-应用主页: http://localhost:8000
- API文档 (Swagger UI): http://localhost:8000/docs
- API文档 (ReDoc): http://localhost:8000/redoc
-健康检查: http://localhost:8000/health

## API 端点

### 通用端点

- `GET /` - 应用根路径，返回欢迎信息
- `GET /health` -健康检查端点
- `GET /api/v1/health` - API健康检查
- `GET /api/v1/info` -应用信息

##测试

```bash
#运行所有测试
pytest

# 运行测试并生成覆盖率报告
pytest --cov=app

# 详细的测试输出
pytest -v

# 运行特定测试文件
pytest tests/test_main.py
```

## 配置

应用配置位于 `app/config/settings.py`，支持通过环境变量覆盖：

```bash
# 设置环境变量
export APP_NAME="My App"
export DEBUG=false
export PORT=8080
```

## Docker部署

```bash
#构建镜像
docker build -t fastapi-starter .

#运行容器
docker run -p 8000:8000 fastapi-starter

# 使用 docker-compose
docker-compose up -d
```

## 开发指南

### 使用 uv管开发理开发环境

```bash
# 创建虚拟环境
uv venv

#虚拟环境
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate     # Windows

#安装依赖
uv pip install -e ".[test]"

#运行测试
pytest

#运行应用
uvicorn app.main:app --reload
```

### 添加新的API路由

1. 在 `app/api/routes/` 目录下创建新的路由文件
2.定义路由和端点处理函数
3. 在 `app/main.py` 中注册路由

### 添加数据模型

1. 在 `app/models/schemas.py` 中定义 Pydantic模型
2. 在路由中使用模型进行数据验证

### 添加中间件

1. 在 `app/middleware/`目录下创建中间件文件
2. 在 `app/main.py` 中注册中间件

## uv 最佳实践

### 依赖管理

- 使用 `uv pip install`而非 `pip install`获更快的安装速度
- 使用 `uv.lock` 文件锁定依赖版本确保可重现的构建
-定使用 `uv pip list --outdated`检查依赖更新

###性能优化

- uv 的依赖解析速度比 pip快 10-100-
- 使用 `uv pip install --no-cache`跳缓存获得最新版本
- 在 CI/CD 环境中使用 `uv pip install --system`虚拟环境

###故排除

常见问题及解决方案：

1. **依赖解析冲突**：使用 `uv pip install --resolution=lowest-direct` 
2. **缓存问题**：使用 `uv pip cache clean`清理缓存
3. **权限问题**：确保有足够的写入权限或使用 `--user`标志

##联系

如需联系作者，请通过以下方式：

- 姓名: shenyi
- 邮箱: 1245332635@qq.com

## 贡

欢迎提交 Issue 和 Pull Request！

1. Fork 本仓库
2. 创建功能分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4.推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启 Pull Request

##许可证

本项目采用 MIT许可证 - 查看 [LICENSE](LICENSE) 文件了解详情