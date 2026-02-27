@echo off
REM 开发环境启动脚本 (使用uv) (Windows)

echo🚀启动 FastAPI 开发服务器...

REM 检查uv是否安装
where uv >nul 2>&1
if %errorlevel% neq 0 (
    echo❌ 未找到 uv命令，请先安装 uv
    echo安装方式: pip install uv 或参考 https://github.com/astral-sh/uv
    exit /b 1
)

REM检查是否已存在虚拟环境
if not exist ".venv" (
    echo📦虚拟 创建虚拟环境...
    uv venv
)

REM激活虚拟环境
call .venv\Scripts\activate

REM安装依赖
echo📥项目依赖...
uv pip install -e ".[test]"

REM启动开发服务器
echo🔄启动 uvicorn 开发服务器...
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000