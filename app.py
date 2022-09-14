from flask import Flask, request

from vsgLic2 import VsgLicense

app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'Hello from Flask!'

@app.route('/reset/', methods = ['GET', 'POST'])
def reset():
	return 'not implemented!'

@app.route('/customer/', methods = ['GET', 'POST'])
def customer():
	key_id = request.args.get('key_id')
	action = request.args.get('action')
	pwd = request.args.get('action')
	return 'not implemented!'


@app.route('/key/', methods = ['GET', 'POST'])
def checkout_keys():
	key_id = request.args.get('key_id')
	action = request.args.get('action')
	pwd = request.args.get('pwd')
	secret_key = request.args.get('secret')
#	txt1 = "key_id {key_id}, action {action}, pwd {pwd}, secret_key {secret_key}".format(key_id = key_id, action = action, pwd = pwd, secret_key = secret_key)
#	return txt1

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
			if secret_key and vsg.validate(key_id, secret_key):
				return 'valid!'
	return 'not so good'

if __name__ == '__main__':
	app.run()
