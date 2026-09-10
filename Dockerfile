FROM python:3.12.11-slim

ARG APP_VERSION
ARG GIT_COMMIT
ARG REPOSITORY_URL
ARG BUILD_DATE

LABEL org.opencontainers.image.title="student-ml-api" \
      org.opencontainers.image.description="Simple, versioned ML inference API" \
      org.opencontainers.image.version="${APP_VERSION}" \
      org.opencontainers.image.revision="${GIT_COMMIT}" \
      org.opencontainers.image.source="${REPOSITORY_URL}" \
      org.opencontainers.image.created="${BUILD_DATE}"

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py VERSION .

EXPOSE 5000

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
