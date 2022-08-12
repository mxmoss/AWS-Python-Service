from flask import Flask, request

import WrapGnupg
import checklicense

app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'Hello from Flask!'

@app.route('/init-keys/', methods = ['GET', 'POST'])
def init_keys():
	WrapGnupg.main()
	return 'good!'

@app.route('/keys/', methods = ['GET', 'POST', 'DELETE'])
def key():
	retStr = ''
	if request.method == 'GET':
		my_key = request.args.get('key_id')
		my_val = validateMyKey(my_key)
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
