from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/role/health')
def health():
    return jsonify({'status': 'role service running'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)
