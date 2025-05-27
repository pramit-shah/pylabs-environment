import requests
print("Monetization Health Check:", requests.get("http://localhost:5007/monetization/health").json())
