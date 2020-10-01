from flask import Flask #for import flask type in your poweshell/ terminal (pip install Flask).
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
    output:
        'Hello World!'
