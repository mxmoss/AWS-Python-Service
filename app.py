from flask import Flask, request

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
    pwd = request.args.get('pwd')
    secret_id = request.args.get('secret_id')

    ver = request.args.get('ver')
    lease = request.args.get('lease')
    temp = request.args.get('temp')
    dante = request.args.get('dante')
    dante_lic = request.args.get('dante_lic')
    sslo = request.args.get('sslo')
    sslo_lic = request.args.get('sslo_lic')
    general = request.args.get('general')
    replay = request.args.get('replay')
    studio = request.args.get('studio')
    review = request.args.get('review')

    vsg = VsgLicense()
    customer = vsg.cust_rec(key_id, secret_id, ver,
                        lease, temp, dante, dante_lic, sslo, sslo_lic,
                        general, replay, studio, review)
    if key_id:
        if action == 'add':
            return vsg.add(key_id, customer)
        if action == 'update':
            if vsg.validate(key_id, secret_id):
                return vsg.update(customer)
        if action == 'delete':
            if vsg.validate(key_id, secret_id):
                return vsg.delete(customer)
    return 'not so good'

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
            if secret_id and vsg.validate(key_id, secret_id):
               return vsg.get_customer(key_id)
    return 'not so good'

@app.after_request
def add_header(response):
    response.cache_control.max_age = 5
    return response

if __name__ == '__main__':
    app.run()
