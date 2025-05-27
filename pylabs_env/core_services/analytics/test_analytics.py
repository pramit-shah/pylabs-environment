import requests
print("Analytics Health Check:", requests.get("http://localhost:5006/analytics/health").json())
