FROM python:3.12-alpine as builder

RUN apk update && apk add sqlite

WORKDIR /app

# Init database
COPY resources ./resources
COPY schema.sql init_db ./
RUN ./init_db


FROM python:3.12-alpine

WORKDIR /app

COPY --from=builder /app/db.sqlite ./
COPY uv.lock pyproject.toml ./

# install dependencies using uv
RUN --mount=from=ghcr.io/astral-sh/uv,source=/uv,target=/bin/uv \
    uv sync --locked --no-editable

COPY static ./static
COPY config.py wsgi.py ./

ENV PATH="/app/.venv/bin:$PATH"

COPY app ./app

CMD ["gunicorn", "-w", "2", "-b", "0.0.0.0:5000", "wsgi:app"]
