from flask import Flask, jsonify
from prometheus_client import Counter, generate_latest

app = Flask(__name__)
request_counter = Counter('http_requests_total', 'Total HTTP Requests')

@app.route('/analytics/health')
def health():
    request_counter.inc()
    return jsonify({'status': 'Analytics Service Running'})

@app.route('/metrics')
def metrics():
    return generate_latest(request_counter), 200, {'Content-Type': 'text/plain; charset=utf-8'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5006)
