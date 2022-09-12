import json

class vsgLicense:
#    def __init__(self, sn):
#        self.sn = sn

    def get_customer(self, sn):
        # Search for customer
        with open('custs.json') as json_file:
            customers = json.load(json_file)
            customer = customers.get(sn)
            return customer

    def validate(self, customer, secret_id):
        if customer[0].get("id") == secret_id:
            return True
        return False

    def load_file(self):
        with open('custs.json') as json_file:
            return json.load(json_file)

    def save_file(self, customers):
        with open('custs.json', 'w') as f:
            json.dump(customers, f)
        return customers

    def add(self, customer):
        newcust = {
            'sn': customer,
            'id': '19090',
            'ver': '2.01',
            'lease': '2023-01-01',
            'temp': '2022-12-01',
            'dante': 'Y',
            'dante_lic': '3465',
            'sslo': '1',
            'sslo_lic': '4567',
            'general': [1, 2, 3, 4],
            'replay': [0, 0, 0, 0],
            'studio': [4, 3, 2, 1],
            'review': [0, 0, 0, 0]
       }

        customers = self.load_file()
        customers[customer] = newcust
        self.save_file(customers)
        return customers

    def update(self, customer):
        customers = self.load_file()
        customers[customer[0]['sn']] = customer
        self.save_file(customers)
        return customers

    def delete(self, customer):
        customers = self.load_file()
        customers.pop(customer)
        self.save_file(customers)
        return customers

    def reset(self, customer):
        #TBD??
        return

def Main():
    vsg = vsgLicense()
    #given a customer id and a "secret id", verify the customer then return the license info
    #we can also include the machine name / ip address in this process if we want
    customer = vsg.get_customer("1234")
    if not customer:
        exit()

    customer[0]['dante_lic'] = '23452345'
    vsg.update(customer)

    if vsg.validate(customer,"5544"):
        print(customer)
    vsg.add("9090")

    vsg.delete("9090")


Main()
