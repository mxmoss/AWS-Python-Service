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
            #Should validate correctly
            if not v.validate(customer, "5544"):
                self.fail()
            #Should not validate correctly
            if v.validate(customer, "1234"):
                self.fail()
            #Should not validate correctly
            if v.validate(customer, ""):
                self.fail()
        except:
            self.fail()

    def test_add(self):
        v = VsgLicense()
        self.fail()

    def test_update(self):
        v = VsgLicense()
        self.fail()

    def test_delete(self):
        v = VsgLicense()
        self.fail()

