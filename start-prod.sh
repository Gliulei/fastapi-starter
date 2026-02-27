#!/bin/bash
# 生产环境启动脚本 (使用uv)

echo "🚀启动 FastAPI 生产服务器..."

#检查uv是否安装
if ! command -v uv &> /dev/null; then
    echo "❌ 未找到 uv命令，请先安装 uv"
    echo "安装方式: pip install uv 或参考 https://github.com/astral-sh/uv"
    exit 1
fi

#安装依赖
echo "📥安装项目依赖..."
uv pip install -e .

#启动生产服务器
echo "🔄启动 uvicorn 生产服务器..."
uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8000} --workers ${WORKERS:-4}