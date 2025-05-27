import requests
print("Deployment Manager Health Check:", requests.get("http://localhost:5008/deployment/health").json())
