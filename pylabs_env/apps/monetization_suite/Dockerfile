FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN pip install flask stripe

CMD ["python", "monetization_service.py"]
