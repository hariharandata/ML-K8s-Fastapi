# Use official Python base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install Poetry
RUN pip install poetry

# Copy only pyproject.toml and poetry.lock first for caching
COPY pyproject.toml poetry.lock* /app/

# Configure Poetry to not use a virtualenv
RUN poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi

# Copy the rest of the app
COPY . /app

# Expose the FastAPI app
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "5000"]