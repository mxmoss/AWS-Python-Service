import json

class VsgLicense:
#    def __init__(self, sn):
#        self.sn = sn

    @staticmethod
    def get_customer(sn):
        # Search for customer
        with open('custs.json') as json_file:
            customers = json.load(json_file)
            customer = customers.get(sn)
            if customer:
                return customer
            return []

    @staticmethod
    def validate(customer, secret_id):
        if customer and customer['secret_id'] == secret_id:
            return True
        return False

    @staticmethod
    def load_file():
        with open('custs.json') as json_file:
            return json.load(json_file)

    @staticmethod
    def save_file(customers):
        with open('custs.json', 'w') as f:
            json.dump(customers, f)
        return customers

    def add(self, customer):
        newcust = {
            'sn': customer,
            'secret_id': '19090',
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
        customers[customer['sn']] = customer
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

def main():
    vsg = VsgLicense()
    #given a customer id and a "secret id", verify the customer then return the license info
    #we can also include the machine name / ip address in this process if we want
    vsg.add("9090")

    customer = vsg.get_customer("9090")
    if not customer:
        exit()

    if vsg.validate(customer,"19090"):
        print(customer)

    customer['dante_lic'] = '23452345'
    vsg.update(customer)

    vsg.delete("9090")

main()
