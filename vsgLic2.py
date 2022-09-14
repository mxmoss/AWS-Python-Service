import json

class VsgLicense:
#    def __init__(self, sn):
#        self.sn = sn

    @staticmethod
    def get_customer(customer_id):
        # Search for customer
        with open('custs.json') as json_file:
            customers = json.load(json_file)
            customer = customers.get(customer_id)
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

    def cust_rec(self, cust_id, secret_id= '0000', ver='2.01',
                 lease_dt='2023-01-01', temp_dt='2022-12-01',
                 dante_yn='Y', dante_lic='0000', sslo_yn='1', sslo_lic='0000',
                 general = [0,0,0,0], replay = [0,0,0,0], studio = [0,0,0,0], review = [0,0,0,0]):
        return  {
            'sn': cust_id,
            'secret_id': secret_id,
            'ver': ver,
            'lease': lease_dt,
            'temp': temp_dt,
            'dante': dante_yn,
            'dante_lic': dante_lic,
            'sslo': sslo_yn,
            'sslo_lic': sslo_lic,
            'general': general,
            'replay': replay,
            'studio': studio,
            'review': review
        }

    def add(self, customer):
        newcust = self.cust_rec(customer)
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

    def check_out(self, customer):
        customer['in_use'] = 'Y'
        self.update(customer)

    def check_in(self, customer):
        customer['in_use'] = 'N'
        self.update(customer)


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

    vsg.check_out(customer)
    vsg.check_in(customer)
#    vsg.delete("9090")

main()
