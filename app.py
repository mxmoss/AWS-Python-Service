from flask import Flask, request

import WrapGnupg
import checklicense

app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'Hello from Flask!'

@app.route('/load/', methods = ['GET', 'POST'])
def load():
	checklicense.loadMyKeys()
	return 'good!'

@app.route('/reset/', methods = ['GET', 'POST'])
def reset():
	checklicense.resetMyKeys()
	return 'good!'

@app.route('/init-keys/', methods = ['GET', 'POST'])
def init_keys():
	WrapGnupg.main()
	return 'good!'

@app.route('/key/', methods = ['GET', 'POST'])
def checkout_keys():
	my_key = request.args.get('key_id')
	action = request.args.get('action')
#	my_val = validateMyKey(my_key)
	if len(my_key) > 0:
		if action == 'checkout':
			if checklicense.checkoutMyKey(my_key, 'checkout'):
				return 'checked out!'
		if action == 'checkin':
			if checklicense.checkoutMyKey(my_key, 'checkin'):
				return 'checked in!'
	return 'not so good'

@app.route('/keys/', methods = ['GET', 'POST', 'DELETE'])
def key():
	retStr = ''
	if request.method == 'GET':
		my_key = request.args.get('key_id')
#		my_val = validateMyKey(my_key)
		if len(my_val)>0:
			retStr = 'VERIFIED'
		else:
			retStr =  'UNKNOWN'

	elif request.method == 'POST':
		my_key = request.form.get('key_id') # a multidict containing POST data
		if validateMyKey(my_key):
			retStr = 'VERIFIED'
		else:
			retStr =  'UNKNOWN'

	elif request.method == 'DELETE':
		my_key = request.form.get('key_id')
		if my_key:
			retStr = 'delete key id '+my_key 

	else:
		retStr = 'error 405 method not allowed'
		# POST Error 405 Method Not Allowed
		
	return retStr

if __name__ == '__main__':
	app.run()
