#!/bin/bash
# 开发环境启动脚本 (使用uv)

echo "🚀启动 FastAPI 开发服务器..."

#检查uv是否安装
if ! command -v uv &> /dev/null; then
    echo "❌ 未找到 uv命令，请先安装 uv"
    echo "安装方式: pip install uv 或参考 https://github.com/astral-sh/uv"
    exit 1
fi

# 检查是否已存在虚拟环境
if [ ! -d ".venv" ]; then
    echo "📦 创建虚拟环境..."
    uv venv
fi

#虚拟环境
source .venv/bin/activate

#安装依赖
echo "📥安装项目依赖..."
uv pip install -e ".[test]"

#启动开发服务器
echo "🔄启动 uvicorn 开发服务器..."
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000