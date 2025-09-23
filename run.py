#run.py
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def api_sample():
    """
    API sample
    :return: json
    """

    result = {"code": "999"}
    return jsonify(ResultSet=result)

@app.route('/healthcheck')
def healthcheck() -> str:
    response = "<p>iam ok</p>"
    return response

if __name__ == '__main__':
    app.run()
