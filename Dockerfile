# 使用uv优化的FastAPI应用基础镜像
FROM python:3.12-slim

# 设置工作目录
WORKDIR /app

# 设置环境变量
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONPATH=/app

# 安装uv用于快速依赖安装
RUN pip install uv

#复项目文件
COPY . .

# 使用uv安装依赖（更快更可靠）
RUN uv pip install --system -e .

# 创建非root用户
RUN useradd --create-home --shell /bin/bash app && \
    chown -R app:app /app
USER app

#端口
EXPOSE 8000

#启动应用
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]