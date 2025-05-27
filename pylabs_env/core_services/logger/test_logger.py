import requests
print("Logger Health Check:", requests.get("http://localhost:5005/logger/health").json())
