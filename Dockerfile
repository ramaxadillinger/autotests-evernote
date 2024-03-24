FROM mcr.microsoft.com/playwright/python:v1.42.0-jammy

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

VOLUME /app/html_report

CMD pytest --html=html_report/report.html && \
    python -m http.server --bind 0.0.0.0 8000
