from flask import Flask, request
import json
import sys

from vsgLic2 import VsgLicense

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello from Flask!'


@app.route('/reset/', methods=['GET', 'POST'])
def reset():
    return 'not implemented!'


@app.route('/customer/', methods=['GET', 'POST'])
def customer():
    key_id = request.args.get('key_id')
    action = request.args.get('action')
    pwd = request.args.get('action')
    return 'not implemented!'

@app.route('/key/', methods=['GET', 'POST'])
def checkout_keys():
    key_id = request.args.get('key_id')
    action = request.args.get('action')
    pwd = request.args.get('pwd')
    secret_id = request.args.get('secret_id')

    vsg = VsgLicense()
    if key_id:
        #	if len(key_id) > 0:
        if action == 'checkout':
            if vsg.check_out(key_id):
                return 'checked out!'
        if action == 'checkin':
            if vsg.check_in(key_id):
                return 'checked in!'
        if action == 'validate':
            return vsg.load_file()
#            if secret_id and vsg.validate(key_id, secret_id):
#               return json.dumps(vsg.get_customer(key_id)[0])
    return 'not so good'

@app.after_request
def add_header(response):
    response.cache_control.max_age = 5
    return response

if __name__ == '__main__':
    app.run()
