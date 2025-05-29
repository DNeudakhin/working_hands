FROM python:3.9

ENV POETRY_VIRTUALENVS_CREATE=false \
    DEBIAN_FRONTEND=noninteractive \
    PYTHONPATH=/app \
    POETRY_VERSION=2.1.3

WORKDIR /app

RUN apt-get update && apt-get install -y \
    python3-dev \
    default-libmysqlclient-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY pyproject.toml .env ./
RUN pip3 install --upgrade pip wheel && \
    pip3 install poetry==${POETRY_VERSION} && \
    poetry install --no-interaction --no-ansi --only main

COPY ./src ./

EXPOSE 8000

CMD ["/bin/sh"]