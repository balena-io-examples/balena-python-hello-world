from flask import Flask
app = Flask(__name__)

# main.py
# at the end point / call method hello_world which returns "Hello World!"
@app.route('/')
def hello_world():
    return 'Hello World!'

#Main function
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
