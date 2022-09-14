from unittest import TestCase
from vsgLic2 import VsgLicense

class TestVsgLicense(TestCase):
    def test_load_file(self):
        try:
            v = VsgLicense()
            customers = v.load_file()
            v.save_file(customers)
        except:
            self.fail()

    def test_get_customer(self):
        try:
            v = VsgLicense()
            customers = v.load_file()
            v.save_file(customers)
        except:
            self.fail()

    def test_validate(self):
        try:
            v = VsgLicense()
            customers = v.load_file()
            customer = v.get_customer("1234")
            # Should validate
            if v.validate(customer, "9988"):
                self.fail()
            # Should not validate
            if v.validate(customer, "5678"):
                self.fail()
            # Should not validate
            if v.validate(customer, ""):
                self.fail()
        except:
            self.fail()

    def test_CRUD(self):
        try:
            v = VsgLicense()
            customers = v.load_file()
            #Create
            v.add("1234")

            #Read
            customer = v.get_customer("1234")

            #Update
            customer['dante_lic'] = '23452345'
            v.update(customer)

            v.delete("1234")
        except:
            self.fail()

