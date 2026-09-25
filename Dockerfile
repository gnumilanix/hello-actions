FROM python:3.14-alpine AS builder

WORKDIR /app

RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

COPY src/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt


FROM python:3.14-alpine AS runner

WORKDIR /app

COPY --from=builder /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

COPY src/ ./

EXPOSE 8080
ENV PYTHONPATH=/app
ENV FLASK_RUN_HOST=0.0.0.0

CMD ["python", "main.py"]
