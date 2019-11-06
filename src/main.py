from flask import Flask
app = Flask(__name__)

import os
from balena import Balena
balena = Balena()
balena.auth.login_with_token(os.environ['BALENA_API_KEY'])

@app.route('/')
def hello_world():
    return 'Hello World! Last vpn event: ' + balena.models.device.get(os.environ['BALENA_DEVICE_UUID'])['last_vpn_event']

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
