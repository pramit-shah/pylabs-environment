from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/monetization/health')
def health():
    return jsonify({'status': 'Monetization Service Running'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5007)
