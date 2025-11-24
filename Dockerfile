FROM python:3.12-alpine

RUN apk update && apk add sqlite

WORKDIR /app

COPY resources ./resources
COPY schema.sql init_db ./
RUN ./init_db

COPY pyproject.toml uv.lock ./

RUN --mount=from=ghcr.io/astral-sh/uv,source=/uv,target=/bin/uv \
    uv sync && uv add gunicorn

ENV PATH="/app/.venv/bin:$PATH"

COPY static ./static
COPY config.py wsgi.py ./
COPY app ./app

CMD ["gunicorn", "-w", "2", "-b", "0.0.0.0:5000", "wsgi:app"]
