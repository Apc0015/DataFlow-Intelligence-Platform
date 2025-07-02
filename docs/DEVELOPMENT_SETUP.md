# 🛠️ Development Setup Guide - DataFlow Intelligence Platform

## Table of Contents
1. [Development Environment](#development-environment)
2. [Local Development Setup](#local-development-setup)
3. [Docker Development](#docker-development)
4. [VS Code Configuration](#vs-code-configuration)
5. [Testing Framework](#testing-framework)
6. [Deployment Guidelines](#deployment-guidelines)

## Development Environment

### System Requirements

#### Minimum Requirements
- **Operating System**: Windows 10+, macOS 10.15+, or Linux (Ubuntu 18.04+)
- **Python**: 3.11.0 or higher
- **Memory**: 4GB RAM (8GB recommended)
- **Storage**: 2GB free space
- **Network**: Internet connection for package installation

#### Recommended Development Tools
- **Code Editor**: Visual Studio Code with Python extension
- **Terminal**: PowerShell (Windows), Terminal (macOS), or Bash (Linux)
- **Git**: Version 2.30 or higher
- **Docker**: Optional, for containerized development

### Python Environment Setup

#### Using Virtual Environment (Recommended)
```bash
# Create virtual environment
python -m venv flight_dashboard_env

# Activate virtual environment
# On Windows:
flight_dashboard_env\Scripts\activate
# On macOS/Linux:
source flight_dashboard_env/bin/activate

# Verify Python version
python --version  # Should be 3.11+
```

#### Using Conda (Alternative)
```bash
# Create conda environment
conda create -n flight_dashboard python=3.11

# Activate environment
conda activate flight_dashboard

# Install pip in conda environment
conda install pip
```

## Local Development Setup

### Step-by-Step Installation

#### 1. Clone the Repository
```bash
# Clone from GitHub
git clone https://github.com/Apc0015/DataFlow-Intelligence-Platform.git
cd DataFlow-Intelligence-Platform

# Verify project structure
ls -la
```

#### 2. Install Dependencies
```bash
# Install all required packages
pip install -r requirements.txt

# Verify installation
pip list | grep streamlit
```

#### 3. Verify Data Files
```bash
# Check data directory structure
ls -la data/raw/

# Expected files:
# - 2022.csv (World Happiness Report)
# - university_data.csv (University performance data)
```

#### 4. Launch Development Server
```bash
# Start Streamlit development server
streamlit run src/app.py

# Alternative with custom configuration
streamlit run src/app.py --server.port 8501 --server.headless false
```

#### 5. Access Application
- Open browser to `http://localhost:8501`
- Application should load within 30-60 seconds
- Check browser console for any JavaScript errors

### Development Workflow

#### Daily Development Process
```bash
# 1. Pull latest changes
git pull origin main

# 2. Activate virtual environment
source flight_dashboard_env/bin/activate  # macOS/Linux
# OR
flight_dashboard_env\Scripts\activate     # Windows

# 3. Install any new dependencies
pip install -r requirements.txt

# 4. Start development server
streamlit run src/app.py

# 5. Make your changes and test

# 6. Run tests (when available)
python -m pytest tests/

# 7. Commit changes
git add .
git commit -m "Your descriptive commit message"
git push origin feature/your-feature-name
```

## Docker Development

### Using Development Container

#### Prerequisites
- Docker Desktop installed and running
- VS Code with Dev Containers extension

#### Dev Container Setup
```bash
# Open project in VS Code
code .

# Use Command Palette (Ctrl+Shift+P)
# Select: "Dev Containers: Reopen in Container"

# Container will build automatically using .devcontainer/devcontainer.json
```

#### Manual Docker Setup
```dockerfile
# Create Dockerfile for development
FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better caching
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy application code
COPY . .

# Expose Streamlit port
EXPOSE 8501

# Run Streamlit
CMD ["streamlit", "run", "src/app.py", "--server.address", "0.0.0.0"]
```

#### Build and Run Docker Container
```bash
# Build development image
docker build -t flight-dashboard-dev .

# Run container with volume mounting for live reload
docker run -p 8501:8501 -v $(pwd):/app flight-dashboard-dev

# For Windows PowerShell
docker run -p 8501:8501 -v ${PWD}:/app flight-dashboard-dev
```

### Docker Compose for Development
```yaml
# docker-compose.dev.yml
version: '3.8'

services:
  dashboard:
    build: .
    ports:
      - "8501:8501"
    volumes:
      - .:/app
      - /app/flight_dashboard_env  # Exclude venv from mounting
    environment:
      - STREAMLIT_SERVER_HEADLESS=false
      - STREAMLIT_SERVER_RUN_ON_SAVE=true
    command: streamlit run src/app.py --server.address 0.0.0.0
```

## VS Code Configuration

### Recommended Extensions
```json
{
  "recommendations": [
    "ms-python.python",
    "ms-python.pylint",
    "ms-python.black-formatter",
    "ms-toolsai.jupyter",
    "ms-vscode.vscode-json",
    "redhat.vscode-yaml",
    "ms-vscode-remote.remote-containers"
  ]
}
```

### VS Code Settings
```json
{
  "python.defaultInterpreterPath": "./flight_dashboard_env/bin/python",
  "python.formatting.provider": "black",
  "python.linting.enabled": true,
  "python.linting.pylintEnabled": true,
  "editor.formatOnSave": true,
  "files.autoSave": "onDelay",
  "files.autoSaveDelay": 1000
}
```

### Launch Configuration
```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Streamlit App",
      "type": "python",
      "request": "launch",
      "program": "${workspaceFolder}/flight_dashboard_env/bin/streamlit",
      "args": ["run", "src/app.py"],
      "console": "integratedTerminal",
      "cwd": "${workspaceFolder}"
    }
  ]
}
```

### Debugging Configuration

#### Enable Streamlit Debugging
```python
# Add to src/app.py for development
import streamlit as st

# Enable debugging in development
if st.config.get_option('global.developmentMode'):
    import logging
    logging.basicConfig(level=logging.DEBUG)
```

#### Debug Mode Launch
```bash
# Launch with debug information
streamlit run src/app.py --logger.level debug

# Enable browser developer tools integration
streamlit run src/app.py --server.enableCORS false --server.enableXsrfProtection false
```

## Testing Framework

### Test Structure
```
tests/
├── __init__.py
├── conftest.py                 # Pytest configuration
├── test_data_processing.py     # Data processing tests
├── test_visualizations.py      # Visualization tests
├── test_dashboard_components.py # Component tests
└── fixtures/
    ├── sample_airport_data.csv
    ├── sample_university_data.csv
    └── sample_happiness_data.csv
```

### Setting Up Tests

#### Install Testing Dependencies
```bash
# Install testing packages
pip install pytest pytest-cov pytest-mock streamlit-testing

# Update requirements.txt
pip freeze > requirements.txt
```

#### Basic Test Configuration
```python
# tests/conftest.py
import pytest
import pandas as pd
import sys
import os

# Add src to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

@pytest.fixture
def sample_airport_data():
    """Fixture for airport test data"""
    return pd.read_csv('tests/fixtures/sample_airport_data.csv')

@pytest.fixture
def sample_university_data():
    """Fixture for university test data"""
    return pd.read_csv('tests/fixtures/sample_university_data.csv')
```

#### Running Tests
```bash
# Run all tests
python -m pytest

# Run with coverage
python -m pytest --cov=src

# Run specific test file
python -m pytest tests/test_data_processing.py

# Run with verbose output
python -m pytest -v

# Run tests and generate HTML coverage report
python -m pytest --cov=src --cov-report=html
```

### Code Quality Tools

#### Linting with Pylint
```bash
# Install pylint
pip install pylint

# Run linting on source code
pylint src/

# Generate pylint configuration
pylint --generate-rcfile > .pylintrc
```

#### Code Formatting with Black
```bash
# Install black
pip install black

# Format code
black src/

# Check formatting without making changes
black --check src/
```

#### Import Sorting with isort
```bash
# Install isort
pip install isort

# Sort imports
isort src/

# Check import sorting
isort --check-only src/
```

## Deployment Guidelines

### Environment-Specific Configuration

#### Development Environment
```python
# config/development.py
DEBUG = True
CACHE_TTL = 300  # 5 minutes
LOG_LEVEL = 'DEBUG'
ENABLE_PROFILING = True
```

#### Production Environment
```python
# config/production.py
DEBUG = False
CACHE_TTL = 3600  # 1 hour
LOG_LEVEL = 'INFO'
ENABLE_PROFILING = False
```

### Pre-Deployment Checklist

#### Code Quality Checks
- [ ] All tests passing
- [ ] Code coverage > 80%
- [ ] No linting errors
- [ ] Code formatted with Black
- [ ] Imports sorted with isort
- [ ] Documentation updated

#### Performance Checks
- [ ] Application loads in < 10 seconds
- [ ] Charts render in < 3 seconds
- [ ] Memory usage < 500MB
- [ ] No memory leaks detected

#### Security Checks
- [ ] No hardcoded secrets
- [ ] Input validation implemented
- [ ] Error handling in place
- [ ] HTTPS configured for production

### Deployment Commands

#### Local Production Testing
```bash
# Install production dependencies only
pip install --no-dev -r requirements.txt

# Run with production settings
streamlit run src/app.py --server.headless true --server.port 8501
```

#### Docker Production Build
```bash
# Build production image
docker build -t flight-dashboard:latest -f Dockerfile.prod .

# Run production container
docker run -p 8501:8501 flight-dashboard:latest
```

### Monitoring and Logging

#### Application Monitoring
```python
# Add to src/app.py
import time
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

def log_performance(func):
    """Decorator to log function performance"""
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        duration = time.time() - start_time
        logging.info(f"{func.__name__} executed in {duration:.2f} seconds")
        return result
    return wrapper
```

---

*This development guide is updated regularly. For the latest setup instructions, check the GitHub repository.*