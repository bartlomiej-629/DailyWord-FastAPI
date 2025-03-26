# Base image
FROM python:3.9-slim AS base

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Copy pytest.ini
COPY pytest.ini pytest.ini

# Stage for running tests
FROM base AS test

# Install testing dependencies
RUN pip install pytest

# Run tests
CMD ["pytest", "tests"]

# Final stage for running the application
FROM base AS final

# Expose port
EXPOSE 8000

# Run the application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
