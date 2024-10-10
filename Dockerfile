FROM python:3.10.4-slim-bullseye

# Set enivronment variables
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

# Set working directory
WORKDIR /code

# Install dependencies
COPY ./requirements.txt .

RUN pip install -r requirements.txt

# Copy project
COPY . .