# use the official Python image as a base
FROM docker.io/library/python:3.13-slim

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# set the working directory in the container
WORKDIR /app

# copy the requirements file and install dependencies
COPY pyproject.toml poetry.lock README.md /app/

# install system dependencies and Poetry
RUN pip install --no-cache-dir poetry==1.8.5 \
    && poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

# execute main script
CMD ["python", "main.py"]
