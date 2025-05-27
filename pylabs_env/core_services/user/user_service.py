from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/user/health')
def health():
    return jsonify({'status': 'user service running'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
