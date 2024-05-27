FROM python:3.10-alpine

ENV PYTHONUNBUFFERED 1
ENV HOST 0.0.0.0
ENV PORT 8064

WORKDIR /app

COPY poetry.lock /app/poetry.lock
COPY pyproject.toml /app/pyproject.toml

RUN --mount=type=cache,mode=0755,target=/root/.cache \
    --mount=type=cache,mode=0755,target=/usr/lib/rustlib \
    apk add --no-cache curl && \
    pip3 install --no-cache-dir poetry && poetry config virtualenvs.create false && \
    poetry install --no-dev --no-root && \
    pip3 uninstall -y poetry

COPY bitcoind_exporter /app/bitcoind_exporter

HEALTHCHECK --interval=1m --timeout=3s CMD curl --silent --fail ${HOST}:${PORT} || exit 1

CMD ["python3", "-m", "bitcoind_exporter"]
