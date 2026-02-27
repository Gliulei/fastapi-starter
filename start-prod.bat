@echo off
REM 生产环境启动脚本 (使用uv) (Windows)

echo🚀启动 FastAPI 生产服务器...

REM 检查uv是否安装
where uv >nul 2>&1
if %errorlevel% neq 0 (
    echo❌ 未找到 uv命令，请先安装 uv
    echo安装方式: pip install uv 或参考 https://github.com/astral-sh/uv
    exit /b 1
)

REM安装依赖
echo📥安装项目依赖...
uv pip install -e .

REM启动生产服务器
echo🔄启动 uvicorn 生产服务器...
set PORT=%PORT:8000%
set WORKERS=%WORKERS:4%
uvicorn app.main:app --host 0.0.0.0 --port %PORT% --workers %WORKERS%