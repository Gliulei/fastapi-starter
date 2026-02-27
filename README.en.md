# FastAPI Starter

## Description

A modern, out-of-the-box FastAPI project skeleton designed to help you quickly build high-performance Python web services or API interfaces. Say goodbye to tedious initial configuration and focus on business logic development.

## Features

- 🚀 Built on FastAPI with async support and high performance
-📦 Standardized project structure for easy maintenance and extension
-🔧 Complete configuration management system
-🛡️ Built-in CORS support and security configuration
-📝 Auto-generated API documentation (Swagger UI & ReDoc)
-🧪 Complete test suite with coverage reports
-🐳 Docker containerization support
- 📊 Request logging and performance monitoring
-⚡-fast dependency management with uv

## Tech Stack

- **FastAPI** - Modern, fast Python web framework
- **Pydantic** - Data validation and settings management
- **Uvicorn** - ASGI server
- **uv** - Ultra-fast Python package manager
- **pytest** - Testing framework
- **Docker** - Containerization deployment

## Project Structure

```
fastapi-starter/
├── app/                    # Core application code
│   ├── __init__.py
│   ├── main.py            # FastAPI application entry point
│   ├── config/            # Configuration management
│   │  └── settings.py
│   ├── api/               # API routes
│   │   └── routes/
│   │       └── general.py
│   ├── models/            # Data models
│   │   └── schemas.py
│   └── middleware/        # Middleware
│       └── logging.py
├── tests/                 # Test code
│  └── test_main.py
├── docs/                  # Documentation
├── Dockerfile
└── docker-compose.yml
```

## Quick Start

### 1. Install Dependencies

```bash
# Install project dependencies using uv (recommended)
uv pip install -e .

# Install development dependencies (including testing tools)
uv pip install -e ".[test]"

# Or use traditional pip (not recommended)
pip install -e .
pip install -e ".[test]"
```

### 2. Run the Application

```bash
# Development mode with hot reload
uvicorn app.main:app --reload

# Or run directly
python -m app.main
```

### 3. Access the Application

- Application homepage: http://localhost:8000
- API documentation (Swagger UI): http://localhost:8000/docs
- API documentation (ReDoc): http://localhost:8000/redoc
- Health check: http://localhost:8000/health

## API Endpoints

### General Endpoints

- `GET /` - Application root path, returns welcome message
- `GET /health` - Health check endpoint
- `GET /api/v1/health` - API health check
- `GET /api/v1/info` - Application information

## Testing

```bash
# Run all tests
pytest

# Run tests and generate coverage report
pytest --cov=app

# Verbose test output
pytest -v

# Run specific test file
pytest tests/test_main.py
```

## Configuration

Application configuration is located in `app/config/settings.py`, supports environment variable overrides:

```bash
# Set environment variables
export APP_NAME="My App"
export DEBUG=false
export PORT=8080
```

## Docker Deployment

```bash
# Build image
docker build -t fastapi-starter .

# Run container
docker run -p 8000:8000 fastapi-starter

# Use docker-compose
docker-compose up -d
```

## Development Guide

### Using uv for Development Environment Management

```bash
# Create virtual environment
uv venv

# Activate virtual environment
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate     # Windows

# Install dependencies
uv pip install -e ".[test]"

# Run tests
pytest

# Run application
uvicorn app.main:app --reload
```

### Adding New API Routes

1. Create a new route file in the `app/api/routes/` directory
2. Define routes and endpoint handler functions
3. Register routes in `app/main.py`

### Adding Data Models

1. Define Pydantic models in `app/models/schemas.py`
2. Use models for data validation in routes

### Adding Middleware

1. Create middleware file in `app/middleware/` directory
2. Register middleware in `app/main.py`

## uv Best Practices

### Dependency Management

- Use `uv pip install` instead of `pip install` for faster installation
- Use `uv.lock` file to lock dependency versions for reproducible builds
- Regularly use `uv pip list --outdated` to check for dependency updates

### Performance Optimization

- uv's dependency resolution is 10-100x faster than pip
- Use `uv pip install --no-cache` to skip cache for latest versions
- Use `uv pip install --system` in CI/CD environments without virtual environments

### Troubleshooting

Common issues and solutions:

1. **Dependency resolution conflicts**: Use `uv pip install --resolution=lowest-direct`
2. **Cache issues**: Use `uv pip cache clean` to clear cache
3. **Permission issues**: Ensure write permissions or use `--user` flag

## Contribution

Welcome to submit Issues and Pull Requests!

1. Fork this repository
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details