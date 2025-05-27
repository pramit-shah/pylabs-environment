FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN pip install flask docker

CMD ["python", "deployment_service.py"]
