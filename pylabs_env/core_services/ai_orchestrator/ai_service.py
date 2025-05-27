from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/ai/health')
def health():
    return jsonify({'status': 'AI Orchestrator running'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5004)
