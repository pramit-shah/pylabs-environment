from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/auth/health')
def health():
    return jsonify({'status': 'auth service running'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
